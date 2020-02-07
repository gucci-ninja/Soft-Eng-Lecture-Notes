# 3FP3 Functional Programming

## Day 1 - Jan 7, 2020
- mark breakdown
    - assignments 50%
    - bonus assignments 50% ?

## Day 2 - Jan 9, 2020
- assignments will be compiled using ghc6
- textbook: craft of functional programming
- hackage is where packages go
    - then you use cabal to fetch packages
- other resources
    - wiki.haskell
    - learnyouahaskell
    - hoogle
- assigment 1 will involve writing tests as well
- twitter users?
    - @Bartosz
    - @pigworker
    - @Kmett
- help
    - IRC
    - haskell.org/community
    - r/haskell
    - stackoverflow
- another good resrouce
    - stephen diehl's what i wish i knew  bwhen learning hasell
        - dev.stephendiehl.com/hask

### Code
- haskell uses space for function application
```haskell
{-# LANGUAGEOverloadedStrings #-}
import CodeWorld

ourPicture :: Picture
ourPicture = colored green $ solidCircle 1 --colored is a function that takes a color and a picture, arguments can be seaprated by dollar sign or brackets -> colored green (solidCircle 1)

main :: IO () -- main is always IO because it does stuff
main = drawingOf ourPicture
```

- how to bring up terminal
- to find out what $ is
    - it's a function
```bash
> ghci
Prelude > :t ($) # tells us type of $
($) :: (a ->) -> a -> b
Prelude > :quit
```

## Day 3 - Jan 10, 2020

### Assignment 1
- part 1
    - go through a list of elements and return all occurences of first element
    - eg given 5 [5,3,5,-2] return [5,5]
    - given 0 and [] return []
    - given 3 and [] return [3]
- part 2
    - define function elem
    - to redefine it put `import Prelude hdiing sum, product, elem`
- marks of assignment
    - code - 40%
    - tests - 40%
    - comments - 20%
- pos 5 -> [0,2] for input [5,3,5,-2]
- tripleNeg1 [-1,0,2,-5,-11] -> [-3,0,2,-15,33]
    - will have o do this using recursion as well
- we'll learn all this by thursday
- q4: magic
    - function of 2 arguments (point and list), needs to be written recursively
    - reverse engineer so that sum product and concat are all one-liners
    - product of no elements is 1
    - concat is also called flatten
- q5 create a new data type
    - will be using the `either` type
- q6: ternary trees
    - mirror takes a tree and flips it
    - flatten takes data at leaves and spits them out as list
        - leftmost deepest to the right
    - bonus: magic function for ternary trees
- submission
    - single .hs file 
    - document when you use stackoverflow or ask a friend


### Learning Haskell
- learned about popd and pushd
    - internal memory stack of directories so you can switch between them without doing cd ../.. or whatever
- ghc - compiler
- ghci - interpreter

```bash
Prelude > :t 3
3 :: Num p => p # 3 is a type Num p which can become p??
```

#### Defining Functions
```haskell
square n = n * n
--------
square 6 gives 36
-- can't do square -6, you get a bad error message
-- this is because - (unary minus) is parsed badly in Haskell
-- it interprets square -6 as performing the function - on 6
-- will work if you do (-6) or square $ -6
---------
let cube n = n * n * n -- the let doesn't really mean anything

```
#### Keboard shortcuts
- up arrow previous cmd
- down arrow forward cmd
- ctrl + a goes to beginning of line
- ctrl + e goes to end of line
- tab completes cmd

#### Terminology
- \t is lambda?

```haskell
double = \t -> 2*t
double' t -> 2*t
--------
foo x = cube $ double x

bar = cube . double
```
- a . b means it executes b first then a

## Day 4 - Jan 14, 2019
- two argument functions -> arg \`func` arg
- Craft3e-0.1.1.1
    - PictureSVG.hs
    - Pictures.hs
    - refresh.html

### Type
- syntactic static classifier of values
    - static - without running (at compile time)
- all classifying commands?
    - values
    - type
    - kind - type of types
    - sort (will prob never see this one)
- haskell is turing complete because it can use arbitrary types

```haskell
id x = x
:t id
id :: p -> p
```

### QuickCheck
- import Test.QuickCheck in ghci
- properties are mini-specifications

```
cabal install cabal-test-quickcheck
stack ghci --package QuickCheck
```

`:m Test.QuickCheck`

- usually runs 100 tests
    - can change this
- given a function tiny we can define prop_tiny

`prop_tiny x = tiny x = x`

