#include "Graph.h"

Graph::Graph(int v) {
    this->v = v;
    adj = new list<int>[v];
}

void Graph::addEdge(int v, int w) {
    this->adj[v].push_back(w);
}

void Graph::PrintState(list<int> state) {
    list<int>::iterator i;
    for (i = state.begin(); i != state.end(); ++i) {
        cout << *i << " -> ";
    }
}

int Graph::DFS(int start, int goal) {
    queue<int> frontier;
    frontier.push(start);
    list<int> reached;
    reached.push_back(start);
    
    while(frontier.size() != 0) {
        int curState = frontier.front();
        frontier.pop();
        
        list<int>::iterator i;
        for (i = this->adj[curState].begin(); i != this->adj[curState].end(); ++i) {
            if (*i == goal) {
                this->PrintState(reached);
                cout << *i;
                return *i;
            }
            list<int>::iterator findIter = find(reached.begin(), reached.end(), *i);
            if(findIter == reached.end()) {
                reached.push_back(*i);
                frontier.push(*i);
            }
        }
    }
    return -1;
}