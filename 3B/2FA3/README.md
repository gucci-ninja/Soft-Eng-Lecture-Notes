## 1BA3 Enterprise Finances

### Evaluating NPV Estimates
- these are just estimates so don't take these too seriously
- Variables:
    - **Forcasting Risk** - how sensitive is the NPV to change in the cash flow estimates. more sensitive = more risk
    - **Sources of Value** - why does this project create value?

#### Scenario Analysis
- What happens to NPV under different cash flows scenarios
- There are at least 3 scenario to remember for each project:
    - **Best Case** - revenues high and costs low
    - **Base Case** - neutral revenues and costs
    - **Worst Case** - revenues low and costs high
    - The range of possible outcomes

Example Scenario Analysis
Scenario | Net Income | Cash Flow | NPV | IRR
---------|------------|-----------|-----|----
Base Case | 19 800 | 59 800 | 15 567 | 15.1%
Worst Case | -15 510 | 24 490 | -111 719 | -14.4%
Best Case | 59 730 | 99 730 | 159 504 | 40.9%

#### Sensitivity Analysis
- How much change happens to NPV when changing a certain variable
- The more volatiliy the NPV in relation to a specific variable shows:
    - Higher forcasting risk associated with that variable
    - More attention should be paid to that variable when making estimates.

Scenario | Unit Sales | Cash Flow | NPV | IRR
---------|------------|-----------|-----|----
Base case | 6000 | 59 800 | 15 567 | 15.1%
Worst case | 5500 | 53 200 | -8 226 | 10.3%
Best case | 6500 | 66 400 | 39 357 | 19.7%

#### Simulation Analysis
- Expanded version of sensitivity analysis and scenario analysis
- Infinite calculations are done to find a set of outcomes and the probability of each set of choices
- Monte Carlo simulation is a class of algorithms that use random sampling in order to obtain numerical results.
- Very dependent on the inputs given

#### Making Decisions
- If positive NPV for majority of scenarios, one can continue with project
- If a variable is very sensitive to making NPV negative, consider dropping project

### Break Even Analysis
- tool to analyze relationship between sales volume and profitability
- 3 types of Break Even:
    - **Accounting Break Even** - sales volume where net income = 0
    - **Cash Break Even** - sales volume where operating cash flow = 0
    - **Financial Break Even** - sales volume where net present value = 0
#### Costs
- 2 important types of costs when talking about break even:
    - fixed costs (FC) = constant, regardless of output, over a time period
    - total variable cost (VC) = cost per unit * quantity = `v*Q`
        - employee salary, if hourly, is not a variable cost as it does not directly affect the quantity sold.
    - total cost (TC) = `FC + VC` = `FC + v*Q`

Other Costs include:
- Average Cost = `TC / Q`
    - lowers as Q increases
- Marginal Cost = `v`
    - cost to produce one more unit

#### Accounting Break Even
Var | Meaning
----|--------
NI | Net Income
S | Sales
VC | Total Variable Costs
FC | Fixed Costs
D | Depreciation
T | Tax percentage
Q | Sale Volume
P | Price of one unit
v | cost of one unit

```
NI = 0 = (S - VC - FC - D) * (1 - T)
QP - vQ - FC - D = 0
Q * (P - v) = FC + D
Q = (FC + D)/(P - v)
```
- Q is the sale volume to reach 0 net income
- Cash Flow = Depreciation
- NPV < 0
- Accounting Break Even is used as early screening
- if project cannot break even, it is probably not worthwhile
- tells managers how profitable a project may be

#### Cash
```
OCF = 0 = (S - VC - FC - D) + D
Q = FC/(P-v)
```

#### Financial
Var | Meaning
----|--------
PV | Initial Investment
RR | Rate of return

1000000