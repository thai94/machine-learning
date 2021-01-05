#include<iostream>
#include<algorithm>
using namespace std;

struct Edge {
    int src;
    int dest;
    int weight;
};

struct Graph {
    int V; // number of vertices
    int E; // number of edges

    Edge* edge;
};

Graph* createGraph(int V, int E) {
    Graph* graph = new Graph();
    graph->V = V;
    graph->E = E;
    graph->edge = new Edge[E];

    return graph;
}

int find(int subset[], int i) {
    if(subset[i] == -1) {
        return i;
    }
    return find(subset, subset[i]);
}

void doUnion(int subset[], int x, int y) {
    subset[x] = y;
}

int myComp(const void* a, const void* b) {
    Edge* a1 = (Edge*)a;
    Edge* b1 = (Edge*)b;
    return a1->weight > b1->weight;
}

void KruskalMST(Graph* graph) {
    int V = graph->V;
    Edge result[V];

    qsort(graph->edge, graph->E, sizeof(graph->edge[0]),
          myComp);
    
    int* subset = new int[graph->V];
    for (int i = 0; i < graph->V; i++) {
        subset[i] = -1;
    }

    int e = 0;
    for (int i = 0; i < graph->E; i++) {
        int x = find(subset, graph->edge[i].src);
        int y = find(subset, graph->edge[i].dest);

        if(x != y) {
            result[e] = graph->edge[i];
            e++;
            doUnion(subset, x, y);
        }
    }

    for (int i = 0; i < e; i++) {
        cout << result[i].src << " - " << result[i].dest << ":" << result[i].weight << endl;
    }
}

int main() {
    int V = 4; // Number of vertices in graph
    int E = 5; // Number of edges in graph
    Graph* graph = createGraph(V, E);

    // add edge 0-1
    graph->edge[0].src = 0;
    graph->edge[0].dest = 1;
    graph->edge[0].weight = 10;
 
    // add edge 0-2
    graph->edge[1].src = 0;
    graph->edge[1].dest = 2;
    graph->edge[1].weight = 6;
 
    // add edge 0-3
    graph->edge[2].src = 0;
    graph->edge[2].dest = 3;
    graph->edge[2].weight = 5;
 
    // add edge 1-3
    graph->edge[3].src = 1;
    graph->edge[3].dest = 3;
    graph->edge[3].weight = 15;
 
    // add edge 2-3
    graph->edge[4].src = 2;
    graph->edge[4].dest = 3;
    graph->edge[4].weight = 4;
 
   
    // Function call
    KruskalMST(graph);
 
    return 0;
}