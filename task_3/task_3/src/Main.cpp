#include <iostream>
#include <fstream>
#include <string>

int main()
{
    std::ifstream file("src/Main.cpp");
    if (!file.is_open())
    {
        std::cout << "Unable to open file!" << std::endl;
        return -1;
    }
    std::string line;
    while (std::getline(file, line))
    {
        std::cout << line << std::endl;
    }
    file.close();
}
