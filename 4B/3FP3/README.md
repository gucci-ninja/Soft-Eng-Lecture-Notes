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