#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

#define FILE "files/english.txt"

void print_char_array(char* start, char* end)
{
    for (char* index = start; index < end; index++)
        std::cout << *index;
    std::cout << std::endl;
}

int main()
{
    std::ifstream file(FILE);
    if (!file.is_open())
    {
        std::cout << "Unable to open file!" << std::endl;
        return -1;
    }

    // pre-run through file
    std::vector<uint16_t> word_lengths;
    unsigned int char_amount = 0;
    std::string line;
    while (std::getline(file, line))
    {
        while (word_lengths.size() <= line.length())
            word_lengths.push_back(0);

        word_lengths[line.length()]++;
        char_amount += line.length();
    }
    file.close();

    char* chars = new char[char_amount];
    // calculated indices
    char** indices = new char*[word_lengths.size()];
    indices[0] = chars;
    for (int idx = 1; idx < word_lengths.size(); idx++)
        indices[idx] = indices[idx - 1] + word_lengths[idx - 1] * (idx - 1);

    char** current_indices = new char*[word_lengths.size()];
    std::copy(indices, indices + word_lengths.size(), current_indices);

    // start reading from beginning again
    file.open(FILE);
    while (std::getline(file, line))
    {
        for (int idx = 0; idx < line.length(); idx++)
            *(current_indices[line.length()] + idx) = line[idx];
        current_indices[line.length()] += line.length();
    }
    file.close();
    delete[] current_indices;

    // print words
    for (int length = 1; length < word_lengths.size(); length++)
    {
        char* start = indices[length];
        char* end = indices[length] + word_lengths[length] * length;
        for (char* pointer = start; pointer < end; pointer += length)
            print_char_array(pointer, pointer + length);
    }

    delete[] chars;
    delete[] indices;

    std::cin.get();
    return 0;
}

// test
