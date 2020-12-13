#include <iostream>
#include <list>
using namespace std;

class Graph {
    private:
        int v; // vertex
        list<int>* adj; 
        void DfsUtils(int v, bool visited[]);
    public:
        Graph(int V);
        void addEdge(int v, int w);
        void DFS(int v);
};