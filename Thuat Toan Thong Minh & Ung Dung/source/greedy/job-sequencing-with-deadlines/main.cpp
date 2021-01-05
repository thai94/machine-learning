#include <iostream>
using namespace std;

struct MyJob
{
    int jobId;
    int deadline;
    int profit;
};

bool myComparison(MyJob a, MyJob b)
{
    return (a.profit > b.profit);
}

bool comparisonByDeadline(MyJob* a, MyJob* b)
{
    return (a->deadline > b->deadline);
}

int findSlot(int *timeSlot, int n, int deadline)
{
    deadline = deadline - 1;
    if (timeSlot[deadline] == -1)
    {
        return deadline;
    }

    for (int j = deadline; j >= 0; j--)
    {
        if (timeSlot[deadline] == -1)
        {
            return j;
        }
    }

    return -1;
}

int *jobSequencing(MyJob *jobList, int n, int &resultNum)
{
    // Sort all jobs according to decreasing order of prfit
    sort(jobList, jobList + n, myComparison);

    resultNum = 0;
    for (int i = 0; i < n; i++) {
        if(jobList[i].deadline > resultNum) {
            resultNum = jobList[i].deadline;
        }
    }

    int *timeSlot = new int[resultNum];
    for (int i = 0; i < resultNum; i++)
    {
        timeSlot[i] = -1;
    }

    for (int i = 0; i < n; i++)
    {
        int slotIdx = findSlot(timeSlot, resultNum, jobList[i].deadline);
        if (slotIdx != -1)
        {
            timeSlot[slotIdx] = jobList[i].jobId;
        }
    }

    return timeSlot;
}

void test1()
{

    int n = 4;
    MyJob* jobList = new MyJob[n];

    MyJob job1 = MyJob();
    job1.jobId = 1;
    job1.deadline = 4;
    job1.profit = 20;
    jobList[0] = job1;

    MyJob job2 = MyJob();
    job2.jobId = 2;
    job2.deadline = 1;
    job2.profit = 10;
    jobList[1] = job2;

    MyJob job3 = MyJob();
    job3.jobId = 3;
    job3.deadline = 1;
    job3.profit = 40;
    jobList[2] = job3;

    MyJob job4 = MyJob();
    job4.jobId = 4;
    job4.deadline = 1;
    job4.profit = 30;
    jobList[3] = job4;

    int jobSeqSize = 0;
    int *jobSeqOrder = jobSequencing(jobList, n, jobSeqSize);
    for (int i = 0; i < jobSeqSize; i++)
    {
        if (jobSeqOrder[i] != -1)
        {
            cout << jobSeqOrder[i] << " -> ";
        }
    }
}
int main()
{
    test1();
    return 0;
}