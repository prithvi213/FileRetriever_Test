#include "node.h"

Node *node_create(char *pathName, char *fileName, int size, int permissions, bool isDirectory) {
    Node *newNode = (Node *) malloc(sizeof(Node));

    // Initialize the node variables
    if(newNode != NULL) {
        newNode->pathName = pathName;
        newNode->fileName = fileName;
        newNode->size = size;
        newNode->permissions = permissions;
        newNode->isDirectory = isDirectory;
    }

    return newNode;
}