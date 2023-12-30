/*  wordle.cpp
    jpmm3005

    wordle.cpp is a for-fun project that I wrote over my winter break to learn how to program in c++

    to run this code, wordle_words.txt must be in the same directory, and it must be compiled with at least c++11 std
    enjoy :)
*/

#include <chrono>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>

class Wordle
{
    // ANSI escape codes for text color
    #define RESET   "\033[0m" 
    #define GREEN   "\033[32m"
    #define BLUE    "\033[34m"
    #define YELLOW  "\033[33m"

    public:

    std::vector <std::string> read_file() // method reads file and returns vector with words
    {
        std::ifstream infile("wordle_words.txt");
        std::string word;
        std::vector <std::string> data; // initialize vector storing words

        if (!infile.is_open()) // if file does not open
        {
            exit(EXIT_FAILURE); 
        }
    
        while (infile.good())
        {
            infile >> word;
            data.push_back(word);
        }
        infile.close();
        return data; // return vector and close file
    }

    // choose random word from vector
    std::string random_word(std::vector <std::string> data)
    {
        unsigned seed = std::chrono::system_clock::now().time_since_epoch().count(); // rand positive number to be used as rand seed

        std::minstd_rand0 generator (seed); // initialize rand generator
        unsigned rand = generator();
        rand = rand % data.size(); // mod with the name # as args in text file

        std::string rand_word = data[rand]; // array index 
        return rand_word;
    }   
};

struct output // initialize struct for output
    {
        std::string output_word = ""; 
        std::string wrong_chars = "";
    };

std::string get_input(); // get input
output make_output_word(std::string user_input, std::string rand_word); // return struct of two strings 
bool check_win_condition(int score); // bool to check if game is won

int main()
{
    while (true)
    {
        Wordle init;
        std::vector <std::string> data = init.read_file(); // method call to read file and store words in a vector
        std::string rand_word = init.random_word(data); // method calls to store rand word
        int score = 0;
        int iteration = 0;
        
        while (iteration < 4)
        {
            std::string user_input = get_input();
            output result = make_output_word(user_input, rand_word);
            std::cout << result.output_word << '\t' << "incorrect letters: " << result.wrong_chars << '\n';
            score = score + 1;
            bool win_condtion = check_win_condition(score); // pass result by reference
            if (win_condtion == true)
            {
                std::cout << "You won! It took you " << score << " tries.\n";
                break;
            }
        }
    if (iteration == 4)
    {
        std::cout << "The word was " << rand_word << '\n' << "Play again (Y/N): ";
        std::string check;
        std::cin >> check;
        if (check != "Y" && check != "y")
        {
            break;
        }
    }
}
    
    return 0;
}

std::string get_input()
{
     std::cout << "Enter a five letter word\n";
    while (true)
    {
        std::string user_input;
        std::cout << ">>";
        std::cin >> user_input;
        if (user_input.length() == 5)
        {
            return user_input;
        }
    }
}

output make_output_word(std::string user_input, std::string rand_word)
{
    output result;
    int index = 0;
    result.wrong_chars = "";
    
    while (index < rand_word.length())
    {

        if (user_input[index] == rand_word[index])
        {
            result.output_word += GREEN + std::string(1, rand_word[index]);
            result.output_word += RESET;
        }
        else if (rand_word.find(user_input[index]) != std::string::npos && rand_word.find(user_input[index]) != index)
        {
            result.output_word += YELLOW + std::string(1, user_input[index]);
            result.output_word += RESET;
        }
        else
        {
            result.output_word += user_input[index];
            result.wrong_chars += user_input[index];
        }
        index ++;
    }
    return result;
}

bool check_win_condition(int score)
{   

    if (score == 4)
    {
        return true;
    }
    else
    {
        return false;
    } 
}