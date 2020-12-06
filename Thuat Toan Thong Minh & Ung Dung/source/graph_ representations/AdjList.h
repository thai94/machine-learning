#pragma once

#include <iostream>
#include <vector> 
using namespace std;

class AdjList {
    private:
        vector<vector<int > > list;
    public:
        bool addVertext();
        bool removeVertext(int vertextNum);
        bool addEdge(int vertexNum1, int vertexNum2);
        bool removeEdge(int vertexNum1, int vertexNum2);

        void show();

};