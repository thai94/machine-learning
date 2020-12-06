#pragma once

#include <iostream>
using namespace std;

class AdjMatrix {
    private:
        int matrix[100][100];
        int v;
    public:
        bool addVertext();
        bool removeVertext(int vertextNum);
        bool addEdge(int vertexNum1, int vertexNum2);
        bool removeEdge(int vertexNum1, int vertexNum2);

        void show();
};