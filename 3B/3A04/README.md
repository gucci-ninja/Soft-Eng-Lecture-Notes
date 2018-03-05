# 3A04 Software Design III 

## Table of Contents
- [Course Breakdown](#course-breakdown)
- [Last Year Final Exam](#last-year-final-exam)
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
- [Behavioural (Dynamic) Diagrams](#behavioural-dynamic-diagrams)
- [General Design Principles](#general-design-principles)
- [Design Principles for Security](#design-principles-for-security)
- [Data Flow Architecture](#data-flow-architecture)
- [Batch Sequential](#batch-sequential)
- [Pipe and Filter Architecture](#pipe-and-filter-architecture)
- [Process Control Architecture](#process-control-architecture)
- [Data Centered Software Architecture](#data-centered-software-architecture)
- [Midterm 2017](#midterm-2017)
- [Hierarchy Structure](#hierarchy-structure)
- [Main Subroutine Software Architecture](#main-subroutine-software-architecture)
- [Master Slave Architecture](#master-slave-architecture)
- [Layered Architecture](#layered-architecture)

## Day 1 Jan 5, 2018

- Fridays are for problem solving :relieved:

### Course Breakdown

1. Software requirements
  - Pre-reqs
  - reqs
  - Architecture design 
  - Coding
  - Testing
2. Software architecture design space (types of software structures, software elements, sofware connectors)
3. Design Principles for sustainable systems
4. How to approach practical problems using architecture design

### Last Year Final Exam

1. Using appropriate design principles, compare 2 designs in the figure.
  Design A - interconnected, multi-directed, a lot of things depend on other things
  Design B - organized, singly directed, not a lot of interdependency
  
  Design B is better as it has low coupling high cohesion! :bowtie:
  
2. Build simple software that translates Fahrenheit to Celcius. Choose suitable architecture design.
    - not that hard :innocent:
    
3. AI system. Algorithm has uncertainty therefore we need specific architecture. What wil be the most suitable architecture?
  
4. Given context for system, system to allow fire dept to follow fire situation in agricultural, forest, industrial areas. System will have sensors for each area.
    - choose appropriate software architecture
 
#### Grading and Textboook
 
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

Design could be viewed as an activity that translates an idea/goal into a blueprint for an artefact or a process that is fit for its envionment

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
- Synchronization mode - eg semaphores, blocking/non-blocking
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
  4. Physical View - specifies physical software, hardware, network configuration, installation and deployment
  5. Scenario/User Interface View - most important, gives look and feel

![](img/4plus1.PNG)

### UML for Software Architecture
- UML is a graphical language for visualizing, specifying, constructing and documenting software artifacts aka **system's blueprints**
- UML provides many modeling diagrams of 2 major categories - structural (static), behavioural (dynamic)
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
- these can be derived from use cases/scenarios
- the elements of a class are class name, attributes, operations
- relationships (connectors)
  - composition (HAS A)
    - components have same lifespan as owner
    - components cannot be involved in another composition
  - aggregation (HAS A) 
    - components do not have same lifespan as owner
    - components can be involved in another comp
  - association (USES A)
    - includes name, type and multiplicity
    - composition is a type of association
  - dependency
    - x depends on y if changes to y leads to changes in x
  - inheritance (IS A)
    - when attributes are common btwn classes
    - this weakens the encapsulation of an OO design
- object diagram
  - gives objects + relationship at runtime
  - overview of instances of class diagram at point in time
  - based on class diagram
- composite structure diagram
  - describes inner structure of component (all classes and interface)
- component diagram
  - describes all components of system
  - gives interrelationships, interactions, interface
  - outline of composition structure of components or modules
- package diagram 
  - describes package structure and organization
  - covers classes in package and packages within packages
- deployment diagram
  - describes hardware, software, network connections for distributed computing
  - covers server configuration and network 


- there are 3 types of classes
  1. **boundary** - secret of this class is how to communicate with the environment (the edge of the system)
    - <span style="color:blue">hardware hiding</span>, environment hiding
    - it is an interface class 
  2. **entity** - secret is the <span style="color:blue">software-hiding</span> modules (like tuple)  
  3. **control** - finite state machine
    - controls flow of system
    - secret is the algorithm of <span style="color:blue">behaviour-hiding</span>
  

### Behavioural (Dynamic) Diagrams
- Use Case Diagrams
  - it is a visual representation of a scenario
  - there are actors that are part of the environment outside the system
  - they trigger business events 
  - sees the system as a blackbox, doesn't tell you what system does

  ![](img/usecase.PNG)
- Activity Diagram
  - outline of activity data and control flow
  - workflow oriented diagram
  - covers decision points
- State Machine
  - life cyce of an object
  - diagram has states and transitions
  - system + business process
- Interaction Overview
  - combines activity and sequence diagrams to provide control flow
- Sequence of Diagram
  - chronological sequence of messages between objects
  - corresponds to 1 use case
  - full arrowhead: synchronous message
  - half arrowhead: asynchronous message
- Communication Diagram
  - describes message passing sequence
  - depicts how object receives and sends messages
  - every communication diagram is equivalent/can be converted to sequence diagram
- Timing Diagram
  - combines state diagram and time sequence
  - dynamic view of state change caused by external events over time
  
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
- don't have a lot of interdependent classes or it will be hard to maintain
- change in one class may lead to cascading updates to other classes
- tight-coupling can be removed with new classes or inheritance
- there should be easy expansion, simplicity and elegance
- improvements in information hiding help system to be more cohesive
- makes systems easier to modify
- 7 +- 2 is a useful guideline - difference between small and large scale projects is amount of nesting btwn modules
- possible architecture for **video games** consists of
  - environment of game (areas, connections)
  - mechanism controlling the game (encounters, reactions to events)
  - participants in game (player, foreign characters)
  - artifacts in game (sword, books)
- personal finance app would have
  - accounts
  - bill paying
  - reports
  - loans
  - investments
  - lots of coupling btwn the above
- alternative architecture could be
  - assets
  - sources
  - suppliers
  - interfaces

#### Open-Closed Principle
- open to extension: system can be extended to meet new requirements
- closed to modification: the existing implementation and code should not be modified as a result of system expansion
- increases reusability
- technical approach is using abstraction via inheritance and polymorphism
- separation of implementation and interface
- keep attributes private
- minimize use of global variables

#### Liskov Subsitution Principle
- let q(x) be a provable property for objects x and type T. Then q(y) should be true for y objects of subset of type T
- in design by contracts, it leads to restrictions on interactions having to do with inheritance
- preconditions cannot be strengthened in subtype
- postconditions cannot be weakened
- invariants must be preserved in subtype

## Day 12 Jan 31, 2018

#### Dependency Inversion Principle

> High level modules should not depend upon low level modules.
> Both should depend upon abstractions.
> Abstractions should not depend upon details.
> Details should depend upon abstraction
- **rule**: design to an interface, not an implementation

> Packages that are maximally stable should be maximally abstract. 
> Instable packages should be concrete. 
> The abstraction of a package should be in proportion to its stability.
- kinda like the Hollywood principle - don't call us we'll call you
- can have partner apps
- concrete but has business rules that are likely to change

#### Interface Segregation Principle
- Clients should not be forced to depend upon interfaces that they do not use
- if there are 2 non-cohesive functionalities, keep them separate
- avoids design of fat interfaces and provides clear design to user
- break the functionalities into atomic interfaces that can be then individually accessed by the user

#### Law of Demeter
> Each unit should have only limited knowledge about other units: only units "closely" related to the current unit.
- style for building systems
- "only talk to immediate frens"

### Design Principles for Security

#### Principle of Least Privilege
> The principle of least privilege states that a subject should be given only those privileges that it needs in order to complete its task.
- if subject does not need access, it shouldn't have access

#### Fail-Safe Defaults Principles
> The principle of fail-safe defaults states that, unless a subject is given explict access to an object, it should be denied access to that object.
- when system fails we back up
- assumes tHt the default access to an object is none
- if the subject is unable to complete its action or task, it should undo those changes it made to thte security state of the system becore it terminates
- fault-tolerance: when we can't guarantee that system will behave in a safe way

#### Principle of Economy of Mechanism
> Security mechanisms should be as simple as possible
- if design and implementation are simple, there is fewer possibility for errors
- simple design => less assumptions, less risks, simpler testing

## Day 13 Feb 2, 2018

#### Principle of Complete Mediation
> requires that all accesses to objects be checked to ensure they are allowed.
- restricts the caching of information
- OS mediates these actions (determining if allowsed and providing resources)

#### Open Design
> The security of a mechanism should not depend on the secrecy of its design or implementation
- complexity does not add security

#### Separation of Privilege
> A system should not grant permission based on a single condition
- this is restrictive because it limits access
- equivalent to separation of duty principle

#### Least Common Mechanism
> The mechanisms used to access resources should not be shared.
- to prevent information being transmitted through channels
- also a restrictive one

#### Psychological Acceptability
> Security mechanisms should not make the resouce more difficult to access than if the security mechanisms were not present
- recognizes human element in security
- configuring and executing should be easy and intuitive
- interpret as: the security mechanism may add extra burden but that burden must be minimal and reasonable

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
- different ways to connect output data of module to input of other modules
  - batch sequential
  - pipes (stateless and serve as conduits for moving streams of data between multiple filters)
  - filters (stream modifiers, which process incoming data and send modified data stream out over pipe to another filter)
  - *pipes are special cases of filters
  - close loop process control is another typical data flow architecture

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
- connection links between batch sequential elements is conducted through temporary files
- common for business data processing 
- scripts are commonly used to make batch sequence

#### Applicable Design Domains
- data is batched
- each subsystem reads related input files and writes output files

#### Benefits
- simple divisions between subsystems
- each subsystem is standalone

#### Limitations
- requires external control
- low throughput
- no interactive interface

## Day 15 Feb 7, 2018

**skipped**

### Pipe and Filter Architecture
- decomposes system into components
  - data source
  - filters
  - pipes
  - data sink
- connections between components are data streams
- a **data stream** is a first-in first-out buffer type data structure
- a **filter** is an independent data stream that reads from input data stream, transforms and process it and then writes transformed data stream over pipe to next filter
- filter does not need to wait for batched data as a whole, it works incrementally
- filter does not know the identity of data
- a **pipe** is a stateless conduit that moves data stream from one filter to next
  - can carry binary or character stream
- an object type data must be serialized to be able to go over stream
- **serialization** is the process of saving an object into storage medium or transmit it across network connection link in binary form
- when resulting series of bytes are reread according to serialization, it can be used to make an architectural clone
- the process of serializing is calling **defalting** or **marshalling** an object
- **deserialization** - opposite operation/extraction of data structure from a series of bytes

![](img/pipeandfilter.PNG)

#### Data Flow Methods
1. Push only (Write only)
  - data source and filter may push data in a downstream
2. Pull only (Read only)
  - data sink and filter may pull data from upstream
3. Pull/Push (Read | Write)
  - a filter may pull data from an upstream and push transformed data in a downstream

#### Types of Filters
1. Active filter
  - pulls in data and pushes out transformed data
  - works with passive pipe which provides read/write mechanisms
2. Passive filter
  - lets connected pipe push data in and pull data out
  - works with active pipes that pull data out from a filter and push data into next filter

![](img/activefilter.PNG)

#### Applicable Design Domain
- whenever system can be broken into series of processing steps
- simple and stable data format
- suitable for producer/consumer model

#### Benefits
- concurrency
- reusability: encapsulation of filters make it easy to plug and play
- modifiability: low coupling between filters
- simplicity: clear division btwn filters
- flexibility: supports sequential and parallel execution

#### Limitations
- not for dynamic interactions
- low common denominator needed for ASCII data
- overhead of data transformation among filters
- error handling is sparse

### Process Control Architecture
- suitable for embedded system software design
- decomposes system into 2 subsystems
  1. executor processor unit for changing process control variables
  2. controller unit for calculating amount of changes

![](img/processcontrol.PNG)

- process control system must have
  - **controlled variable**
  - **input variable**
  - **manipulated variable**

#### Applicable Domains
- embedded software system involving continuing actions
- system that needs to maintain an output to remain stable
- system with target point

#### Benefits
- better solution to control system where no precise formula can be used to decide manipulated var
- software can be completely embedded

#### Limitations
- can be unstable and requires really careful math

## Day 16 Feb 9, 2018

#### Midterm Question
Compiler involves several elements that provide tranformation phase of source file to machine file.
- lexical analysis
- syntax analysis
- type checking
- intermediate code generation
- register allocation

Discuss conditions under which we cn use the styles of data flow architecture

#### Midterm Question 2
- propose batch sequential architecure for payroll system. system takes id, work time, rank and generate paycheck for each worker. 

```
<Type files>---> ??? ----> ??? ----> taxes and reduction ---> reduction files --->> generate paycheck
```

## Day 17 Feb 12, 2018

#### Data Flow Architecture Review
1. Pipe and Filter
  - discrete flow of data
2. Batch Sequential
  - flow in quantity
3. Control (gateways)
- the data is either contained and controlled by an entity or is given in a complete or partial view of considered world
- AI is used when there is no clear view of considered world

### Data Centered Software Architecture
- characterized by centralized data store belonging to entity that holds it
- data store: data transfer and its knowledge - explicit and reasoning (in our case data and knowledge is the same)
- data store is shared by all related components
- system is decomposed into
  1. data store
  2. independent software component agents
- connections between data modules and software components are implemented by
  - explicit method invocation
  - implicit method invocation based on repository catgeory
- in pure data centered software architecture
  - software components do not communicate with each other directly, they only communicate via data store
  - shared data module provides all mechanisms for software components to access it
    - insertion
    - deletion
    - update
    - retrieval
- 2 categories of data centered architecture
  - repository
    - data store is passive
    - clients of data store are active
    - client may access repo interactively or by batch transaction request
    - widely used in DBMS, library system

    ![](img/repo.PNG)

  - blackboard
    - widely used in real life
    - data store is active
    - clients are passive and are knowledge sources
    - will reach approximation, not definite
    - new data change may trigger evnts to its listeners
    - infrom clients through notify
    - can keep adding more clients
    - knowledge based systems like voice and image recognition, security systems

    ![](img/blackboard.PNG)

## Day 18 Feb 14/15, 2018

![](img/written.jpg)

- What is innovative about blackboard?
  - blackboard allows you to add more observers without modification
- used commonly for machine learning
- repo style examples
  - eg water - clients need water
  - ecommerce/Amazon - packaging is the interface
  - religion - ppl go to a priest

## Day 19 Feb 16, 2018

Software Archicture Design by Tao Ch 6

### Midterm 2017
- 9 questions 25/20 marks

1. Main characteristics that an event needs to satify to be event
s
#### Exercise 1
AI software system for speech that has minimal uncertainty?
- need to use different techniques to recognize voice

Which software architecture is suitable?
- Black board because you can have multiple experts that can be added to minimize uncertainty
- combination of partial results to reach approximation
- dont say batch sequential or pipes and filters

#### 2
S/w system to control robot given typica functions.
Challenges: obstacles blocking path, sensor input imperfectm may run out of power, restrict accuracy of movement (this adds uncertainty so we need blackboard)

## Day 20 Feb 28, 2018

- Master Slave - dependapbility and performance

### Hierarchy Structure
- a substystem or element is assigned a functionality
- method invocation 
- we need lower level modules because of design principles
- modules communicate with adjacent modules
- middle layers are usually for processing
- characterized by explicit method invocation (call-and-return) connection styles
- all architectural styles have this structure (except maybe Master-Slave)

#### Unix Architecture
- interface includes shell, utilities, app
- system call interface sends and receives signals from file system
- device drivers send signals to hardware control
- middle layer includes process control
- usually there are many scheduling and memory managment algorithms

### Main Subroutine Software Architecture
- traditional style
- purpose it to have maximum reuse of subroutines and make individual subroutine be developed independently
- we start from data flow diagram (acquired in Requirements stage)
- in OO, data is encapsulated in indiavidual object
- system decomposed into subroutines hierarchially according to system functionality
  - behaviour hiding
  - software hiding
  - machine hiding
- we start building from bottom-up

![](img/ms1.PNG)

![](img/ms2.PNG)

- not good design
  - not easy to maintain

#### Benefits
- easy to decompose system
- can be used in sub-system of OO design

#### Limitations
- globally shared data is vulnerable
- tight coupling can cause ripple effects

## Day 21 Mar 2, 2018

### Master Slave Architecture
- variant of main/subroutine architecture style
- supports fault tolerance and system liability
- slave provides replicated services to master
- master selects particular result among slaves

#### Midterm Solutions
 - distance of connectors - two elements related with a connector have a distance expressed as in the same thread/process/computer/or on different computers across a network
- observer pattern example - blackboard, MVC
- compiler architecture - data flow (using files) - batch sequential and data-centered (repository, diagsram from slides)
- main elements and characteristics of black board architecture
  - knowledge sources (problem solving modules sharing common global database called blackboard)
  - data store (holds knowledge)
- biometric system question - blackboard

## Day 22 Mar 5, 2018

#### Applicable Design Domains
- suitable for parallel computing and accuracy
  - open to addition, closed to modification
- when liability is critical
  - eg need many sensors (european, american)
- where performance is critical (to a limit)
- capacity issue solution: delegate requests to different workers that can handle the requests

### Layered Architecture
- system decomposed into higher and lower layers
- request to layer i+1 invokes services provided by layer i
- high cohesion

```
Joseph's diagram
```

![](img/layered_arch.PNG)

- what kind of class would be at the user interface?
  - boundary class
- for utility class, we can use blackboard architecture
- last layer, Layer 1, only has one link and can be a virtual machine

#### Applicable Design DOmain
- any system that can be divided between application specific protions and plaform specific
- apps with clean division between core services, critical services, user interface services
- apps that have a number of classes closely related to each other

#### Benefit
- incremental software development based on increasing levels of abstraction
- rnhanced independence of layers
- enhances reusability
- component-based technology is suitable technology to implment layered structure
- promotion of protability - each layer can be abstract machine deployed independently (because of design)

#### Limitations
- long path from request to service (many layers) so lower runtime performance
- performance concerns on overhead on data marshalling and buffering by each layer
- many apps cannot fit this architecture
  - they are usually networks
- expections and error handling are an issue
- related architectures
  - repo
  - cliend-server
  - virtual machine

## Day 23
