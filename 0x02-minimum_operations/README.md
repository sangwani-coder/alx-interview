# 0x02. Minimum Operations
## Problem
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
## Solution
**Depth-First-Search**
I solved this interview questions by using **Depth-First-Search**.
The Depth-First Search is a recursive algorithm that uses the concept of backtracking. It involves thorough searches of all the nodes by
going ahead if potential, else by backtracking. Here, the word backtrack means once you are moving forward and there are not any more nodes
along the present path, you progress backward on an equivalent path to seek out nodes to traverse. All the nodes are progressing to be visited on
the current path until all the unvisited nodes are traversed after which subsequent paths are going to be selected.

## Solution File:
[x] [0-minoperations.py](./0-minoperations.py)