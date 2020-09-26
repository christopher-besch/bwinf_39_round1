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
    char** indices = new char*[word_lengths.size() + 1];
    indices[-1] = nullptr;
    char* last_length = chars;
    for (int idx = 1; idx < word_lengths.size(); idx++)
    {
        indices[idx] = last_length + word_lengths[idx - 1] * (idx - 1);
        last_length = indices[idx];
        // std::cout << reinterpret_cast<int>(indices[idx]) << std::endl;
    }

    char** current_indices = new char*[word_lengths.size()];
    std::copy(indices, indices + word_lengths.size() + 1, current_indices);

    // start reading from beginning again
    file.open(FILE);
    while (std::getline(file, line))
    {
        for (int idx = 0; idx < line.length(); idx++)
            *(current_indices[line.length()] + idx) = line[idx];
        // print_char_array(current_indices[line.length()], current_indices[line.length()] + line.length());
        current_indices[line.length()] += line.length();
    }
    file.close();

    // print words
    for (int length = 0; length < word_lengths.size(); length++)
    {
        for (char* pointer = indices[length]; pointer < indices[length + 1]; pointer += length)
        {
            // std::cout << reinterpret_cast<int>(pointer);
            print_char_array(pointer, pointer + length);
        }
    }

    std::cout << chars << std::endl;

    std::cin.get();
    return 0;
}
