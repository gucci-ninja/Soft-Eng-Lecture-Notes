# 3S03 Software Testing 

## Table of Contents
- [Course Outline](#course-outline)
- [Software Testing](#software-testing)
- [Testing and Measurement](#testing-and-measurement)
- [Defects](#defects)
- [Testing Principles](#testing-principles)
- [Testing Strategies and Plans](#testing-strategies-and-plans)
- [Tutorial 1 Jan 17, 2018](#tutorial-1-jan-17-2018)
- [Test Strategy](#test-strategy)
- [Testing Strategies and Plans](#testing-strategies-and-plans)
- [Developing Unit Test Plan](#developing-unit-test-plan)
- [Tutorial 2 Jan 24, 2018](#tutorial-2-jan-24-2018)
- [Test Factors](#test-factors)
- [Test Examples](#test-examples)
- [Testing Techniques](#testing-techniques)
- [Functional vs Structural Testing](#functional-vs-structural-testing)
- [Dynamic vs Static Testing](#dynamic-vs-static-testing)
- [Tutorial 3 Jan 31, 2018](#tutorial-3-jan-31-2018)
- [Functional Testing Techniques](#functional-testing-techniques)
- [Test Report](#test-report)
- [Structural Testing Techniques](#structural-testing-techniques)
- [Quiz 2 Regression Testing](#quiz-2-regression-testing)
- [Unit Testing](#unit-testing)
- [Tutorial 5 Feb 14, 2018 ](#tutorial-5-feb-14-2018-)
- [Empirical Unit Testing Principles](#empirical-unit-testing-principles)
- [Parameterized Tests](#parameterized-tests)
- [Security Testing](#security-testing)
- [Tutorial 8 Mar 14, 2018](#tutorial-8-mar-14-2018)
- [Basics of Measurement](#basics-of-measurement)
- [Tutorial 9 Mar 21, 2018](#tutorial-9-mar-21-2018)
- [Scales](#scales)
- [Tutorial 10 Mar 28, 2018](#tutorial-10-mar-28-2018)
- [Scales contd](#scales-contd)
- [Admissible Transformation](#admissible-transformation)
- [Statistical Operations on Measures](#statistical-operations-on-measures)

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
- accuracy of measure depends on measuring instrument and definition of measurement
- always a margin of error
- when is a scale acceptable?

### Defects
1. Software does something it's not supposed to do 
2. Software does something the specs say it should not do
3. Software does something that specs doesn't mention
    - it's a **bug** because it can have side effects
4. The software does not do something that spec does not mentiion but should
    - common sense
    - if x happens, y shoudl happen 
5. The software is difficult to understand, hard to use, slow or just not right

- goal of testing is to demonstrate that errors are not present and show that a program performs its intended functions properly
- goal (2) is to find defects as early as possible and make sure they get fixed
- testing is the process of executing program with intent of finding errors

### Testing Principles
1. Necessary part of test case is the definition of the expected output or result
    - due to this, a test case must consist of 2 things, description of input data to program AND precise description of correct output of the program for that set of input data
    - hint: write pre and post-conditions befre writing program
2. A programmer should avoid attempting to test his/her own program
    - this doesn't apply to debugging
    - hard to look at program with destructive eye
    - will carry same misunderstanding into tests
3. Programming organizations should not test its own programs
    - same reasoning as 2
4. Thoroughly inspect the results of each test
5. Test cases must be written for input conditions that are invalid and unexpected as well as valid and expected

## Day 5 Jan 15, 2018

**Skipped but I'm guessing we went over the rest of the Principles of Testing**

6. Avoid throwaway test cases unless the program is truly a throwaway program
    - coming up with test cases on the fly and then throwing them away, making it hard to recreate
7. Do not plan a testing effort under the tacit assumption that no errors will be found
    - Testing is **not** just the process of showing that the system functions correctly
    - Testing is the process of executing system with intent of finding functional errors or qualities attribute mismatches
8. The probability of the existence of more errors in a section of a program is proportional to the number of errors already found in that section
9. Testing is an extremely creative and intellectually challenging task

#### Good Software Tester
- explorer, troubleshooter, relentless, creative, perfectionist, persuasive

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

- **errors** by process actors lead to **defects** in software
- **defect** that leads to unacceptable behaviour is called **failure**
- some defects don't cause any failures, some cause millions
- **risk** is a condition that can result in loss
    - types of risks
        - incorrect results from system
        - system accepting unauthorized transactions
        - computer file integrity lost
        - processing cannot be reconstructed
        - continuity of processing will ve lost
        - service provided will degrade to unacceptable level
        - system security will be compromised
        - procesing wont comply with govt/company policy
        - unreliabe results
        - system difficult to use/operate
        - unmaintainable
        - not portable to other environment
        - not able to interconnect with other computer systems
        - unacceptable performance level
- risk of **undertesting** - translates into system defects
- risk of **overtesting** - uses valuable resources
- problems associated with testing:
    - failure to define testing objectives
    - testing at wrong phase
    - use of ineffective testing techniques

#### Testing Policy
- management's definition of testing
- criteria:
    - definition of testing
    - testing system
    - evaluation
    - standards - against which testing will be measured

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

### Test Strategy
- objective: decrease risks
- strategy must address risks and present process to reduce them
- 2 components
    1. test factor - risk/issue
    2. test phase

#### Test Factors
- Correctness
    - data entered, processed and outputted is accurate and complete
- Data integrity
    - data entered will be returned unaltered
- Authorization
    - data is processed in accordance with intents of management
- Audit trail
    - processing of data can be supported through retention of sufficient evidential matter to substantiate accuracy, completeness, timeliness and authorization
- Continuity of processing
    - ability to sustain processing in event of problems
    - timelineness of recovery operations
- Service levels
    - desired results will be available within acceptable time frame
- Access control
    - system resources will be protected against accidental and intentional modification, destruction, misuse and disclosure
- Compliance
    - system in accordance with organizational strategy, policies
- Reliability
    - application iwll perform its intended funtions with required precision over extended period of time
- Ease of use
    - effort to learn and operate system
- Maintainability
    - effort required to locate and fix error/defect in operational system
- Portability
    - effort to transfer program from one hardware configuration to another
- Performance
    - amount of computing resources and code for system to perform functions
- Ease of operation
    - effort required to integreate system into OS

#### Developing Test Strategy
1. Select and rank test factors:
    - who
    - what: 3-7 factors
    - how: specific test risks can be subbes for factors
2. Identify the system development phased (Requirements, Arch Design, Deisgn, Coding, Unit/System Test, Maintenance)
3. Identify the business risks associated with the system under development.
4. Place risks in a test factor/test phase matrix. Should place plans in these?

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
1. same as the Plan from before
    - functions that arent tested
2. Business and Structural Function Testing
    - business functions
    - structural functions
    - test descriptions
    - expected result
    - condition to stop test
    - test number
3. Intrface Test Descriptions
    - interface
    - test descriptions
    - expected results
    - test number
4. Test Progression

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
1. System functional testing techniques
2. System structural testing techniques
3. Unit testing techniques
- testing can be classified as
    - functional vs structural
    - dynamic vs static
    - manual vs automated
- OR classified by adequacy criterion:
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
- need to deteremine what faults to seed
    - Technique 1: construct by hand (unlikely that they will be realistic)
    - Technique 2: have the program independently tested by 2 groups
        - faults found by 1 group can be seeded for the other but both might find the same faults
- **Rule of thumb** - if we find many seeded faults and relatively few others, the result can be trusted (but not the opposite)

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

### Dynamic vs Static Testing

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
- test adequacy criterion specifies requirements for testing and can be used as a stopping rule, measurement or test case generator

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

#### Test Adequacy Criteria
- Can be used as a tool to measure testing and whether you are done or not and to generate test cases
- Reduce finite…
- Ex. bubble sort
    - N = 2, a = {10,5}
    - This test set is adequate for 100% statement coverage but no for 100% branch coverage

#### Dynamic vs Static testing
- How do we find suitable test cases
- Ex. need to perform binary search
    - Input – key, set of pre-sorted elements, size of set

#### Selecting Techniques
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
    - Manual-support testing
    - Intersystems testing
    - Control testing
    - Parallel testing

#### Functional Requirements Testing
- The sys can perform its function correctly and that the correctness can be sustained over a continuous period of time (reliability)
- Objectives
    - User reqs are implemented
    - Correctness is maintained over extended processing periods

#### Requirements Testing
    - Boundary value analysis – test boundaries for specified range of values
    - Equivalence partition – partition the range into equal parts/groups that tend to have the same behavior
    - State transition – test based on the change of software state following particular action
    - Error guessing- anticipate the error that may arise while testing
- Ex. factorial
    - req is prescriptive not descriptive 
        - It tells you how to test something which it shouldn’t do really
    - Partitions at 0, 20, 200, some sort of max integer
        - Things should happen same way inside each partition

#### Regression Testing
- retest previously tested segments to ensure they still function properly after a change is made
- specific onjective is to ensure documentation is current, test data and test conditions remain curent and previously tested functions perform properly after changes
- how to use regression testing
    - corrective - rerun same tests that were previously executed
        - when specs haven't changed
    - progressive - (re)run modified or new tests for previously tested components
        - when specs have changed
    - retest all
        - when before new release
    - selective - based on dependencies between components and tests
        - any time modifications are made
- regression testing should be used wen there is high risk new changes will affect unchanged areas

#### Error Handling Testing
- ability of application system to properly process incorrect transactions
- specific objectives is to ensure app recognizes all reasonably expected error conditions and accounts for processing errors that are likely
- how to use
    - create set of transations that contain errors/produce errors
    - enter them into system to determine if app can identify
    - check for improper handling and improper communication to user

#### Manual Support Testing
- evaluates functions performed by the people while preparing the data for and using the data from automated system
- specific objectives include documenting manual-support procedures, assigning manual support responsability, adequately training manual support team and interfacing manual support with automated segment
- how to use
    - manual-support group must understand system functionality
    - they should prepare environment of testing
    - they prepare and execute test cases manually
    - observe, verify, record pass/fail

#### Intersystem Testing
- ensures that integration between systems functions correctly
- specific objectives are proper passing of data, proper coordination and timing of functions between application sysems and accurate documentation for involved systems
- how to use
    - integration nodes between multiple systems are executed to check that data transfers are acceptable and processed properly
    - develop test transactions set and pass to another system to verify processing
- when to use
    - there is change in parameters between app system
- integration vs compatibiity vs portability vs intersystem

#### Parallel Testing
- results of new application are consistent with processing of previous applicatiion
- specific objectives are ensuring that new version performs correctly and demonstrate consistency/inconcesistency btn 2 versions
- how to use
    - same input data should be run through 2 versions of same app
    - done with whole system or part of system
- when to use
    - in apps that use complex processing and there is uncertainty regarding correctness of processing

#### Summary

Technique | Objective
----------|----------
Requirements | system performs as specified
Regression | anything unchanged still performs correctly
Error-handling | errors can be prevented or detected and then corrected
Manual-support | human-computer interface works
Intersystem | resources are correctly shared btwn system
Parallel | new system gives same results as old

## Day 14 Feb 5, 2018

**skipped** but notes are continued in Day 13

## Day 15 Feb 6, 2018

- if there is previous working application, you can perform parallel testing

### Test Report
- include all details - date, module, Test Case ID, Version, build #
- give steps to reproduce defects
- include input data
- type, severity, priority
- environment
- visual support
- log, error codes
- maybe recommendations

#### Tutorial 4 Feb 7, 2018

**skipped**

## Day 16 Feb 8, 2018

**skipped** but covered

### Structural Testing Techniques
- ensure that product designed is structurally sound and will function correctly
- determines that technology has been used properly and all parts are assembled cohesively
- focus on process, not correctness
- uncovers errors that occured during implementation
- techniques are:
    - stress testing
    - execution testing
    - recovery testing
    - operations testing
    - compliance testing
    - security testing

#### Stress Testing
- if system can handle heavy loads
- stressed areas are:
    - input, users accessing
    - disk space, communication
    - memory capacity
- robustness, availability and error-handling
- how to use
    - simulate production environment (really well)
    - enter heavier than expected volumes of data
    - simulate large # users
    - error conditinos included
- looking for issues in
    - load balancing
    - bandwidth
    - system capacity
    - respone time

#### Execution Testing
- if system machieves desired level of proficiency in production status
- verifies reponse time, turnarouns time, design performance
- can be tested in whole or in part using actual system or simulated model
- objectives are determining performance of system structure, verifying optimum use of hardware/software, determining response time to users requests and transaction processing turnaround time

#### Recovery Testing
- ability to restart operations after integrity of app has been lost
- revert to point where integrity of system is known, reprocess transactions up to point of failure
- time required to recover is affected by
    - number of restart points
    - volume of applications running on computer
    - training/skil of ppl conducting recovery
    - tools available
- specific objectives are preservation of adequate backup data in secure location, documented recovery procedures, trained recovery personnel, available tools
- how to use
    - assess procedures, methods, tools
    - introduce faiure in system and evaluate recoerability
    - perform recovery testing by ppl who will do it IRL
- when to use
    - when continuity of operation of app is essential 

#### Operations Testing
- verify that operating procedures and staff can properly execute app
- specific objectives are determining completeness of computer operator documentation, ensuring necessary support mechanisms are prepared, completeness of operator training and that operators can operate
- how to use
    - QA assess operator documention and gather key acceptance criteria
    - QA trains operational stadd
    - operation stadd performs and gives feedback
- when to use
    - prior to placing in production status

#### Compliance Testing
- verifies app was developed in accordance with IT standards, procedures, guidelines
- methodologies used to increase success, enable transfer of ppl w/ minimal cost, increase maintainability
- specific objectives include determining that systems development emthodologies are followed, compliance to standards.., complete documentation

#### Security Testing
- ensure secure confidential info and for competitive purpose assure 3rd parties their data is protected
- amount of security depends on risks
- security defects aren't very obvious
- specific objectives are
    - determining adequate attention is devoted to securit
    - realistic definition and enforcement has been implemented
    - sufficient expertise for security testing
    - conducting reasonable tests
- highly specialized part of testing
- physical security deals with penetration by ppl
- logical security deals with use of computer/communication to improperly access info
- when to use
    - prior to operational status
    - after system in operational status

#### Summary

Technique | Objective | When to Use (Req, Design, Dev, Pre-prod, Maint)
----------|-----------|------------
Stress | system behaves outside expected volumes and load | all(?)
Execution | system achieves desired lvl of proficiency (performance) | all
Recovery | system can be returned to operational status after failure | all(?)
Operations | system can be used in normal operational status | pre-prod, maint
Compliance | system is developed in accordance with standards and procedures | all
Security | system is protected | all

## Day 17 Feb 12, 2018

**Assignment 1 due** 

#### Quiz on Regression Testing

## Day 18 Feb 13, 2018

### Quiz 2 Regression Testing
Regression testing vs recover testing
- regression means we're not going backwards
    - goes in structural lbecause it's not about functionality, it's about behaviours 
    - you have already tested and now there is a change to the system
    - you have multiple components and one component changes therefore you have to test the whole thing since all components work together
    - want to make sure that something that has been working is _still_ working
- recovery testing
    - want to make sure the system can recover but mention recovery from where/what/how
    - what: possible failure
    - introduce the failure and see if the system can recover

#### Equivalent Partitioning Classes
- dividing system into out of bounds on the right and left and within bounds
- use max int and min int for partition ends
- partitions should not intersect

### Unit Testing
- piece of code that exercises a specific area of functinality
- helps you communicate the code's intended use (ie learn how to use the code)
- this is the basic testing
- any function of the system, class, module, component is considered for unit testing
- a good test:
    - has good probability of catching an error
    - not redundant
    - best of its type
    - not too simple, not too complex
    - it makes obvious failures
- no absolute certainty can be gained from pure testing activity
- natural approach such as using randomly generated test cases is inappropriate in most cases
- unit testing should be based on sound and systematic techniques
- tests should be repeatable, very critical for concurrent software

#### Unit Testing in Java
- assertions, written as Boolean expressions
- if false, then
    - error msg generated
    - execution is aborted
- assertions can be turned on when running the program for test purposes and turned off when the program is shipped to the user
- assertions can be turned on again by "-ea" flag

```
public void assertTrue(boolean condition) {
    if (!condition) {
        abort();
    }
}

public void assertEquals(int a, int b) {
    assertTrue(a == b);
}

```

#### Testing a Simple Method
- testing class that returns the largest element in a list

```
import junit.framework.*;
pubilc class TestLargest extends TestCase {
    public TestLargest(String name) {
        super(name);
    }

    public void testSimple() {
        assertEquals(9, Largest.largest(new int[] {7,8,9}));
    }
}


```

### Tutorial 5 Feb 14, 2018 

#### Miderm Review

1. Goal of software testing?
    - find defects and fix them
2. Difference between errors, defects and failures
    - errors are in defects are in failures
3. Which of them is/are component(s) of a test case?
    - a description of output data :heavy_check_mark:
    - invalid input
    - a description of procedure
    - all of the above
4. What is a test case?
    - Description of input data and dscription of data
5. What is the precondition and postcondition of the square root of x function?
    - precondition: x >=0
    - postcondition: x = ans*ans
    - for test cases we also need to give input conditions that are valid and unexpected as well as valid and expected ones
6. Setting up testing policy should meet 4 main criteria. Which of the following should be included in a testing policy?
    - Standards :heavy_check_mark:
    - Data requirements
    - Specification --- goes in the plan
    - Testing system :heavy_check_mark:
    - all of the above
- **4 main criteria**
    1. evaluation
    2. definitions of testing
    3. standards
    4. testing system
7. Which one of the above is/are component of the testing strategy
    - a process that can reduce those risks
    - test phase :heavy_check_mark: (?)
    - address the risks
    - test plan
    - test factor :heavy_check_mark:
    - all of the above
8. which are test factors?
    - portability :heavy_check_mark:
    - ease of operation :heavy_check_mark:
    - compliance :heavy_check_mark:
    - access control :heavy_check_mark:
    - error guessing
    - continuity of processing :heavy_check_mark:
    - ease of use :heavy_check_mark:
    - all of the above
9. which is/are not testing principle(s)?
    - programming organization must not attempt to find some of its error :heavy_check_mark:
    - thoroughly inspect the results of each test
    - programmer should avoid attempting to test his/her own program
    - plan the testing effort under the assumption that no error will be found :heavy_check_mark:
    - all of the above
10. Which one of them should be included in a test strategy matrix?
    - risks :heavy_check_mark:
    - script mapping
    - test phases :heavy_check_mark:
    - test cases
    - all of the above
- good test startegy matrix: test factors, phases (8 of them) and risks
- may need to make one for the exam
11. Which of them refers to recovery testing technique?
    - ensuring that recovery procedures are documented and back up data preserved :heavy_check_mark:
    - ensuring that the recovery testing activities are performed by the QA team
    - ensuring that the backup data is stored on site of rapid recovery
    - ensuring that the recovery personnel have been assigned and trained :heavy_check_mark:
12. Regressing tsting, stress testing and security testing are types of
    - dynamic testing (executing code) :heavy_check_mark:
    - static
    - both
    - none
13. The types of techniques useful in performing functional testing include:
    - parallel testing :heavy_check_mark:
    - integration testing
    - manual-support testing :heavy_check_mark:
    - error-handling testing :heavy_check_mark:
    - all of the above
14. Funtional testing is designed to ensure that:
    - the system performs as expected
    - the system delivers the results with appropriate accuracy
    - the system requirements and specification are achieved :heavy_check_mark:
    - all of the above
15. Which of the methods is requirements testing?
    - state transition :heavy_check_mark:
    - error handling
    - boundary value analysis :heavy_check_mark:
    - none of the above/all of the above
- requirements testing is a part of functional testing. error handling is a functional testing method but not a function of requirement testing.
16. Regression testing is used to ensure that:
    - segments perform as before
    - segments perform properly after a change has been applied :heavy_check_mark:
    - segments perform properly before a change is applied
    - none of the above
17. How to use error-handling testing?
    - create set of transactions that contain errors, determine if the application can identify the errors, check both improper handling and improper communication
18. How and when to use intersystem testing?
    - when: there is a change in parameters between application system
    - how: generate test transaction set in one application and pass to another system to verify the processing
        - execute the integration nodes between multiple systems to check data transfers are acceptable and processed properly
19. What is the difference between regression testing and manual support testing? Answer by contrasting 2 specific objectives for each 
    - regression testing
        - systems documentation remains current
        - system test data and test conditions remain current
        - previously tested systems functions perform properly after changes are introduced into the application system
    - manual-support testing
        - manual-support procedures are documented and complete
        - manual-support responsability has been assigned
        - manual-support team is adequately trained
        - manual support and the automated segment are properly interfaced
20. How and when to use parallel testing?
    - when: the result of complex processing are similar, uncertainty
    - how: same input data through 2 versions, done with part of whole system
21. You have been asked to test a system called M. There are several risks like system consistency (different versions), correctness (after change) and exception processing. Which 2 functional testing techniques are suitable to test system M?
    1. progression
    2. error-handling
22. Suppose there's a function called nextDate which takes 3 input integers - day, month and year. The requirement indicated that 1991 <= year <= 2060, 1 <= day <= 31. Generate test cases using boundary value analysis (take Feb as normal month). Ex input: year=2001, month=2, day=6 has expected output nextDate(year, month, day) = 2001.3.7
    - boundary value analysis
        - Year: 1990, 1991, 1992, 2000, 2059, 2060, 2061
        - Month: 0, 1, 2, 11, 12, 13
        - Day: 0, 1, 2, 30, 31, 31
        - Cartesian product
    - don't forget the 2 components of a test case: input and description of output
23. Generate test cases of question above using equivalence partition
    - Valid partition
        - Y1 = {year: 1991 <= year <= 2060}
        - M1 = {month: 1 <= month <= 12}
        - D1 = {day: 1 <= day <= 31}
    - Invalid partition
        - Y2 = {year: year < 1991}
        - Y3 = {year: year > 2060}
        - M2 = {month: month < 1}
        - M3 = {month: month > 12}
        - D2 = {day: day < 1}
        - D3 = {day: day > 31}
    - Test cases (low robust)

test case | year | month | day | expected output
----------|------|-------|-----|---------------
T1 | 1992 | 3 | 12 | 1992.3.13
T2 | 1903 | 3 | 12 | Year not in valid partition
T3 | 2070 | 3 | 12 | Year not in valid partition
T4 | 2000 | 0 | 12 | Month not in valid partition
T5 | 2000 | 13 | 12 | Month not in valid partition
T6 | 2000 | 3 | 0 | Day not in valid partition
T7 | 2000 | 3 | 32 | Day not in valid partition

    - some test cases (strong)
test case | year | month | day | expected output
----------|------|-------|-----|---------------
T8 | 1880 | -1 | 12 | Year, month not in valid partition
T9 | 1880 | 1 | -1 | Year, day not in valid 

24. Which one of them are included as structural testing techniques?
    - compliance testing :heavy_check_mark:
    - operations testing :heavy_check_mark:
    - manual support testing
    - recovery testing :heavy_check_mark:
    - parallel testing
    - all of the above
25. How to use stress testing:
    - Simulation, heavier volumes of data, larger number of users, error conditions
26. How to use recovery testing
    - access and evaluate adequancy, introduce a failure and evaluate recoverability, performing by people who would execute system IRL
27. What is the difference between execution testing and operations testing (answer by contrasting 2 specific objectives for each)
    - execution testing
        - performance of system structure
        - optimum use of hardware and software
        - response time to on-line use requests
        - transaction processing turnaround time
    - operation testing
        - completeness of computer operator documentation
        - support mechanisms
        - completeness of operator training
        - operators using prepared documentation can, in fact operate the system
28. What is the difference between compliance testing and security testing (answer by constrasting 2 specific objects of each)
    - compliance testing
        - development and maintenance methodologies
        - compliance to departmental standards, procedures and guidelines
        - completeness and reasonableness of applciation system documentation
    - security testing
        - adequate attention to identifying security risks
        - realistic definition and endorsement of access to the system
        - sufficient expertise exists to perform adequate security testing
        - conducting tests to ensure implemented security measures function properly
29. Test Principles: What are test principles
    - test policy: main criteria
    - test strategy components: test phase and test vector
    - test plan: the standard phases (8 of them)
30. Difference between functional and structural testing technique
    - for both
        - what it's used to do
        - what testing techniques does it contains
        - specific objective of each testing technique
        - when and how to use each testing technique
        - differences between each testing technique
31. For a specific testing scenario, which techniques is/are the best choice
32. How to generate test cases by using those principles.

- 12 questions in total
- will cover everything up to and including structural functions
    - testing principles
    - test policy, strategy, factors
    - testing techniques: functional structural
- at University Hall 213

## Day 19 Feb 26, 2018

----

## Day 20 Feb 27, 2018

### Empirical Unit Testing Principles

#### Complete Coverge Principle
- subject to many interpretations
    - each class consists of single elemt
    - group all input data into just one class
- this, we may evaluate how good a testing criterion is based on how significant the representatives of the classes obtained by decomposition are
- may need to partition to get deeper and deeper into the system
- for example below, D1 = x>0 && x > y, y > x would be one partion
- another partition, D2 = x > 0 && y > 0 && x <= y
- D3 = x<=0 || y <=0
- D4 = x < 0 || y < 0
- we need to branch when partitioning

```
f(int x, int y)
if(x>0 ^ y >0)
    if (x > y)
        x = x-y
        y = y-x
    else
        y = y-x

## Euclidiean GCM

Domain = Z x Z
d = (x, y)
T = {<x,y>, <x2, yz>,...}

Try
x <= 0
y <= 0
x = -5
y = 4
```
**Inconsistent Partition Example**

```x>0 && y=0```

#### Tutorial 6 Feb 28, 2018

**skipped**

## Day 21 Mar 1, 2018

**skipped**

## Day 22 Mar 5, 2018

## Day 23 Mar 6, 2018

#### Tutorial 7 Mar 7, 2018

## Day 24 Mar 8, 2018

## Day 25 Mar 12, 2018

[JUnit](https://junit.org/junit4)

### Parameterized Tests

```
import ..
@RunWith(Parameterized.Class)
public class Tests {
    Parameters(name = "")
    public static Collection<Object> data() {
        return Arrays.asList(new Object[][]....)
    }
}

```
#### Using Data Files
- concurrency testing
- DigitalAd app - as you move through mall, it displays ads relevant to you
- problem with unit testing this app
    - get location and get user is hidden so it cannot be tested
    - when you write code, think about you it will be tested
    - if get user/get location is in the same class as the mainfunction, it is hard to test

```
@Test
public void tGetAd() {
    assertEquals(expected, GetAd())
}
```
##### Solution/WorkAround
- capture system vars in to local
- use setup and teardown
- system variable: System.setOut(System.out)
- capture system input, work with it, reset it
- look for constructors that do one thing only

```
Type A f1;
int f2;

TYpe B(int i) {
    f1 = new TypeB();
    f2 = i;
}
```

```
TypeA f1;
int f2;

TYpe B(int i, TypeA a) {
    f1 = a;
    f2 = i;
}
```

```
method(~~user u...~~ Address) {
    calc SalesTax(user.address);
    return tax;
}

/global vs singleton/
```

**Look for _Guide: Writing Testable Code_**

## Day 26 Mar 13, 2018

### Security Testing
- types of security vulnerabilities
    - design
    - implementation
- design must specify security model's structure
    - if security mechanisms are required, how do they work
    - in multi-user program, desgn specifies how system users are **authenticated, authorized and audited**
    - for data input, how threats are mitigated

#### Design Vulnerability
- a mistake in the design that precludes the program from operating securely
- often found in software's security features
- parts that have no direct connection to security features

#### Implementation Vulnerability
- caused by security defects in the actual coding
- flaws in the code

#### Good Secure Software Design Principles
- compartmentalization
    - what does they user need to know to do his job
    - use of strong abstractions (many layers) and interface validations to ensure proper use of module
- least privilege principle
    - granting user or process the fewest privileges possible for it to complete its job
- separation of privileges
    - has to do mainly with not allowing one user to do everything but thinking of system's domain privileges
    - ensures multiple keys are needed to compelte sensitive transactions
- attack surface reduction
    - _how many_ points of interactions does the system have
    - more points = more surface for attack
    - solution: minimalize interface, 'need-to-know' basis
    - eliminates interfaces to software tht are not necessary to complete its work
- cryptography
    - hiding the message
    - protects the data so that if one security mechanism fails, the data needs decryption

#### Cryptography
- pitfalls
    - creating you own
    - choosing the wrong one
    - relying on security by obscurity
    - hard-coded secrets
    - mishandling private information
- symmetric/public key generation

### Tutorial 8 Mar 14, 2018
- use ignore for things that haven't been implemented but have a test case
- testing if statements
    - @org.junit.Test(timeout=1000)

#### Runner (annotations)
1. Parameterized
    - organize test cases
2. Suite
    - execute all (classes)
3. Category
    - classify test methods
4. Theories
    - cartesian product

#### Test Driven Development
- consider a project with testing in mind
- opposite is BDD (Behaviour)

#### Designing for Testability
- design that allows for automated testing
- should be
    - repeatable
    - easy to write 
    - easy to understand
    - fast
    - order independent
- need to encapsulate, isolate (dependencies), separate (simple methods), use protected instead of private 
- statement coverage: all inputs all statements
- alt-enter -> test

## Day 27 Mar 15, 2018

**skipped** :( we probably did cryptography

## Day 28 Mar 19, 2018

**skipped**

## Day 30 Mar 20, 2018

### Basics of Measurement
- as we understand more about attributes and relationship s between them, we develop
    - framework for describing them
    - tools for measuring them
- we have no deep understanding of software attributes

#### Basic Theory of Measurement
- this theory tells us
    - how to measure
    - how o analyze and depict data
    - how to tie results back to our original questions
- examples
    - euclidean (parallel lines never meet)
    - non-euclidean (parallel lines do meet)

#### Representational Theory of Measurement
- emiprirical relations
- we understand things better by comparing them, not assigning numbers
- observation reflects set of rules
    - we form pairs of people and define a binary relation "taller than" on them
    - we say who is taller than who
    - this is an empirical relation for height
- a (binary) empirical relation is one for which there is reasonable concensus about which pairs are in the relation
- they don't have to be binary
- they are mappings from the empirical, real world to a formal mathematical world
- intuitive

### Tutorial 9 Mar 21, 2018

#### Software Metrics
- **Halstead's Science**
    - n1 number of distinct operators in code
    - n2 number of distinct  operands
    - N1 occurences of operators
    - N2 occurences of operands
- lines of code (LOC) is a common metric
- program length (N) = N1 + N2
- volume = Nlog2(N1+N2)

#### Bug Counting Using Dynamic Analysis
1. failure count model
    - failure rate
2. error seeding model
    - debug vs bebug
    - error seeding = bebug
    - we have known errors that we introduce to the code and the programmer tries to identify them
    - developer testing
    - concerns performance
- number of exposed faults and number of undiscovered ones
- to help count total bugs and ensure if code is working

#### Software Reliability Metrics
- program is intangible so we use a matrix
- does software work within the 'stated time'?
- execute until failure occurs
    - fix an error in no time, resume and execute again
- there is also defensive programming

#### Software Requirement Metrics
- function points
    - number of inputs/output
    - how many user interactions
    - files
- used to calculate size and cost
- what sdlc

#### Programmer Productivity Metrics
- loc
- pgs of documntation
- depends on scale of project

#### Design Metrics
- cohesion and coupling
- fan in - how many modules are calling this module
- fan out - how many modules it calls

## Day 31 Mar 36, 2018

**skipped**

## Day 32 Mar 27, 2018

#### Quiz 4
- SQL injection
- difference between assertTrue and fail

### Scales
- differences among different kinds of mappings
- we're going to look at real world and mathematical domain
- homomorphic: whaetever happens in the real world should be mapped to mathematical
- 3 important questions
    1. how do we know when one numerical (or symbolic) relation system is preferable to another
        - generally we stick to numbers because it's simpler
    2. how do we know that what we see in the real world has a representation in mathematics
        - if a particular empirical relation sstem has a representation in a given numerical system
        - representation problem
    3. what do we do when we have several different possible representations in the same numerical relation system
        - want to know if they are equivalent or not
        - uniqueness problem
- generally, many different representations for a given emipirical relation system (S, {Ri | i in I}) where I is set of indices
- the higher the size of I, the fewer the representations
- R is richer than Q if Q in R because we have Q and some more

#### Scale Types
- 5 major types of scales, most richest to least (ie absolute you can do whatever you can do in 2-5 and more)
    1. absolute
    2. ratio
    3. interval
    4. ordinal
    5. nominal
- scale examples - height mapped in inches, km, etc
- scale is defined by homomorphism and the notion of admissible transformation
- mapping from one acceptable measure to another is called an admissible transformation (aka rescaling)
- scales and scales types lead to the notion of meaningfulness (and validity)
- meaningfulness - a statement with measurement values is meaningful iff its truth value is invariant to admissible transformations

```
M1(I1) : 5 ft
M2(I1) : 60 in
=> M_1(I1) = aM(I1) for a > 0
```

#### Nominal Scale
- nominal: comes from nomen, latin word for name
    - so nominal gives us names/categories
- Let (P, ~) be an empirical relational system, where P is a non-empty countable set and where ~ is an equivalnce relation on P. Let (R, =) be numerical mathematical structure with R its carrier set and = is its identity relation. Let μ: P --> R be a real value function. The system ((P,~),(R,=),μ) is a nominal scale iff - for all p and q where p, q are in P, p ~ q <--> μ(p) = μ(q))
- meaningful statistical operations
    - the admissible tranformation is only a one-to-one transformation
- only has identity (no magnitude)
- eg error is from design, requirements, code

### Tutorial 10 Mar 28, 2018

#### Lorenz Metrics
- avg method size - < 8 LOC (smalltalk) or < 24 LOC  (c++)
- smalltalk is oop
- average # methods per class - < 20 (more: too much responsability)
- average # instance vars - < 6
- class hierarchy - < 6
- number of comment lines per method - < 1
- high defect rate if high # methods/class
- low performance if low # methods/class

#### MOOD Metrics
- encapsulation
    - MHF - method hiding factor
    - shos sum of invisibilites attributed in all classes
    - formula
    - high HD means attributes are private
- inheritance
    - MIF - method inheritance factor
    - low - no methods existing in class as well as lacking inheritance statement
- polymorphism
    - complicated formula
    - if 100% it means all methods are overridden

#### CK OO Metrics Suite
- WMD - Weighted Methods per Class
    - sum of complexities of methods
- DIT - depth of ineritance tree
- NOC - number of children of a class
    - number of immediate subclasses
- CBO - Coupling Between Object classes
    - number of classes a given class uses
- RCF - Response for a class
- LCOM - lack of cohesion on methods
    - how closely methods are related to instance variables
- wmc low, dit high, noc low all imply low reuse through inheritance
- cbo/rfc difference indicates lack of use of inheritance
- low dit and noc - lack of inheritance reuse
- wmc, rfc, cbo - highly correlated

#### Li and Henry's Metrics
- DAC - number of attributes of a class
- DAC' - 
- NOM - number of local methods
- SIZE2

#### Productivity Methods
- units of output/units of effort
    - classes/methods - person-year
- possible estimates and if they are reached

#### Quality Metrics
- FP - function point 
- KLOC
- defects/KLOC, defects/FP

#### Education and SKills
- 18 mnths OOP

## Day 33 Mar 29, 2018

### Scales contd

#### Ordinal Scale
- entities have an order/severity
- an emprirical relational system where P is a non-empty countable set and yo uhave a emprircal relation describing ranking propertis on P
-  there is also a numerical mathematical strucuture with R as a carrier set and a partial order
-  μ: P --> RR is a real value function and you have an oridinal scale iff we can say p is somehow higher than q is the same thing as saying that μ(p) >= μ(q)
- there is identity + magnitude

#### Interval Scale
- mostly will look at nominal and ordinal
- there are units associated with this one
- eg if we have ordinal scale of high, med, low - we can say that each is 6, 4, 2
- not intuitive in software measurement
- algebraic difference structure // 
    - A x A cartesian product with interval relation
    - there are 5 axioms tis above relation satisfies
        1. Weak Order
        2. Transitivity
        `- if you have interval 1 A x A and interval 2 A x A, either interval 1 is greater than 2 or 2 is greater than 1
        3. another transitivity relation?
        4. equivalence of intervals: if ab > cd and cd > ab then we have 2 d's, d' and d"
            - very unintuitive
        5. if a sequence is strictly bounded, it is finite
- interval scale is an algebraic difference structure
    - when looking at intervals (a,b) >~ (c,d), there is a function μ saying that μ(a) - μ(b) >= μ(c) - μ(d)
    - only good one is f or c but not k

#### Ratio Scale
- set of entities with relation

## Day 34 Apr 2, 2018

### Admissible Transformation
- is LOC a direct measurement? - obtained by looking and counting
- is 1000 lines of code direct or indirect?

Scale | Admissible Transformation
---------|------------------------
nominal | any one-to-one (no repeats)
ordinal | g is a strictly increasing monotonic function (since things have order + no repeats)
interval | g(x) = a*μ(x) + b, a > 0, b !=0 - x is infinite set
ratio | g(x) = aμ(x), a > 0

*interval - to show it is not admissible, find an x for which g(x) does not hold?
μ2 = aμ1 + b

### Statistical Operations on Measures

you can compute | nominal | ordinal | interval | ratio
------------------|---------|---------|-------|----------
frequency distribution | 1 | 1 | 1 | 1
medians and percentiles | 0 | 1 | 1 | 1
add or subtract | 0 | 0 | 1 | 1
mean, std deviation, std error | 0 | 0 | 1 | 1
ratio, or coefficient of variation | 0 | 0 | 0 | 1

## Day 35 Apr 3, 2018

#### Tutorial Apr 4, 2018

## Day 36 Apr 5, 2018
- estimating defects (using math but also make assumptions)
-  measurements - be v mathematical
- scale is a representaion of the mapping of a function real+math world

