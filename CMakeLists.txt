cmake_minimum_required(VERSION 3.15) # Adjust the version according to your needs
project(YourProjectName VERSION 1.0 LANGUAGES CXX)

# Ensure the build system can find the Python interpreter
find_package(Python REQUIRED COMPONENTS Interpreter)

# Define the original source, the python script, and the names of the generated files
# Use absolute paths for the source file and the script
set(ORIGINAL_SOURCE ${CMAKE_CURRENT_SOURCE_DIR}/test.cpp)
set(PYTHON_TRANSLATION_SCRIPT ${CMAKE_CURRENT_SOURCE_DIR}/translate.py)
set(GENERATED_SOURCES ${CMAKE_CURRENT_BINARY_DIR}/test_ops.cpp ${CMAKE_CURRENT_BINARY_DIR}/test_kernels.cpp)

# Custom command to generate test_ops.cpp and test_kernels.cpp from test.cpp
add_custom_command(
  OUTPUT ${GENERATED_SOURCES}
COMMAND ${CMAKE_COMMAND} -E copy_if_different ${ORIGINAL_SOURCE} ${CMAKE_CURRENT_BINARY_DIR}/test.cpp
  COMMAND ${Python_EXECUTABLE} ${PYTHON_TRANSLATION_SCRIPT} ${CMAKE_CURRENT_BINARY_DIR}/test.cpp ${GENERATED_SOURCES}
  DEPENDS ${ORIGINAL_SOURCE}
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  COMMENT "Generating source-to-source translation"
)

# Add the executable target that compiles the original and generated sources
add_executable(${PROJECT_NAME} ${GENERATED_SOURCES})

# Set the C++ standard for the project
set_target_properties(${PROJECT_NAME} PROPERTIES
  CXX_STANDARD 17
  CXX_STANDARD_REQUIRED YES
  CXX_EXTENSIONS NO
)

# If you have additional include directories or need to link libraries, specify them here
# target_include_directories(${PROJECT_NAME} PRIVATE some/include/directories)
# target_link_libraries(${PROJECT_NAME} some_libraries)
