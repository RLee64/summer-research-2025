cmake_minimum_required(VERSION 3.10.2)

project("libCellML Testing" VERSION 0.1.0)

find_package(libCellML REQUIRED)

add_executable(simpleProcessing simpleProcessing.cpp)
target_link_libraries(simpleProcessing PUBLIC cellml)

add_executable(symtest symtest.cpp)
target_link_libraries(symtest PUBLIC "C:/symengine/lib/symengine.lib")
target_include_directories(symtest PUBLIC "C:/symengine/include")
target_link_libraries(symtest PUBLIC "C:/gmp/lib/gmp.lib")
target_include_directories(symtest PUBLIC "C:/gmp/include")

add_executable(testCopies testCopies.cpp)
target_link_libraries(testCopies PUBLIC cellml)