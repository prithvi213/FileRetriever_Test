#include "node.h"

#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <string.h>
#include <dirent.h>

#define ABSOLUTE_FILEDIR_PATH "/Users/prithvi/Library/CloudStorage/OneDrive-Personal/desktop_clutter/FileRetriever_Test/testfiles/"

int main(void) {
    // Initial code used to test database
    FILE *f = fopen("../database/load_testretriever.sql", "w+");
    struct dirent* file;
    struct stat file_stat;
    DIR *directory = opendir(ABSOLUTE_FILEDIR_PATH);

    fprintf(f, "COPY Files FROM stdin USING DELIMITERS '|';\n");

    while((file = readdir(directory)) != NULL) {
        char *filename = file->d_name;

        if(strcmp(filename, ".") != 0 && strcmp(filename, "..") != 0 && strcmp(filename, ".DS_Store") != 0) {
            char path[100] = "";
            strcat(path, "../../testfiles/");
            strcat(path, filename);
            if(stat(path, &file_stat) == 0) {
                int filesize = file_stat.st_size;
                fprintf(f, "%s|%d\n", filename, filesize);
            } else {
                printf("%s\n", path);
                perror("Error with stat");
            }
        }
    }

    


    //char *filename[3] = {"a.text", "b.xls", "c.csv"};
    //int filesize[3] = {10, 3, 4};

    /*for(int i = 0; i < 3; i++) {
        fprintf(f, "%s|%d\n", filename[i], filesize[i]);
    }*/

    fprintf(f, "\\.\n");
    fclose(f);
    return 0;
}
