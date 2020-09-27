#include <cstdlib>
#include <iostream>
#include <ctime>

int main() {

	// Add random number
	std::srand(std::time(0)); //use current time as seed for random generator
	int random_variable = std::rand();
	std::cout << "Random value on [0 " << RAND_MAX << "]: " << random_variable << '\n';

	return 0;
}