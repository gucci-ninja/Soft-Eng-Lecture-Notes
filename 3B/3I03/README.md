# 3I03 Communication Skills

## Table of Contents
- [Marking Scheme](#marking-scheme)
- [Elevator Pitch (sell yourself)](#elevator-pitch-sell-yourself)
- [Elevator Pitch (business)](#elevator-pitch-business)
- [Resumes and Interviews](#resumes-and-interviews)
- [Group and Cluster Hiring](#group-and-cluster-hiring)
- [What About the Interview?](#what-about-the-interview)
- [How to Become a More Perfect Candidate](#how-to-become-a-more-perfect-candidate)
- [Technical Questions](#technical-questions)
- [How to Approach Problems ](#how-to-approach-problems-)
- [Machine Learning](#machine-learning)
- [Assignment 2](#assignment-2)
- [The Writing Process](#the-writing-process)
- [Assignment 2](#assignment-2)

## Day 1 Jan 4, 2018

Prof email - fchian@mcmaster.ca

> Will try to incorporate machine learning

### Marking Scheme

* Individual
	* Written ------------- 40%
	* Presentation -------- 15%
* Group
	* Final tech report --- 25%
	* Final presentation -- 20%

> Can pick group members from other tutorials but coordinator
> gets to pick which tutorial for presentation

\*_20% penalty per day late_

\*_must cite all sources!!!_
 
### Elevator Pitch (sell yourself)
:no_mouth:
- 30-90 sec speech that summarizes important points about you
- give enough info such that they want to know more
- what do you want them to know about you
- different pitches are for different purposes/points in your career
	- who are you?
	- what do you do?
	- where are you going?
	- **supplement with your unique special skills**
- consider employer perspective
	- what's in it for them?
	- how will it contribute to the organization
	- do they want to meet you again
	
- effective
	- concise, clear, compelling
	- credible, conceptual, concrete
	- customized, conversational
	
### Elevator Pitch (business)

- what is the market?
- why you?
- what do you offer?
- ask for follow-up

## Day 2 Jan 11, 2018

### Resumes and Interviews
- employers look for (in STEM fields)
	1. communication
	2. creativity
	3. adaptability
	4. teamwork
	5. leadership
- key skills, highlight them as you read job description

**T exercise**

What Employer Wants | What you have that matches
--------------------|-------------------------
Java | Java, Python

#### Resumes
- highlight accomplishments and achievements catered to job
- reasonable resume length - 1 preferred, no more than 2 pages
- for students: education, then skills, then experience
- reverse chronological order
- use action words to strengthen experiences (I _achieved..._) and other verbs
- convey that if you're hired, you'll be active and get things done
- tailor cover letter and resume to job
- don't use _I_ in resume

**How to describe your experiences**
- **S**ituation. Describe what you were faced with
- **T**ask. Provide Context
- **A**ction. WHat did YOU specifically do
- **R**esult. Quanify

#### Incorporating Action Words
- use **past tense** for past experiences
- **present tense** for current
- **active voice** whenever possible (put yourself in focus, not activity)

#### Cover Letters
- 3-4 paragraph, 1-page business letter introducing you and your resume
- express interest in position and inquiry to whether a specific position is available
- make your writing targeted, persuasive, clear/consise, and accurate

#### Leveragin your Contacts
- mention name of contact if possible, they might endorse you
- get permission from contact
- it helps a loooOOoOoT :scream:

### Group and Cluster Hiring
- recent trend to hire small teams
- benefits: team collegiality, proven track record
- popular in blockchain area

#### Social Media and Internet
- consider online presence
- list your courses on LinkedIn
- what will recruiters see when they creep you :no_mouth:

### What About the Interview?
- better to overdress than under
- enter with confidence, shake hands and make eye contact
- expand on skills mentioned in resume/cover letter
- talk about trasnferrable skills

#### Types of interviews
- screening - email, phone
- behavioural
	- idea that yor past is an indicator of future
	- prepare 5-7 experiences
	- Questions
		- tell me about a time ou did not achieve a goal
		- example of when you were creative
- technical
- group
- case
- coding

#### Different Mediums
- in person
- skype
- lunch/dinner

## Day 3 Jan 18, 2018

- dress code for interviews - dress decently :grimacing:

### How to Become a More Perfect Candidate
- coursera, bootcamps, read lots, write lots
- hackathons, diversity lanuages, independent projects
- resumes 1-2 pages, 1-2 points bullet-form

### Technical Questions
- Knowledge Questions
	- what is a static class
	- descreibe graph traversal algorithm
	- what is your favourite algorithm
- Design/Scalability 
	- design database system for distributed system that operates in parallel
	- scope the problem/ask questions
	- figure out biggest components (which area has higher load)
	- discuss tradeoffs, challenges, bottlenecks
	 
### How to Approach Problems 
1. Listen
2. Come up with an example - largle cases and general purpose
	- eg intersection of 2 sorted distinct arrays
	- look at special cases
3. brute force if you have to
4. optimize your solution by walking through brute force solution and pointing out drawbacks and areas of imporovement
	- BUD: bottlenecks, unecessaary work, duplicated areas
	- has tables
	- precomputation/caching
	- space/time tradeoff
	- other data structures: heaps, trees, stacks, queues
5. Walk through your solution before coding
	- don't rush into coding
6. Good Coding Style
	- modular code
	- think about edge cases
	- clean and neat, proper variables
7. Testing
	- make sure your code makes sense
	- test your edge cases

## Day 4 Jan 25, 2018

### Machine Learning
- learning models from specific examples or experience
- statistics - inference from a sample
- efficient algorithms to do things better

#### Why Now?
- machine learning has been gaining popularity since 2010
-  due to large amount of data
- higher computation power
- demand from industry
	- the goverment of canada have invested over a hunderd million over the next 5 years to create AI strategy that will help students
	- to develop techniques and train students to apply machine learning
- advancements in algorithms and theory
	- deep learning
	- predicting what something is using good algorithm
- demands for self-cutomization to user or environment
	- very useful since it targets people specifically

#### Growth of ML
- speech recognition, natural language processing
	- devices like Google Home, Amazon Echo do this
- computer vision
- medical outcomes anlysis
	- radiology - you take images and the software tries to identify abnoramlities
- robotics
- computational biology
	- looking at DNA, the genome project?
- customer relations

#### Goal of Machine Learning
- making predictions or decisions from data
- three borad areas
	1. data mining - using data to generate new knowledge
	2. software applications - autonomous driving, speech recognition, image recognition
	3. self-learning algorithms - applications that learn your preferences

#### ML Examples
- 9714 patient data describing pregnancy and birth
- each patient record has 215 features (age, first pregance, elective/emergency C-section)
- given this data we can predict the future patients that have a high risk for a C-section
- if no previous delivery and abnormal 2nd trimester ultrasound and abnormality at admission then the likelihood of C-sectio is 60%
- self-driving cars

#### ML Framework
- apply prediction function to a feature representation of the image to get desired output
- define images as what they are with _labels_
- y = f(x) where y is the output, f is the prediction function and x is the image feature
1. **Training** data which is a set of labelled examples (x, y) which will estimate the prediction function f by minimizing the prediction error on the set
2. **Testing** by applying f to a never before seen test example x

#### Features for Training
- raw pixels
- histograms of what you've seen how many times
- descriptors - boundaries

#### Models for training
1. Classifiers: Linear
	- used for autonomous vehicles
	- finding linear function to separate classes/data
	- used for spam emails by classifying certain words under spam or not spam. 
	- some examples: SVM, Neural networks, naive bays, bayesian netowrk, logistic regression, randomized forests, boosted decision trees, K-neares neighbour
	- **Recognition task and supervision** - images in training set must be annotated with the correct model
		- for motorbike can also annotate important components such as the two wheels
	- **Spectrum of supervision** - how much annotation there is per image (unsupervised, weakly supervised, fully supervised)
		- it's very hard to do full supervised
	- **Generalization** - develop a model that can work on many different kinds of test data
		- components of generalization error
			- bias: how much the average model over all training sets differ from true model
			- variance: how much the model estimates from different training sets that are different from each other (is the model sensitive)
		- we can have 2 outcomes: 
			1. **underfitting** model that is too simple to represent all the class and has high bias, low variane, high training error and high test error
			2. **overfitting** model is too complex and fits irrelevant characteristics (noise) in the data and has low bias, high variance and low training error, high test error

## Day 5 Feb 1, 2018

### Assignment 2
- Identify real world problem and come up with technical solution
- Then write a proposal for it
- Present idea to tutorial in form of investor pitch

### The Writing Process
- Writing should be a part of the project process
- Its really hard to “do the work” and then “write it up”
- b/c work is never done – its constantly changing
- write something everyday – write casually, fix it later
- create an outline with bullet points of what you want to put in each section
	- helps with flow

#### Components of a Proposal
1.	title
	- introduce and identify proposal
	- should be short, easy to remember, capture main idea of proposal
	- if proposal is accepted, title will usually become name of project
2.	background
	- includes background needed to understand and appreciate proposal
	- includes
		- description of problem that needs to be solved
		- technical background info
		- past experiences
	- be succinct
3.	objective
	- state what you want to accomplish
	- can be formulated as a collection of goals
		- minor and major goals
		- short term and long term goals
4.	approach
	- how you intend to accomplish the objective
	- presents the ideas that will make the project/idea successful
		- plan of attack
		- methods/tech that will be employed
		- people, money etc that you need
		- products/services that will be provided
		- timeline for completion
		- criteria for knowing when job is done
		- any maintenance plans for keeping the project ongoing
	- section where details are presented and provides main substance of proposal
5.	impact
	- expected results of implementing the proposal
	- both positive and negative results can be discussed should be net positive tho
	- clearly set expectations of what you intend to deliver (+ / -)
	- delineate benefits of proposal
		- products/services
		- short/long term
		- inside your group/ organization and outside
6.	cost
	- expected cost of implementing the proposal ideas
		- often presented as a budget
	- cost includes all resources that will be needed to implement the proposal
		- monetary resources
		- physical resources
		- person/time/ energy
		- goodwill – IP, trademarks, brands, customers
		- political capital – influence/goodwill of public or political person

#### Writing Style
**Goals of Scientific Writing**
- clear
- unambiguous
- correct
- interesting
- direct

## Day 6 Feb 8, 2018

## Day 7 Feb 15, 2018

### Assignment 2
- new and innovative
- max 6 pages
- written proposal due Feb 27, 10pm
- content: problem, slution, market, business, influence, ask (for money/time?)

#### Guest Speaker

## Day 8 Mar 1, 2018

**skipped** but details on final presentatino announced - need to join a group.