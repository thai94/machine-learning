#include <iostream>
using namespace std;

void printMaxActivities(int s[], int f[], int n)  {
    int choose = 0;
    cout << "(" << s[choose] << ";";
    cout << f[choose] << ")";

    for (int j = choose + 1; j < n; j++) {
        if(s[j] >= f[choose]) {
            cout << "(" << s[choose] << ";";
            cout << f[choose] << ")";

            choose = j;
        }
    }
}

int main()
{
    int s[] =  {1, 3, 0, 5, 8, 5}; 
    int f[] =  {2, 4, 6, 7, 9, 9}; 
    int n = sizeof(s)/sizeof(s[0]); 
    printMaxActivities(s, f, n); 
    return 0;
}