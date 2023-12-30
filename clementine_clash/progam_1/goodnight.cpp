#include <cctype>
#include <iostream>
#include <unistd.h>

class Print_iteration
{
    std::string concatenate_ascii()
    {
        std::string all_ascii;
        for(char ch =' '; ch < '~'; ch++)
        {
            all_ascii += ch;
        }
        return all_ascii;
    }
    std::string all_ascii = concatenate_ascii();
    // initialize strings with all alpha and all special characters

    int i = 0; // pointer to integer i
    
    public:

    std::string get_user_input() // insteading of returning new str, addd to old str;
    {   
        char *new_line = new char[100];
        std::string user_input = "";
        std::cout << ">>";
        std::cin.getline(new_line, 100);
        user_input += new_line;
        return user_input;
        delete[] new_line; // free memory
    }
    std::string make_new_string(const std::string& user_input)
    {
        std::string new_string = "";
        int length1 = new_string.length();
        int length2 = user_input.length();
        int i = 0;
        while (i < user_input.length()) // check if last is equal to one
        {
            char current = user_input[i];
            for(int j = 0; j < all_ascii.length(); j++)
            {
                if (all_ascii[j] == current)
                {
                    new_string += all_ascii[j];
                    std::cout << new_string << '\n' <<std::flush;
                    usleep(700);
                }
                else if (all_ascii[j] != current)
                {
                    std::cout << new_string << all_ascii[j] << '\n' <<std::flush;
                    usleep(700);
                }
                if (length1 == length2 && new_string[i] == user_input[i])
            {
                break;
            }
            }
            i++;
        }
        return new_string;
    }   
};

int main()
{
    Print_iteration goodnight;
    std::string user_input = goodnight.get_user_input();
    std::string new_string = goodnight.make_new_string(user_input);
    std::cout << new_string << '\n';
    return 0;
}