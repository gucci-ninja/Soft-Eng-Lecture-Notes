# 4AA4 Real Time Systems

## Day 1 - Sept 3, 2019

### Prof Details
- Wenbo He
- Office: ITB124,12:30-1:30 on Tuesdays and Thursdays
- email: hew11@mcmaster.ca

### Grading
- midterm 1 -15% - sept 26
- midterm 2 - 15 - oct 24
- midterm 3 - 15 nov 21
- labs - 20% - 
- final - 35%
- bonus marks for quizzes + participation

### General Systems
- set of interacting or independent component parts forming a complex whole
- takes input followed by black box and gives output
- there's a delay for the reponse and this is an important characteristic of the given system
- there are first order and second order systems, which charaterize how the step response would look wtr time

### Computing Systems
- besides the performance (aaccuracy, functionality, robustness, usability) the response speed (delay) is also important
- computing systems can be defined as systems where the response time or speed matters

### Formal Definition
- as a computer system in which the correctness of the system behaviour depends not only on logical results but also the physical instant at which these results are produced


### Real Time Systems
- response time
- time interval between a stimulus (inupt) and corrsponcing respone (output)

- a real time system is where a timely response to external stimuli is vital
- does not meean faster is better but that it must satisfy explivit response time contrainct otheriwse failure may occur :( 

### Different Kinds of Real Time Systems
1. Soft RTS 
    - where performance is degraded but not destroyed by failure to meet response time constraints
    - for example network sytems/ network applications
    - TCP/IP protocols - the time constaints of packet being delivered to reciever, if it is not deliered on time then the receiver has to request for packet again from sender
    - it's tolerable
    - more examples
        - streaming videos
        - computer games
        - online chatting

![](img/soft_rts.png)

2. firm RTS
    - missing a few deadlines will not lead to total failure but missing more than a few may lead to complete catasrophic system failure
    - more examples
        - manufacturing systems with robot assembly lines
        - coursework submission

![](img/firm_rts.png)

3. Hard RTS
    - missing even a dingle deadline will caus a complete catastrophic system failure
    - more examples
        - mission critical systems
        - nuclear systems
        - mdeical applications such as pacemakers

![](img/hard_rts.png)

### Comments about RTS
- mutitasks
    - periodic tasks
    - aperiodic tasks
- schedulability
    - the ability of tasks to meet all deadlines
- performance
    - what happens if the system cannot schedule, if the system cannot meet the tasks to meet deadlines what should be done


### Questions
1. what should we do if not all deadlines are met
2. does a real time system mean a "fast system"?


### Quiz 1
- what are the major differences between a thread an a process
- given an open loop transer G(s), what is the closed loop transfer function (with unit feedback)
- what do you expect to leanr in this course

## Day 2 - Sept 5, 2019

### Quick Review T/F
1. A good scheduling algorithm for hard realt time tasks must try to complete each task in the shortest time possible. False
2. Soft real time systems are those which do not have any time constraint associated with them. False

### Opertin System
- what is an operating system and what it do
    - knows whih task is using which computer resources
    - based on the needs it does resource allocation

### Kernel and Kernel SPace
- service provided by kernel
    - process management
    - memory management
    - file system
    - scheduling
    - interrupt handling
    - inter-proces communcaition and netowking
- kerne provides process and memory management s well as scheduling
- interprocess communciation
- there's kernel space and user space
- kernel space is space in ememory where kernel processes run
- user speace is space in memory where user proesses run

```
vm --- RAM
    |
    disks?
```

### User and Kernel (supervisor) mode
- in kernel mode, all the instructions can be accessed including OS routings and unlimited hardware
- in user mode the access to instructions is limited
- in user mode you can't access hrdwre
- so if you want to access hardware in user mode ou can use the system call

### How OS delivers he servies to user process
 -system call is similar to the function of your user program
 - then there's an elabroate procedure for each syem call
 - you can ass a parameter to the kernel
 - the parameter or the value of the paramter will be saved in a register
 - then the TRAP instructions are called
 - the TRAP instructons 
 - the space for user function call is differnt
 - you calla function f(x), where x is a paramter
 - in the function you can specify a set of instructions

 ```
f(x) {
    instructions...
}
 ```
 - in a user program you call f(x), the parameter is defined by the user
- the parameter passed as a reference (x will be saved somehwere in memory)
- after the functoin is executed, a return is called
- that is the procedure of program call in user program
- system call is kinda similar in that the param is stored in a regsiter
- the register has a status of whether system call wa compelte successfully
- the control is passd to user process when system instruction is executed
- then its passed to kernel then back to user (return)

### System Call and Argument Passing
- if the user program needs to make a system call
- after execution of system call the control is passed to kernel

### Process Scheduling
- OS must decide which process to run first and in what order to run remaining processes should run
- what are the objectives of good scheduling algorithm (for non-real-time system)
    - fairness - make sure each process gets fair share of CPU
    - efficiency - keepthe CPU busy to serve as much workload as possible
    - response time - minimize waiting ime of users to obtain results
    - throughut - maximize the number of tasks processed per hour

### Real-Time Operating Systems (RTOS)
- objective is to make tasks to meet deadlines
- RTOS designed for real-time tasks where logical resultd + time to complelte them matters
- hard or soft RTS depends n how to define cost of missing deadlines
- examples of RTOS
    - QNX
    - VxWorks
    - RTLinux
    - LynxOS
    - Windows CE
    - RTAI
- what makes OS real time?
    - guarantee that deadlines are met, if not met there is some control mechanism. the tasks get rejected if there is no garantee to meet deadlines
    - predictability, most hard real time tasks/apps are periodic so you can tell frequency of task arrival
        - need to know what tthe maximum requests from certain tasks are so you can predict if deadlines will be met
    - not necessarily fast and may be mediocre throughputs

### OS vs RTOS
- design philosophy: general OS based on time-sharing to provide fiarness and RTOSis event driven
- general OS - fast response and high thrughput, RTOS: schedulability ad ensure that wrost-case response time still meets deadlines
- overload: OS is fair and RTOS meets critial deadlines

#### Is Linux a RTOS
- no
- because kernel of linux may have exclusive access to some data 
- so if there is a RT task, it must wait for kernel to compelte task to access data
- linux provides limited ernel mode pre-emption
- so when there is a RT task, it will have to wait for completion of system calls
- sometimes, linux systems make high priority calls to wait for copletion of low prority tasks, in which case he low priority task may take up resources
- rt guarantee can not be achieved in that case ^
- in linux high priotity pre-empt low prioruty so efficiency can be satisfies
- in order to achieve efficiency of deviec usage, linux re0rders requests from multple oprocesses and btach operations to use hardware efficiently

###
- how to impetment RTOS on top of Linux
- we can add a new layer that will take oeer the contol of the processor
- eg RTAI abd RTLinux
- another iway is to impement necessary change to re-impement components
    - eg Reempt RT
    - it impleents RT tasks as kernel modules
    - that's why module programming is gonna be part of the course
    - Preeempt RT is the OS we will be using in the course, (myRIO Textas Instruments)

### Kernel Module
- can use them without rebooting system
- can install all baic functionalities at first and can always rewrite/insert to kernel module
- they are essentially pieces of code that can be loaded/unloaded into kernel on demand
- this ensures memory is saved not wasted
- jsut need to write certain functionaliy and install specific module

### Development Fundamentals
- related commands
    - insmod: insert module
    - rmmod: remove module
    - lsmod: list modules
    - modinfo: module information
- a real time tas running as a kernel module has 3 sections
1. initializiation - function init_module() to initilizae module
    - invoked by insmod
    - tell the kernel what kid of resources need to be set up 
2. task specific code - instructions of module 
3. function cleanup_module() to clean up resources to so pmodules from executing and delete the task

#### Simple example

```
#include <linux/module.h>
#include <linux/kernel.h>

int init_module(void) {
    printk(KERN_INFO "Hello World\n");
    return 0;
}

void cleanup_module(void){
    printk(KERN_INFO "gg\n");
}
```

### Compiling modle
- after you have it programmed u can compile module by writing makefile

#### simple makefile

```
obj-m +=hello.o

all:
  make -C /lib/modules/$shell uname -r)/build M=$(PWD) modules

clean:
  make -C 

```

### module_init and module_cleanup
- if you don't want to use default methods you can use ??
- can use __init to specify entrance and __exit for exit before the method name
- you have to include <linux/init.h> to require macros

### Passing Commandline Arguemnts
- cant use argv and argc for modules
- first you have to decalre variables that will store values
- then use module_param(name, type, permissions) to set up parameters
- then in run time use insmod to accept/fill up the variables with values

```
static int my_int = 5; (initliaze defaults)

module_param(My_int, int, S_IRUSR | S_IWUSR | S_IRGRP | S_IROTH)
```


