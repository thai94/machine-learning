#include "Graph.cpp"

// Driver code
int main()
{
    // Create a graph given in the above diagram
    Graph g(8);
    g.addEdge(0, 1);
    g.addEdge(0, 7);
    g.addEdge(1, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 2);
    g.addEdge(3, 4);
    g.addEdge(4, 3);
    g.addEdge(4, 5);
    g.addEdge(4, 6);
    g.addEdge(6, 4);
    g.addEdge(6, 7);
    g.addEdge(7, 0);
    g.addEdge(7, 6);
 
    cout << "Following is Depth First Traversal"
            " (starting from vertex 2) \n";
    g.DFS(1);
 
    return 0;
}