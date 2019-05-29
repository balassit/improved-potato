# Complexity

## Big O Notation

- language and metric we use to describe the efficiency of algorithms.

1. big O: upper bound
2. big Ω: lower bound
3. big Ѳ: both O and Ω. Tight bound on runtime

Best case
Worst case
Expected case

O(g(n)) =  upper bound - c*g(n)
Omega(g(n)) = lower bound - c*g(n)
Theta
### Data Structure Complexity

Excellent - O(log(n)) O(1)
Good - O(n)
Fair - O(n*log(n))
Bad - O(n^2)
Horrible - O(n^2) O(n!)

http://bigocheatsheet.com/

## Recurssion


## Big O Examples

[details of complexity](https://rob-bell.net/2009/06/a-beginners-guide-to-big-o-notation)

1. O(1) - constant time. Requires 1 step.
  - Ex. print statement of user input
2. O(log(n)) - for each step rule out half of what the input is. Problem space becomes much smaller with every single pass
  - Ex. binary search
3. O(n) - lineary time. As many as there are inputs
  - Ex. iterate over an array
3. O(n*log(n)) - iterate over but compare sets to rule out half of input at a time.
  - Ex. update all records in a list to be sorted
  - comparison based sorts worst case
4. O(n^2) - iterate over list by the square of input
  - Ex. double for loop
5. O(2^n) - exponential function
  - Ex. recursive calculation of Fibonacci numbers
6. O(n!) - factorial based. Iterate
  - Ex. List all permutations of an array