cmake_minimum_required(VERSION 3.21)
set(BINARY ${CMAKE_PROJECT_NAME})
set(SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})

add_compile_options(-fconcepts)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

set(SOURCES
        main.cpp

        calculator.hpp
        kingdom.hpp
        player.hpp
        server.cpp
        server.hpp
        timer.hpp
        warehouse.hpp)

add_executable(${BINARY} ${SOURCES})

target_link_libraries(${BINARY} ${CONAN_LIBS})

if(RUN_TESTS)
    add_library(${BINARY}_lib STATIC ${SOURCES})
endif()

