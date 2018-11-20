import functools
import operator

num = 4


def fib(n):
    current, nxt = 0, 1
    for i in range(n):
        yield current
        current, nxt = nxt, current + nxt


print("fibonacci")
print(list(fib(num)))


def factorial_nums(n):
    for i in range(n):
        yield i + 1


factorial = lambda n: functools.reduce(operator.mul, factorial_nums(n))

print("factorial")
print(factorial(num))


def squares(n):
    square, prev_x = 0, 0
    for x in range(n):
        square = square + x + prev_x
        yield square
        prev_x = x


print("squares")
print(list(squares(num)))


def sum(n):
    return int(n * (n + 1) / 2)


print("sum")
print(sum(num))


def sum_of_squares(n):
    return int(n * (n + 1) * (2 * n + 1) / 6)


print("sum of squares")
print(sum_of_squares(num - 1))


def list_of_sum(n):
    for i in range(n):
        yield sum_of_squares(i)


print("list of squares sums")
print(list(list_of_sum(num)))
