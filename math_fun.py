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


def selectionSort(items):
    for i in range(len(items)):
        min_idx = i
        for j in range(i+1, len(items)):
            if items[min_idx] > items[j]:
                min_idx = j
        items[i], items[min_idx] = items[min_idx], items[i]
    return items

def insertionSort(items):
    for i in range(1, len(items)):
        current = items[i]
        j = i - 1
        while j >=0 and current <= items[j]:
            items[j+1] = items[j]
            j -= 1
        items[j+1] = current
    return items

class QuickSort():
    def partition(self, items, low, high):
        i = low - 1
        pivot = items[high]
        for j in range(low, high):
            if items[j] <= pivot:
                i = i+1
                items[i],items[j] = items[j],items[i]
        items[i+1],items[high] = items[high],items[i+1]
        return i+1

    def sort(self, items, low, high):
        if low < high:
            partition = self.partition(items, low, high)
            self.sort(items, low, partition - 1)
            self.sort(items, partition + 1, high)

    def quickSort(self, items):
        self.sort(items, 0, len(items)-1)
        return items

def mergeSort(items):
    if len(items) >1:
        mid = len(items)//2 #Finding the mid of the items
        L = items[:mid] # Dividing the items elements
        R = items[mid:] # into 2 halves

        mergeSort(L) # Sorting the first half
        mergeSort(R) # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                items[k] = L[i]
                i+=1
            else:
                items[k] = R[j]
                j+=1
            k+=1

        # Checking if any element was left
        while i < len(L):
            items[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            items[k] = R[j]
            j+=1
            k+=1
    return items

def countingSort(items, maxval=5):
    m = maxval + 1
    count = [0] * m               # init with zeros
    for a in items:
        count[a] += 1             # count occurences
    i = 0
    for a in range(m):            # emit
        for c in range(count[a]): # - emit 'count[a]' copies of 'a'
            items[i] = a
            i += 1
    return items

items = [5,4,3,2,1]
print("selection sort", selectionSort(items))
print("insertion sort", insertionSort(items))
print("quick sort", QuickSort().quickSort(items))
print("merge sort", mergeSort(items))
print("counting sort", countingSort(items))