- then run `quickCHeck prop_tiny`
- it passes
- if we try prop_bad = tiny x = -x 
it fails after 2 tests

```
zzz = repeat 0
take 20 zzz
prop_zzz = n = sum (take n zzz) == 0
quickCheck prop_zzz
```

### How to write tests
- first write trivial tests and make sure they work
- then move on to more cplicated ones

```haskell
d1 n = 2 * n
d2 n = n + n
-- :module + Data.Bits in ghci
d3 n = n `shiftL` 1
d3 50
quickCheck (\n -> d2 n == d3 n)
-- passes all tests
d3 (-6) gives -12

--- reverse function test
quickCheck (\s -> reverse (reverse s) == s)
```

## Day 5 - Jan 16, 2020

### QuickSort Implementation
- refer to code in Assignments
- inefficient because the implementation uses linked lists 

#### Factorial
- product [1..3] = 6
- product [1..(-1)] = 1
- can also do ['a'..'z']
- ['a'..'Z'] is empty because capitals come first

### Weird Languages
- Malbolge (8th circle of hell???)

#### Memoizing

```haskell
facs = scanl (*) 1 [1..]
facs !! n 
```

## Day 6 - Jan 17, 2020
- making executable: `ghc Main` 
- `:load ___`
- `:reload`
- `:type (Expression)`
- `:info (thing)`
- `:browse (Module)`

### Syntax
- can use curly braces and semi-colons but its rarely used
- if it starts with a lowercase it's probably a function
- can also use quotations and underscores and numbers for function names

#### Either
- like a union operator
- even_odd $ take 20 [1..]
- bad_rev: quadratic, to concat the x at the end you need to iterate through whole lists
- rev []
    - doit [] [] = []
- rev [x]
    - doit [x] []
    - doit [] (x:[]) = [x]
- rev [x,y]
    - doit [x,y] []
    - doit [y] (x : [])
    - doit [] (y:x:[]) = y:x:[] = [y,x]

## Day 7 - Jan 21, 2020

### Enumerated types
- look at Jan21 module

### Tuples
- comma separated value enclosed in ()
- fst, snd
- int vs integer - diff between precision

### Lists
- can do [3.1..7.0] and it'll go up tp 7.1
- [10,9..1] to descend
- ['a'..'n'] returns a string since strings are lsits of chars
- can combine strings and lists using ++ 
- read "5" Int turns 5 into integer type

## Day 8 - Jan 23, 2020
- quickcheck ternary tree quickcheck on discord

### Keywords
- type
    - allows you to create a synonymn for something that already exists
    - need to start with capital
    - transparent
        - representation of alias is completly seeable
- newtype
    - wrapper for a type
    - intensional infomation
    - opaque
        - need to unwrap it before you can see what it really is
- data
    - for creating entirely new types
    - transparent since you get to see all of the details of implementaion
    - take values
- intension -> syntax (newtype)
- extension -> semantics (data)

## Day 9 - Jan 24, 2020
- module Jan24

## Day 10 - Jan 28, 2020
- module

## Day 11 - Jan 30, 2020
- skipped

## Day 12 - Jan 31, 2020
- skiiped

## Day 13 - Feb 4, 2020

### Assignment 2 Overview
- programs
- literate programming (.lhs)
- question 1
    - for all routine
    - take a list and a predicate (p: a-> bool) 
        - if x is in the list then p(x) holds true and the run on the rest (xs)
    - prove range split by induction
    - if list is concatenation of two lists then running function on both lists should yield same result
- question 2
    - given mstery function, provide implementation
    - figure out type as well
        - tTUeplEs?
- question 3 - fold
    - express primitve functions of list using fold
    - calculate how reverse can be expressed as fold
    - reverse = fold + some params f and e
- question 4
    - mirror for trees
    - posdt goes right and pre goes left? (double mirror)
    - prove they work by induction
    - everything is by induction
- question 5 - unzip
    - can commute unxip with pair and map
    - pair = apply f to both parts of a pair
    - prove by induction
    - counter example for
        - pair of list and list of pairs is not the same in unzip
- question 6
    - tree'
    - show that data in leaves vs data in branches is equivalent
    - quickcheck for first pair
- bonus: extra proofs, comments, quickcheck, extra clever solutions

### Literate Programming
- 2 ways
    1. latex style
        - put beginning/end
        - this is the one we'll be using
    2. bird style
        - put prompt > 
- intero
    - `stack build intero --copy-compiler-tool`

## Day 14 - Feb 6, 2020

