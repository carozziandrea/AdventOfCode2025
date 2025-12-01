#include <stdio.h>
#include <iostream>
#include <fstream>

int main(int argc, char const *argv[])
{
    std::string filePath = "dayXXinput.txt";
    std::string line;
    std::ifstream f(filePath);

    if(!f.is_open()){
        std::cerr << "Errore apertura file!";
        return 1;
    }

    // Part 1
    while(getline(f, line)){
        std::cout << line << std::endl;
    }

    std::cout << "Part 1: " << std::endl;
    f.close();

    return 0;
}

