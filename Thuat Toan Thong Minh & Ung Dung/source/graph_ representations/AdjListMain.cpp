#include <iostream>
#include "AdjList.cpp"

using namespace std;

int main() {

    AdjList adjList = AdjList();
    adjList.addVertext();
    adjList.addVertext();
    adjList.addVertext();

    adjList.addEdge(0, 1);
    adjList.addEdge(0, 2);
    adjList.addEdge(2, 1);
    adjList.show();

    adjList.removeEdge(0, 1);
    adjList.show();

    adjList.removeVertext(2);
    adjList.show();
    return 0;
}