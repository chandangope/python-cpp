cmake_minimum_required(VERSION 3.5)

project(py_c)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")
set(CMAKE_BUILD_TYPE Release)
IF(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)
  SET(CMAKE_INSTALL_PREFIX .. CACHE PATH "default install path" FORCE)
ENDIF(CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT)



#Bring the headers
include_directories(
	./
	)

#Sources
file(GLOB SOURCES
	./mylib.c
	)

MESSAGE("SOURCES = ${SOURCES}")

#Generate the shared library
add_library(py_c SHARED ${SOURCES})

#Set the location for library installation
install(TARGETS py_c DESTINATION c_lib)
