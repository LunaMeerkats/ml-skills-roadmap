#include <iostream>
#include <vector>
 
// https://en.cppreference.com/w/cpp/container/vector.html

int main()
{
    // Create a vector containing integers
    std::vector<int> v = {8, 4, 5, 9};
 
    // Add two more integers to vector
    v.push_back(6);
    v.push_back(9);
 
    // Overwrite element at position 2
    v[2] = -1;
 
    // Print out the vector
    for (int n : v)
        std::cout << n << ' ';
    std::cout << '\n';

    // Multidimensional vector
    std::vector<std::vector<int>> v2 = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    // Print out the multidimensional vector
    for (const auto& row : v2) {
        for (int n : row)
            std::cout << n << ' ';
        std::cout << '\n';
    }
}