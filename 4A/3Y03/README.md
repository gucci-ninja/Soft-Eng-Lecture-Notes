# 3Y03 Statistics and Probability

## Day 1 - Sept 4, 2019
- assignments due Thursdays midnight
- Test 1 - Mon Sept 30
- https://www.childsmath.ca/childsa/forms/3yStuff/student_admin.php

### Intro
- Statistics is roughly the science and application of collecting andanalyzing data and inferring information from possibly incomplete data sets
- Probability is the mathematics of random events
- Probability Theory (2.1) in textbook
- an experiment is anything that produces data
- a random experiment is one which can produce different outcomes each time that you run it
    - ex flip a coin, roll a die
    - check the temperature
#### Sample Spaces
- Defn: A sample space, S, is the set of all possible outcomes of the given experiment
    - ex flipping a coin: S = {H, T}
    - sample space for rolling a die: S = {1..6}
- sample spaces can be
    - discrete i.e - finite sample spaces, countably infinite
    - continuous i.e contains n interval of the real number R
        - eg checking temperature S = {x>=0 : x ∈ R}

#### Tree diagrams for visualizing saple spaces
- Experiment: flip the coins consecutively
    - possible outcomes: HTH, TTT, ...

```
         .
       /   \
      H     T
    /  \   / \
   H   T  H   T 
```
- possible outcomes for 2 flps is 4 outcomes

#### Events
- Say in the last example, we are interested in the outcomes such that there are two H's.

{ HHH,...} excludes { TTT, TTH, THT, HTT}

- Such a set is called an event
- Defn: An event is a subset of a sample space E ⊆ S

#### Construting Events
- we have orpeatins to construct evtns from others
    1. Union: GIven E1 and E2 events, the union E1 U E2 := {x: x ∈ E1 or x ∈ E2} is an event
        - Ex: S = {1..6}
        - E1 = {2,3,5} E2 = {5,6} then E1 U E2 = {2,3,5,6}
    2. Intersection: Given E1 and E2 events, the intersection E1 ⋂ E2 = {x: x ∈ E1 and x ∈ E2} is an event
        - Ex: E1={2,3,5}, E2={5,6}, E1 ⋂ E2 = {5}
    3. Complementation: Given E ⊆ S, E' = {x ∈ S: x is not in E} is an even
        - Ex If E = {1,2,3} S = {1..6} then E' = {4,5,6}
    - Note: in some cases people write E<sup>C</sup> or E'
    - Note: E U E' = S, S' = {} = Ø


## Day 2 - Sept 5, 2019

### Event Operations
- Recall that, given a sample space S, an event is a subset E ⊆ S
- Definition: Two events E1 and E2 are mutually exclusive if E1 ⋂ E2 = Ø (they have nothing in common)
- We have laws concerning the operatins U, ⋂, '
    1. (E')' = E
    2. Distributivity
        - i. (A U B) ⋂ C = (A ⋂ C) U (B ⋂ C)
        - ii. (A ⋂ B) U C = (A U C) ⋂ (B U C)
    3. DeMorgans Laws
        - i. (A U B)' = A' ⋂ B' if you take a union and a complement, you flip the union
        - ii. (A ⋂ B)' = A' U B'

### Counting Techniques (aka Combinatorial Analysis)

#### Basic Counting Principle
- suppose you have r-many experiments. say for 1 <= i <= r, the ith experiment has n<sub>i</sub> many possible outcomes. Then the total # of outcomes is the product

```
multiply ni starting at i=1 up to r, which is = n1 * n2 * ... nr
```

#### Simple Example
- tossing a coin 3 times
- 2 * 2 * 2 = 8 outcomes

#### Realistic Example
- a single game of OLG Lotto Max consists of choosing 7 numbers each from 1-50
- so 7 slots, each with 50 options
- 50<sup>7</sup> possible outcomes
- 781 250 000 000 outcomes

### Permutations
- consider the set {a, b, c}
- how many ways can we arrange the letters?
- abc, acb, bac, bca, cab, cba (6 permutations)
- general situation: n objects -> n!
- fun fact - 52! is more than the number of particles
- consider we have n objects but we want to permute r of them
- so the number of ways to permute r objects chosen from set of n objects is \frac{n!}{(n-r)!}


