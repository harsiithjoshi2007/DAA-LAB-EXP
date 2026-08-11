# Experiment 3: Minimum Spanning Tree Algorithms

## Objective
Implement and compare Kruskal's and Prim's algorithms for finding a minimum spanning tree.

## Algorithm Overview
- Kruskal sorts all edges and selects the lowest-weight non-cyclic edges.
- Prim grows a spanning tree from the smallest vertex by adding the least-cost adjacent edge.

## Time Complexity
- Kruskal: O(E log E)
- Prim: O(E log V) with a priority queue

## Space Complexity
- O(V + E)

## Conclusion
Both algorithms produce the same MST cost, but their implementations and performance differ depending on graph density.
