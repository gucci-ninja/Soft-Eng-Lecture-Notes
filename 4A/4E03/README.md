# 4E03 Performance Analysis of Computer Systems

## Day 1 - Sept 4, 2019
- weekly assignments (11 in total) 
- mark is based on best 5 assignments
- assignments will come out on mondays and TAs will do questions related to the assigment
- key points when talking about performance 
    - how long it takes to do something (response time -> computation time + waiting time)
    - reliability
    - energy consumption
- performance metrics
    - when talking about response time, some metrics we can use is the average, maximum but we can als say like 95% of the time your response time will be less than x
    - for reliability, we can use a percentage for uptime but that doesn't tell you if the system is down for long priods a a time or short
    - energy consumption measures ??
- other factors for performance
    - workloads - how do computer systems work under certain work loads
        - how often to requests arrive (arrival patterns/times)
    - failures
    - user behaviour 
        - eg google's page ranking algorithm uses user behaviour statistics

## Day 2 - Sept 6, 2019

### Crash Course in Probability
- suppose we have 3 servers A, B and C
- we check at random times which servers are working, which are failing
- sample space Ω = {(w,w,w), (w,w,f), (w,f,w)...} all possibilities

#### Events
- any subset of sample set Ω
- eg if server A fails then E1 = {(f,w,w), (f,w,f), (f,f,w), (f,f,f)}
- intersection E1 and E2 is at least 2 servers fail - {(f,w,f), (f,f,w), (w,f,f)}
- complement of E2 = at least 2 servers work 

#### Probabilities
- 0 <= P{E} <= 1
- 0 is the event never happens, 1 is that is always happens
- given a bunch of probabilities of each situation
    - P{(w,w,w)} = 0.85
    - P{(w,w,f)} = 0.05
- all the probabilities of each possible outcome will add up to one

#### Unions
- we use properties to compute probabilities more easily
- the probability of E union F (probability that both event E and F happen)

![](img/union.png)

- last term is because both E and F have been counted twice in the the first 2 terms

#### Conditional Probability
- conditional robabilty of event E given event F (F is something we know has happened)
- notation: P{E|F}
- denominator renormalizes over new sample space and numerator restricts to samples in E and new space

![](img/conditional_probability.png)

![](img/conditional_probability.jpg)

##### Conditional Probability - Example
- we want to compute probability that A is failed given that exactly one server is failed
- F = {(f,w,w), (w,f,w),(w,w,f)} = exacly one server is failed
- E = {(f,w,w),(f,f,w),(f,w,f),(f,f,f)} = A is failed
- apply conditional probability formula
    - P{E ⋂ F} = {(f,w,w)} = 0.03
    - P{F} = {(f,w,w),(w,f,w),(w,w,f)} = 0.03 + 0.06 + 0.05
- P{E|F} is 0.03/(0.03+0.06+0.05) = 0.2143
- this means A is a little less likely to fail than the others ._.

#### Independent Events
- events E and F are independent if 
- ![](img/independent_events.png)
- P{E} is not affected by whether F occurs or not
- if we plug this into the conditional probabitiy equation then we would get that P{E|F} = P{E}
- an example of independent events is rolling a die twice

##### Independent Event Example 1
- are the events that server A fails (E) and B fails (F) independent?
- we can get the probabiltiies of E happensing and F happening and see if the product of the two is equal to E intersect F
- in the case provided, P{E ⋂ F} = {(f,f,w),(f,f,f)} = 0.003 + 0.001 = 0.004
- we can use this value to see if the conditional probability formula yields the same result as P{E} on its own
- P{E} = all the possibilities where server A fails, which we add up to get 0.0370
- similarly, P{F} = 0.06 + 0.003 + 0.003 + 0.001 = 0.0670
- using conditional probability formula, P{E|F} = P{E ⋂ F}/P{F} = 0.004/0.067 which gives 0.0597
- since the probability is not the same as P{E} that means that event F affects the probability of event E occuring
- usually, if the servers share a common power supply then they are not independent

##### Independent Event Example 2
- with different data, we can conclude that knowing B fails does not affect whether A fails
- these values are from knowing the probability of A working (0.9), P{B} = 0.92 and P{C} = 0.95
- usng the above we can compute the probability of everything else (assuming they are independent)
    - so when we are computing P{w,w,w} it is just P{A}\*P{B}*P{C} = 0.7866

