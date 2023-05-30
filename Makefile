CC = clang
CFLAGS = -g -Wall -Werror -Wextra -Wpedantic

all: fileretriever

fileretriever: fileretriever.o
	$(CC) $(CFLAGS) -o fileretriever $^

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f fileretriever *.o

format:
	$(CC)-format -i -style=file *.[ch]

scan-build: clean
	scan-build make