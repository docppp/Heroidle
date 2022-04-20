set(BINARY ${CMAKE_PROJECT_NAME}_tst)
conan_basic_setup()

file(GLOB_RECURSE TEST_SOURCES LIST_DIRECTORIES false *.h *.cpp)

set(SOURCES ${TEST_SOURCES})

add_executable(${BINARY} ${TEST_SOURCES})

target_include_directories(${BINARY} PRIVATE ${SOURCE_DIR}/src)
target_link_libraries(${BINARY} PUBLIC ${CMAKE_PROJECT_NAME}_lib ${CONAN_LIBS})

add_test(NAME ${BINARY} COMMAND ${BINARY})
