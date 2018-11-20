# Python Notes
```
import this
```

## Dicts

- As of python 3.5+, a dict maintains order so you do not need to sort to iterate in order

## Strings

## Indexing and Splicing

## List Methods

## Date Formatting

## Class methods

__repr__

__str__

__init__

__slots__

### generator expression

## Pythonic Code

1. Dictionairies for performance

- significant performance difference over list 

2. Memory efficiency with slots

- allows you to explicitly state which instance attributes you expect your object instances to have, with the expected results:
  - faster attribute access.
  - space savings in memory.
- stores outside the instance, only one (immutable) cannot change values once the class is created
- no new properties but can do all other things that a class can do while saving 50% memory 

https://stackoverflow.com/questions/472000/usage-of-slots

3.  Merging Dictionaries

- copy
- list comprehension
-   {**a, **b, **c} # merges values of a list using kwargs (python 3.5+ )

4. yield

- Yield: this requires no extra runtime memory! The iteration process uses the magic behind yield, which "freezes" the state (call stack, "instruction pointer", etc) when it returns the result, and continues from the exact place it last was, when the iterator protocol asks for the next value.

def generate_fib():
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, nxt + current
        yield current

5. lambdas

expression similar to creating a function
lambda x: x % 6 == 0 # numbers divisible by 6
list_of_words.sort(lambda w: w.lower()) # sort lowercase 

# iterators must implement __iter__ and __next__ called iterator protocol
# We use the next() function to manually iterate through all the items of an iterator.
# When we reach the end and there is no more data to be returned, it will raise StopIteration. 
# iterate over a sorted list and return the items 
def __iter__(self):
    for i in sorted(self.items, key = lambda x: x.price):
        yield i


This is how a for loop actually works
# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

The advantage of using iterators is that they save resources. Like shown above, we could get all the odd numbers without storing the entire number system in memory. We can have infinite items (theoretically) in finite memory. Easiest way is to use a generator with yield