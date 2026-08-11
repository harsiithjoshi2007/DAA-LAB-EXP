# Experiment 5: Min-Max Value by Divide and Conquer

## Objective
Find the minimum and maximum values in an array using the divide-and-conquer strategy.

## Algorithm
The array is split into halves recursively; each half computes its local min and max, then combined.

## Time Complexity
- O(n)

## Space Complexity
- O(log n) recursion stack

## Conclusion
This method reduces the number of comparisons compared with a naive pairwise scan while maintaining linear time.
