# Formal Methods of Software Design

| Date                 | Segments                                                               | Subsections                                          | Exercises                            | Test                       |
| -------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------ | -------------------------- |
| Tuesday September 15 | **Segments 0 and 1**                                                   | Subsection 1.0.1                                     | 0, 2, 14, and 17                     | No                         |
| Friday September 18  | **Segments 2 and 3**                                                   | Section 2.1                                          | 6fmps, 7c, 22, 49, and 53            | No                         |
| Tuesday September 22 | **Segment 4**.                                                         | end of Chapter 2                                     | 62                                   | Practice Test. 3:30        |
| Friday September 25  | **Segments 5 and 6**; **Segment 7** (about using a list as a function) | end of Chapter 3 ~~Sections 3.2 and 3.4~~ (optional) | 64 and 73                            | No                         |
| Tuesday September 29 |                                                                        |                                                      |                                      | Today is Test 0. 4:30-5:20 |
| Friday October 2     | **Segment 8**                                                          | Subsection 4.0.1                                     | 116                                  | No                         |
| Tuesday October 6    | **Segments 9 and 10**                                                  | Section 4.1                                          | 137, 142, 143                        | No                         |
| Friday October 9     | **Segment 11**                                                         | Subsection 4.2.2                                     | 156                                  | No                         |
| Tuesday October 20   | **Segment 12**                                                         | Subsection 4.2.5, but you can skip Subsection 4.2.3  | 186                                  | No                         |
| Friday October 23    | **Segment 13**                                                         | Section 4.2                                          | 189                                  | No                         |
| Tuesday October 27   | **Segments 14 and 15**                                                 | Section 5.1                                          | 252 and 297                          | No                         |
| Friday October 30    | **Segment 16**                                                         | Section 5.2                                          | 242a using a for-loop                | No                         |
| Tuesday November 3   | **Segment 17**                                                         | No readings                                          | 237                                  | Test 1. 4:30-5:20          |
| Friday November 6    | ~~Segments 18, 19, 20, and 21~~ **Segments 22 and 23**                 | end of Chapter 6                                     | 356 and 370abc                       | No                         |
| Tuesday November 10  | **Segment 24**                                                         | Section 7.0                                          | 387                                  | No                         |
| Friday November 13   | **Segment 25**                                                         | Section 7.1                                          | 400                                  | No                         |
| Tuesday November 17  | **Segment 26**                                                         | Subsection 7.2.0                                     | 423                                  | No                         |
| Friday November 20   | **Segment 27**                                                         | Subsection 7.2.3. You can skip Subsection 7.2.4      | 427                                  | No                         |
| Tuesday November 24  |                                                                        |                                                      |                                      | Test 2. 4:30-5:20          |
| Friday November 27   | **Segment 28**                                                         | Section 8.0                                          | 435                                  | No                         |
| Tuesday December 1   | **Segment 29**                                                         | end of Chapter 8                                     | 444                                  | No                         |
| Friday December 4    | ~~Segments 30, 31, and 32~~ **Segment 33**                             | You should review the course                         | 256; course evaluation questionnaire | No                         |
| December 10-23       |                                                                        |                                                      |                                      | Final Exam                 |

---

## Symbols

