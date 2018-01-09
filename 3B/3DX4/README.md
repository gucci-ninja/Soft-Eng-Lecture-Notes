# 3DX4 Dynamic Systems and Control

## Table of Contents
- [Grading](#grading)
- [Textbook](#textbook)
- [Software](#software)
- [What is a Control System](#what-is-a-control-system)
- [Why Need?](#why-need)
- [System Configurations](#system-configurations)
- [Closed-Loop System](#closed-loop-system)
- [Transient and Steady-State Response](#transient-and-steady-state-response)
- [Stability](#stability)
- [Modelling in the Frequency Domain](#modelling-in-the-frequency-domain)
- [Written Examples](#written-examples)
- [MatLab Commands](#matlab-commands)
- [Partial Fractions Decomposition](#partial-fractions-decomposition)
- [Partial Fractions Decomposition](#partial-fractions-decomposition)

## Day 1 Jan 4, 2018

### Grading

- Assignments/Quizzes 10%
- Labs 10% (ITB 235)
- Midterm 30%
- Exam 50%

\*_8 or 9 quizzes, drop lowest 1 or 2_\*

### Textbook
- Control Systems Engineering - N. Nise (7th Edition)

### Software
- Matlab simulink
- Labview

[Link to Matlab and Labview](https://virtualdesktop.cas.mcmaster.ca/)

### What is a Control System
- simplest form - output provided for a given input
![](Day1/control_system.PNG)
- unity feedback - input 1 output 1

### Why Need?

- power amplification
- remote control
- convenience on input
- compensation for disturbances - i.e slope of ball, air, door opening
- improve system speed, accuracy, repeatability, performances

### System Configurations

#### Open-Loop System

![](Day1/open_loop_system.PNG)
- open loop control (cheap, not robust)
- no way of knowing if expected output is actual output

### Closed-Loop System

![](Day1/closed_loop_system.PNG)
- allows you to check output

### Transient and Steady-State Response

![](Day1/transient_steady_state_response.PNG)
_tansient = in transition_
- transient response tradeoff
	- if you get where you want really fast (high gain)
	- oscillates around point and doesn't settle
	![](Day1/high_gain.PNG)
	- low gain: doesn't overshoot
```	
overshoot = a/b * 100%
a = x-axis to highest point
b = x-axis to lowest point
```

### Stability

```
Total response = Natural response + Forced response
```

- Natural response (homogeneous) - evolution of system due to initial conditions
- Forced response (particular soln) - Evolution of system due to input
- bounded input doesn't create bounded output :dizzy_face:
- system has to be stable

## Day 2 Jan 5 2018

### Modelling in the Frequency Domain

- Laplace Transform
- do by hand and by matlab

#### Lab 1: Compensator Terminology

- 70% of problems can be solved with PID

##### Proportional Control System 

- calculating controlled output to make motor go proportionally faster
- open loop version: apply step voltage to motor
   - through feedback, you can put more energy into the system “cranking up the gain” enough so that it doesnt go unstable or start to oscillate
- makes things go faster

##### Integral Control System

- keep the motor moving in theory
- however, not always how it works in practicality therefore, a step voltage doesnt mean anything
- therefore you need to integrate over time so the voltage becomes big
- integral gain gets rid of steady state air  
- gets ready of steady state air

##### Derivative Control System
- prevents overshoot or get desired amount of overshoot
- later we will learn the theory to predict the control of systems
- in practice, requires a lot of tweeking and fine tuning 
- basically helps to reduce overshoot and improve performance of system

##### More on Lab 1 - underdamped response specifications

1. Rise time is the time for output to go from 10% (0.1Cfinal) to 90% (0.9Cfinal)
2. peak time - time required to reach first and largest peak
3. percent overshoot - %OS percentage that output overshoots final value

```
%OS = ((Cmax - Cfinal)/Cfinal)*100%
``` 
4. settling time - is it close enough to do whatever we have to do? (settles within plus or minus 2% of Cfinal

#### PID Controller

- transfer function of proportional integral derivative controller
```
Gc(s) = K1 + K2/s + K3s = (K3(s^2+(K1/K3)s+K2/K3)/s
```

- first term is proportional, second integral.. etc

#### Block Diagram Representation of System

#### Laplace Transform Review

- time domain vs laplace domain
- laplace is best used for stability analysis, controller design, block diagrams
   - polynomial A divided by polynomial B
   - converts diferential equations (time domain) to algebraic (s-domain)

_Definition_ 

![](Day2/laplace.PNG)

- ![](Day2/transform_variable.PNG) = Laplace transform variable
- no information for time less than zero so we multiply f(t) by u(t) 
- but its ok if you write L(1/s^2) = t

##### Common Laplace Transforms

![](Day2/laplace_transforms.PNG)

##### Important properties of laplace

- linearity
- differentiation: limit as t goes to zero
- frequency shifting: if you multiply by exponential e<sup>-at</sup> you replace F(s) by F(s+a)

##### Laplace Transform Theorems

![](Day2/transform_theorems.PNG)

- #11 could have poles on left side and maybe one at origin but if it doesnt it violates condition and is unstable

##### Transfer Function

- n<sup>th</sup> order LTI differential equation is of the form a<sub>n-1</sub>*d<sup>n-1</sup>c(t)/dt<sup>n-1</sup> + ... +
a<sub>0</sub>c(t)
- c(t) is output, r(t) is input
- Take Laplace, C(s)/R(s) = G(s)
- example with differential equation can turn into first order system
- inverse laplace transform
	- ![](Day2/inverse_laplace.PNG)
- partial fraction expansion 
   ```
		s^2 + 2s - 3		       			
	F(s) = ----------------
		s^5 + s^4 - s - 1	   	   

		= s^2 + 2s - 3
		  -----------------
		(s-1)(s+1)^2(s^2+1)

		= A      B       C        Ds + E
		----- + ----- + ----- +  -------
		s-1     s+1    (s+1)^2   s^2 + 1
	```
   - expect a bunch of dif terms
   - pole zero cancellayion, when both denom and numerator have same pole
   - so when you expand the term with s - 1 wont be there

## Day 3 Jan 9, 2018

### Written Examples
- **take pic of note**

### MatLab Commands
- define F = blah blah blah
- define syms s, t, etc
- ```ilaplace```

### Partial Fractions Decomposition
1. Divide if improper, degree of numerator is denominator
	- do long division
2. Factor denominator
3. Linear factors
	- if you have (s+a)<sup>m</sup>, include A/(s+a) ... A<sub>m</sub>/(s+a)<sup>m</sup>
4. Quadratic factors
5. Determine unknowns

