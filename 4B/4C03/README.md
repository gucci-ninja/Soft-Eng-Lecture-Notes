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

## Day 3 - Jan 9, 2020

### Packet Switching vs Circuit Switching
- packet is for internet
- circuit is more for telephonic
- packet switching prod
    - good for bursty data because you can change up your path

### Internet Strcuture
- bigger companies like GOogle have their own dedicated connections to the backbone

### Four sources of packet delay
1. processing delay
    - if the contents of the packet were succesffuly received
2. queueing delay   
    - depends on hw much work the node has to do
    - error checking
    - traffic
    - similar to processing delay
    - if there the buffer gets filled the packet gets dropped
3. transmission delay
    - L/R
4. propagation delay
    - depends on lenght of link (wire length)
- the network of routers and switches is designed so that there is as less overhead and delay as possible
- basic principle
    - routers and switches keep on fowarding packages and if something doesn't work out the package is dropped

#### Queuing Delay in more detail
- R: link bandwidth (bps)
- L: packet lenggth (bits)
- a: average packet arrival rate
- La/R ~ 0: avg queing delay is really small
- if La = R then the the avg queuing delay is large
- if La/R > 1 then more work arriving than can be serviced

#### Packet Loss
- finite capcity buffer
- packet arriving to full queue is lost
- routers and switches have buffers for incoming and outgoing queues
    - every link has a queue
    - every router has more than one link and every link has more than 1 queue
- if the incoming queue is full then the packet is dropped
- the sending host then somehow realizes that the package was dropped and resends the packet
- internet provides 'best effort' service
- there are protocols that can be implemented to guarantee packet delivery

#### Throughput
- rate (bits/time unit) at which bits are transferred between sender/reciever
- throughput can be calculated for a single link or between sender/reciever
- throughput would be equivalent to transmission rate if there is no delay/loss of data
- if there are multiple hops with different transmission rates, the end to end throughput from sending host to recieving host changes
- the throughput can not be more than the throughput of the bottleneck

#### Throughput: Internet Scenrario
- all servers have a capcity Rs and clients have a capcity Rc
- 10 connections sharing the links
- it is possible that we can fairly share and get a equal bandwidth R/10

### Protocol Layers
- network is comprised of
    - hosts
    - routers
    - links (switches)
    - different applciations
    - audio/text/video --> bits gets transmitted
    - protocols (decides a formt for 2 devices to communicate)
    - hardware
    - software
- basic approach: sender initializes msg, converted to bits, signal to router, router signals sm else..
- idea of layering is to breakdown the process into smaller tasks an execute as steps
    - combination of protocols that pass info forward
- 2 layering models
    1. ISO/OSI model

#### ISO/OSI reference model
- job should be plit into 7 steps
- there isn't a separate protocol for every activity
- evolved to 5 layer model
1. applciation layer
    - communication initiaites from application by sender host
2. presentation
    - physical layer recieves the message and passes it upstream
3. session
4. 

#### Internet Protocol Stack
- evolution of ISO/OSI
- 5 layers
1. application layere protocols
    - FTP, SMTP, HTTP
    - this is a guideline
    - the software implemenents these guidelines
2. transport
    - TCP, UDP
    - TCP is more common
    - message creaed byg applciation layer is passd to one of the abvoe protocols
    - TCP/UDP are APIs implemented by your OS
    - need to make a system call to use TCP or UDP
3. network
    - IP, routing protocols
    - also OS driven
    - once your host app has produced a msg using HTTP and passes it using TCP, it is in control of your OS
4. link layer
    - also OS driven
    - slightly hardware dependent
    - in order to have hardware compatibility across manufacturers we have protocols (called standards) laid out by IEEE
        - Ethernet, 802.11 (WiFi standard)
5. physical layer
    - the actual wire
    - receieves msg from Ip laye via link layer
    - converts it to a suitable format for the node
    - the jobs of this aye is to transmit the bits
    - half ofthe job of the link layer is perofrmed b ynetowrk inteface card
    - some component of link layer is iplmened by OS
- when wiriting an app, we only have to worry about implementing the application layer
- merges some parts of OSI ISO ref model
    - the acitivities of the omited layers are grouped together
- layers are numbered bottom up so physical is 1
- if you hear layer 2.5 protocol it means there are some tasks from layer 2 and some from 3
- each layer resturctures information based on its rules
- on the receiver end, the reverse proces is performed
    - end receiver msg goes from physical and back up to the application layer

#### Encapsulation
- transport layer adds a header to the message sent by the application layer
- when referring to transport layer protocols, we refer to the message + header as a TCP segment or UDP segment
- network layer does the same thing and calls the msg + header + another header as datagram
- link calls it a frame???
- basically every layer adds some more information to the original message so the end receiver knows how to unpackage it
- switches
    - have 2 layers
        1. link
        2. physical
    - so you can't send raw messags to the switch bc it won't be able to decode it
- router
    - has 3 layers
        1. network
        2. link
        3. physical
    - so it can decode the datagram
    - routers provide security so your data can't be sniffed
- ISPs have a layer for security that lets them see what users are doign
    - these can look into the data you're sending
- https guarantees the applciation layer is encrypting your message
    - so if there is a layer that can open it, it still won't be able to read it

### Network Security
- denial of service attack (DoS)
    - a lot of attackers send useless traffic
    - s