# 0x08-making_change
In this project I learnt problem-solving using dynamic programming.

## Understanding the Problem
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount **total**.
* We may assume that we have an infinite supply of each kind of coin with the value coins[0] to coins[n-1]. If the total cannot be met by any number of coins, return -1.

### Example 1

**input**: coins[] = [10, 5, 2], total = 30, Output: 3

**Explanation**: Minimum 3 coins required: we use 3 coins of value 10.

### Example 2**
**input**: coin[] = [1,3,5,7], total = 18, Output: 4
**Explanation**: Minimum 4 coins required: We use any one of these combinations to provide change using 4 coins:(7,7,3,1),(5,5,5,1) and (5,5,5,3) respectively.

## Solutions
**Why NOT the Recursive approach**
The time complexity of the recursive solution was exponential and space complexity was way greater than O(n). Because the running time of my solution was been evaluated, I decided to make my algorithm more efficient by using the DP approach.

**Why the Dynamic programming method**
Since many subproblems have to be solved again and again, that makes the **making change** problem to have both the **optimal substructure** and **overlapping subproblems** properties of a dynamic programming problem..

* **solution file**
[0-making_change.py](./0-making_change.py): File containing the makeChange implementation.

** DP bottom-up approach**
This is a dynamic programming problem, we can solve it using the bottom-up approach. The idea is to calculate the solution of the smaller problems in an iterative way and store their result in a table.

### Time and space complexity analysis
There are two nested loops in the [code](./0-making_change.py). The frst loop is iterating from 1 to total(T) and the second is iterating from 0 to size(s) - 1. Time Complexity = O(Ts).
Space complexity = O(T), for extra array change[] of size T + 1.

Author: Sangwani PZ