#### Bayes Law
- suppose we know P{F|E} but we want to know P{E|F}

![](img/bayes_law.png)

##### Bayes Law Example
- someone is tested for a rare disease. if you don't have it, the test will be negative 99% of the time and if you have it it'll be positive 99% of the time
- disease is found 1/10000 ppl          9
- what are the chances that someone testing positive actually has the disease?
- event A: one actually has disease
- event B: one tests positive
- P{A|B} = (P{A}P{B|A})/P{B}
- P{A} = 0.0001 and P{B|A} = 0.99
- to calculate we use the law of total probability
- P{B} = P{B|A}P{A} + P{B|A<sup>C</sup>}P{A<sup>C</sup>}
-      = (0.99)(0.0001) + (0.01)(0.9999)
- so P{A|B} = 0.0098
- so this test sucks if you don't have the disease

#### Random Variables
- denoted by capital letters, it is a real-valued function of the outcome of an experiment
- examples
    1. sum of rolls of 2 dice
    2. number of arrivals to a website by some time t
    3. time until ext arrival to website
    4. cpu requirement of an http request
- if we consider time to be continous then they would be continuous random variables 
- 1 and 2 are discrete, 3 and 4 continous 
- if we just define the possible outcomes of these random variables, it's a more natural method of representing information
- we want to represent the particular vaus they can take one (called distribution)

## Day 3 - Sept 9, 2019

#### Distributions
- cumulative distributighon function 
- any probability can be calculated given this function
- if there's only one variable, drop the subscript

![](img/cdf.png)
```
P{ 1 < X <= 4}
= F(4) - F(1)
```

##### Continuous Random Variables
- for quantities tha take on values on a continuum - eg time
- F(x) is continous
- integrals
- assocaied density function

#### Discrete Random Variables
- random variable x takes on the value i and sums it

#### Summary Statistics - Mean (Expected Value)
- sometimes called avergae but we wil use tha for another purpose
- if you were measureing respnse time from db server every 5 minutes, and take the numerical average
- the expected vaue (mean) may be the same as the average but doesn't have to be

### Higher Moments
- kth moment is raising the value to kth value
- k = 2 is the second moment
- statisicians work with higher moments, wewill only use 1st and s2nd moments

### Variance
- an important summary statistic
- measures how spread out hte distributoin is
- Var(X) = expected difference from random vairables from the mean squared
- squaring it makes it positive, and is actually easier to work with than absoute value
- Var(X) = sigma^2 = E[(X - E[X])^2]
- when we tlk about computing systems, knowing variance can help us get an idea ofhow the computer system performs
- if we're scheduling requests on a web server and the request are roughly the same sizes then variance is low and the requests can just be processed in order
- if we have different kind of requests with small files vs large files, the variance is high. we would have to worry about delaying the small files when there are large files

#### Example
Given the denisity of a a function (lifetime of a omponent in days)

1. Find probability that lifetime is between 9 and 90 days
    - do we need to answer in terms of k or independent of k?
    - can check integral 0 to 100 f(x) = 1
<work>

### Geometric Distribution
- how many times do i do the same experiment where q is the probability of success, i get the kth experiment to be a success.

```
px(k) = q(1-q)^(k-1), k = 1,2
```

- as probablity of sucess gets lower, you have to wait longer to see a success
- variane goes up as q goes down

### Poisson Distribution
- probabilty that random value takes on value of k :)((((()))))
- all the values hsould sum up to 1
- if you do the sumamtion of  to infinity, e^-lambae^-lmb = 1
- taylor series expansion
- E[X] = mean, Var(X) = variance, both are equal to lambda
- the satistician Poisson used this to model deaths by horse kicks in the Prussian army

#### Uniform Distribution
- what most people think of when we say somethig is compeltley random
- `f(x) = {1/(b-a) a<= x <= b and 0 otherwise}`
- random variable is equally lieky to take values anwhere between a and b
- this doesnt mean P{X = i} = P{X = j}, though it is trivially true
-

### Exponential Distribution
- the probability that it takes on negative vakue should be 0 
- if you plug in 0 for x, you get 1 - 1
- when x goes to infinity, the value should equal 1

