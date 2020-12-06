#include <iostream>
#include "AdjMatrix.cpp"

using namespace std;

int main() {

    AdjMatrix adjMatrix = AdjMatrix();
    adjMatrix.addVertext();
    adjMatrix.addVertext();
    adjMatrix.addVertext();

    adjMatrix.addEdge(0, 1);
    adjMatrix.addEdge(2, 2);

    adjMatrix.removeEdge(2, 2);
    adjMatrix.removeVertext(1);

    adjMatrix.show();
    return 0;
}