- lhstotex
- midterm will be up to everything we do today
- ghci -Wall Feb6

#### Proof by Induction
- bonus marks to type it in latex
- 2 lists for length (xs ++ ys) ->
    1. induction on xs? (doing induction on this one is enough)
    2. " " ys?
    3. " " both?
- induct
    - length (xs ++ ys)

```
base
    length ([] ++ ys)
        ≡ < ++ .1 >
    length (ys)
        ≡ < arith >
    0 + length ys
        ≡ <length.1>
    length [] + length ys


length ((x.xs ++ 1 ys))
    ≡ < *+.2 >
lengh(x: (xs ++ ys))
    ≡ <length.2>
1 + length(xs ++ ys)
    ≡ < ind hypothesis >
1 + length xs + length ys
    ≡ <>
1 + length xs + length ys
    ≡ < length.2 >
length(x,xs) + 1 ys
```

#### Proof for reverse

```
base
    reverse ([] ++ ys)
        ≡ ++.1
    reverse ys
        ≡ < lemma >
    reverse ys ++ []
        ≡ {reverse 1}
    reverse yz ++ reverse []

lemma -> ∀ l , l ++ [] ≡ l
```

#### Induction for the other one :(

```
reverse ( (x:xs) ++ ys)
    ≡ < ++, 2 >
reverse( x : (xs ++ ys))
    ≡ < rev 2 >
reverse (xs ++ ys) ++ [x]
    ≡ < induction hypothesis >
(reverse ys ++ reverse xs) + [x]

    ≡ < ++ is associative > (this would need a lemma, either given or need to prove)

reverse ys ++ (reverse xs ++ [x])
    ≡ < rev 2 >
reverse ys ++ reverse(x:xs)
```

## Day 15 - Feb 7, 2020
- went over proofs (written)

### Tutorial 4 - Feb 7, 2020

<strong>Proposition 1. P(xs) := xs ++ [] == xs</strong>

----------------------------------------

```
Base Case : P([]) := [] ++ [] == []

=> (left) := [] ++ []
    //equiv < by ++ >
=> [] (stop)

=> (right) := [] (stop)

(left) = (right) [ - ]
```

----------------------------------------------

```
Induction Hypothesis (IH) P(xs) := xs ++ [] = xs
Induction Step P(x:xs) := (x:xs) ++ [] = (x:xs)

=> (left) := (x:xs) ++ []
    //equiv < by ++ >
=> x : (xs ++[])
    //equiv < by IH >
=> x:xs (stop)

=> (right) := xs

(left) = (right)
```

- if you append empty list to list it'll be list itself
    - PrP 1: xs ++ [] = xs
- reverse 2 list and append to each other
    - PrP : reverse (xs ++ ys) == reverse (ys) ++ reverse (xs)


<strong>Proposition 3: P(xs) := sum (xs ++ ys) == sum xs + sum ys</strong>

-----------------------------------

```
Base Case: P([]) := sum  ([] ++ ys) == sum [] + sum ys

=> (left) := sum ([] ++ ys)
    //equiv < by prp 1 >
=> sum ys

(left) = (right)

=> (right) := sum [] + sum ys
    //equiv < by sum >
=> 0 + sum ys
```

```
Induction Hypothesis P(xs) := sum (xs ++ ys) == sum xs + sum ys
Induction Step P(x:xs) := sum ((x:xs) ++ ys) = sum (x:xs) + sum ys

=> (left) := sum ((x:xs) ++ ys)
    //equiv < by ++ >
=> sum (x : (xs ++ ys))
    //equiv < by  sum>
=> x + sum(xs ++ ys)
    //equiv < by IH >
=> x + sum(xs) + sum(ys) 

=> (right) := sum (x:xs) + sum ys
    //equiv < by  sum>
=> x + sum xs + sum ys
```

<strong>Proposition 4: P(xs) := sum (reserse xs) == sum xs</strong>

```
Base case : P([]) := sum (reverse []) = sum []

LEFT SIDE
sum (reverse [])
    by reverse
sum []

RIGHT SIDE
sum []

LHS = RHS
```

```
Induction Hypothesis P(xs) := sum (reverse xs) == sum xs
Induction Step P(x:xs) := sum (reverse (x:xs)) == sum x:xs

LEFT SIDE
sum (reserse (x:xs))
    by reverse
sum (xs ++ [x])
    by < prp 3 >
sum (reverse xs) + sum [x]
    by HI


RIGHT SIDE
sum x:xs
```