| Symbol | Definition                    | <!--shortcut (dev only)--> |
| ------ | ----------------------------- | -------------------------- |
| ⊥      | Antitheorem (False, Bottom)   | <!-- T -->                 |
| ⊤      | Theorem (True, Top)           | <!-- F -->                 |
| ¬      | Negation (not)                | <!-- not  -->              |
| ∧      | Conjuction (and)              | <!-- and  -->              |
| ∨      | Disjuction (or)               | <!-- or  -->               |
| ⇒      | implies                       | <!-- implies  -->          |
| ⇐      | implied by                    | <!-- implied  -->          |
| ⧧      | unequal                       | <!-- unqual  -->           |
| ×      | multiply                      | <!-- times  -->            |
| ‘      | intersection(bunch)           | <!-- inter  -->            |
| ¢      | size, cardinality(bunch)      | <!-- cent  -->             |
| \$     | size, cardinality(set)        | <!--$-->                   |
| ϟ      | power(set)                    | <!-- sPower  -->           |
| ∪      | union                         | <!--   -->                 |
| ∩      | intersect                     | <!--   -->                 |
| ⊇      |                               | <!--   -->                 |
| ⊆      |                               | <!--   -->                 |
| ↔      | string length                 | <!-- sLen  -->             |
| ⊲      | string modifier (old string)  | <!-- sModL  -->            |
| ⊳      | string modifier (new element) | <!-- sModR  -->            |
| 〈     | function scope (start)        | <!-- fs-->                 |
| 〉     | function scope (end)          | <!-- fe-->                 |
| →      | list modifier/mapping         | <!-- map  -->              |
| ☐      | function domain               | <!-- fDom  -->             |
| ∀      | for all (quantifier)          | <!-- forall  -->           |
| ∃      | there exists (quantifier)     | <!--  exists -->           |
| Σ      | sum (quantifier)              | <!--  sum -->              |
| ∏      | product (quantifier)          | <!-- product  -->          |
| §      | solution (quantifier)         | <!--  sol -->              |
| σ      |                               | <!--   -->                 |
| ʹ      |                               | <!--   -->                 |
| ⦂      |                               | <!--   -->                 |

---

## Segment 0

programs are:

- commands to a computer
  - execution
- mathematical expressions
  - theory of programming

why theory?

- proof, calculation, precision, understanding
- theory = formalism + rules of proof, calculation, manipulation

formal != careful, detailed
formal = formulas (mathematical expressions)

informal != sloppy, sketchy
informal = using natural language (English)

Project:

- always starts informal (with discussion)
- always ends formal (with program)

testing:
how do you know if program if working
what about the inputs you didn't test

proof tells whether program is correct for all inputs

program development, with proof at each step
program modification, with proof

### Other Theories

Hoare triples

- first
  Model checking
- used the most in industry
- exhaustive automated testing
- up to 10^60 states ~~ 2^200 states = 200 bits ~~ 6 variables
  - not very special
- abstraction, proof if state space is too large

### Our Theory

- simplier
  - just binary (boolean) expressions
- more general
  - includes terminating and nonterminating computation
  - includes sequential and parallel computation
  - inclues stand-alone and interactive computation
  - inclues time and space bounds and real time
  - includes probabilistic computations
- prerequisite
  - language with assignment and if statement

## Segment 1

### Introduction of math using in the course

- Binary Theory
  - binary expressions: represents anything that comes in two kinds
    - statements about the world
    - digital circuits
    - human behavior
  - theorems: represents one kind
    - representing true statements
    - circuits with low voltage
    - innocent behavior
  - antitheoem: represents teh other kind
    - representing false statemetns
    - circuits with high voltage
    - guilty behavior

### Operators

- 0 operands
  - **⊤** True (Top)
  - **⊥** False (Bottom)
- 1 operand
  - 4 operators exist
  - **¬** not (negation)
- 2 operands
  - 16 operators exist
  - **∧** and (conjucts)
    - gives the minimum of the two values
  - **∨** or (disjuncts)
    - gives the maximum of the two values
  - **⇒** implies (left is falser than or equal to right)
    - left is antecent
    - right is consequent
  - **⇐** implied by (left is truer or equal to right)
    - left is consequent
    - right is antecent
  - **=** equals
  - **⧧** unequal (xor)
- 3 operands
  - 256 operators
  - **if then else fi** conditional operation
- precedence and parenthese
- associative operators: ∧, ∨, =, ⧧
  - x ∨ y ∨ z means **(x ∨ y) ∨ z** or **x ∨ (y ∨ z)**
- continuing operators: ⇒, ⇐, =, ⧧
  - x = y = z means **x = y** ∧ **y = z**
  - x ⇒ y ⇒ z means (x ⇒ y) ∧ (y ⇒ z)
    - = takes precedence over ∧ but ⇒ does not
- big operator
  - same as regular operator but later precedence
  - written to be bigger than regular counterpart

