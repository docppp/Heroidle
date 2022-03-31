cmake_minimum_required(VERSION 3.21)
project(Heroidle)

set(CMAKE_CXX_STANDARD 17)
add_subdirectory(libs/cppzmq)

add_executable(Heroidle
        main.cpp resource.hpp)

find_package(cppzmq)
target_link_libraries(Heroidle cppzmq)
