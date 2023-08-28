#include "node.h"

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <dirent.h>
#include <unistd.h>

int main(int argc, char **argv) {

    if(argc != 2) {
        printf("BAD");
    }
    char *path_name = argv[1];

    // Initial code used to test database
    FILE *f = fopen("../database/load_testretriever.sql", "w+");
    FILE *q = fopen("../database/queries_testretriever.sql", "w+");
    struct dirent* file;
    struct stat file_stat;
    DIR *directory = opendir(path_name);

    fprintf(f, "COPY Files FROM stdin USING DELIMITERS ':';\n");

    while((file = readdir(directory)) != NULL) {
        char *filename = file->d_name;

        if(strcmp(filename, ".") != 0 && strcmp(filename, "..") != 0 && strcmp(filename, ".DS_Store") != 0) {
            char path[4096] = "";
            strcat(path, path_name);
            strcat(path, filename);
            if(stat(path, &file_stat) == 0) {
                int filesize = file_stat.st_size;
                fprintf(q, "INSERT INTO Files (filename, filesize) VALUES ('%s':%d);\n", filename, filesize);
            } else {
                printf("%s\n", path);
                perror("Error with stat");
            }
        }
    }

    fclose(f);
    return 0;
}