### Truth Tables

- ⊤ represents an entire theorem
- ⊥ represents an entire antitheorem

#### 1 operand

| --  | ⊤   | ⊥   |
| --- | --- | --- |
| ¬   | ⊥   | ⊤   |

#### 2 operands

| --  | ⊤⊤  | ⊤⊥  | ⊥⊤  | ⊥⊥  |
| --- | --- | --- | --- | --- |
| ∧   | ⊤   | ⊥   | ⊥   | ⊥   |
| ∨   | ⊤   | ⊤   | ⊤   | ⊥   |
| ⇒   | ⊤   | ⊥   | ⊤   | ⊤   |
| ⇐   | ⊤   | ⊤   | ⊥   | ⊤   |
| =   | ⊤   | ⊥   | ⊥   | ⊤   |
| ⧧   | ⊥   | ⊤   | ⊤   | ⊥   |

#### 3 operands

| --              | ⊤⊤⊤ | ⊤⊤⊥ | ⊤⊥⊤ | ⊤⊥⊥ | ⊥⊤⊤ | ⊥⊤⊥ | ⊥⊥⊤ | ⊥⊥⊥ |
| --------------- | --- | --- | --- | --- | --- | --- | --- | --- |
| if then else fi | ⊤   | ⊤   | ⊥   | ⊥   | ⊤   | ⊥   | ⊤   | ⊥   |

### Variables

- used for substitution(instantiation)
- add parenthses to maintain precedence
  - x ∧ y
  - x = ⊤
  - y = ⊤ ∧ ⊥
  - x ∧ y = ⊤ ∧ (**⊤ ∧ ⊥**)

### new binary expressions

- applications will supply its own binary expression

  - (the grass is green)
  - 1 + 1 = 2

- consistent: no binary expression is both a theorem and antitheorem
  - (no overclassified expression)
  - required
- complete: every binary expression is either a theorem or antitheorem
  - (no unclassified expression)
  - not required

### Proving

- deciding whether a binary expression is a theorem or antitheorem
- simplifying to True
- **Axiom Rule**

  - if a binary expression is an axiom, then it is a theorem
  - if a binary expression is an antiaxiom, then it is an antitheorem
  - example
    - parallel lines never meet
      - this isn't true in every form of mathematics
      - made into an axiom so it represents the truth
  - axioms describe the rules of the world that it is in
    - x + y = y + x
      - represents truth in an application where order of adding does not affect end quantity
      - is a axiom
      - is a theorem
      - is equivalent to ⊤
    - axiom: ⊤
    - antiaxiom: ⊥
    - axiom: (the grass is green)
    - antiaxiom: (the sky is green)
    - axiom: (intelligent messages are coming from space) implies (there is life elsewhere in the universe)

- **Evaluation Rule**

  - if all the binary subexpressions of a binary expression are classified, the binary expression is classified using the truth table
    - x ∨ y
    - x = ⊤
    - y = ⊥
    - x ∨ y is a theorem as ⊤ or ⊤ = ⊤

- **Completion Rule**

  - if a binary expression contains unclassified binary subexpressions, and all ways of classifying them place it in the same class, it is in that class
    - x ∨ ⊤
      - can only be a theorem despite one subexpression (x) not known

- **Consistency Rule**

  - if a classified binary expression contains binary subexpressions and there is only one consistent way to classify them, they are classified that way
    - x = ⊤
    - x ⇒ y = ⊤
    - y = ⊤ as
      - if y = ⊥, then x ⇒ y = ⊥.
      - That would be **inconsistent**.

- **Instance Rule**

  - if a binary expression is classified as a theorem or antitheorem
    - all its instances have that same classification
    - axiom: x=x
    - theorem: x=x
    - theorem: (⊤ = (⊥ ∨ ⊥)) = (⊤ = (⊥ ∨ ⊥))

- **Classical Logic**: using all 5 rules
- **Constructive Logic**: not using Completion Rule
- **Evaluation Logic**: not using the Completion Rule nor Consistency Rule

### Formatting

