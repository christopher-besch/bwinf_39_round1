#include <iostream>
#include <fstream>

int main()
{
    std::ios::pos_type size;
    char* mem_block;

    std::ifstream file("files/english.txt", std::ios::in|std::ios::ate);
    if(file.is_open())
    {
        size = file.tellg();
        // + NULL termination
        mem_block = new char[static_cast<int>(size) + 1];
        file.seekg(0, std::ios::beg);
        file.read(mem_block, size);
        file.close();
        mem_block[-1] = NULL;

        std::cout << mem_block << std::endl;

        delete[] mem_block;
    }
    else
        std::cout << "Unable to open file!" << std::endl;

    std::cin.get();
    return 0;
}
