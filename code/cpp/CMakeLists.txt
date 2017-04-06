cmake_minimum_required(VERSION 3.7)
project(cpp)

set(CMAKE_CXX_STANDARD 14)

#set(SOURCE_FILES main.cpp basics/vectors_in_cpp.cpp basics/animal.cpp basics/animal.h basics/if-else.cpp)
#add_executable(cpp ${SOURCE_FILES})

#set(SOURCE_FILES_if_else basics/if-else.cpp)
#add_executable(cpp ${SOURCE_FILES_if_else})

set(SOURCE_FILES_test basics/constructors.cpp)
add_executable(cpp ${SOURCE_FILES_test})