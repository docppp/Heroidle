#include <chrono>
#include <thread>
#include <iostream>
#include <ctime>
#include "resource.hpp"

int main()
{
    auto x = std::chrono::steady_clock::now() + std::chrono::milliseconds(1000);
    std::chrono::time_point<std::chrono::system_clock> time_point;

    time_point = std::chrono::system_clock::now();
    std::time_t ttp = std::chrono::system_clock::to_time_t(time_point);
    std::cout << std::ctime(&ttp);

    std::this_thread::sleep_until(x);

    time_point = std::chrono::system_clock::now();
    std::time_t ttp2 = std::chrono::system_clock::to_time_t(time_point);
    std::cout << std::ctime(&ttp2);
}
