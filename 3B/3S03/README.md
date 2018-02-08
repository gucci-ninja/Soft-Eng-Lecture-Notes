# 3S03 Software Testing 

## Table of Contents
- [Course Outline](#course-outline)
- [Software Testing](#software-testing)
- [Testing and Measurement](#testing-and-measurement)
- [Types of Defects](#types-of-defects)
- [Testing Principles](#testing-principles)
- [Testing Strategies and Plans](#testing-strategies-and-plans)
- [Tutorial 1 Jan 17, 2018](#tutorial-1-jan-17-2018)
- [Testing Strategies and Plans](#testing-strategies-and-plans)
- [Developing Unit Test Plan](#developing-unit-test-plan)
- [Tutorial 2 Jan 24, 2018](#tutorial-2-jan-24-2018)
- [Test Factors](#test-factors)
- [Test Examples](#test-examples)
- [Testing Techniques](#testing-techniques)
- [Functional vs Structural Testing](#functional-vs-structural-testing)
- [Tutorial 3 Jan 31, 2018](#tutorial-3-jan-31-2018)
- [Test Adequacy Criteria](#test-adequacy-criteria)
- [Dynamic vs Static testing](#dynamic-vs-static-testing)
- [Functional Testing Techniques](#functional-testing-techniques)
- [Tutorial 3 Feb 7, 2018](#tutorial-3-feb-7-2018)

## Day 1 - Jan 4, 2018 

### Course Outline

#### Textbooks
- Software Testing - Ron Patton
- Software Metrics: A Rigorous and Practical Approach - Norman E. Fenton

#### Language
- Java

#### Assignments
A | Given | Due
--|-------|----
1 |Jan 20 | Feb 12
2 | Feb 26 | Mar 12
3 | Mar 19 | Apr 5

#### Breakdown
- Assignments 30%
- Midterm 30%
- Exam 40%

\*Midterm and exam will be multiple choice & short answer.

#### Midterm
- Thursday Feb 15 9:30-10:20AM

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

## Day 10 Jan 25, 2018

### Test Factors
- Correctness, Data Integrity, Authorization, Audit Trail, Avilability, Access Control, Compliance, Reliability, Ease of Use, Maintainability, Portability, Coupling, Performance, Ease of Operation
- Access control defines what you have access to and enforces it, authorization defines what you can and can't do

**Activity coming up with test cases**

### Test Examples
We are given 2 lists A, B where B is an anagram of A. Find an index mapping P from A to B eg. P[i] = j means the i-th element in A is the j-th element in B. 
-   A and B may contin duplicates, if there are multiples, output any of them.
- Elements A and B are in the range 1, 100

Input | Output
-------|--------------
A and B empty | p=empty message
a = [2,2] = b | [0,1] or [1,0]
a = [1,2], b = [1,2,3] | err mesg

## Day 11 Jan 29, 2018
- skipped

## Day 12 Jan 30, 2018
- Quiz 1

#### Agile Development
- prototyping in an incremental way

### Testing Techniques
- functional vs structural
- dynamic vs static
- manual vs automated

OR

- coverage-based
- fault-based
- error-based
- black-box vs white-box

#### Fault Seeding
- finding total number of pikes present in lake A
    - estimated as (M-M')*(N/M')
    - you catch a number of pikes, N in lake B
    - you mark them and throw into lake A
    - you catch the number of pikes, M in lake A
    - suppose M' out of M pikes are found to be marked
- this technique can be used to find faults of a program
- easiest way to do this is to artificially seed number of faults
- when tested you will find seeded and new faults
- total faults can then be estimated
- **Assumption:** distribution(real) faults = distribution(seeded) faults
- need to steremine what faults to seed
    - Technique 1: construct by hand (unlikely that they will be realistic)
    - Technique 2: have the program independently tested by 2 groups
        - faults found by 1 group can be seeded for the other but both might find the same faults
- **Rule of thumb** - if we find many seded faults and relatively few others, the result can be trusted (but not the opposite)

> The probability of the existence of more errors in a section 
> of a program is proportional to the number of errors already
> found in that section - Myers 1979
### Functional vs Structural Testing
- tests can be derived from a description of the system's **function** or from the system's internal **structure**


.  | Functional | Structural
---|------------|-----------
Uncovers errors in | Rqmt. implementations, Design Spec | Actual coding
Concerned with | the WHAT | the HOW
Evaluates the | Results of Behaviour processing | Implementation algorithms
Ensures that | requirements are satisfied | the structure is sound


. | Dynamic | Static
--|---------|------
How | Execute code | By inspection
Stage | Validation | Verification
SDLC Phases | Implementation, testing | Requirements, Design
What | Behaviour (F and NF) | Documentation, Syntax, Structure

#### Exhaustive Testing
- dynamic techniques involve running all possible inputs and if they all give us the expected result, we have validated the product - which is really not feasible
- domain of inputs is very large so exhaustive testing is not practical

#### Test Adequacy Criteria
- reduce to finite testing process by finding criteria for choosing representative test cases
- a combo of static and dynamic tests is used
    - select reasonable subset of test conditions to provide high probability that system will perform correctly

### Tutorial 3 Jan 31, 2018

#### Test Objectives
- all members of a project team have these
    - developers
        - Objective: code
    - testers
        - Objective: find defects
    - quality team
        - Objective: ensure that a quality project is given to customer
    - management
        - Objective: do management of the project
- if there are no clear objectives you must identify them for test phases and test plans
- objectives need to be set to minimize risk
- define
    - itemize
    - prioritize (low, medium, high)
    - completion criteria

#### Test Scenario
- has a description
- has a test case (set of actions that you perform for a scenario)

#### Validation vs Verification
- are we building the right product? - validation
- are we building the product right? - verification

#### Test Matrix

Test Factors | Operations | Recovery | Stress | Regression | Manual
-------------|------------|----------|-------|-----------|--------
reliability | | | |
security | | | |
maintainability | | | | 
portability | | | | 

## Day 13 Feb 1, 2018

### Test Adequacy Criteria
- Can be used as a tool to measure testing and whether you are done or not and to generate test cases
- Reduce finite…
- Ex. bubble sort
    - N = 2, a = {10,5}
    - Want 100% statement coverage

### Dynamic vs Static testing
- How do we find suitable test cases
- Ex. need to perform binary search
    - Input – key, set of pre-sorted elements, size of set
- Once an individual concern has been identified, it must be determined whether to perform a structural or function test
- Once the technique has been selected, the test method for implementing that technique needs to be determined
- Last step is to select for either dynamic or static test method a manual or automated too

### Functional Testing Techniques
**Preliminaries**
- Designed to ensure that the system reqs and specs are achieved
- Create test conditions for use in evaluating the correctness of the application
- Techniques
    - Req testing/acceptance testing
    - Regression testing
    - Error handling testing
    - Manual-sys testing
    - …

#### Functional Requirements Testing
- The sys can perform its function correctly and that the correctness can be sustained over a continuous period of time (reliability)
- Objectives
    - User reqs are implemented
    - Correctness is maintained over extended processing periods
- How to use req testing
    - Boundary value analysis – test boundaries for specified range of values
    - Equivalence partition – partition the range into equal parts/groups that tend to have the same behavior
    - State transition – test based on the change of software state following particular action
    - Error guessing- anticipate the error that may arise while testing
- Ex. factorial
    - req is prescriptive not descriptive 
        - It tells you how to test something which it shouldn’t do really
    - Partitions at 0, 20, 200, some sort of max integer
        - Things should happen same way inside each partition

## Day 14 Feb 5, 2018

**skipped**

## Day 15 Feb 6, 2018

- if there is previous working application, you can perform parallel testing

### Tutorial 3 Feb 7, 2018

**skipped**
