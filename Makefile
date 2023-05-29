CC = clang
CFLAGS = -g -Wall -Werror -Wextra -Wpedantic

# Make all the files
all:

# Remove all binary/executables
clean:

# Format files
format:

scan-build: clean
	scan-build make