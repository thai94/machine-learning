#include "Graph.cpp"

// Driver code
int main()
{
    // Create a graph given in the above diagram
    Graph g(7);
    g.addEdge(0, 1, 5);
    g.addEdge(0, 5, 10);
    g.addEdge(1, 2, 2);
    g.addEdge(1, 4, 1);
    g.addEdge(2, 5, 4);
    g.addEdge(3, 1, 1);
    g.addEdge(3, 4, 4);
    g.addEdge(4, 5, 3);
    g.addEdge(6, 0, 3);
    g.addEdge(6, 3, 2);

    g.UCS(6, 5);
    return 0;
}