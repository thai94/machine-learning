#include "AdjMatrix.h"

bool AdjMatrix::addVertext() {
    int size = this->v + 1;
    for(int i = 0; i < size; i++) {
        this->matrix[this->v][i] = 0;
        this->matrix[i][this->v] = 0;
    }
    this->v = size;
    return true;
}

bool AdjMatrix::removeVertext(int vertextNum) {

    for(int i = 0; i < this->v; i++) {
        this->matrix[vertextNum][i] = -1;
        this->matrix[i][vertextNum] = -1;
    }
    return true;
}

bool AdjMatrix::addEdge(int vertexNum1, int vertexNum2) {
    this->matrix[vertexNum1][vertexNum2] = 1;
    this->matrix[vertexNum2][vertexNum1] = 1;
    return true;
}

bool AdjMatrix::removeEdge(int vertexNum1, int vertexNum2) {
    this->matrix[vertexNum1][vertexNum2] = 0;
    this->matrix[vertexNum2][vertexNum1] = 0;
    return true;
}

void AdjMatrix::show() {
    for (int i = 0; i < this->v; i++) {
        for (int j = 0; j < this->v; j++) {
            cout<< this->matrix[i][j] << " ";
        }
        cout << endl;
    }
}