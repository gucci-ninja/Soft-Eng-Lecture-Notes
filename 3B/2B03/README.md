# 2B03 Engineering Economics

## Table of Contents
- [Grading](#grading)
- [Decision Pyramid](#decision-pyramid)
- [Dealing with Abstractions](#dealing-with-abstractions)
- [Modelling Process](#modelling-process)
- [Design Criteria](#design-criteria)
- [What is Sustainability](#what-is-sustainability)
- [Case Study Interface Carpets](#case-study-interface-carpets)
- [Time Value](#time-value)
- [Interest](#interest)
- [Simple Interest vs Compund Interest](#simple-interest-vs-compund-interest)
- [Cash Flow DIagrams](#cash-flow-diagrams)
- [Nominal Interest Rate](#nominal-interest-rate)
- [Timing of Cash Flow and Modelling](#timing-of-cash-flow-and-modelling)
- [Compound Amount Factor](#compound-amount-factor)
- [Present Worth Factor](#present-worth-factor)
- [Textbook](#textbook)
- [Sinking Fund Factor](#sinking-fund-factor)
- [Uniform Series Compound Amount Factor](#uniform-series-compound-amount-factor)
- [ Effective Interest Rate](#-effective-interest-rate)
 
## Day 1 Jan 4, 2018

Professor email: church@mcmaster.ca

### Grading
- Midterm 30% (March 6 @ 7-9pm)
- Quizzes 20% 
	- (on [Avenue](http://avenue.mcmaster.ca/)) 
	- open Thursday, due Sunday - **1 attempt only**
- Exam 50%

_Final and midterm - 2 sided cribsheet & open textbook (can't print pdf)_
_will do problems in class_

\*_Sunday March 4th - 2hr tutorial before midterm_*

### Decision Pyramid

![](Day1/decision_pyramid.PNG)

### Dealing with Abstractions
- engineering econ models typically represent a project through estimates
of costs and benefits of project over time

### Modelling Process

![](Day1/modelling_process.PNG)

### Design Criteria
- function, cost, safety, sustainability

## Day 2 Jan 8, 2018

### What is Sustainability

- Linear Model
	- yields a lot of waste

	![](Day2/linear.PNG)

- Closed Loop Model
	- Nothing should be wasted

	![](Day2/closed.PNG)

#### Global Goals
- Waste nothing
- adapt to the place
- use free resources
- optimize not maximize
- create livable environemtnt

#### Metrics and Tools
- life cycle cost analysis
- life cycle assessment
- ecological footprint analysis

#### Stakeholders
- should take end-user into consideration
- eg juice box design - one time use, flimsy straws

#### Ethics
- engineers have responsibility towards
	- client
	- profession
	- society

#### Complexity

#### Triple Bottom Line
- need to think about social sustainbaility
	- socially sound, acessible to users
- environmental sustainability
	- conserve earth's resources and raw material
- economic sustainability
	- used to be the main focus

**Three Legged Stool**

![](Day2/stool.PNG)

### Case Study Interface Carpets
- cut down ecologcal footprint by 1/3
- claims to be world's first sustainable corporation
- over 5 billion pounds of carpet now in landfills
- went from selling carpets to leasing carpets (floor covering services)
- Benefits
	- carpet tiles used so only worn out parts replaced
	- increases net employment
	- eliminates disruption
	- less glue fumes
	- incentive of keeping it in good condition '**_drive it like a rental_**
- invented new type of floor-covering called Solenium that can be remanufactured
- all worn materials can be completely separated
- in 10 years they saved $262 mill
- won $20M contract from U of California
- went from trucking to rail
- cut shipping cost by 50%
- inspired Wal-Mart to deploy sustainable practices
- 72% reduction in waste water

## Engineering Economics

### Time Value
- would rather get a million dollars today vs 10 years
	- due to inflation
	- money has earning power over time (investments)
	- time allows money to earn interest

### Interest
- **_compensaion for giving up the use of money_**
- **_difference between amount of money lent vs paid_**


	```future worth = present worth + interest```

	```F = P + I```
	- I = Lump sum interest
	- i = interest rate

#### Lump-Sum Interest Rate
- 

**There is a legal interest rate, you can't go over 60%**
- or you get charged with usury

#### Nominal Interest Rate
- Interest rate - rate of interest charged for use of money, usually expressed as annual rate
- interest period - base unit over time whihc an interst rate is quoted, usually 1 year
- interest rate specified for one year is a **_nominal interest rate_**
- same as annual percent rate (APR)

#### Simple Interest
- rate that doesn't change
- rarely used in practice
- I<sub>S</sub> = PiN
- ``` F = P + PiN```

#### Compound Interest
- results in a lot more money

## Day 3 Jan 9, 2018

- Amortization Period
	- the duration over which a loan is calculated to be re-paid

### Simple Interest vs Compund Interest
- Simple Interest - method of computing interest where interest earned during interest period is **NOT** added to principal amount used to calculate interest in next period
- Compound - standard method of computing interest where interest accumulated in one interest period is added to principal amount used to calculate for next period
	- F = P(1 + i)<sup>N</sup> OR
	- P = F/(1 + i)<sup>N</sup>
	- I<sub>C</sub> = P(1 + i)<sup>N</sup> - P
	- F is future worth
	- P is principal 
	- i is interest rate/compunding period
	- N is number of compounding periods

#### Interest Rate Terms
- compounding period:time between points when interest is computed and added to initial amount
- Annual Percentage Rate (APR) - this is what you see in commercials
	- nominal interest rate on yearly basis
	- Cdn Tire is 25% per year

#### Sample Question
- if 5000 invested in savings account at nominal 4% compunded yearly, what is future worth in 3 years.
```
Question 1

P = $5000
i = 4%
N=3

F = P(1+i)^N 
  = (5000)(1 + 0.04)^3
```

```
Question 2

1626 to 2018
i = 6%
P = 24$
F = P(1 + i)^N
     = 1.88 B
```

#### Credit Card tool

### Cash Flow DIagrams
- represented by arrows and relevent periods
- upward arrow = positive flow
- down arrow = negative flow
- time 0 is considered **now**
- ![](Day3/cashflow.PNG)

- can construct table outlining all cashflow activites
	- won't get marks for it but it helps 

### Nominal Interest Rate
- conventional method of stating annual interest rate
- 18% compounded daily --> ```i = 18%/365```
- ``` i = r/# compounding periods per year ```
- N --> if nothing is stated, assume yearly **except** in car payments and mortgages - assume monthly

## Day 4 Jan 11, 2018

### Timing of Cash Flow and Modelling

- Discrete Model
	- models that assume all cash flows occur at ends of conventional periods
- Continuous Model
	- not that common
	- assumes that all cash flow occurs continuously - continuous compund period

- can have discrete _cashflow_ and discrete _compounding_
- discrete - continuous
- continuous - continous
- can't have continuous - discrete (continuous money and monthly period)

#### Equivalence
- condition that exists when value of cost is equivalent to another
1. Mathematical equivalence
	- million dollars today or million dollars in 10 years -- not equivalent in terms of value
	- million today or 1.5 mill in 10 years **may** be equivalent
	
2. Decisional equivalence
	- indifferent between P dollars now abd F dollars N periods from now
	- inferring implied interest rate from P, F and N

3. Market equivalence
	- decision makers can echange different cashflows in market at 0 cost
	- common when you're shopping around eg mortgages

- if market equivalence holds and decisional can be expressed in monetary terms, then we can assume that mathematical equivalnce can be used

#### Simplification of Cash Flow
- for when it gets too complex
- Convention: Sample Factor (compund amount factor)
	- ```(F/P, i, N)``` = (1+i)<sup>N</sup>
	- F = P(1+i)<sup>N</sup> = P(F/P, i, N)
	- P = F/(i+1)<sup>N</sup> = F(P/F,i,N)

##### Assumptions of Compunding Interest Factors
- if we have N periods, they have to be equally spaced
- payment at time 0 can be considered at end of period -1: _today_
```
@ 2 is end of 2nd month, beginning of 3rd month
          |
  --------------
  0   1   2   3	
  ```

#### Example
- present worth P of cashflow with arrows at 3 and 5
- P = sum of those future amounts 
= P<sub>0</sub> = F1/(1+im)^3 + F2/(1+im)^5
- in short form = F1(P/F, im, 3) + F2(p/F, im, 5)


## Day 5 Jan 15, 2018

### Compound Amount Factor

```(F/P, i, N)```

- gives future amount F that is equivalent to present amount P when i interest ate and number of periods is N
- comes from eqn F=P(1+i)<sup>N</sup>
- (F/P,i,N) = (1+i)<sup>N</sup>
- allows you to mve single arrow to the future

#### Example 1
- loan a friend $5000 and they promise to repay you with interest 4% per year and they'll pay you back in 3 years.
	- nominal interest rate - 4%
	- m = 1 
	- i = f/m = 4%
	- N = 3 years
	- P = 5000
- F = P(1 + i)<sup>N</sup> OR F = P(F/P, i, N)
- = 5000(1 + 0.04)<sup>3</sup> = $5624.50 - textbook has these factors with 4 significant digits

**First quiz will be up on avenue on thursday! Due Sunday**
	- everything up to the thursday lecture

#### Example 2
- same as before, i = 12% monthly, N = number of compunding periods
	- m = 12
	- i = f/m = 12%/12 = 1%
	- N = 24 (in months)
- F = P(1 + i)<sup>N</sup> OR F = P(F/P, i, N)
- = 5000(1 + 0.01)<sup>24</sup> = $6348.67

#### Example 3
- same as first, four years, $5000 deposited at the end of each year. Interet rate is 12% compounded monthly
	- multiple arrows for this one

```
       |    |    |    |
  ---------------------
  0   12   24   36   48

```

- move all arrows to the future (to 48 months)
- use equation F = P(1 + i)<sup>N</sup> 4 times
- 5000(F/P, 0.01, 36) + 5000(F/P, 0.01, 24) + 5000(F/P, 0.01, 12) + 5000

### Present Worth Factor

```(P/F, i, N)``` = 1/(1+i)<sup>N</sup>

- gives present amount from F
- bringing arrow from future back _N compounding periods_

#### Example 4
- what amount is desposited today into account bearing 12% nominal interest will give 5000 at the end of 2 years. Interest compunded monthly
	- i = f/m = 12%/12 = 1%
	- P = F(i/(1+i)<sup>N</sup>)
	- P= F(P/F, 1%, 24)

#### Example 5
- how much would you deposit into savings account at nominal interest rate 6% **yearly** to accumulate $5000 in 3 years
- P = F(P/F, 6%, 3)

### Textbook
- find it online and put the formulas in your crib sheet
- Appendix A - discrete discrete
- Appendix B and C - continuous - continous, discrete - continuous 

#### Examplw 6
- using interest tables, 12% nominal interest with monthly compunding (1%), N = 24 months, how much do i deposite today therefore you now F not P
- look for 1% and N = 24 = 0.7875 (tbh it's easier to calculate :grimacing:)

## Day 6 Jan 16, 2018

### Sinking Fund Factor

```(A/F, i, n)``` = i/[1+i)<sup>N</sup> - 1]

#### Annuity
- a series of equal cash flows that start at the end of the first period, continue over N reglarly spaced time intervals
	- paycheck (in), cellphone bill (out)
- gives size of annuity that is equivalent to a future amount F
- N is the number of annuities

#### Example
- if N = 12, there should be 12 annuities on cash flow diagram
- Melissa is saving up for server in 3 years. She thinks she neds $5000 and intends to put aside an amount at the end of each year (an annuity). If nominal interest rate is 6%, how much should she put aside each year?
- r = rate = 6%
- i = f/m = 6%
- cashflow diagram would have 3 annuities, totalling on the third one
- **note**: last annuity has to be on same space as total
```
A = F(A/F, i, N)
  = 5000(A/F, 6, 3)
```

- however, if her first deposit is today, N=4

### Uniform Series Compound Amount Factor

```(F/A, i, n)```

```F = A(1 + i)```<sup>```N-j```</sup>

- if you have a quetion like what is F at 20 given 10 annual payments of $1000 at an interest rate of 5%. 
- F20 = 1000(F/A, 5%, 10) **wont** tell you what you have after 20 years, it's only after 10 years
- To get 20 years, use F given P equation. multiply the above by (F/P, 5%, 10) or if after 15 years, (F/P, 5%, 5)
- **DON'T WRITE** F20 = 1000(F/A, 5%, 20) because it means you have 20 $1000 payments

#### For Single Transactions
- Compound Amount Factor (F/P, i, N)

#### Example
- Bob wants new truck in 3 years. If he saves $25000 each year and puts it in savings w/ annual rat 4% how much will he have in 3 years
- N = 3, F = ?
- 25000(1 + 0.04)<sup>3-1</sup> + 25000(1 + 0.04)<sup>3-2</sup> + 25000(1 + 0.04)<sup>3-3</sup>
 = 27040 + 26000 + 25000 = 78040

 ### Effective Interest Rate

 - actual annual interest rate obtained when the compunding period is less thaan 1 year is called the _effective interest rate/year_
 - denoted by i<sub>e</sub> (or subscript annual, quarterly, weekly)
 - if cashflow period is less than compounding period the cashflows will be _collapsed_ to the compounding period
 - no effective interest rates in first quiz
	- will be about first lecture, calculations on moving arrows on cashflow diagram, F given A, A given F application

## Day 7 Jan 18, 2018

### Nominal vs Effective Interest
- nominal - stated rate of interest
- effecive interest rate
	- i<sub>e</sub> = effectve i/year
	- r = nominal i/year
	- m = # of compounding periods in 1 year
	- r/m = nominal i/compunding period

Equating future worth after 1 year

```F = P(1 + i```<sub>```e```</sub>```) = P(1 + r/m)```<sup>```m```</sup>

```i```<sub>```e```</sub> ```= (1 + r/m)```<sup>```m```</sup> ``` - 1```

### Efective Interest Examples

#### Example 1 Slide 49
- r = 6%
- m = 365
- i<sub>e</sub> = = (1 + r/m)<sup>m</sup> - 1 = **6.18%**

**\*if i<sub>e</sub> only compounded once a year then it's equivalent to r*\**

**\*if compoounded daily for ex. 6% it becomes 6.18%*\**

#### Example 2 Slide 53
- single arrow on cashflow diagram
- (F/P, i N) = (1 + i)<sup>N</sup>
- F = 5000(1 + 12%/12)<sup>24</sup> = i<sub>e</sub> = (1 + 12%/12) - 1
- F = 5000(1 + i<sub>e</sub>)<sup>2</sup> = 6348.67

### Effective Interest Rate and Cash Flow Period
- (F/A, i, N)

