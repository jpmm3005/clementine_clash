#include <iostream>
#include <cstring>

char* input(int *key);
char* encoding(char *ciphertext, int *ord_storage, int *key);
int main() // function declarations 

{
    int *key = new int;
    char *ciphertext = input(key); // function call to input function and storing string
    int max_size = std::strlen(ciphertext); // intiializing maximum size for string array
    int *ord_storage = new int[max_size];
    char *output = encoding(ciphertext, ord_storage, key); // function call to encoding function

    std::cout << "Plaintext: "<< ciphertext << '\n';
    std::cout << "Ciphertext: ";
    for (int i = 0; i < std::strlen(ciphertext); i++)
    {
        std::cout << output[i];
    }
    std::cout << '\n';
    delete[] ciphertext;
    delete[] ord_storage;
    return 0;
}

char* input(int *key)
{
    const int max_size = 100;
    char *ciphertext = new char[max_size]; // allocating static memory using static integer


    std::cout << "Enter plaintext: ";
    std::cin.getline(ciphertext, max_size);

    std::cout << "Enter key: ";
    std::cin >> *key;
    return ciphertext;
}

char* encoding(char *ciphertext, int *ord_storage, int *key)
{
    int length = std::strlen(ciphertext);
    char *output = new char[length + 1];

    for (int i = 0; i < length; i++)
    {
        if (ciphertext[i] >= 'a' && ciphertext[i] <= 'z')
        {
            ord_storage[i] = static_cast<int>(ciphertext[i]);
            ord_storage[i] = (((ord_storage[i] + *key - 'a') % 26) + 'a');
            output[i] = static_cast<char>(ord_storage[i]);
        }
        else if (ciphertext[i] >= 'A' && ciphertext[i] <= 'Z')
        {
            ord_storage[i] = static_cast<int>(ciphertext[i]);
            ord_storage[i] = (((ord_storage[i] + *key - 'A') % 26) + 'A');
            output[i] = static_cast<char>(ord_storage[i]);
        }
        else
        {
            output[i] = ciphertext[i];
        }
    }
    output[length] = '\0';

    return output;
}