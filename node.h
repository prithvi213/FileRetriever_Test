// node.h (Header for Node ADT)

#ifndef NODE_H
#define NODE_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct NodeObj* Node;

// Define Node Properties
struct NodeObj {
    char *pathName;
    char *fileName;
    int size;
    int permissions;
    bool isDirectory;
    char *extension;
    // Stack *files; /* Stack ADT implementation pending */
} NodeObj;

// Allocation Functions
Node node_create(char *pathName, char *fileName, int size, int permissions, bool isDirectory);
void node_delete(Node *n);

// Accessor Functions
char *getPath();
char *getFileName();
int getSize();
int getPermissions();
bool isDir();
int getExtension();
// Will add getFiles();

// Manipulation Functions (to add later)

#endif