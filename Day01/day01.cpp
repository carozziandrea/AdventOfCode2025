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
    int part2zeroes = 0;

    while(getline(f, line)){
        //std::cout << line << std::endl;
        char dir = line[0];
        int rot = std::stoi(line.substr(1, line.size()-1));
        if (dir == 'L'){
            while(rot != 0){
                dial--;
                if(dial == -1){
                    dial = 99;
                }
                if(dial == 0){
                    part2zeroes++;
                }
                rot--;
            }
            //dial = (((dial - rot) % dial_size) + dial_size) % dial_size;
        }else{
            while(rot != 0){
                dial++;
                if(dial == 100){
                    dial = 0;
                }
                if(dial == 0){
                    part2zeroes++;
                }
                rot--;
            }
            //dial = (((dial + rot) % dial_size) + dial_size) % dial_size;
        }
        //std::cout << '\t'<< dial << std::endl;
        if(dial == 0){
            zeroes++;
        }
    }

    std::cout << "Part 1: " << zeroes << std::endl;
    std::cout << "Part 2: " << part2zeroes << std::endl;
    f.close();

    return 0;
}

