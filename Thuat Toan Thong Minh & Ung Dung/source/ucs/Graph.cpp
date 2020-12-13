#include "Graph.h"

Graph::Graph(int v) {
    this->v = v;
    adj = new list<pair<int, int> >[v];
}

void Graph::addEdge(int v, int w, int cost) {
    this->adj[v].push_back(make_pair(w, cost));
}

void Graph::PrintState(list<pair<int, int > > state, int cost) {
    list<pair<int, int > >::iterator i;
    for (i = state.begin(); i != state.end(); ++i) {
        cout << "(" << (*i).first << "," << (*i).second << ")" << " -> ";
    }

    cout << " : " << cost;
}

class MyCompare
{
public:
    bool operator() (pair<int, int > e1, pair<int, int > e2)
    {
        return e1.second > e2.second;
    }
};

int Graph::UCS(int start, int goal) {

    int cost = INT_MAX;
    priority_queue<pair<int, int >, vector<pair<int, int > >, MyCompare> frontier;
    frontier.push(make_pair(start, 0));
    list<pair<int, int > > reached;

    while(frontier.size() != 0) {
        pair<int, int> curState = frontier.top();
        frontier.pop();
        reached.push_back(curState);

        if (curState.first == goal) {
            if(curState.second < cost) {
                cost = curState.second;
            }
            this->PrintState(reached, curState.second);
            cout << endl;
            return cost;
        }

        list<pair<int, int > >::iterator i;
        for (i = this->adj[curState.first].begin(); i != this->adj[curState.first].end(); ++i) {
            frontier.push(make_pair((*i).first, curState.second + (*i).second));
        }
    }

    return -1;
}