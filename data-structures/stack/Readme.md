# Stack

## Linked List

- each node has additional space to maintain pointer to previous and next item
- push and pop are O(1)

## Array

- push an element in amortized O(1)
- Because allocations are infrequent and accesses are fast, dynamic arrays are usually faster than linked lists.

## What do I use???
The break-even point beyond which the array-based implementation of a list is more space efficient than the linked-list: n>D*E/(P+E), where D is the length of the array-based list, E is the size of a data element, and P is the size of a pointer.

### Linked list space efficency is greater when the size of an item varies or is unknown

ex. 1 (choose array)

```
D = 10
E = 1
P = 1
n > 10/(2) = 5
```

ex. 2 (choose linked list)

```
D = 100
E = 100
P = 1
n > 100/(101) ~= 1
```