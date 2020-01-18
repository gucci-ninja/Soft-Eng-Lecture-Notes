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