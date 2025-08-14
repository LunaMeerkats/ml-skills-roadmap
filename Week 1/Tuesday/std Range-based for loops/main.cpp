#include <iostream>
#include <map>
#include <string>
#include <string_view>
#include <algorithm>   // ok to keep; erase_if for map is declared in <map>
#include <version>     // for feature-test macro __cpp_lib_erase_if

void print_map(std::string_view comment, const std::map<std::string, int>& m)
{
    std::cout << comment;
    for (const auto& [key, value] : m)
        std::cout << '[' << key << "] = " << value << "; ";
    std::cout << '\n';
}

int main()
{
    std::map<std::string, int> m{{"CPU", 10}, {"GPU", 15}, {"RAM", 20}};

    print_map("1) Initial map: ", m);

    m["CPU"] = 25;
    m["SSD"] = 30;
    print_map("2) Updated map: ", m);

    std::cout << "3) m[UPS] = " << m["UPS"] << '\n'; // inserts "UPS" with value 0
    print_map("4) Updated map: ", m);

    m.erase("GPU");
    print_map("5) After erase: ", m);

    for (auto it = m.begin(); it != m.end(); ) {
    if (it->second > 25)
        it = m.erase(it);
    else
        ++it;
    }


    print_map("6) After manual erase: ", m);
    std::cout << "7) m.size() = " << m.size() << '\n';

    m.clear();
    std::cout << std::boolalpha << "8) Map is empty: " << m.empty() << '\n';
}
