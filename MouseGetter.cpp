#include <iostream>
#include <fstream>
#include <string>

int main()
{

    std::ofstream outfile ("test.txt");
    outfile << "my text here1" << std::endl;

    for (std::string line; std::getline(std::cin, line);)
    {
        outfile <<"CPPGOT: " << line << "\n";
        outfile.flush();
    }
    outfile.close();
    return 0;
}