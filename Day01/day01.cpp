#include <stdio.h>
#include <iostream>
#include <fstream>

int main(int argc, char const *argv[])
{
    std::string filePath = "Day01/day01input.txt";
    std::string line;
    std::ifstream f(filePath);

    if(!f.is_open()){
        std::cerr << "Errore apertura file!";
        return 1;
    }

    // Part 1
    int dial_size = 100;
    int dial = 50;
    int zeroes = 0;

    while(getline(f, line)){
        //std::cout << line << std::endl;
        char dir = line[0];
        int rot = std::stoi(line.substr(1, line.size()-1));
        if (dir == 'L'){
            dial = (((dial - rot) % dial_size) + dial_size) % dial_size;
        }else{
            dial = (((dial + rot) % dial_size) + dial_size) % dial_size;
        }
        //std::cout << '\t'<< dial << std::endl;
        if(dial == 0){
            zeroes++;
        }
    }

    std::cout << "Part 1: " << zeroes << std::endl;
    f.close();

    return 0;
}

