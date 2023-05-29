#include "node.h"

Node node_create(char *pathName, char *fileName, int size, int permissions, bool isDirectory) {
    Node newNode = (Node) malloc(sizeof(NodeObj));

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

//-------------------------------- Accessor Functions ---------------------------------------
char *getPath(Node n) {
    return n->pathName;
}

char *getFileName(Node n) {
    return n->fileName;
}

int getSize(Node n) {
    return n->size;
}

int getPermissions(Node n) {
    return n->permissions;
}

bool isDir(Node n) {
    return n->isDirectory;
}