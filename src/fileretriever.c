#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *f = fopen("../datafiles/load_testretriever.sql", "w+");
    fprintf(f, "COPY Files FROM stdin USING DELIMITERS '|';\n");
    char *filename[3] = {"a.text", "b.xls", "c.csv"};
    int filesize[3] = {10, 3, 4};

    for(int i = 0; i < 3; i++) {
        fprintf(f, "%s|%d\n", filename[i], filesize[i]);
    }

    fprintf(f, "\\.\n");
    fclose(f);
    return 0;
}
