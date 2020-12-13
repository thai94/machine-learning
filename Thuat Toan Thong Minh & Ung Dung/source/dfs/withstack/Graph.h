#include <iostream>
#include <list>
#include <stack>
#include <algorithm>
using namespace std;

class Graph {
    private:
        int v; // vertex
        list<int>* adj;
        void PrintState(list<int> state);
    public:
        Graph(int V);
        void addEdge(int v, int w);
        int DFS(int start, int goal);
};