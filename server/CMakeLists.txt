cmake_minimum_required(VERSION 3.21)
project(Heroidle)

set(CMAKE_CXX_STANDARD 17)

include(conan.cmake)

include_directories(src)
add_subdirectory(src)

option(RUN_TESTS "Build the tests" ON)
if(RUN_TESTS)
    enable_testing()
    add_subdirectory(ut)
endif()
