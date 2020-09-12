# Formal Methods of Software Design

| Date                 | Segments                                                               | Subsections                                             | Exercises                            | Test                       |
| -------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------ | -------------------------- |
| Tuesday September 15 | **Segments 0 and 1**                                                   | Subsection 1.0.1                                        | 0, 2, 14, and 17                     | No                         |
| Friday September 18  | **Segments 2 and 3**                                                   | Section 2.1                                             | 6fmps, 7c, 22, 49, and 53            | No                         |
| Tuesday September 22 | **Segment 4**.                                                         | end of Chapter 2                                        | 62                                   | Practice Test. 3:30        |
| Friday September 25  | **Segments 5 and 6**; **Segment 7** (about using a list as a function) | end of Chapter 3 ~~Sections 3.2 and 3.4~~ (optional) | 64 and 73                            | No                         |
| Tuesday September 29 |                                                                        |                                                         |                                      | Today is Test 0. 4:30-5:20 |
| Friday October 2     | **Segment 8**                                                          | Subsection 4.0.1                                        | 116                                  | No                         |
| Tuesday October 6    | **Segments 9 and 10**                                                  | Section 4.1                                             | 137, 142, 143                        | No                         |
| Friday October 9     | **Segment 11**                                                         | Subsection 4.2.2                                        | 156                                  | No                         |
| Tuesday October 20   | **Segment 12**                                                         | Subsection 4.2.5, but you can skip Subsection 4.2.3     | 186                                  | No                         |
| Friday October 23    | **Segment 13**                                                         | Section 4.2                                             | 189                                  | No                         |
| Tuesday October 27   | **Segments 14 and 15**                                                 | Section 5.1                                             | 252 and 297                          | No                         |
| Friday October 30    | **Segment 16**                                                         | Section 5.2                                             | 242a using a for-loop                | No                         |
| Tuesday November 3   | **Segment 17**                                                         | No readings                                             | 237                                  | Test 1. 4:30-5:20          |
| Friday November 6    | ~~Segments 18, 19, 20, and 21~~ **Segments 22 and 23**                 | end of Chapter 6                                        | 356 and 370abc                       | No                         |
| Tuesday November 10  | **Segment 24**                                                         | Section 7.0                                             | 387                                  | No                         |
| Friday November 13   | **Segment 25**                                                         | Section 7.1                                             | 400                                  | No                         |
| Tuesday November 17  | **Segment 26**                                                         | Subsection 7.2.0                                        | 423                                  | No                         |
| Friday November 20   | **Segment 27**                                                         | Subsection 7.2.3. You can skip Subsection 7.2.4         | 427                                  | No                         |
| Tuesday November 24  |                                                                        |                                                         |                                      | Test 2. 4:30-5:20          |
| Friday November 27   | **Segment 28**                                                         | Section 8.0                                             | 435                                  | No                         |
| Tuesday December 1   | **Segment 29**                                                         | end of Chapter 8                                        | 444                                  | No                         |
| Friday December 4    | ~~Segments 30, 31, and 32~~ **Segment 33**                             | You should review the course                            | 256; course evaluation questionnaire | No                         |
| December 10-23       |                                                                        |                                                         |                                      | Final Exam                 |

---

## Symbols

| Symbol | Definition                  |
| ------ | --------------------------- |
| ⊥      | Antitheorem (False, Bottom) |
| ⊤      | Theorem (True, Top)         |
| ¬      | Negation (not)              |
| ∧      | Conjuction (and)            |
| ∨      | Disjuction (or)             |
| ⇒      | implies                     |
| ⇐      | implied by                  |
| ⧧      | unequal                     |
| ×      |                             |
| ‘      |                             |
| ∈      |                             |
| ∪      |                             |
| ∩      |                             |
| ⊇      |                             |
| ⊆      |                             |
| ↔      |                             |
| ⊲      |                             |
| ⊳      |                             |
| 〈     |                             |
| 〉     |                             |
| →      |                             |
| ☐      |                             |
| ∀      |                             |
| ∃      |                             |
| Σ      |                             |
| ∏      |                             |
| σ      |                             |
| ʹ      |                             |
| ⦂      |                             |

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