#### Example
Jobs ariving to server have CPU time (total time needed to process begining to end). We looked at some data and foud the data exponenetially dsitributed with mean 140msec. CPU scheduing dsciple is quantum-oriented so that a job nt completeing within 100 msec will be routed back to tail of the queue of waiting jobs. Find probability that a job has to wait for a second quantim.
<ex 3.2>

## Day 4 - Sept 11, 2019

### Memoryless Property
- given X > Exp(λ) and X > b
- X has been running for at least 6 months
- we want to calculate probability that it runs 7 months (1 more month)
- what is the probBILITY that X> a + b
- = e<sup>-λa</sup>

#### Example
What is the probability that a job finishs in the second quantum given it does not finish in the first quantum

<ex 4.1>

### Discrete-Time Markov Chains
- how system evolves over time
- dependent random variables
- used for user web page navigation
    - google's page rank algorithm
- cache contents and performance
- speech recognition
- machine learning (reinforcement learning - working with discete-time markov chains)
- composers
- baseball (how runs are scored)

#### Intro Example
- 3 web pages A,B,C linked to each other
- A links to B,C
- B links to C
- C links to A and B
- 1/3 of time we go to B, 2/3 to C when you leave A
- B always to C
- C to A and C to B is 50/50
- want to know what proporitoin of visits are made to each of the pages
- it doesn't take into account how much time is psent on each page but rather discretly, the nth time point corresponds to nth page visited

#### Stochastic Process
- stochastic measn random
- process means evolving through time
- the probability at step n+1, the state is equal to j, given that you know every state it's been in the past
- that probability boils down to just knowing the most recent state
- this is the Markov property
- its a form of a memoryless property
- last property is stationarity - sats of process are independent of time
- chain refers to state space being discrete, states are chained together by transitions

#### Markovian Property 
- future is independent of past given the present
- makes analysis easy (1)
- reasonable assumption for practical situations (2)
- if you ever want to simulate this thing on a computer it means you only need to store present state (3)
- sqaure matrix
- can be infintely dimensional based on how mny states you have
- rows of P sum to one because the sum of the probabilities that you go somewhere has to be 1
- if it is less than 1 that means there is a state that is missing
- we are gonna allow self transitions so P<sub>ii</sub> > 0

#### BAck to webpage example

    P = [0   1/3  2/3,
         0   0    1,
         1/2 1/2  0]

#### Umbrella Problem
<diagram 4.2>

### Tutorial 1 - Sept 13, 2019


## Day? - Sept 13, 2019

#### Umbrella Problem contd
- 

### Limitiing Probabilities
- not obvous thwt limit always exists


#### Revisiting Umbrella Problem
- raining P = 0.4
- p^30 has a limiting probability
- prob that one gets wet =  0.4*0.23 = 0.092
- is there a better way to compute pi_i
- yee
- by stationary probabilities

### Stationary Probabilities
- more equations than unknowns
    - no solution or
    - if we know there is a solution then at least one of the equations may be redundant
    - but you can't just throw away an equation
- simplest possible solution is that all pis are 0, which is why we need the equation that pi_i summed up = 1

### Key Theorem
- these 2 ways of calculating the probabilities give u the same answer

#### Example 1
- toy model - if we look at the execution of a pgroam, we can track it using a DTMC
- 3 resources - cpu, storage A, storage B
- assume that wiht this programs execution it doesnt simulataneously use the resources
- you are given the probability transition matrix
- if u discretize time, high probability that we stay at one resource for P[0,0]
- what is the prob that given a program is using cpu, it uses disk A 2 units later
- wanna get P[0,1]
- note: (P[0,0])^2 is the prob that you stay at 0,0 for2 steps and P^2[0,0] is prob that you are at 0,0 after 2 steps


```
[pi_0 pi_1 Pi_3][0.8 0.1 0.1, 0.1 0.9 0,0.1 0 0.9] = [pi0 pi1 ]
we are gonna throw away one of those equations

first 2 colum eqns:

0.8pi_0 + 0.1pi_1 + 0.1pi_2 = pi0
```

## Day ?? - Sept 16, 2019

written notes

### Expect Number of JObs in System
- the priciple of randomness degrading how the system works is an important thing to take away
- 