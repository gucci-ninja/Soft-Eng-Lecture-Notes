# Algorithms and Data Structures

## Fundamentals

**algorithm** : a finite, deterministic and effective problem-solving method

gcd

```
gcd(x, y):
    if y == 0:
        return x
    
```

### Basic Programming Model
- will be using Java and libraries provided by Princeton University
- let's start by defining language constructs, features and libraries

### Data Abstraction
- here we will be defining _abstract data types_ (ADTs) in modular programming
- ADT's are implemented in Java by specifying an _applications programming interface_ (API) and then making a Java class to be used by clients

### Bags, Queues, and Stacks
- these are 3 fundamental ADTs you will encounter
- we will define their APIs and implementations using arrays, resizing arrays and linked list as our models
- these will come in handy when you implement algorithms in the future

### Analysis of Algorithms
- you may have heard of Big O notation and runtime complexity because performance is an important attribute for an algorithm
- we use a scientific method to find out how an algorithm performs
    1. develop hypotheses
    2. create mathematical models
    3. run experiments
    4. test
    5. repeat as necessary

### Case Study: Union Find
