# 3A04 Software Design III 

## Table of Contents
- [Course Breakdown](#course-breakdown)
- [Last Year Final Exam](#last-year-final-exam)
- [Grading and Textboook](#grading-and-textboook)
- [Introduction to Software Architecture](#introduction-to-software-architecture)
- [SDLC V Model](#sdlc-v-model)
- [What is meant by Software Architecture](#what-is-meant-by-software-architecture)
- [Role of Software Architect](#role-of-software-architect)
- [Code Structure](#code-structure)
- [3 things in architecture](#3-things-in-architecture)
- [Project Runtime Structure](#project-runtime-structure)
- [Software Management Structure](#software-management-structure)
- [Software Elements](#software-elements)
- [Group Project Overview and Deadlines](#group-project-overview-and-deadlines)
- [Software Connectors](#software-connectors)
- [Iterative Refinement of an Architecture](#iterative-refinement-of-an-architecture)
- [Models](#models)
- [4 plus 1 Model](#4-plus-1-model)
- [UML for Software Architecture](#uml-for-software-architecture)
- [Surprise Quiz 1](#surprise-quiz-1)
- [How to find the views](#how-to-find-the-views)
- [Tutorial 2 Jan 23, 2018](#tutorial-2-jan-23-2018)
- [UML](#uml)
- [Structural Static Diagrams](#structural-static-diagrams)
- [Structural (Static) and Behavioural (Dynamic) Diagrams](#structural-static-and-behavioural-dynamic-diagrams)
- [General Design Principles](#general-design-principles)
- [Design Principles for Security](#design-principles-for-security)
- [Data Flow Architecture](#data-flow-architecture)
- [Batch Sequential](#batch-sequential)

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
 
### Grading and Textboook
 
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
  - may be oral?
  
**Textbook**
Software Architecture and Design Illuminated
  
## Day 2 Jan 8, 2018

### Introduction to Software Architecture

#### What is Design
- can be seen in any human artefact and in nature
- objective and subjective
  - aesthetic (look and feel) vs functional (speed performance)
  - artistic or mathematical or both?
- decomposition of complex systems/artifacts is an aim of design

#### Design as a mathematical activity
- Construction of a deterministic finite automata that takes in strings of binary with even number of 0s and number of 1s is a multiple of 3
- **Design Process**: create a language to satisfy constraints
- L(M3) is an intersection of 2 languages L(M1) and L(M2) therefore we use product construction

Design coukd be viewed as an activity that translates an idea/goal into a blueprint for an artefact or a process that is fit for its envionment

## Day 3 Jan 10, 2018

- Group project: **identifying objects** :frog:
- good design in software reduces risks
- makes system traceable for implementation and testing

### SDLC V Model

![](img/VModel.PNG)

### What is meant by Software Architecture
- blueprint for developing small and large systems based on requirement analysis
- highlights early decisions
- has set of constraints (space, time, budget)
- Considers separation of concerns
  - each software component hides something
- there are connectors between software components

:sleepy:

**Must be included in software architecture**
- specialization of software elements
- connection types
- set of constraints (space, time, budget)
- set of desired quality attributes (eg performance)

#### Architecture Style
- families of similar architectures
- represents the way elements are arranged, connections and interactions among elements, quality attributes, etc

#### System Architecture
- IEEE Std 1471 - "the fundamental organization of a system embodied in its components, their relationships to each other, and to the environment, and the principle guiding its design and evolution"

### Role of Software Architect
- system static partioning
- decomposing system into sub-systems
- establish dynamic control relationships between sub-systems
- quality attribute tradeoff analysis

## Day 4 Jan 12, 2018

**Discussion Day**

- software architecture can be given from several perspectives
  - software code units (elements are source, binary code, modules)
  - project's runtime structure (elements are threads, processes, transactions)
  - allocation structure (project management structure)
- each structure class uses different connectors and different performance attributes

:cry: :cry: **so hungry** :cry: :cry:
 
### Code Structure
- **module** : software component that hides a secret - big part of code structure
  - behaviour hiding modules
  - hardware hiding modules (hide communication between software and hardware)
    - eg robot's secret is its language
  - software hiding modules
    - have secrets like algorithms, data structures (can be generalized to 3 types - tuples, list, sets)
- amount of knowledge that component modules have of each other kept to minimum (**high cohesion low coupling**)
- information flow between compoenents is restricted to flow from method calls
- connectors in structures have:
  - direction - if module A invokes a method of module B then A -> B is connected
  - synchronization
    - asynchronous - operates independently
    - synchronous - process runs as result of other processes
  - sequence - some connectors must be used in particular sequence (label connector with sequence id)

 ## Day 5 Jan 15, 2018

- last week we began to look at 3 architectural views - code view, runtime view, management view

### 3 things in architecture
- we give many views that provide 3 things
  1. components
  2. connectors
  3. rationale for having the above to explain non-functional reqs

### Project Runtime Structure
- at runtime project can be **threads**, **processes**, **functional units** and **data units**
- these elements ay run on the same or multiple computers
- elements in code structures can implement or support multiple runtime elements (modules implement processes)
- several code structure elements may implement or support single runtime element (many threads in different code units)
- connectors at this level inherit atributes from their source-code counterparts
  - **multiplicity** - one element may be connected to multiple other elements if it needs to invoke methods of multiple elements at runtime
  - **distance and connection media** - two connected elements may communicate in the same process/thread/computer
    - eg communication by optical cable OR LAN to the media
  - **universal invokable** - protocol to communicate with an element
    - software protocol is a way of exchanging information eg bluetooth is 15 dif protocols
  - **self-descriptive** - allow external software system to invoke its target methods without pre-installation

### Software Management Structure
- ~~are we skipping this just because???~~
- used for project resource allocation

### Software Elements
- they have functions and are connected into dependency graphs through connectors
- each one has different synchronization and performance constraints
- some elements are re-entrant - usually more efficient since they avoid synchronization, therefore can be safely executed concurrently, they can be implemented by any thread or process

#### Basic Guidelines for runtime elements
1. business logics may not allow some elements to be reentrant since order of operations matters a lot when you have shared resources
2. if element is reentrant and multiple threads or processes may need to communicate with it, must run on separate threads or processes (thread safety)
3. if element has high multiplicity and performance is important to global system, use an application server for implementation
4. if heavy computations innvolved for deployment at particular location, consider using _cluster of processes_
  - architecture is master-slave but it will suffer from performance problem if a master is connected to like 1000 slave processors at one layer
    - if multiple layers it is mores manageable
  - size of cluster is determined by computation load and communication traffic

  ![](img/cluster.PNG)

5. if element is assigned well-defined complex functions and similar off-the-shelf software exists and performance not critical then use **off the shelf solution**
6. complex system can be expanded into sub-system with its own elements and connectors
7. complex element can be transformed into sequence of layered elements
  - each layered element hides low-level system details from upper layers
![](img/layered.PNG)

8. complex element can be transformed into sequence of tiered elements (each interface must be well-defined)

![](img/tiered.PNG)

## Tutorial 1 Jan 16, 2018

### Group Project Overview and Deadlines
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

## Day 6 Jan 17, 2018

### Software Connectors
- in abstract form, connector indicates necessity during system execution for 1 element to send message to another elemnt
- if those 2 elements mapped to single process, connector could be mapped to local method invocation
- if those 2 elements mapped to two different processes on same computer, then connector could be mapped to local message queue or an operating system pipe
- if those 2 elements mapped to 2 different computers then remote method invocation or Web service invocation can be used

#### Software Connector Attributes
- Synchronization mode - eg sempaphores, blocking/non-blocking
- Initiator
  - makes request for communication
  - one-initiator connectors - client initiates communication
  - two-initiator connectors - if they are non-blocking
  - callback support - requires two-initiator connectos
- Information carrier perspective
  - what medium to use
    - variable (2 threads in same process)
    - environment resource (register, pipes, file, local message queues)
    - method invocation and message
- Implementation type 
  - protocol-based can implement multiple operations
  - signature-based methods implemnt **one** type of operation
- Active Time
  - when you make connection to program
  - event-driven - when something becomes active, something happens (reactive systems like thermostat)
- Connective Span (Perspective)
  - scope: local or global (network)?

  ![](img/elements.PNG)

- Connector fan-out
  - is it a one-to-one connector or many-to-many
  - one-many have more important impacts on implementation
- Connector environment
  - homogeneous (same programming language and software framework and same OS)
  - heterogeneous

### Iterative Refinement of an Architecture
- third part of architecture (elements, connectors, now **iterative refinement**)
- givem project spec, an absract high level software architecture is proposed (elements + connectors)
- goes through multiple refinement phases

#### Example steps of implementing an architecture
1. standalone, local system
  ![](img/step1_standalone.PNG)
2. remote system
  ![](img/step2_network.PNG)
3. refine system by adding protocols
  ![](img/step3_http.PNG)
4. layered architecture
  ![](img/step4_layered.PNG)

### Models
**Third slide set**

- Will discuss the 4 + 1 model for architecture
- architecture has components, connections and interactions between these components
- need to specify configuration topology
  - **Bus** is an infrastructure or more formally, a sofware system
    - the bad thing about the bus infrastructure is that if a single part of the system fails, the inter-related system makes it so that the whole thing fails (most of the time)
  - **Star** architecture has a central node with things coming into it
    - not that much differnet from bus
  - **C4/K4** is like a square with an X in the middle
    - aka C<sub>N</sub>, every edge has N-1 connections
    - the good thing is: if one of the nodes fails the system still functiona
    - bad thing: it is complex so it might require more maintenance as well as redundant information

#### Ways to describe software architecture
  - formal (ADL) and informal (UML) ways
  - Box-and-line diagram - formal way
    - describes business concept
    - lines indicate relationshp among components (unlike UML)
    - lines may refer to dependancy, control flow, data flow
    - lines may be associated with arrows to indicate process direction and sequence
  - UML is one of the Object-Oriented solutions for software modeling and design
  - "4+1" view is another way to show different views with different concerns for dif aspects (F + NF reqs)
    - it is formal, UML

## Day 7 Jan 19, 2018

### 4 plus 1 Model
- has 5 views
  1. Logical View - identifies software modules and their boundaries
  2. Process View - addresses non-functional requirements and performance at runtime
  3. Development View - organizes software units appropriately
  4. Physical View - specifies physical software, hardwar, network configuration, installation and deployment
  5. Scenario/User Interface View - most important, gives look and feel

![](img/4plus1.PNG)

### UML for Software Architecture
- UML is a graphical language for visualizing, specifying, constructing and documenting software artifacts aka **system's blueprints**
- system within environment has interactions, actors, initiators for events
- **event** - initializes set of interactions
- **business event** - is independent from the system. It is from the environment to the system. has an initiator
  - happening that the system has to deal with outside of the system is followed by interaction between environment and system
- **scenario** - series of interactions between system and environment triggered by business event
- for every business event, there are view points, each view point is associated with a scenario
 
**Scenario View**

- BE<sub>2</sub>
  - VP1
    - Scenario
  - VP2
    - Scenario
    - ```Scenario has system response and actor and system - should end with system```

...

- BE<sub>n</sub>

## Day 8 Jan 22, 2018

### Surprise Quiz 1
What is a business event?
- An occurence outside of the environment of the system that initiates some sort of interaction in the system.

What role business events play in determining the scenario view in the 4+1 model?
- Each business event has view points and each view point has a scenario
- business events can be modelled using templates such as Volere, IEEE, Boeing, Ministry of Defense of UK
- systems have modes (assisstants) which denote a set of states of a program
- these sets of states are encompassed by classes
- scenarios can be described using modes (a scenario for each mode) - tells you how machine is supposed to work
  - however each mode can have multiple view points and a scenario for each viewpoint
  - ex James Bond's car can have a car viewpoint and a submarine view


### How to find the views
- 4+1 model is what most software architectures follow

#### Logical View
1. Read the scenario
  - identify the names
    - ie user, which is outside of the system

    ```
    Scenario:
      -------Name 1------
      -------Name 2------
    ```
    - we are looking for if the above name belongs to the environment
    - if the name belongs to the system then it is potentially a class/module
  - identify the verbs
2. Write a diagram

#### Process View
Looking at logical view we can determine the process view.
Below is a package diagram for procss view.

![](img/process_view.PNG)

#### Development View
- once you have identified classes and modules
- this is also known as the source code view
- below is an activity diagram for development

![](img/development_view.PNG)

#### Physical View
- depends on the other views
- allows you to organize what packages you need (from development view)
- need to know specifications like concurrency (from process view)

![](img/physical_view.PNG)

### Tutorial 2 Jan 23, 2018
- tips on writing software requirements document
- user characteristics: who is going to be using your product and what is the scope of their knowledge?
- constraints: any constraints that you, the team, has that must be abided
- apportioning of requirements: any requirements you need to cut out (this should **not** be part of this SRS)
- section 3 - highlight your **innovative idea**, usually the longest section
- use slide 29, not 30 for the viewpoints (business events followed by viewpoints)
- you don't need to have political requirement so just say n/a

## Day 9 Jan 24, 2018

### UML
- used to describe structural software architecture
- there is a class hierarchy and structure
- the relationshps between classes include:
  - inheritance
    - is-a
  - aggregation - aka composition
    - has-a
  - association
    - uses-a
  - messaging
    - method invocation
- we wish to depict the control flow between software elements (class diagram, component diagram, deployment diagram)
- Behavioural dynamic software architecture describes behaviour of objects (classes) and entails sequence diagrams, collaboration diagrams and activity diagrams

#### Tools for UML
- Rational Rose, Boland Together, Microsoft Visio
- might get these in the future

### Structural Static Diagrams

#### Class Diagrams
- each of the views in the 4+1 model have a class diagram
- the elements of a class are class name, attributes, operations
- there are 3 types of classes
  1. **boundary** - secret of this class is how to communicate with the environment (the edge of the system)
    - <span style="color:blue">hardware hiding</span>, environment hiding
    - it is an interface class 
  2. **entity** - secret is the <span style="color:blue">software-hiding</span> modules (like tuple)  
  3. **control** - finite state machine
    - controls flow of system
    - secret is the algorithm of <span style="color:blue">behaviour-hiding</span>
  
### Structural (Static) and Behavioural (Dynamic) Diagrams
  
#### Structural (Static) Diagrams
  - object diagram (objects)
  - composite structure diagram (inner structure)
  - component diagram (relationships and interactions)
  - package diagram (package structure)
  - deployment diagram (hardware, software, network)

#### Behavioural (Dynamic) Diagrams
- Use Case Diagrams
  - it is a visual representation of a scenario
  - there are actors that are part of the environment outside the system
  - they trigger business events 
  - sees the system as a blackbox, doesn't tell you what system does

  ![](img/usecase.PNG)
- Activity Diagram
  - 

## Day 10 Jan 26, 2018
- looking over at diagrams

**Finite state machine**
- components are
  - start state
  - set of inputs
  - set of states
  - language

1. What are the main characteristics that an event needs to satisfy to be considered as a relevent business event. Explain the role played by business events in identifying the functional requirements
- it needs to be inititaed from outside the system that evokees some resonse from the system
- each scenario and viewpoint is a functional requirement
- good starting point for writing functional requirements

2. Read the following informal requirements and identify one business event
> the turnstile consists of a rotating barrier and a coin slot and is fitted with an 
> electrical interface. The mechanial apparatus has alrady been chosen and the 
> development project is to provide controling software. To enter the stadium, a vistor
> must first insert the correct coin into the coin slot and then push the turnstile
> barrier for access. The turstile is equipped with a locking device, when locked it
> prevents barrier from rotating. The controlling s/w should only allow the barrier to
> rotate once when a valid coin has been inserted.

- request to enter the stadium

3. - What are the models of a software system? Give an example of one formal design model and one rigorous design model
- (partial and approximative) descriptions of different aspects of the system/artefact that put emphasis on some things
- graph (set of edges and vertices)

4. Software architects initiate their work from the requirements specification document. Explain the influence of the non-functional requirements on the architecture of a system. Can the architect always satisfy the non functional requirements as stipulated in the requirements document and why?
- in canada the registration system _works_ but it had to be cancelled because a lot of non functional requirements were left out
- sometimes the architect cannot satisfy nf reqs completely and must compromise

5. WHen designing a trave application, a designer came up with the followin class diagram. (AppClass ---> [trip1, trip2]) However new requirements reveal we can have several other categroies of trips such as land trip, sea trip, river trip that involves a non-empty subset of these catgeories. Propose new class diagram that captures these new requirements and would easily allow addition of new trip categories.
- System ---> Trip ---> all the different kinds of trips

6. Many to many relationships can be awkward to implement. They can sometimes be simplified thanks to a mediator class or 'event remembered'. Consider a wedding gift registration system. Every store registers many couples Every couple registers with many stores. The Store <---> couple diagram caputres many-to-many. Propose another diagram modeling the system but introduce mediator called _Registration_.
- Store ------ Registration --------- Couple

7. Name and explain the role of 3 types of classes used in Analysis Class Diagram. Which one has an n-tuple secret
- boundary, entity, controller
- entity is tuple

## Day 11 Jan 2, 2018

### General Design Principles
- low coupling and high cohesion
- in object oriented need to have controller classes

![](img/cohesion_coupling.PNG)

- **interface** - abtract class that implements a contract. it tells you it doesn't have a concrete implementation of its methods but it has the method signature

#### Principle Of High Cohesion Low Coupling

#### Open-Closed Principle
- open to extension: system can be extended to meet new requirements
- closed to modification: the existing implementation and code should not be modified as a result of system expansion
- separation of implementation and interface
- keep attributes private
- minimize use of global variables

#### Liskov Subsitution Principle
- let q(x) be  a provable property for objects x and type T. Then q(y) should be true for y objects of subset of type T
- by design by contracts, it leads to restrictions on interactions having to do with inheritance
- preconditions cannot be strengthened in subtype
- postconditions cannot be weakened
- invariants must be preserved in subtype

## Day 12 Jan 31, 2018

#### Dependency Inversion Principle
- Packages that are maximally stable should be maximally abstract. Instable packages should be concrete. The abstraction of a package should be in proportion to its stability.
- can have partner apps
- concrete but has business rules that are likely to change

#### Interface Segregation Principle
- Clients shouls not be forced to depend upon interfaces that they do not use
- if there are 2 non-cohesive functionalities, keep them separate
- avoids design of fat interfaces and provides clear design to user
- break the functionalities into atomic interfaces that can be then individually accessed by the user

#### Law of Demeter

### Design Principles for Security

#### Principle of Least Privilege

#### Fail-Safe Defaults
- when system fails we back up
- unless subject is given explicit access to an object, it should beb denied access to that object
- assumes tHt the default access to an object is none
- if the subject is unable to complete its action or task, it should undo those changes it made to thte security state of the system becore it terminates
- fault-tolerance: when we can't guarantee that system will behave in a safe way

#### Principle of Economy of Mechanism
- security mechanisms should be as simple as possible

## Day 13 Feb 2, 2018

**skipped**

## Day 14 Feb 5, 2018

### Data Flow Architecture
- Data coming in, going through a bunch of tranformations
- software system is decomposed into functional processing modules
- focus in data flow architecture is data availability
  - in batches or streams
  - linear
  - cyclic
  - tree
- no interaction between modules except the data connection between them
- modifiability and reusability are the property attributes of data flow architecture
- function is a relation that is deterministic


### Batch Sequential
- this architecture is available in the financial sector
- they use COBOL or RPG
- COBOL is specifically designed for this stuff
- in Java, your class has declaration (the datatype), behavioural (the functions)
- in COBOL you have:
  - identification
    - program id
    - author
    - installation
    - date written/compiled
  - environment
    - configuration
      - source computer - the one on which we compile
      - object computer - the one where it is supposed to run
    - input - all the input files
  - data
    - file section 
      - file description
      - blockage factor - allows you to read files in 'N' factors, N = blockage factor
    - tape section
  - procedure
    - the program and its functions

![](img/batch.PNG)

- when sorting with batch sequential you can run into 2 situations
  - after partitioning N ways, can I sort the data?
     - merge and sort and merge and sort and merge and sort
    - hadoop
