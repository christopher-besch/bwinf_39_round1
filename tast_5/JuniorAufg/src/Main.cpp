#include <cstdlib>
#include <iostream>
#include <fstream>
#include <string>
#include <ctime>


int main() {

	std::ifstream file("Beispieldateien/spielstaerken1.txt");
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

	// Add random number
	std::srand(std::time(0)); //use current time as seed for random generator
	int random_variable = std::rand();
	std::cout << "Random value on [0 " << RAND_MAX << "]: " << random_variable << '\n';

	return 0;
}