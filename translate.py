import sys
import os
# Read the contents of test.cpp
# Check if the command line argument is provided
if len(sys.argv) < 2:
    print("Please provide a file name as a command line argument.")
    sys.exit(1)

# Get the input file name from the command line argument
input_file = sys.argv[1]

# Open the input file
with open(input_file, 'r') as file:
    content = file.read()

# Replace "Hello World" with "Goodbye World"
new_content = content.replace('Hello, World', 'Goodbye, World')

# Get the output file names
output_ops_file = os.path.splitext(input_file)[0] + '_ops.cpp'
output_kernels_file = os.path.splitext(input_file)[0] + '_kernels.cpp'

# Write the modified content to the output ops file
with open(output_ops_file, 'w') as file:
    file.write(new_content)

# Create an empty output kernels file
with open(output_kernels_file, 'w') as file:
    pass