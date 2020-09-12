# Linear Optimization

## Introduction

input is linearly scaled with output
F(x) = y
F(2x) = 2y

http://www.cas.mcmaster.ca/~deza/secs34O03_20.html

Carlos Suarez - teaches all tutorial

## Lecture 1

### Example

A = { a1,a2,a3,... an }  
ai : integer, ai > 0 for all i  
ai != aj for all i != j

A1 and A2 are partitions of A
(A1 || A2 = A), (A1 && A2 = [])

find minimum difference between A1 and A2

let xi = {1 if **ai in A1** else 0 **if ai in A2** }  
Sum(A1) = Sum(xi \* ai) for 0 < i < n  
Sum(A2) = Sum((1-xi) \* ai) for 0 < i < n

min(abs(Sum(A1)-Sum(A2)))  
= min(abs(Sum(xi \* ai) - Sum((1-xi) \* ai)))  
= min(abs(Sum(xi \* ai - (1-xi) \* ai)))  
= min(abs(Sum(ai \* (xi - (1-xi))))  
= min(abs(Sum(ai \* (2 \* xi - 1))))

scaling xi coefficient by k will also scaled the minimum value by k

## Lecture 2

x is a vector that partitions A into A1

- x = (x1,x2,x3,...,xn)
- xi = {1 if **ai in A1** else 0 **if ai in A2** } for 0 < i <= n

instead of min(abs(Sum(xi \* ai) - Sum((1-xi) \* ai))), we can square the function (Sum(xi \* ai) - Sum((1-xi) \* ai)) \*\* 2. However, we are no longer a linear function.

w.l.o.g.: (without loss of generality) an assumption made that will not add any restrictions to the problem

- Assume A1 is larger than A2.

Question then changes to:

- find minimum sum of A1
- Sum(A1) >= Sum(A2)

Sum(A1) >= Sum(A2)  
Sum(xi \* ai) >= Sum((1-xi) \* ai)  
Sum(xi \* ai) >= Sum(ai) - Sum(xi \* ai)  
2 \* Sum(xi \* ai) >= Sum(ai)  
Sum(xi \* ai) >= 0.5 \* Sum(ai)

- Lets us create a linear equation to solve for x

### Linearizing

to linearize functions, we can set up a set of linear functions.

#### Example

- x^2 + y^2 = 1

we can approximate this circle with:

- x = 1
- x = -1
- y = 1
- y = -1

Thus linearizing the circle

## Lecture 3
<!-- Will write later -->