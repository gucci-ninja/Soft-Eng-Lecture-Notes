# Algorithms and Data Structures

## Fundamentals

### Basic Programming Model
- will be using Java and libraries provided by Princeton University
- starting with language constructs, we should be aware that Java classes have the following 7 components
    1. [primitive data types](#primitive-data-types-and-expressions)
    2. [statements](#statements)
    3. [arrays](#arrays)
    4. [static methods](#static-methods)
    5. [strings](#strings)
    6. [input/output](#input-and-output)
    7. data abstraction
- compiling in a virtual terminal involves the commands ```javac program.java```, which gives us the class file that contains bytecode and then ```java program``` allows us to run it

#### Primitive Data Types and Expressions
- integers (```int```), real numbers (```double```), booleans (```boolean```) and characters (```char```)
- in Java there are _variables_, named with _identifiers_, which we can make _expression_ with by using _operators_ and _literals_
- type conversion: normally numbers are promoted so that information is not lost (int + double = double)
- there is also casting, which is a directive to use a certain data type
- comparisons are ==, !=, <, <=, >, >=
- Java's int has 2<sup>32</sup> different values so it can be represented in a 32-bit machine word

Type | Bits
-----|-----
int | 32
double | 64
long | 64
short | 16
char | 16
byte | 8
float | 32

#### Statements
- declarations
- assignments
- conditionals
- loops
- break and continue - exits loop or continues to net iteration of loop
- calls
- returns

#### Arrays
- stores values that are all the same type
- in Java you decalre the array name and type, create the array and then initialize its values
- size is fixed and bound checking is automatic, throws ```ArrayIndexOutOfBoundsException```
- aliasing - an array name refers to the whole array so if you declare array A and then make array B = A, whatever changes you make to B will reflect in A

```
double[] a = new double[n]
int[] a = { 1, 2, 3 }

// 2D
double[][] = new double[m][n]
```

#### Static Methods
- properties
    - arguments passed by value
    - method names can be overloaded (same name and different signatures)
    - single return value but multiple return statements
    - doesn't need to have a return, signature instead includes ```void```
```
public static double method(double c) {
    t = 1e-15;
    return t;
}
```
- recursion
    - base case
    - address subproblems

#### APIs
- Java libraries
- standard libraries found on [here](https://algs4.cs.princeton.edu/)
- your own libraries

#### Strings
- concatentation
- conversion with ```toString()```
- automatic conversion
- command-line arguments using ```parseInt``` for example

#### Input and Output
- commands and arguments ```% java RandomSeq args[0]```
- standard I/O
- formatted output using %, number indicates the number of spaces, negative for the right side and .2 indicates 2 decimal places
- redirection and piping

```
% java Average < data.txt
data.txt --> std input --> Average

% java RandomSeq 1 2 3 > data.txt
RandomSeq --> std input --> data.txt

% java RandomSeq 1 2 3 | java Average
```
- input/output from a file
- standard drawing

#### Q&A 1
- ```Double.POSITIVE_INFINITY``` (or negative) is a built-in constant
- 1/0 gives a runtime exception, 1.0/0.0 gives ```Infinity```
- we use && and || because & and | are bitwise operators that do AND, OR or exclusive or (^)

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
