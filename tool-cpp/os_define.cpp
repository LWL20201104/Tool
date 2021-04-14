#include <iostream>

int main(int argc, char** argv) {
#ifdef _WIN32
	std::cout << "win32" << std::endl;
#elif _WIN64
	std::cout << "win64" << std::endl;
#elif __APPLE__ || __MACH__
	std::cout << "macos" << std::endl;
#elif __linux__
	std::cout << "linux" << std::endl;
#elif __FreeBSD__
	std::cout << "FreeBSD" << std::endl;
#elif __unix || __unix__
	std::cout << "FreeBSD" << std::endl;
#else
	std::cout << "Other" << std::endl;
#endif //OS

	return 0;
}