- https://www.cs.usfca.edu/~galles/visualization/Algorithms.html
- https://www.toptal.com/developers/sorting-algorithms
- http://bigocheatsheet.com/

This all applies for arrays, but for linked list, since you do not have a locality of reference in memory, merge sort is much better than quick sort. It avoids the need for the auxiliary space, and becomes a simple, reliably O(N log N) sorting algorithm. And as an added bonus, it's stable too.

### Insertion sort, Selection sort, Bubble sort

1. Insertion Sort: use for nearly sorted. it is used as a base for Timsort in combination with merge sort
- sorts everything to the left of current index. compares 2 elements, if not in correct order swaps indexes until correct for left side.
- Worst case time O(n^2), better than merge sort for very small sets
- best method to sort when data is already sorted
- Space complexity O(1)
- Stable
- Adaptive: O(n) time when nearly sorted
- Very low overhead

2. Selection Sort: never use unless high cost of swaps
- Not stable
- O(1) extra space
- Θ(n2) comparisons always
- Θ(n) swaps
- Not adaptive
- take the current element and exchange it with the smallest element on the right hand side of the current element.
-  minimizing the number of swaps. In applications where the cost of swapping items is high, selection sort very well may be the algorithm of choice.

3. Bubble Sort: never use it
- Stable
- O(1) extra space
- O(n2) comparisons and swaps
- Adaptive: O(n) when nearly sorted

### Merge Sort, Quicksort

1. Merge Sort:
-  best when the input is large
- Stable
- Θ(n) extra space for arrays
- Θ(lg(n)) extra space for linked lists
- Θ(n·lg(n)) time
- Not adaptive
- Does not require random access to data

2. Quick Sort:
- choose a pivot
- recurssiion
- swap pivot with
- Not stable
- O(lg(n)) extra space
- O(n2) time, but typically O(n·lg(n)) time
- Not adaptive
https://medium.com/human-in-a-machine-world/quicksort-the-best-sorting-algorithm-6ab461b5a9d0


Binary Search

Breadth First Search (BFS)

Depth First Search (DFS)

Lee algorithm | Shortest path in a Maze

Flood fill Algorithm

Floyd’s Cycle Detection Algorithm

Kadane’s algorithm

Longest Increasing Subsequence

Inorder, Preorder, Postorder Tree Traversals

### Heap Sort
- max heap: max value is root node, all parents are greater than children, complete binary tree
- min heap: same as max, but parents are minimum values
- use when you care about the worst case more than average case runtime over quicksort
- O(n·log(n)) time always
- not stable
- O(1) space which gains benefit over merge sort

1. Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be performed in the bottom up order.
2. If the parent node is stored at index `i`, the left child can be calculated by 2 * `i` + 1 and right child by 2 * `i` + 2 (assuming the indexing starts at 0).

Topological Sorting in a DAG

Disjoint-Set Data Structure (Union-Find Algorithm)

Kruskal’s Algorithm for finding Minimum Spanning Tree

Single-Source Shortest Paths — Dijkstra’s Algorithm

All-Pairs Shortest Paths — Floyd Warshall Algorithm

Suffix tree: Useful for string operations
Locating a substring if a certain number of mistakes are allowed, locating matches for a regular expression pattern etc. Suffix trees also provide one of the first linear-time solutions for the longest common substring problem. These speedups come at a cost: storing a string's suffix tree typically requires significantly more space than storing the string itself.


Timsort is a hybrid sorting algorithm, derived from merge sort and insertion sort
