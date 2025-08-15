#include <iostream> // for std::cout, std::endl
#include <vector>   // for std::vector

int main()
{
    // Create a vector of ints with elements 0 to 5
    std::vector<int> v = {0, 1, 2, 3, 4, 5};

    // Loop 1: Range-based for loop, accessing each element by const reference
    // - 'const int& i' means:
    //   - no copy of the element is made (good for performance)
    //   - the element cannot be modified inside the loop
    for (const int& i : v)
        std::cout << i << ' ';
    std::cout << '\n';

    // Loop 2: Access by value
    // - 'auto i' deduces to 'int' (copy)
    // - Each element is copied into 'i' — modifying 'i' here won’t affect v
    for (auto i : v)
        std::cout << i << ' ';
    std::cout << '\n';

    // Loop 3: Access by forwarding reference (auto&&)
    // - For a non-const lvalue container, 'auto&&' deduces to 'int&'
    // - This allows modification of elements
    for (auto&& i : v)
        std::cout << i << ' ';
    std::cout << '\n';

    // Create a const reference to the vector
    const auto& cv = v;

    // Loop 4: Forwarding reference with a const container
    // - Here 'auto&&' deduces to 'const int&' because cv is const
    // - You can read elements but not modify them
    for (auto&& i : cv)
        std::cout << i << ' ';
    std::cout << '\n';

    // Loop 5: The range expression can be a braced initializer list
    // - This creates a temporary std::initializer_list<int>
    for (int n : {0, 1, 2, 3, 4, 5})
        std::cout << n << ' ';
    std::cout << '\n';

    // Loop 6: The range expression can also be a plain array
    int a[] = {0, 1, 2, 3, 4, 5};
    for (int n : a)
        std::cout << n << ' ';
    std::cout << '\n';

    // Loop 7: Variable can be unused — [[maybe_unused]] suppresses compiler warnings
    // - Here, we ignore 'n' and just print 1 each iteration
    for ([[maybe_unused]] int n : a)
        std::cout << 1 << ' ';
    std::cout << '\n';

    // Loop 8: C++20 feature — init-statement in a range-based for loop
    // - 'auto n = v.size();' runs once before iteration starts
    // - Then, for each element 'i', we print '--n + i'
    for (auto n = v.size(); auto i : v)
        std::cout << --n + i << ' ';
    std::cout << '\n';

    // Loop 9: C++20 feature — typedef declaration as init-statement
    // - 'typedef decltype(v)::value_type elem_t;' declares elem_t = int
    // - 'elem_t i : v' declares i as int in the loop
    for (typedef decltype(v)::value_type elem_t; elem_t i : v)
        std::cout << i << ' ';
    std::cout << '\n';
}
