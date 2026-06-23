cmake_minimum_required(VERSION 3.20)

# Project configuration
project(fmt_example LANGUAGES CXX)

# Require C++20 standard
set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

# Find the fmt library (assumes it is installed or available as a subdirectory)
# If fmt is not installed system‑wide, you can add it as a submodule or use FetchContent.
include(FetchContent)
FetchContent_Declare(
    fmt
    GIT_REPOSITORY https://github.com/fmtlib/fmt.git
    GIT_TAG 12.2.0
)
FetchContent_MakeAvailable(fmt)

# Add the example source
add_executable(example example.cpp)

# Link fmt library
target_link_libraries(example PRIVATE fmt::fmt)

# Enable the new C11 type‑safe API (fmt 12.2 provides it by default)
# No extra compile definitions are required; the header provides the API.

# Optional: enable warnings and treat them as errors
if(MSVC)
    target_compile_options(example PRIVATE /W4 /WX)
else()
    target_compile_options(example PRIVATE -Wall -Wextra -Werror)
endif()
