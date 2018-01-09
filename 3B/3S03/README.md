# 3S03 Software Testing 

## Table of Contents
- [Textbooks](#textbooks)
- [Language](#language)
- [Assignments](#assignments)
- [Breakdown](#breakdown)
- [Software Testing](#software-testing)
- [Testing and Measurement](#testing-and-measurement)
- [Testing and Measurement](#testing-and-measurement)

## Day 1 - Jan 4, 2018 

### Textbooks
- Software Testing - Ron Patton
- Software Metrics: A Rigorous and Practical Approach - Norman E. Fenton

### Language
- Java

### Assignments
A | Given | Due
--|-------|----
1 |Jan 20 | Feb 12
2 | Feb 26 | Mar 12
3 | Mar 19 | Apr 5

### Breakdown
- Assignments 30%
- Midterm 30%
- Exam 40%

\*Midterm and exam will be multiple choice & short answer.

## Day 2 Jan 8, 2018

### Software Testing

#### Famous Software Failures 
- Ariane 5 - 1996
    - Flight failure 40 seconds after initiation
    - Incaccurate conversion of 64 bit floating point to 16 bit integer for velocity
- Mars Polar Lander Crash - 1999
    - robotic spacecraft that was supposed to establish connection upon landing
    - crashed at speed of 22 m/s
- Northeast Blackout - 2003
    - cascading problem in system shutdown due to grid overload
    - error in alarm, which did not go off for 1 hour
    - 256 power plants that went off for 4 hours
- Nissan Recall for Airbag Malfunction - 2014
    - sensor for airbags did not work
    - 1 million cars recalled
- Airbus crash - 2015
    - configuration issue
- Bitcoin Unlimited node crash - 2017
    - 70% of their nodes disappeared

### Testing and Measurement

- Software quality measured in defects per 1000 lines of code
    - Today, the average of defects/1000 lines of code in new software is 10-50 (_KLOC_)
    - In released products, KLOC = 0.5-3 
- Challenges
    - Software complexity
    - Stringent non-functional reqs
    - Software visibility (absence of features is not obvious)
    - Nature of development process
- Budget and time should be considered together
    - budget cuts usually alleviating by removing testing and/or requirements phase

## Day 3 Jan 9, 2018
_Tutorials start next week_

**Excercise**
- write test cases to test simple java program about triangles
- program takes in 3 integers as sides) and returns scale, isoceles, equilateral
- what kind of information does tester need to know?
    - domain knowledge - geometry of triangles
    - precise requirements (speed)
- test cases
    - check if it is a valid triangle (1, 2, 4 wouldn't be valid)
    - non-integer values
    - values greater than 0, less than 0


