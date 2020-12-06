#include "AdjList.h"

// O(1)
bool AdjList::addVertext() {
    vector<int> vertext = vector<int>();
    this->list.push_back(vertext);
    return true;
}

// O(n^2)
bool AdjList::removeVertext(int vertextNum) {
    this->list.erase(this->list.begin()+ vertextNum);

    int size = this->list.size();
    for(int i = 0; i < size; i++) {
        vector<int> vertext2 = this->list[i];
        int pos = -1;
        for (int i = 0; i < vertext2.size() ; i++) {
            if(vertext2[i] == vertextNum) {
                pos = i;
                break;
            }
        }
        if(pos >= 0) {
            this->list[i].erase(this->list[i].begin() + pos);
        }
    }
    return true;
}

bool AdjList::addEdge(int vertexNum1, int vertexNum2) {
    this->list[vertexNum1].push_back(vertexNum2);
    this->list[vertexNum2].push_back(vertexNum1);
    return true;
}

// O(2n)
bool AdjList::removeEdge(int vertexNum1, int vertexNum2) {

    vector<int> vertext1 = this->list[vertexNum1];
    int pos = -1;
    for (int i = 0; i < vertext1.size() ; i++) {
        if(vertext1[i] == vertexNum2) {
            pos = i;
            break;
        }
    }
    this->list[vertexNum1].erase(this->list[vertexNum1].begin() + pos);
    // vertext1.erase(vertext1.begin() + pos);

    vector<int> vertext2 = this->list[vertexNum2];
    pos = -1;
    for (int i = 0; i < vertext2.size() ; i++) {
        if(vertext2[i] == vertexNum1) {
            pos = i;
            break;
        }
    }
    this->list[vertexNum2].erase(this->list[vertexNum2].begin() + pos);
    // vertext2.erase(vertext2.begin() + pos);x
    return true;
}

void AdjList::show() {
    int size = this->list.size();
    for (int i = 0; i < size; i++) {
        cout << i << "-> ";
        int adjEdgeSize = this->list[i].size();
        for (int j = 0; j < adjEdgeSize; j++) {
            cout << this->list[i][j] << ",";
        }
        cout << endl;
    }
}