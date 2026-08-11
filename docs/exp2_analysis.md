# Experiment 2: Comparative Analysis of String Matching Algorithms

## Objective
Compare naive, Rabin-Karp, and KMP string matching algorithms.

## Algorithms
- Naive matching checks every window one by one.
- Rabin-Karp uses rolling hash values.
- KMP uses prefix-function matching to skip unnecessary comparisons.

## Time Complexity
- Naive: O(nm)
- Rabin-Karp: O(n + m) average, O(nm) worst-case
- KMP: O(n + m)

## Space Complexity
- Naive: O(1)
- Rabin-Karp: O(1)
- KMP: O(m)

## Conclusion
KMP is best for large-scale matching when pattern length is relevant because of its linear-time behavior.