- space subexpressions with less precedence bigger
  - a∧b ∨ c
- newline at main connective
- brackets should start and end at the same line as a subexpression
- continuing expression should have hints explaining why one expression is equal to the next expression

## Segment 2

### Monotonicity and Antimonotonicity

| Monotonicity                                               | Antimonotonicity                                           |
| ---------------------------------------------------------- | ---------------------------------------------------------- |
| x &le; y ⇒ f(x) &le; f(y)                                  | x &le; y ⇒ f(x) &ge; f(y)                                  |
| x ⇒ y <span style="font-size:larger;">⇒</span> f(x) ⇒ f(y) | x ⇒ y <span style="font-size:larger;">⇒</span> f(x) ⇐ f(y) |

- for binary equations, instead of x &le; y, we use **x ⇒ y**
  - aka x is stronger than y
  - aka x is falser than y
- as x gets falser, f(x) goes falser (or equal)

| expression                            | description                        |
| ------------------------------------- | ---------------------------------- |
| ¬ a                                   | antimonotonic in a                 |
| a ∧ b                                 | monotonic in a, monotonic in b     |
| a ∨ b                                 | monotonic in a, monotonic in b     |
| a ⇒ b                                 | antimonotinic in a, monotonic in b |
| a ⇐ b                                 | monotonic in a, antimonotinic in b |
| **if** a **then** b **else** c **fi** | monotonic in b, monotonic in c     |

- useful in proofs

### Context

- a and b are long expressions
- in a ∧ b, when changing a, we can assume b
- in b ∧ a, when changing b, we can assume a
  - if we are right in assumption, good
  - if we are wrong in assumption, answer is ⊥ by default

### Number Theory

- number expression represent quantity
- ∞ may be unfamiliar
- if a then x else y fi
  - a is binary, but x and y are number expressions

### Character Theory

- character written between ""
- left quote: """"
- right quot: """"

## Segment 3

### Collections

- 4 simplest data structures
  - defined by **packaging** and **indexing**

| --     | packaged | indexed |
| ------ | -------- | ------- |
| bunch  | ⊥        | ⊥       |
| set    | ⊤        | ⊥       |
| string | ⊥        | ⊤       |
| list   | ⊤        | ⊤       |

### Bunch Theory

- can be used represent collections
  - simplest
  - no difference between an object and a bunch consisting of only that object
  - any number, character, binary or set is an **elementary bunch**, or **element**
  - operators
    - **,** union
    - **‘** intersection
    - **¢** size, cardinality(number)
      - repeat elements don't change size
        - ¢(1,2,3) = 3 = ¢(1,2,3,1)
    - **:** inclusion(binary)
      - ⊤ if all elements of left are elements of right (subset?)
        - 2:1,2,3 (2 is an element in 1,2,3)
      - acts like &le; and ⇒
- special bunches

| name    | elements                    | description               |
| ------- | --------------------------- | ------------------------- |
| _null_  |                             | empty bunch               |
| _bin_   | ⊤,⊥                         | binary values             |
| _nat_   | 0,1,2,...                   | natural numbers           |
| _int_   | ...,-1,0,1,...              | integers                  |
| _rat_   | ..., -1,0,1/2,...           | rational numbers          |
| _real_  | ..., 2<sup>1/2</sup>,...    | real numbers              |
| _xnat_  | 0,1,2,...,∞                 | extended natural numbers  |
| _xint_  | -∞,...,-1,0,1,...∞          | extended integers         |
| _xrat_  | -∞..., -1,0,1/2,... ∞       | extended rational numbers |
| _xreal_ | -∞..., 2<sup>1/2</sup>,...∞ | extended real numbers     |
| _char_  | ..., "a",..."A",...         | characters                |

- final notation
  - x,..y
    - x to y for x &le; y
  - i: x,..y = x &le; i < y
  - ¢(x,..y) = y-x
- distribution
  - -(1,2,3) = -1, -2, -3
  - (1,2) + (10,20) = 11,12,21,22
  - (1,2) + 10 = 11,12
  - 1 + 10 = 11
  - null + 10 = null
  - ¢ of sum of two bunch is at most the × of ¢ of both bunch

