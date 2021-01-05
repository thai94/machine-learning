Problem

You are given a set of jobs.
Each job has a defined deadline and some profit associated with it.
The profit of a job is given only when that job is completed within its deadline.
Only one processor is available for processing all the jobs.
Processor takes one unit of time to complete a job.

Sulution

1) Sort all jobs in decreasing order of profit. 
2) Iterate on jobs in decreasing order of profit.For each job , do the following : 
a)Find a time slot i, such that slot is empty and i < deadline and i is greatest.Put the job in 
this slot and mark this slot filled. 
b)If no such i exists, then ignore the job. 