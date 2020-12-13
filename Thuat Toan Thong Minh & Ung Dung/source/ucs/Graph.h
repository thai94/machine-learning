#include <iostream>
#include <list>
#include <queue>
using namespace std;

class Graph {
    private:
        int v; // vertex
        list<pair<int, int > >* adj;
        void PrintState(list<pair<int, int > >, int cost);
    public:
        Graph(int V);
        void addEdge(int v, int w, int cost);
        int UCS(int start, int goal);
};