### Set Theory

- operators
  - **{A}** set formation operator
    - performed on a bunch
    - {_null_} empty set (informal)
  - **~S** contents of S
    - undos a set into a bunch
    - ~{1,2,3} = 1,2,3
  - **\$** size cardinality
  - **ϟ** returns a bunch containing power set
    - ϟ{1,2} = {null}, {1}, {2}, {1,2}

## Segment 4

### String Theory

- indexed sequences
- any object is a one item string
- operator
  - _nil_ is empty string
  - **;** join
  - **↔** string length
    - can be placed on string measure ruler
    - indexes go between letters
  - **(S)<sub>i</sub>** is the ith index of string S
    - 0 indexed
    - at index **n**
      - the number of items processed is n
      - next item is item n
    - if i is a string, we get a string of results
      - (0;1;2;3;4;5)<sub>3;5</sub> = 3;5
  - **\*** is a repetition operator
    - 3\*(4;2) = 4;2;4;2;4;2
    - if left is empty, means any number of repititions
      - \*2 = _nil_, 2, 2;2, ...
  - **⊲ i ⊳** modification operator
    - change left element at i to right string
- special ordering of strings
  - lexicographical order
  - 3;6;4;1 < 3;7;12
  - 3;6;4 < 3;6;4;1
  - x;..y means **x to y** for x &le; y
  - ↔(x;..y) = y-x
  - (x;..y) ; (y;..z) = x;..z
- string joins distributes over bunch unions
  - string of bunches = bunch of strings

#### Text

