# 4C03 Computer Networks and Security

## Day 1 - Jan 6, 2020
- biweekly labs
- mark breakdown
    - 36 % labs (6 each)
    - 24% midterms (12 each)
    - 40% final exam
- do assignments at home and demo during lab time
- textbook: [Computer Networking : A top down Approach](https://github.com/QSCTech/zju-icicles/blob/master/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C%E5%9F%BA%E7%A1%80/%E6%95%99%E6%9D%90/Computer%20Networking%20-%20A%20Top%20Down%20Approach%2C%207th%2C%20converted.pdf)

### What is the Internet
- billions of connected computing devices
    - hosts running network apps
- communication links
    - fiber
    - copper
    - radio
    - satellite
- packet switches
    - forward packets of data
    - routers
    - switches
- internet = network of networks
    - interconnected ISPs
- protocols for sending/receiving msgs
    - TCP
    - IP
    - HTTP
- internet standards
    - RPC
    - IETF
    - IEEE
    - more strict because physical constraints are resrictive

#### What is a protocol
- specific messages sent, specific actions taken when messages are received 

#### Network Structure
- client and server, client requests, server provides

#### Read at Home
- access networks
    - DSL cable network
    - shared vs dedicated access
    - DSL is thinner than coaxial
        - coaxial has more bandwidth
    - tv can be transmitted over DSL
- frequency division multiplexing
    - send signals with diff frequency through same wire and they wont's interfere as long as there is a considerable difference between the signal frequencies

## Day 2 - Jan 8, 2020

### Accessing Networks
- digital subscriber line (DSL)
- older cable network was a shared service whereas these days they're not shared (dedicated) services
- the term shared/dedidcated can be for the srvice or the channel

### Enterprise access networks
- additional switches on site for a huge number of ndoes
- need to split them into smaller groups to manswtage
- we can't have a single device connecting to the network
- have different transmission rates availble

### Wireless access networks
- in wireless access we have to frther banches
    - small cale wireless networ
        - home wifi/router since range is smaller
    - wide area wireless netowrk
        - smartphones belong here since the range is greater
- the data which is sent to transmit internet vs telephonic vs mobile has the same udnerlying technology
    - the way this information is converted depends
- example
    - how voice signals are transmitted (audio waves)
        - how does a sound wave get converted to electromagnetic wave
- signal processing
    - convert data into numbers, then send numbers over the network as numbers

### Host and Data
- host sends packets of data
- host machine takes application message, breaks it into chunks called packets, thre is an upper limit on the size but based on the task the size of packets differs
    - if you have more data it gets split to multiple packets
- transmition rate (sometimes bandwidth) is importnat here
    - the medium (wireless or wired) has a range of frequency it can travel
    - the wireless medium has no upper limit for max frequency
    - copper wire has a range
        - this is the bandwidth (min and max frequency that can be transmitted)
    - wireless transmission rates are usually in gigahertz
- transmission rate: range of frequencies you can transmit over a medium
- to increase the capcity of wired mediums you can make the wire thicccccer
- transmission rate is about producing the signal, the second part is sending the signal across the wire
- the second part is called propagation (when the signal is travelling towards its destination)
- packet transmission delay = L/R where L is the bits and R is the bits/second

### Physical Media
- in wireless the signals propagate in any direction
- when the frequency is higher, the waves can reflect from physical medium (maybe)
- guided
- unguided
- unidrectional
- duplex

### Network core
- mesh of interconnected routers
- special purpose devices (switch and router)
    - one common job they both do is packet switching
    - they recieve the packets and forward them using a certain algorithm
    - they take decision based on the content of the packet
    - if there are 10 packes being transmitted between A and B, they will all be considered independently
- in circuit swtiching the decision is based on ??
- the devices in the mesh have to decide which path to take
    - swtiching time is based on which path is taken
- circuit switching says the decision should be based on the end source
    - the path of packets is the same
        - dedicated resources
- packet swtiching says that the swtiching decision will be independent since they are all in chunks


### Packet Switching - store and forward
- when a packet is received, the device will collect the compelte package and then transmit it on the next hop
- a hop is a step
- another fundamental principle is that the devices in the middle perform a store and forward
- they also verify that the content is correct
- if you have N hops the end to end delay is NL/R

### Packet Switching - queuing and delay
- id arrival rate to link exceeds transmission rate of link for a period of time
    - packets will queueu and wait to be transmitted by link
    - packets can be dropped if memory buffer fill ups
- follows store and forward principle, if multiple packets arriving t a rate grater than transmission rate then packets are either queueued or dropped
- once memory buffer fills up the packet is ALWAYS dropped

### Two key network core functions
- routing
    - if the destination of packet is X then it should be transmitted on links 1, 2, 3 for example
- forwarding
    - move packet from routers input to appropriate output

### Alternativ core - circuit switching
- end to end resources allocated between source and destination
- in circuit switching there is no delay except the constraints provided by bandwidth


### Circuit Switching- fdm vs tdm
- in fdm there are 4 signals with 4 different frequencies
    - all hosts don't get a lot of bandwidth
- in tdm we split the time dedicated to transmiting data
    - for time slot 1 you transmit data for host A
    - if the size of the slot is too big then the users will feel a long delay so the trick is to make the time slots as small as possible
