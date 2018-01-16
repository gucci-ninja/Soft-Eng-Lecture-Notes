# 3A04 Software Design III 

## Table of Contents
- [Course Breakdown](#course-breakdown)
- [Last Year Final Exam](#last-year-final-exam)
- [Grading](#grading)
- [Textbook](#textbook)
- [SDLC V Model](#sdlc-v-model)
- [Code Structure](#code-structure)
- [Project Runtime Structure](#project-runtime-structure)
- [Software Management Structure](#software-management-structure)
- [Software Elements](#software-elements)
- [Tutorial 1 Jan 16, 2018](#tutorial-1-jan-16-2018)

## Day 1 Jan 5, 2018

- Fridays are for problem solving :relieved:

### Course Breakdown

1. Software requirements
  - Pre-reqs -> reqs -> Architecture design -> Coding -> Testing
2. Software architecture design space (types of software structures, software elements, sofware connectors)
3. Design Principles for sustainable systems
4. How to approach practical problems using architecture design

### Last Year Final Exam

5. Using appropriate design pricnciples, compare 2 designs in figure.
  Design A - interconnected, multi-directed, a lot of things depend on other things
  Design B - organized, singly directed, not a lot of interdependency
  
  Design B is better as it has low coupling high cohesion! :bowtie:
  
6. Build simple software that translates Fahrenheit to Celcius. Choose suitable architecture design.
    - not that hard :innocent:
    
8. AI system. Algorithm has uncertainty therefore we need specific architecture. What wil be the most suitable architecture?
  
9. Gives context for system, system to allow fire dept to follow fire situation in agricultural, forest, industrial areas. System will have sensors for each area.
    - choose appropriate software architecture
 
### Grading
 
- Project
  - teams of 4-5 (not chosen by us :cold_sweat:)
  - need log book 
  - will appoint leader 
- Surprise 5-10 minute Quizzes :expressionless:
  - up to 6, can drop 1
- Midterm (Feb 26) worth 20%
- Exam
  - counts for (40 - 2* number of quizzes that count)% of your score
  - eg if 4 quizzes then (40 - 2*3)% = 34%
  - may be oral?????
  
### Textbook
Software Architecture and Design Illuminated
  
## Day 2 Jan 8, 2018

**What is Design**
- not easy to define
- can be seen in ny human artefact and in nature
- objective and subjective
  - aesthetic (look and feel) vs functional (speed performance)

**Deterministic Finite Automata**
- take in strings of binary with even number of 0 and numberof 1s is multiple of 3
- Product Construction: when you have 2 machines 

## Day 3 Jan 10, 2018

- Next week's project: **identifying objects** :frog:
- good design in software reduces risks
- makes system traceable for implementation and testing

### SDLC V Model
Steps | Relation | Corresponding steps
------|----------|-----------------
1. Pre-requirements | <-Cost-> | 9. Production Operation and Maintenance
2. Production Reqs |<------>| 8. System Testing
3. Architecture Design |<------>| 7. Integration Testing
4. Detailed Design |<------> |6. Unit Testing
  - | 5. Coding | -

#### What is meant by Software Architecture
- blueprint for developing small and large systems based on requirement analysis
- highlights early decisions
- has set of constraints (space, time, budget)
- Considers separation of concerns
  - each software component hides something
- there are connectors between software components

:sleepy:

## Day 4 Jan 12, 2018

**Discussion Day**

- software architecture can be given from several perspectives
  - software code units (elements are source, binary code, modules)
  - project's runtime structure (elements are threads, processes, transactions)
  - allocation structure (project management structure)
- each structure class uses different connectors and different performance attributes
- **module** : software component that hides a secret
  - behaviour hiding
  - hardware hiding (hide communication between software and hardware)
    - eg robot's secret is its language
  - software hiding modules
    - have secrets like algorithms, data structures (can be generalized to 3 types - tuples, list, sets)

:cry: :cry: **so hungry** :cry: :cry:
 
### Code Structure
- amount of knowledge that compnents/modules have of each other kept to minimum
- information flow between compoenents is restricted to flow from method calls
- connectors in structures have:
  - direction - if module A invokes a method of module B then A -> B is connected
  - synchronization
    - asynchronous - operates independently
    - synchronous - process runs as result of other processes
  - sequence - some connectors must be used in particular sequence (label connector with sequence id)

 ## Day 5 Jan 15, 2018

- last week we began to look at 3 architectural views - code view, runtime view, management view

- **3 things in architecture** - we give many views that provide 3 things
  1. components
  2. connectors
  3. rationale for having the above to explain non-functional reqs

### Project Runtime Structure
- many threads can run multiple methods from multiple classes
- connectors at this level inherit atributes from their cource-code counterparts
  - **multiplicity** - one element may be connected to multiple other elements if it needs to invoke methods of multiple elements at runtime
  - **distance and connection media** - two connected elements may communicate in the same process/thread/computer
    - eg communication by optical cable OR LAN to the media
  - **universal invokable** - protocol to communicate with an element
    - software protocol is a way of exchanging information eg bluetooth is 15 dif protocols
  - **self-descriptive** - allow external software system to invoke its target methods without pre-installation

### Software Management Structure
- are we skipping this just because???

### Software Elements
- each one has different synchronization and performance constraints
- reentrant elements - usually more efficient since they avoid synchronization, can be implemented by any thread or process
- business logics may not allow some elements to be reentrant since order of operations matters a lot when you have shared resources
- **rule** if element is reentrant and multiple threads or processes may need to communicate with it, must run on separate threads or processes (thread safety)
- **rule** if element has high multiplicity and performance is important to global system, use an appliatoin server for implementation

**Basic Guidelines**
- if heavy coomputations innvolved for deployment at particular location, consider using _cluster of processes_
  - architecture is master-slave but it will suffer from performance problem if a master is connected to like 1000 slave processors at one layer
    - if multiple layers it is more manageable
  - size of cluster is determined by computation load and communication traffic
- if element is assigned well-defined complex functions and similar off-the-shelf software exists and performance not critical then use **off the shelf solution**

### Tutorial 1 Jan 16, 2018

- identification app for Android
- can be specific or general
- need 3 experts that guess what the thing is (experts must be disjoint, communicate with central forum)
- experts can say I don't know
- must use some sort of database to store results
- _keep a log book_

**Deadlines**
- Feb 9 - SRS Doc (list functional/nf reqs by business event)
- Mar 9 - Use Case Diagram and SRC Diagram, introduce classes
- Mar 30 - Code
- Apr 6 - Final