- text is displayed within **""**
  - """Hello"", said Sushi"
  - double quotes require repeated "" within the text
  - can also join all the characters with separate text
- can perform string operators
  - takng an index of string with a string becomes a subtext
    - "01234"<sub>2;..4</sub> = "23"

#### Zero

- invented after
  - natural numbers
  - negative numbers
  - rational numbers
  - irrational numbers
- widely used arouind 1000 years ago
- still not used very well
  - "there are **a number** of things to discuss"
    - meaning non-zero
  - taxes and other documentations sometimes requires writing _nil_ instead of 0
  - keyboards and telephones have zero after 9
  - Time differences sometimes have **N/A** or **0** instead of 0
    - or they have to explain zero
- Measuring must start at 0. Counting is measuring
  - octave is an interval of 8, 2 octaves is an interval of 15
    - it starts counting at 1 so its always off by 1
  - AD started counting at year 1, so the difference between year after AD and before BC is off by 1
  - Fortran 1955 loop requires at least once
  - Pascal arrays must have at least 1 element
    - brought back data structure algebra
- first: preceding all others in time, order, importance
  - associated with 1 (1st)
- last: following all others in time, order, importance
- second: following first
- avoid third onwards as they are really associated with the number before

### List Theory

- string in a package
  - not unlike set is a bunch in a package
- operators
  - **[A]** list formation operator
    - also distributes over union of bunches
      - list of bunches = bunch of lists
  - **~[A]** contents of a list
  - **#[A]** length of a list
  - **[A] i** index of a list
    - **[A] [i]** composition of a list
      - returns a new list with elements corresponding to list [i]
  - **[A] ;; [B]** join
  - elements of A followed by elements of B in a string
  - folows lexicographic order **<, >**
  - **i → e | [A]** modification
    - change ith element of A with e
    - 2 → 4 | [10;..15] = [10;11;4;13;14]
    - can have multiple modifications at once
      - done right to left
      - when modifying while referencing self, it is referencing pre-changes
      - Example
        - L = [10;..15]
        - 2 → L3 | 3 → L2 | L &nbsp;&nbsp;&nbsp;&nbsp; // technically referencing L, not itself
        - = 2 → 13 | 3 → 12 | [10;11;12;13;14] &nbsp;&nbsp;&nbsp;&nbsp; // replace references with literal
        - = 2 → 13 | [10;11;12;12;14]
        - = [10;11;13;12;14]
- when indexing a list or string the returning object is equal to the object of the index

| Index                    | Result                                                                        |
| ------------------------ | ----------------------------------------------------------------------------- |
| S<sub>n,m</sub>          | S<sub>n</sub>,S<sub>m</sub>                                                   |
| S<sub>{n,m}</sub>        | {S<sub>n</sub>,S<sub>m</sub>}                                                 |
| S<sub>n;m</sub>          | S<sub>n</sub>;S<sub>m</sub>                                                   |
| S<sub>[n;m]</sub>        | [S<sub>n</sub>;S<sub>m</sub>]                                                 |
| Ln,m                     | Ln,Lm                                                                         |
| L{n,m}                   | {Ln,Lm}                                                                       |
| L(n;m)                   | Ln;Lm                                                                         |
| L[n;m]                   | [Ln;Lm]                                                                       |
| ---                      | ---                                                                           |
| S<sub>0,{1,[2;1];0</sub> | S<sub>0</sub>, {S<sub>1</sub>, [S<sub>2</sub>; S<sub>1</sub>]; S<sub>0</sub>} |
| L(0,{1,[2;1];0)          | L0,{L1,[L2;L1];L0}                                                            |

#### Multidimensional structures

- Array is a multidimensional list
  - we want to index using list operators
  - A i j...
    - i will give content at index i (usually a list)
    - j will give content of i at index j
    - etc.
  - if A was 2 dimensions
    - i will give a list
    - j would give an element
  - if we use bunch notation
    - A (i,j) = A i, A j = 2 lists
    - A [i,j] = [A i, A j] = a new array

## Segment 5

### Functions

- **〈_v:D → b_〉**
  - "map _v_ in _D_ to _b_"
  - _v_ variable name
  - _D_ domain,type (a bunch)
  - _b_ body (may use _v_)
    - what is returned
  - _v:D_ is a local axiom within _b_
- operators
  - **〈〉** function scopes
    - renaming just requires equal to same function with different variable name
  - **☐** returns domain of function
  - **_f x_** applying function _f_ to _x_
    - f of x
    - can be (f) x or f (x) but in isolation, wouldn't matter
    - substitute _v_ in _f_ to _x_
  - **f|g** selective union of functions _f_ and _g_
    - ☐(f|g) = ☐ f, ☐ g
    - (f|g) x = if x: ☐ f then f x else g x fi
- 2 variable functions
  - f = 〈_x:D →_ 〈_y:D → x &le; y_〉〉
  - f 3 = 〈_y:D → 3 &le; y_〉
  - f 3 5 = 3 &le; 5
  - f (3,5) = f 3, f 5
    - since function distributes over bunch
- predicate
  - function returns binary (⊤,⊥)
- relation
  - function returns predicate
- abbreviated function notations
  - 〈_x:D →_ 〈_y:D → x &le; y_〉〉= 〈_x,y:D → x &le; y_〉
    - multiple variables
  - 〈_n:nat → n+1_〉 = 〈_n: → n+1_〉
    - only use when domain is known or doesn't matter
  - 〈_n: 2 → 3_〉 = _2 → 3_
    - constant function
    - scope brackets used with variables

#### Scope and Substitution

- local
  - bound, hidden, private
  - introduced in expression (formal)
- non-local
  - global, free, visible, public
  - introduced outside expression (formal or informal)

## Segment 6

### Quantifiers

- operator that applies to a funct ion
  - defined from a two-operand symmetric associative operator
  - **∀** for all
    - binary result
    - defined from ∧
    - ∀〈_r:rat → r>0 ∨ r=0 ∨ r<0_〉
      - every number r in rational domain is less than 0, equal to or greater than 0
  - **∃** there exists
    - binary result
    - defined from ∨
    - ∃〈_n: nat → n=0_〉
      - there exists a number n in natural domain equal to 0
  - **Σ** sum of
    - numerical result
    - defined from +
    - Σ〈_n:nat+1 → 1/2<sup>n</sup>_〉
      - 1/2+1/4+1/8+...=1
  - **∏** product of
    - numerical result
    - defined from ×
      - ∏〈_n:nat+1 → (4×n<sup>2</sup>)/(4×n<sup>2</sup>-1)_〉
        - 4/3×16/15×36/35×...=π/2

#### abbreviations

- no scope operators (〈〉)
- → replaced by •
  - ∀*r:rat • r>0 ∨ r=0 ∨ r<0*
  - Σ*n:nat+1 • 1/2<sup>n</sup>*
    <br/><br/>
- group variables with the same domain together into a bunch
  - ∀*x,y:rat • x=y+1 ⇒ x>y* **=** ∀*x:rat •* ∀*y:rat • x=y+1 ⇒ x>y*
  - Σ*n,m:0,..10 • n×m* **=** Σ*x:rat •* Σ*m:0,..10 • n×m*

### Defining own quantifier

- need to define the axioms for
  - empty domain
  - single domain
  - union domain
- example, **_MAX_**
  - _MAX x:rat • 4timesx-x<sup>2</sup>_ = 4
  - _MAX v:null • n_ = -∞
    - or most negative number possible in context
  - _MAX v:x • n_ = 〈_v:x → n_〉 x
  - _MAX v:A,B • n_ = _max (MAX v:A • n) (MAX v:B • n)_

### Solution Quantifier

- **§** is the solution (bunch) of predicate
  - solves for the variable
  - examples
    - §_i:int • i<sup>2</sup>=4_ = -2,2
    - §_n:nat • n<5_ = 0,..5
  - default as bunch equations
  - applying set operators ({}) gives set equations
    - {§_i:int • i<sup>2</sup>=4_} = {-2,2}
  - can remove quantifier (abbreviation)

### Expression talks about its nonlocal variables

- if there is a variable that isn't defined by the function
- ∃〈_n:nat → x = 2×n_〉
- says
- "_x_ is an even natural"
  - there exists n in natural domain where _2×n_ = x
  - can only be true if x is an even natural, so that is what it is trying to define.

## Segment 7

### Function Fine Points

- functions can be defined as
  - **partial**: doesn't have to return result (for domain elements)
  - **total**: always at least one result (for domain elements)
    <br/><br/>
  - **deterministic**: always at most one result
  - **nondeterministic**: sometimes more than one result
- Example
  - 〈_n:nat → n,n+1_〉
    - total and nondeterministic
    - 〈_n:nat → n,n+1_〉3 = 3,4

#### distribution

- applying a bunch of functions to an element equals a bunch of results
  - (_f, g_) x = _f x, g x_
- applying a function to a bunch of elemtents equals a bunch of results
  - _f_ (_x, y_) = _f x, f y_
- cannot substitute parameter in function with non-elementary bunch
  - double = 〈_n:nat → n+n_〉
  - double 2 = 4
  - double (2,3) = double 2, double 3 = 4,6
  - double (2,3) ⧧ (2,3) + (2,3) = 4,5,6

#### inclusion

- _f:g_ = ☐*g:* ☐*f* ∧ ∀*x:* ☐*g • f x:g x*
  - function f is included in g if
    - domain of g is a subset of domain of f
    - with variable x in g domain, f x is a subset of g x
- example
  - _A → B_ = 〈_a:A → B_〉
    - constant function
    - _A → B_ is a function whose domain is A and whose result is
  - _f:A → B_ **=** _A:_ ☐*f ∧ ∀a: A • f a:B*
    - _A → B_ is all functions whose domain is at least A and whose results is at most B
  - therefore _A → B_ is antimonotonic in A and monotonic in B
    - as A gets bigger, the fewer possible domains f can have
    - as B gets bigger, the more results f can have
- more literal example
  - _suc_ =〈_n:nat → n+1_〉(successor function)
  - _suc_:_nat → nat_
  - = _nat:_ ☐*suc ∧ ∀n:nat • suc n:nat*
  - = _nat:nat ∧ ∀n:nat • n+1:nat_
  - ⊤

#### equality

- _f=g_ **=** ☐*g=* ☐*f* ∧ ∀*x:* ☐*g • f x=g x*

#### higher order function

- functions with functions as domain and parameter
- _g_:_A → B_
- 〈_f: (A→B)→ ... f ..._〉_g_
  - applies a function to _g_

#### composition

- occurs when applying two functions one after the other where the functions are not included in other's domain
  - _g f_
    - ¬*f:* ☐*g*
    - _g_ is not a higher order function that is applied to _f_
    - it is instead a new function that applies _f_ then _g_
  - (_g f_) _x_ = _g_ (_f x_)
  - ☐(_g f_) = §_x:_ ☐*f • f x:* ☐*g*
    - _x_ is a bunch of everything that can be applied to _f_ and then applied to _g_
  - example
    - ☐(_even suc_)
    - = §_x:_ ☐*suc • suc x:* ☐*even*
    - = §_x:nat • x+1: int_
    - = _nat_
- can compose operators with functions too
  - (-_suc_) 5 = -(_suc_ 5) = -6
  - (¬*even*) 4 = ¬(_even_ 4) = ¬⊤ = ⊥
- polish notation
  - remove brackets and the results can sort itself out though composition axiom
  - x,y: int
  - f,g: int → int
  - h: int → int → int
    <br></br>
  - h f x g y
  - = (((h f) x) g) y
  - = ((h (f x)) g) y
  - = (h (f x)) (g y)
  - = h (f x) (g y) &nbsp;&nbsp;&nbsp;&nbsp; not due to composition, its just useless

#### list as a function

- if _m:0,..#L_ (_L_ represents a list)
  - 〈_n:0,..#L → L n_〉= L m
  - this function serves same purpose as indexing list _L_
  - function composition can be used with list composition
    - -[2;4;5] = [-2;-4;-5]
    - suc[2;5;6] = [3;6;7]
- list map operator can be thought of in terms of a selective operator (|) applied to 2 functions
  - 1 → 21 | [10;11;12] = [10;21;12]
- quantifiers can be applied to lists too
  - Σ*L* = Σ*n:0,..#L • L n*

#### limits

- **_LIM_**: quantifier applied to function
- _f:nat → rat_
- f 0; f 1; f 2; ... is a sequence of rationals
  - _LIM f_ finds the limit of the sequence
  - (_MAX m • MIN n • f_ (_m+n_)) &le; (_LIM f_) &le; (_MIN m • MAX n • f_(_m+n_))
    - the domain is _nat_ in this example
    - lower bound of _LIM f_ is the maximum of the minimum of all starting points of f
      - find minimum n of f (m+n)
      - then find maximum m of f(m+n)
    - upper bound of _LIM f_ is the minimum of the maximum of all starting points of f
      - find maximum n of f (m+n)
      - then find minimum m of f (m+n)
  - doesn't tell us what the min/max of sequence of f are, just that it lies between the two
  - the two bounds can be equal
    - 0 &le; (_LIM n • 1/_(_n+1_)) &le; 0
    - _LIM_ of the function can only be 0
  - in general,
    - (_MIN f_) &le; (_LIM f_) &le; (_MAX f_)
    - if f is monotonic
      - _LIM f_ = _MAX f_
    - if f is antimonotonic
      - _LIM f_ - _MIN f_
- extended real numbers can be defined:
  - xreal = _LIM_(_nat → rat_)
- _p:nat → bin_
- p 0; p 1; p 2; ... is a sequence of binary values
  - ∃*m •* ∀*n • p*(_m+n_) ⇒ _LIM p_ ⇒ ∀*m •* ∃*n • p*(_m+n_)
    - ∃ is the same as _MAX_
    - ∀ is the same as _MIN_
    - &le; is the same as ⇒
  - ∃*m •* ∀*i • i&ge;m ⇒ p i* **⇒** _LIM p_
    - if the statement becomes ⊤ and stays ⊤, the limit is ⊤
  - ∃*m •* ∀*i • i&ge;m ⇒ p i* **⇒** _LIM p_
    - if the statement becomes ⊥ and stays ⊥, the limit is ⊥
