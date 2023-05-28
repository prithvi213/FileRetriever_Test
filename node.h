#pragma once

#ifndef NODE_H
#define NODE_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <stdbool.h>

typedef struct Node Node;

// Define Node Properties
struct Node {
    char *pathName;
    char *fileName;
    int size;
    int permissions;
    bool isDirectory;
    char *extension;
    // Stack *files; /* Stack ADT implementation pending */
};

// Allocation Functions
Node *node_create();
void node_delete(Node **n);

// Accessor Functions
char *getPath();
char *getFileName();
int getSize();
int getPermissions();
bool isDir();
int getExtension();
// Will add getFiles();

// Manipulation Functions (to add later)