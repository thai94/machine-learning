#include<iostream>
#include<queue>
using namespace std;

struct HuffmanNode {
    char data;
    unsigned int freq;
    HuffmanNode* left;
    HuffmanNode* right;

    HuffmanNode(char data, unsigned int freq) {
        this->data = data;
        this->freq = freq;
        this->left = this->right = NULL;
    }
};

// For comparison of 
// two heap nodes (needed in min heap) 
struct compare {
  
    bool operator()(HuffmanNode* l, HuffmanNode* r) 
  
    { 
        return (l->freq > r->freq); 
    } 
}; 

// The main function that builds a Huffman Tree and 
// print codes by traversing the built Huffman Tree 
HuffmanNode* HuffmanCodes(char data[], int freq[], int size) {
    // Create a min heap & inserts all characters of data[] 
    priority_queue<HuffmanNode*, vector<HuffmanNode*>, compare> minHeap;

    for (int i = 0; i < size; i++) {
        minHeap.push(new HuffmanNode(data[i], freq[i]));
    }

    HuffmanNode* left;
    HuffmanNode* right;
    HuffmanNode* top;
    while(minHeap.size() >= 1) {
        left = minHeap.top();
        minHeap.pop();
        right = minHeap.top();
        minHeap.pop();

        top = new HuffmanNode('$', left->freq + right->freq);
        top->left = left;
        top->right = right;

        minHeap.push(top);
    }

    return minHeap.top();
}

void PrintCodes(HuffmanNode* huffmanTree, string str) {
    if(huffmanTree == NULL) {
        return;
    }

    if(huffmanTree->data != '$') {
        cout << huffmanTree->data << ": " << str << endl;
    }

    PrintCodes(huffmanTree->left, str + '0');
    PrintCodes(huffmanTree->right, str + '1');
}

int main() 
{
    char arr[] = { 'a', 'b', 'c', 'd', 'e', 'f' }; 
    int freq[] = { 5, 9, 12, 13, 16, 45 }; 

    int size = sizeof(arr) / sizeof(arr[0]); 
  
    HuffmanNode* huffmanTree = HuffmanCodes(arr, freq, size);
    PrintCodes(huffmanTree, "");

}