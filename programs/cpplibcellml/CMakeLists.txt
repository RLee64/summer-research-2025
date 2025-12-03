cmake_minimum_required(VERSION 3.10.2)

project("libCellML Testing" VERSION 0.1.0)

find_package(libCellML REQUIRED)

add_executable(simpleProcessing simpleProcessing.cpp)
target_link_libraries(simpleProcessing PUBLIC cellml)
