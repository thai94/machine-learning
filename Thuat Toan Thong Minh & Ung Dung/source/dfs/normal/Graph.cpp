#include "Graph.h"

Graph::Graph(int v) {
    this->v = v;
    adj = new list<int>[v];
}

void Graph::addEdge(int v, int w) {
    this->adj[v].push_back(w);
}

void Graph::DfsUtils(int v, bool visited[]) {
    cout << v << " -> ";
    visited[v] = true;
    list<int>::iterator i;
    for (i = this->adj[v].begin(); i != this->adj[v].end(); ++i) {
        if(!visited[*i]) {
            this->DfsUtils(*i, visited);
        }
    }
}

void Graph::DFS(int v) {
    bool* visited = new bool[v];
    for (int i = 0; i < v; i++) {
        visited[i] = false;
    }

    this->DfsUtils(v, visited);
}