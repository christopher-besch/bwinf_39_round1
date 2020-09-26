#include <iostream>
#include <fstream>
#include <array>
#include <string>

int main()
{
    std::ifstream file("files/english.txt");
    if (!file.is_open())
    {
        std::cout << "Unable to open file!" << std::endl;
        return -1;
    }

    int words_amount = 0;
    std::string line;
    while (std::getline(file, line))
        ++words_amount;

    std::string* words = new std::string[words_amount];

    file.seekg(0, std::ios::beg);
    for(int line_idx = 0; line_idx != words_amount; line_idx++)
    {
        std::getline(file, line);
        words[line_idx] = line;
    }

    for(int word_idx = 0; word_idx != words_amount; ++word_idx)
        std::cout << words[word_idx] << std::endl;

    std::cin.get();
    return 0;
}
