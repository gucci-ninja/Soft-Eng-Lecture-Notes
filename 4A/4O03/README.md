# Linear Optimization

## Introduction
input is linearly scaled with output
F(x) = y
F(2x) = 2y

http://www.cas.mcmaster.ca/~deza/secs34O03_20.html

Carlos Suarez - teaches all tutorial

### Example
A = { a1,a2,a3,... an }  
ai : integer, ai > 0 for all i  
ai != aj for all i != j

A1 and A2 are partitions of A
(A1 || A2 = A), (A1 && A2 = [])

find minimum difference between A1 and A2

let xi = {1 if **ai in A1** else 0 **if ai in A2** }  
Sum(A1) = Sum(xi * ai)        for 0 < i < n  
Sum(A2) = Sum((1-xi) * ai)    for 0 < i < n

min(abs(Sum(A1)-Sum(A2)))  
=   min(abs(Sum(xi * ai) - Sum((1-xi) * ai)))  
=   min(abs(Sum(xi * ai - (1-xi) * ai)))  
=   min(abs(Sum(ai * (xi - (1-xi))))  
=   min(abs(Sum(ai * (2 * xi - 1))))

adding a coefficient k to the equation will change the minimum value but won't change the partitions that will create the minimum (not completely sure what happened here :camel:)