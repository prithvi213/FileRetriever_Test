#include "node.h"

#include <stdio.h>
#include <stdlib.h>

int main() {
    // Initial code used to test database
    /*FILE *f = fopen("../datafiles/load_testretriever.sql", "w+");
    fprintf(f, "COPY Files FROM stdin USING DELIMITERS '|';\n");
    char *filename[3] = {"a.text", "b.xls", "c.csv"};
    int filesize[3] = {10, 3, 4};

    for(int i = 0; i < 3; i++) {
        fprintf(f, "%s|%d\n", filename[i], filesize[i]);
    }

    fprintf(f, "\\.\n");
    fclose(f);*/

    // Test out node creation and properties
    Node N = node_create("a", "b", 50, 2, false, "c");

    printf("Node path name: %s\n", getPath(N));
    printf("Node file name: %s\n", getFileName(N));
    printf("Node size: %d\n", getSize(N));
    printf("Node permissions: %d\n", getPermissions(N));
    printf("Node is directory: %d\n", isDir(N));
    printf("Node extension: %s\n", getExtension(N));
    return 0;
}
