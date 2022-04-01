cmake_minimum_required(VERSION 3.21)
project(Heroidle)

set(CMAKE_CXX_STANDARD 17)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_executable(Heroidle
        main.cpp
        resource.hpp
        timer.hpp)

find_package(cppzmq)
target_link_libraries(Heroidle ${CONAN_LIBS})
