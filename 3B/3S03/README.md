# 3S03 Software Testing 

## Table of Contents
- [Textbooks](#textbooks)
- [Language](#language)
- [Assignments](#assignments)
- [Breakdown](#breakdown)
- [Software Testing](#software-testing)
- [Testing and Measurement](#testing-and-measurement)
- [Types of Defects](#types-of-defects)
- [Testing Principles](#testing-principles)
- [Testing Strategies and Plans](#testing-strategies-and-plans)
- [Tutorial 1 Jan 17, 2018](#tutorial-1-jan-17-2018)
- [Testing Strategies and Plans](#testing-strategies-and-plans)
- [Developing Unit Test Plan](#developing-unit-test-plan)
- [Tutorial 2 Jan 24, 2018](#tutorial-2-jan-24-2018)

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

## Day 4 Jan 11, 2018

**Still on Testing and Measurement**
- accuraacy of measure depends on measuring instrument and definition of measurement
- always a margin of error
- when is a scale acceptable?

### Types of Defects
1. Software does something it's not supposed to do 
2. Software does something the specs say it should not do
3. Software does something that specs doesn't mention
    - it's a **bug** because it can have side effects
4. The software does not do something that spec does not mentiion but should
    - common sense
    - if x happens, y shoudl happen 
5. The software is difficult to understand, hard to use, slow or just not right

### Testing Principles

1. Necessary part of test case is the definition of the expected output or result
2. A programmer should avoid attempting to test his/her own program
    - hard to look at program with destructive eye
    - will carry same misunderstanding into tests
3. Programming organizations should not test its own programs
    - same reasoning as 2
4. Throughly inspect the resuts of each test
5. Test cases must be written for input conditions that are invalid and unexpected as well as valid and expected

## Day 5 Jan 15, 2018

**Skipped but I'm guessing we went over the rest of the Principles of Testing**

6. Avoid throwaway test cases unless the program is truly a throwaway program
7. Do not plan a testing effort under the tacit assumption that no errors will be found
    - Testing is **not** just the process of showing that the system functions correctly
    - Testing is the process of executing system with intent of finding functional errors or qualities attribute mismatches
8. The probability of the existence of more errors in a section of a program is proportional to the number of errors already found in that section
9. Testing is an extremely creative and intellectually challenging task

## Day 6 Jan 16, 2018

- 5-6 quizzes in tutorials, worth 2% extra

### Testing Strategies and Plans

The following may be defects
- Functionality
- Communication (intuitive)
- Command strcture
- Missing commands
- Program rigidity
- Performance
- Error handling
- Boundary-related errors
- Calculation errors
- Concurrency issues

### Tutorial 1 Jan 17, 2018

- **error**: mistake made my the developer
- **defect**: mistake made by developer found by tester
- **bug**: when developer acknowledges mistake that tester found(?)
- **failure**: when product can't perform the way it is supposed to

- **software tester** - finds bugs
- **quality assurance** - prevent bugs

#### Characteristics of SQA components
1. Pre-project component
    - budget, schedule
2. Customer Involvement
    - approvals/rejections
    - Agile -> has scrum master, 1 task in 2-4 weeks (sprints), continuous custumer involvement
3. Required teamwork
4. Cooperation
5. Show goes on
    - maintenance

#### SQA Architecture
- Pre-project -> development plans, commitments
- SDLC -> planning, analysis, design/build, implement, maintain
- Quality Infrastructure -> eliminate all errors
- Standards (like ISO) 
- All of these are noted on the BRD (Business Requirements Document)

#### Constract Review
- time, budget, risks, everyone's ability, training
- **reviews** are conducted after sprints and they can be _formal_ (which are mandatory) or they can be _peer_ reviews

#### Regression Testing
- when changes are made, quickly test everything that is associated with the change made

#### Infrastructure Components
- procedure - what methodology
- templates/checklists
- staff training

#### Project Progress Control
- works on deviation of ongoing process
- takes into account the resource usage, schedule, budget, risk
- likeeee what do we do if certain things ruin our progress
- controlled documents also exist

## Day 7 Jan 18, 2018

**skipped**

## Day 8 Jan 22, 2018

**skipped**

## Day 9 Jan 23, 2018

### Testing Strategies and Plans

1. General Information
    - Summary
    - Environment and Pretest Background
    - Test Objectives 
        - SMART: Specific, Measurable, 
    - Expected Defect Rates
    - References
        - requirements
    - Project request authorization
    - Previously published documents on project
    - Documentation concerning related projects

2. Plan
    - Software Description
    - Test Team (_WHO_ + _ASSIGNMENT_)
    - Milestones (like in weeks, days)
    - Budgets
    - Testing (systems checkpoint)
        - Schedule (and budget)
        - should test in order of what depends on what

3. Specification and Evaluation
    - Specifications
        - <span style="color:red">business functions</span>, Functional, Structural, Test/Function relationship, progression
    - Methods and Constraints
        - Methodology
        - Test tools
        - Extent (total or partial, rationale for partial testing)
        - Data recording (how are you going to record the data, like a spreadsheet)
        - Constraints
    - Evaluation
        - Criteria, data reduction

4. Test Descriptions
    - Test (identify unqiuely)
         - control (manual, semi-automatic, automatic)
         - inputs/outputs
         - procedures (test setup, initialization, termination)
    - Test Cases
        - start with your requirements/specs/documentation
        - look for most likely, most visible errors
            - most often used areas of program
            - hardest to fix areas of program 

### Developing Unit Test Plan
- system divided into components
- same as the Plan from before
- functions that arent tested

### Tutorial 2 Jan 24, 2018
- Advantages of Test Plans
    - Test does not have to determine the process
    - Test process can be continually improved
- Guidelines for test plans
    - Reduce development risk
    - Testing should be performed effectively
    - should uncover defects
    - should use business logic
    - should be performed throughout development life cycle phases
    - test both structure and function
- When testing should occur (6 phases)
    - requirements phase: accuracy of requirements
    - design phase: determine consistency and adequecy
        - where you figure out structural and functional test conditions
    - implemntation phase: determine adequecy 
        - where you make functional and structural unit tests
    - also test phase, installation phase maintenance

#### Risk Based Testing
- need to identify risks, prioritize risks and then document risks
- software can't be completely tested so you gotta test effectively :eyes:
- structural risks
    - consider more information that has influence on the project
- technical risks
- size risks
