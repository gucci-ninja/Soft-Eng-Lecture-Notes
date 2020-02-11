# 4C03 Computer Networks and Security

## Table of Contents
- [1.1 What is the Internet](#11-what-is-the-internet)
- [1.2 The Network Edge](#12-the-network-edge)
- [1.3 Network core](#13-network-core)
- [Alternative Core - Circuit Switching](#alternative-core---circuit-switching)
- [Delay, Loss, Throughput in Packet Switched Networks](#delay-loss-throughput-in-packet-switched-networks)
- [1.5 Protocol Layers](#15-protocol-layers)
- [2.1 Principles of Network Applications](#21-principles-of-network-applications)
- [Processing COmmunicating](#processing-communicating)
- [2.2 Web and HTTP](#22-web-and-http)
- [HTTP Status Codes](#http-status-codes)
- [Web Caches (Proxy Server)](#web-caches-proxy-server)
- [Electronic Mail](#electronic-mail)
- [DNS](#dns)
- [Client Server vs P2P](#client-server-vs-p2p)
- [Chapter 3 - Transport Layer](#chapter-3---transport-layer)
- [Sequence of Execution](#sequence-of-execution)
- [Tunnel Vision](#tunnel-vision)
- [ UDP Segment Header](#-udp-segment-header)
- [Principles of Reliable Data Transfer](#principles-of-reliable-data-transfer)
- [rdt2.0 fatal flaw](#rdt20-fatal-flaw)
- [Pipeline Protocols](#pipeline-protocols)
- [COntinuation of reliable data transfer](#continuation-of-reliable-data-transfer)
- [TCP Overview](#tcp-overview)
- [TCP seq numbers, ACKS](#tcp-seq-numbers-acks)
- [](#)
- [Connection Management](#connection-management)
- [Quiz Overview](#quiz-overview)
- [Chapter 4 The Network Layer - Data Plane](#chapter-4-the-network-layer---data-plane)
- [How IP Addressing Works](#how-ip-addressing-works)

## Day 1 - Jan 6, 2020
- biweekly labs
- mark breakdown
    - 36 % labs (6 each)
    - 24% midterms (12 each)
    - 40% final exam
- do assignments at home and demo during lab time
- textbook: [Computer Networking : A top down Approach](https://github.com/QSCTech/zju-icicles/blob/master/%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%BD%91%E7%BB%9C%E5%9F%BA%E7%A1%80/%E6%95%99%E6%9D%90/Computer%20Networking%20-%20A%20Top%20Down%20Approach%2C%207th%2C%20converted.pdf)

### 1.1 What is the Internet

#### Nuts and Bolt View (Hardware)
- billions of connected computing devices
    - hosts/end systems running network apps
- communication links - connect end systems together
    - physical media
        - coaxial cable
        - optical fiber
        - copper wire
        - radio spectrum
        - satellite
    - different links transmit data at different rates (bits/s)
- packet switches - connect end systems together
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

#### Service View
- internet as an infrastructure that provides services to (distributed) applications
    - web
    - VoIP
    - email
    - games
- distributed apps because they involve multiple systems exchanging data

#### What is a protocol
- define format, order of messages sent and received among network entities and actions taken on message transmission/receipt
- example between client and server
- client initiates TCP connection request, server gives ok response, client sends get request for webpage, server responds with contents

### 1.2 The Network Edge
- where the end-systems sit
- includes desktops, servers, mobile devices, IoT stuff
- also referred to as hosts because they run applications
    - hosts can be clients or servers

#### Network Structure
- client and server, client requests, server provides
- servers usually in data centers

#### Access Networks
- the closest connection to edge of system - first router
    - aka edge router
- wired and wireless

#### Read at Home
- access networks
    - home access connections: DSL, cable, FTTH, dial-up, satellite
    - 2 most prevalent for broadband residential access
        1. Digital Subscriber Line (DSL)
            - built on existing telephone line
            - dedicated line
            - < 2.5 Mbps upload (typocally < 1)
            - < 24 Mbps download (typically < 10)
            - different transmission rates set by DSL standards to make it assymetric (non-interfering)
            - max rate limited by gauge of twisty wire, distance from home to central office, congestion, cheap plan
        2. Cable
            - built on existing cable television infra
            - since both fibre optic and coaxial are used, it's called hybrid fiber coax (HFC)
                - assymetric
                - 30 Mbps download
                - 2 Mbps upload
            - shared not dedicated
    - shared vs dedicated access
    - DSL is thinner than coaxial
        - coaxial has more bandwidth
    - tv can be transmitted over DSL
- frequency division multiplexing
    - send signals with diff frequency through same wire and they wont interfere as long as there is a considerable difference between the signal frequencies

## Day 2 - Jan 8, 2020

#### Access Networks: Home Network cont'd
- digital subscriber line (DSL) or cable hybrid fiber coaxial (HFC)
- older cable network was a shared service whereas these days they're not shared (dedicated) services
- the term shared/dedidcated can be for the service or the channel
- consists of a bunch of devices, access point, wired ethernet, router + firewall, connect to cable/DSL and then ISPs central office
- router connects the cable/DSL modem and access point

#### Enterprise access networks
- additional switches on site for a huge number of ndoes
- need to split them into smaller groups to manage using ethernet switches
- ethernet uses twisted-pair copper wire
- we can't have a single device connecting to the network
- have different transmission rates availble

#### Wireless access networks
- shared wireless access network connects user to router from a base station (access point)
- in wireless access we have
    - small scale wireless networ
        - home wifi/router since range is smaller (must be within 10-30 metres depending on enterprise vs home)
    - wide area wireless netowrk
        - smartphones belong here since the range is greater (10km)
        - 3G/4G/LTE/5G
- the data which is sent to transmit internet vs telephonic vs mobile has the same udnerlying technology
    - the way this information is converted depends
- example
    - how voice signals are transmitted (audio waves)
        - how does a sound wave get converted to electromagnetic wave
- signal processing
    - convert data into numbers, then send numbers over the network as numbers

#### Host and Data
- host sends packets of data
- host machine takes application message, breaks it into chunks called packets, thre is an upper limit on the size but based on the task the size of packets differs, packet size is length L in bits
    - if you have more data it gets split to multiple packets
- transmition rate (sometimes bandwidth) is denoted by R
    - range of frequencies you can transmit over a medium
    - the medium (wireless or wired) has a range of frequency it can travel
    - the wireless medium has no upper limit for max frequency
    - copper wire has a range
        - this is the bandwidth (min and max frequency that can be transmitted)
    - wireless transmission rates are usually in gigahertz
- to increase the capcity of wired mediums you can make the wire thicccccer (coaxial is thiccccer than DSL)
- transmission rate is about producing the signal, the second part is sending the signal across the wire
- the second part is called propagation (when the signal is travelling towards its destination)
- packet transmission delay = L/R where L is the bits and R is the bits/second -= the time needed to transmit L-bit packet into link

#### Physical Media
- bit - propagates between transmitter and receiver pairs
- when the frequency is higher, the waves can reflect from physical medium (maybe)
- physical link - what lies between transmittr and receiver
- guided media - signals propagate in solid media (copper, fiber, coaxial)
- unguided media - (in wireless) the signals propagate in any direction, also radio
- twister pair
    - two insulated copper wires

##### Coax, Fiber
- coaxial 
    - 2 concentric copper conductors
    - bidrectional
    - used for cable TV snd cable internet
    - can achieve higher transmission rate than twised wire (10s of megabits/s)
    - guided
    - shared
- fiber optic cable
    - glass fiber carrying light pulses, each pulse is a bit
    - high speed (10-100 gigabits/s)
    - low error since repeaters are far apart
    - immune to electromagnetic noise, hard to tap, low attenuation signal up to 100km
    - good for overseas/long distance calls
    - standard link speeds range = 51.8mbps to 39.8gbps
- unidrectional (half duplex)
- bidirectional (full duplex)

##### Radio
- exclusively use electromagentic spectrume
- no wire
- bidirectional
- can go through walls
- signal depends on propagation environment
- radio link types
    - terrestrial micorwave (45 mbps)
    - LAN (WiFi) - 54 mbps
    - wide-area (cellular) - 10 mbps for 4G
    - satellite - kbps to 45 mbps + delay

### 1.3 Network core
- mesh of interconnected routers (packet switches + links)
- packet switching - hosts break app-layer msgs into packets and forward them from one router to the next
- special purpose devices (linklayer switch and router)
    - one common job they both do is packet switching
    - they recieve the packets and forward them using a certain algorithm
    - they take decision based on the content of the packet
    - if there are 10 packes being transmitted between A and B, they will all be considered independently
- the devices in the mesh have to decide which path/route to take
    - swtiching time is based on which path is taken
- packets are transmitted over link at rate = full transmission of link

#### Packet Switching - store and forward
- when a packets bits are received, the packet switch will collect the complete packet (store) and then transmit it on the next hop (forward)
- a hop is a step
- another fundamental principle is that thedevices in the middle (routers) perform a store and forward
- they also verify that the content is correct
- a router has many links and its job is to take packet from input link and send it to the appropriate output link
- if you have N hops the end to end delay is NL/R
    - here we ignore propagation delay
- given it takes L/R to transmit packet to the store, it will take another L/R to forward it
- so the total delay is 2L/R
- if there was no store, it would just be L/R delay but we kinda need to store

##### Example of Packet Switching

```
Length = 7.5 mb
Rate = 1.5 mbps
1 hop transmission delay = L/R = 7.5/1.5 - 5 sec
```

#### Packet Switching - queuing and delay
- a packet switch has an output buffer for every attached link (since links are bidirectional every link has this)
- if arrival rate to link exceeds transmission rate of link for a period of time
    - packets will queueu and wait to be transmitted by link
    - useful if the link is busy tranmitting another packet
    - packets can be dropped if memory buffer fill ups (either the arriving one or an already queued one)
- so apart from transmission delay, there is also a queuing delay

#### Two Key Network Core Functions
- routing - determine source-destination route of packets
    - if the destination of packet is X then it should be transmitted on links 1, 2, 3 for example
- forwarding
    - move packet from routers input to appropriate output
- forwarding tables that use IP addresses
    - each router has its own forwarfing table
    - based on packet destination value, the router will pass onto adjacent router based on that IP
    - maps destination address to router's outbound links
    - forwarding tables are set based on routing protocols

### Alternative Core - Circuit Switching
- end to end resources allocated between source and destination
- kind of like restaurant that takes reservations only
- in circuit switching there is no delay except the constraints provided by bandwidth
- circuit switching says the decision should be based on the end source
    - the path of packets is the same
        - dedicated resources
- packet swtiching says that the swtiching decision will be independent since they are all in chunks
- common for traditional telephone
- circuit segment is idle if it is not used by call (no sharing)
- when network establishes circuit, the transmission rate is also reserved and is guaranteed
- first, end-to-end connection must be established (reservation)
- if you have 4 circuit switches each able to have 4 simultaneous circuits, the transmission rate would be 1/4th of the link's total transmission

#### Circuit Switching- FDM vs TDM
- also possible in packet switching
- in fdm there are 4 signals with 4 different frequencies
    - all hosts don't get a lot of bandwidth
    - horizontal split 
- in tdm we split the time dedicated to transmiting data
    - for time slot 1 you transmit data for host A
    - if the size of the slot is too big then the users will feel a long delay so the trick is to make the time slots as small as possible (like in millisecs)
    - vertical split

## Day 3 - Jan 9, 2020

#### Packet Switching vs Circuit Switching
- packet is for internet
    - allows more users
    - eg 1mbps means each user gets 100kbs when active (probabilistically active 10% of the time)
- circuit is more for telephonic
- packet switching pros
    - good for bursty data because you can change up your path
    - simpler since there is no setup
- packet switching cons
    - excssive congestion possible (leads to delay/packet loss)

#### 1.3.3 A Network of Network
- internet users connect to the internet using ISPs
- we want ISPs to be interconnected so packets can be sent across
- this is a very complex structure
- option 1: 
    - connecting each ISP to every ISP would be O(N^2)
- option 2: Network Structure 1
    - conecting each ISP to one global transmit ISP would allow customer and provider to have economic agreement
    - user pays customer ISP and customer ISP pays provider - global transit ISP
    - con: if one company can make a global ISP then others will too
- option 3: Network Structure 2
    - multiple global ISPs that interconnect
    - two tier hierarchy with global trnsit providers at top tier and access ISPs at bottom tier
- option 4: Network Strcture 3
    - multi-tier hierarchy
    - access ISP pays regonal ISP pays teir-1 ISP
    - there are internet exchange points that connect tier-1 ISPs as well as peering links
    - points of presence exists in all lvls of hierarchy except lowest level
        - group of routers where customer ISPs connecy
- bigger companies like GOogle have their own dedicated connections to the backbone so they run their own network to bring content closer to users
    - act as tier 1 ISPs in hierarchy

### Delay, Loss, Throughput in Packet Switched Networks

#### How does delay occur?
- packes queue in buffers when arrival rate to link exceeds output link capacity

#### Four sources of packet delay
1. processing delay
    - if the contents of the packet were succesffuly received
    - check bit errors
    - determine output link - < a couple ms
2. queueing delay   
    - depends on hw much work the node has to do
    - time waiting at output link
    - error checking?
    - depends traffic
    - similar to processing delay
    - if there the buffer gets filled the packet gets dropped
3. transmission delay
    - L/R
4. propagation delay
    - depends on lenght of link (wire length)
    - based on speed of light (2-3 x10^8 m/s)
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
- this ratio is called traffic intensity

#### Real Internet Delays and Routes
- traceroute for delay measurement from source to router
- send 3 packets to each router 
- router returns packets to sender
- for N-1 routers, the end-to-end delay is N(d_proc + d_trans + d_prop) for uncongested network
- when you get \*** from traceroute it means the probe was lost and router stopped replying

#### Packet Loss
- finite capcity buffers
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
- instantaneous - rate at a single point
- average - rate over period of time
- throughput can be calculated for a single link or between sender/reciever
- throughput would be equivalent to transmission rate if there is no delay/loss of data
- if there are multiple hops with different transmission rates, the end to end throughput from sending host to recieving host changes
- the throughput can not be more than the throughput of the bottleneck
    - bottleneck link = path that constrains the end-to-end throughput

#### Throughput: Internet Scenrario
- all servers have a capcity Rs and clients have a capcity Rc
- 10 connections sharing the links
- it is possible that we can fairly share and get a equal bandwidth R/10

### 1.5 Protocol Layers
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
    2. internet protocol stack

#### ISO/OSI reference model
- job should be plit into 7 steps
- there isn't a separate protocol for every activity
- evolved to 5 layer model because presentation and session can be implemented in application layer
1. applciation layer
    - communication initiaites from application by sender host
2. presentation
    - allow apps to interpret and understand data by encryption/decryption/compression
3. session
    - synchronization checkpoint
    - recovery of data exchange
4. transport
5. network
6. link
7. physical

#### Internet Protocol Stack
- evolution of ISO/OSI
- 5 layers
1. application layer protocols
    - FTP, SMTP, HTTP
    - this is a guideline
    - the software implemenents these guidelines
    - where dns gets IP from domain
    - packet of information is a message
2. transport
    - transports messages between app endpoints
    - TCP, UDP
    - TCP is more common
    - message created by applciation layer is passed to one of the above protocols
    - TCP/UDP are APIs implemented by your OS
    - need to make a system call to use TCP or UDP
    - process-process data transfer
    - transport layer packet = segment
3. network
    - IP, routing protocols
    - also OS driven
    - once your host app has produced a msg using HTTP and passes it using TCP, it is in control of your OS
    - sends datagrams from source to destination
4. link layer
    - also OS driven
    - slightly hardware dependent
    - in order to have hardware compatibility across manufacturers we have protocols (called standards) laid out by IEEE
        - Ethernet, 802.11 (WiFi standard)
    - at each node, network layer relies on this layer to deliver the datagram to next route
5. physical layer
    - the actual wire
    - receieves msg from Ip laye via link layer
    - converts it to a suitable format for the node
    - the jobs of this layer is to transmit the bits
    - half ofthe job of the link layer is perofrmed b ynetowrk inteface card
    - eg ethernet physical layer -> twisted pair or coaxial or fiber
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

#### 1.6 Network Security
- denial of service attack (DoS)
    - a lot of attackers send useless traffic
    - server cannot handle all the traffic and can't serve actual users

## Day 4 - Jan 13, 2020

### 2.1 Principles of Network Applications

#### Creating network app
- write programs that run on different end systems
- just focus on application layer
- if the application inteacts with some third-party hosts then you need some extra protocols?
- we will be workng on generic structure application layer programs
- network core devices don't run user apps
    - each layer provides a generic interface to the neighbouring layer (in API form)
- 2 architectures
    - client-server
    - P2P

#### Client Server
- one node requests for a service and the other provides a service
- communication is inititated by client
- server has a permanent IP address
- if a huge number of nodes are being serviced, need multiple copies of server node (data centers)
- client has dynamic IP addresses and do not talk to each other

#### P2P architecture
- no fixed role
- both devices are switching roles (either can initiate and either can respond to requests)
- usually there is a server which holds a list of nodes which can participate in communication
    - each 'peer' needs to register itself to the server to be added to the list
- there is no 'always-on' servicing node
- useful for file-sharing, content-sharing

### Processing COmmunicating
- process: program running on a host machine
- process comuncation between same host uses OS defined interprocess communcation (not what we are interested in)
- network communication is communcation between a process running on one machine and a process running on another
    - these processes communicate by exchanging messages
- dealt with by OS
- both architectures have client process (initiator) and server (waiter)

#### Socket
- the communcation point through which communciation(app?) layer sends messages to transport layer
- a socket is a software interface that allows processes to send and recieve messages
- usually every socket is bound to some port
- OS provides multiple sockets to communicate with trasnport layer
- circuit programming
    - process controlled by app developer

#### Addressing Processes
- every app is identified by 2 things
    1. IP address (destination host)
    2. port number (connection between trasnort and applicatio layer)
- when using client-server, the server needs a fixed address so clients can easily access the service
- also need to fix port number
- for HTTP servers the default port number is 80
    - for SMTP servers its 25

#### App-layer protocol
- defines what messages will be sent (their contents) and sequence of messages (response)
- error handling is also done at this layer
- can add variations that allow you to bypass layers (eg go straight from app layer to network layer)

#### Transport Layer
- udp or tcp
- qualities of a good trasport layer
    - data integrity (need 100% for file transfer but not audio)
    - security - want to make sure data is securely and successfully transferred
    - timing - delay constraints
    - throughput - min rate for effectiveness bandwidth sensitivity) vs best effort (elastic apps)
- different requirements for different types of applications

#### TCP service vs UDP service
- TCP
    - connection oriented
    - for reliable data transfer
    - establish connection before exchanging information (handshake)
    - includes congestion control and flow control
    - guarantees that data will reach the other end
        - udp doesn't do that
    - buffering: start to download data but don't service it until there is enough data to service
- UDP
    - unreliable data trasnfer (no guarantees)
    - does not require connection setup
    - good solution for a "no frills attached" app
    - no flow/congestion control
    - if you want to send a huge amount of data as quickly as possible and not care about congestion then UDP is your best bet
    - will only work if there is not a lot of traffic
- neither protocol provides min throughput, timing, security
    - solutionL appp dev has to add additional sources
    - for video streaming apps, there is additional code that guarantees min throughput and min delay
- most apps use TCP (mail, remote access, web, file tranfer) and some use either (streaming, video/online call)

#### Securing TCP
- tcp and udp have no encryption
- SSL sits between app layer and transport layer
    - takes info from HTTP and secuely sends it to tcp layer
    - encrypts data
    - denoted by lock sign in browser window (HTTPS = HTTP + SSL)
    - ssl socket API encrypts pwasswords to be sent

### 2.2 Web and HTTP
- web is a network of computers with specialzed web service available
- http is the protocol that makes this service possible (defines rules for www)
- webpage consists of objects
    - html file, jpeg, java applets, audio files..
    - webpage is identified by URL (server host + path to obejct)

#### HTTP overview
- hyppertext transfer protocol
- client - browser requesting onjects, server respsonds with objects
- communication is initated by client who sends HTTP request (requesting document they wanna open)
- request reaches server and server responds with contents
- http request is FOooOrrr an html page
- THe Google.com gets a TCP connection on port 80 from some client and accepts the TCP connection 
- http is stateless
    - servers don't store info on requests made
- if you want the server/client to maintain state you can add code for that
    - common technique is saving cookies on client-side
    - client can say they dont want to store cookies

## Day 5 - Jan 15, 2020

#### HTTP Overview cont'd
- websites provide content through webserver
- the port numbers through which service is provided is known
    - i.e HTTP uses port 80
    - TCP socket connection on port

#### Types of HTTP

##### Non-Persistant HTTP
- when you requeest a new document, a new TCP connection is made
- all audio/video/image files are independent objects
- separate requests are made for each object
- new TCP connection for each object

##### Persistent HTTP
- keeps TCP connection open
- multiple objects can be sent over one TCP connection
- this is the default in the current model of HTTP but canconfigure to use non-persistent

#### Response Time for Non-persistent HTTP
- RTT (round tripe time)
    - time for a small packet to travel from client to server and back (round trip time)
    - can never be preciely measured because factors such as network congestion affects the value
- RTT = time from TCP request initiation to file request
- RTT = time from file request to when the file is received
- the two steps above are assumed to have the same RTT
- depending on file size, the RTT will vary
- 2RTT + file transmission time = non-persistant HTTP response time
    - 2RTT means more overhead
- 2RTT would be fo every object

#### Persistent vs Non-persistent
- persistent is obviously better because you have an open connection and the client can send requests as soon as it encounters referenced objects
    - as little as 1 RTT for all referenced objects

#### HTTP request message
- two types
    - request (written in ASCII text)
    - response
- \r\n is after every line, it is the carriage return and linefeed to indicate where header lines start and end
    - 2 at once = message end
- format is request line + header lines
- if connection type is close then it means you don't want to keep the connection open (you want non-persistent)

```
GET /index.html HTTP/1.1\r\n (method path protocol)
Host: host_url\r\n
User-Agent: browser\r\n
Accept: text/html,...\r\n
Accept-Language: en-us\r\n
Accept-ENcoding: gzip\r\n
Accept-Charset: utf-8\r\n
Keep-Alive: ##\r\n <----- how long you want to try before just dropping packet
Connection: keep-alive\r\n

\r\n
```

#### General Format
- method path version cr lf
- header field name: value cr lf
    - can have multiple of this or none
- cr lf (blank line)
- entitiy body (for post requests)

#### Form Input
- post method
    - input uploaded to server
- url/get
    - input in path field of request line

#### Method Types
- HTTP/1.0
    - get
    - post
    - head (used for debugging, leaves object out of resposne)
- HTTP/1.1
    - get
    - post
    - head
    - put (uploads file to path specified)
    - delete

#### HTTP Response MEssage
- status line has protocol, status code and status phrase
- bunch of header lines (date,server, last modified), content-length, keep-alive, content-type
- blank line
- data you requested (HTML file maybe)

### HTTP Status Codes
- 1st line in server-to-client response message
- 200 - OK
- 301 - moved permanently
    - new location specified later in msg
    - sometimes do automatic redirection
- 400 - bad request
- 404 - not found
- 505 - HTTP version not supported
- 304 not modified
- 418 - i'm a teapot :tea:

#### Trying out HTTP
1. Telnet
    - command prompt utility (network based)
    - allows remote connection to machines
    - `telnet url port_number`
    - one of the default original services of internet
2. type in a GET HTTP request
    - `GET /page HTTP/1.1 Host: base_url`

#### Cookies
- small text-based pieces of info stored on the client side in a small file
- server sends client a message saying they want to store cookies
- the browser checks to see if client has cookies enabled
- if yes then some information is stored in some text file locally
- next time you visit the same url the browser will look for a cookie file
- 4 parts
    1. cookie header line in HTTP response (true/false?)
    2. cookie header line in next HTTP request (cookie file/say yes/no)
    3. cookie file on user side managed by browser
    4. backend database access to return appropriate data based on cookie file
- line in header = Set-cookie: user_id which creates the file
- subsequent requests will have a header cookie: user_id 

### Web Caches (Proxy Server)
- doesn't have anything to do with web service
- proxy server is any server working behind the scene for some service (FTP, mail, web, etc)
    - works to satisfy client request without using origin server
- most browsers maintain their own web cache
- browser sends request to cache, if it finds it, the contents are returned else it goes to the origin server
- used to immeditwly service user through local means
- most of the time we're not able to tell the difference since generic websites don't usually have big changes
    - if you refresh this forces the HTTP request to go to the origin server
    - if that doesn't work, clear cache
- proxy servers fetch new copies behind the scenes so the content is updated
    - more frequent for ISP caches
    - not that frequent for local
- hitting refresh adds an extra parameter in the header to specify tha the user wants a fresh copy
- pros
    - reduces response time
    - reduces traffic to origin server
- cons
    - if you're trying to access a website in which the content frequently updates, web caching is not that useful
- application can add a refresh rate to ensure the user is getting a fresh copy every time

#### Caching Example
- assumptions
    - avg object = 100Kb
    - avg reqest rate = 15/s
    - avg data rate = 1.5 Mbps (15 * 100)
    - RTT = 2 sec
    - access link rate = 1.54 Mbps
- consequences
    - if all the requests are forwarded to origin server, there will be 1.5 Mbps traffic (99% usage)
    - can improve if you change access link rate to 154 Mbps but that might be expensive
    - another solution would be local web caching
        - 40% requests can be serviced though cache
        - 60% need to go to the origin service
        - therefore data rate to browser over access link = 0.6\*1.5 Mbps = 0.9
        - so utilixation = .9/1.54 = 0.8
        - total delay = ?

### Electronic Mail
- SMTP, POP3, IMAP
- when you want to send a message to another user
- 3 major components
    1. user agents 
        - email clients like browser, Outlook, email apps
        - produce and receive
    2. mail servers
        - receive or send emails
    3. simple mail transfer protocol
        - smtp and others
- uses TCP on port 25
- 3 phases
    1. handshake
    2. transfer msg
    3. closure

#### User Agents
- mail-reader
- smtp
    - client uses TCP to send mail to mail server (ie McMaster)
    - mail server then uses smtp protocol to send mail to recipeient mail server (ie GMAIL)
    - tcp uses port 25
- tcp is the only protocol that guarantees your message will be sent

#### Mail Servers
- mailbox
- has a msg queue of outgoing messages to be sent

#### SMTP [RFC 2821]
- 3 phases of transfer
    - handshaking (greeting)
    - trasnfer of messages
    - closure
- kind of like a chat between your mail server and recipient mail server?
- commands - ASCII
- response - status code + phrase
- msgs must be in 7-bit ASCII
- need another protocol to actually pull the email form recipeient sever to recipient user agent

## Day 6 - Jan 16, 2020

#### Electronic Mail servers
- client sends a request and server responds
- message format has a 'to:' 'from:' and 'subject:' followed by a blank line and then the body (ASCII only)
- this is different from SMTP MAIL FROM, RCPT TO:

#### Mail Access Protocols
- SMTP
- mail access protocol
    - IMAP (INternet Mail Access Protocol to manipulate stored messages on server)
    - POP (Post office Protocol for authorization and downloadin)
    - HTTP (browser email - gmail, Hotmail)
- tunneling
    - messages of one protocol can be sent through another protocol

#### POP3
- pull new mail messages every 10 seconds
- authorization
    - asks for username and password
    - server responds with ok or err
- transaction
    - list - list message numbers
    - retr - retrieve message b ynumber
    - dele - delete
    - quit
- stateless

#### IMAP
- allows user folders 
- can split and organize emails

#### Browser Based (HTTP)
- allows splitting and roganizng too

### DNS
- domain name system
- port number is fixed
- IP address of servers is also fixed
- internet hosts and routers convert word urls to the IP address
- before TCP connectionis created, the domain name getsresolved into IP address
    - happens before message is sent
- gmail gay
- yahoo good

#### Hierarchial Database
- each url ending has its own DNS server (.com, .org, .ca)
- then each root url has its own DNS server (yahoo.com, amazon.com, pbs.org)

#### Top Level Domain Servers
- all top-levl country domains

#### Authoritative DNS server
- ??

#### Local DNS nameserver
- doesn't belond to hierarchy
- each ISP has one
- also can be called a proxy DNS server
- works like a cache for DNS servers to reduce traffic to root DNS servers

#### DNS name resolution example
- 2 ways
    1. iterative query
    2. recursive query
        - not good for load balancing since it sends more traffic to root and TLD servers

#### DNS Caching, Uploading Records
- records
- tuple of 4 values (name, value, type, ttl)
- type can have 4 values
    - A
        - direct mapping between host name and IP address
    - NS
        - domain name that is mapped to another domain name
        - ie if you type www.google.com it might actually be www.abc.google.com
        - split into multiple subdomain names
        - this info is stored in the authoritative name server, not the root or TLD server
    - CNAME
        - name is alias for real name
        - ie ib.com is really servereat.backup2.ibm.com
    - MX
        - sm to do with mailservers

#### DNS protocol, messages
- width is always 4 bytes, 32 bits
- message header includs identification (2 bytes) + flags (2 bytes)
- have to set the bit to specify if you want to do an iterative or recrusive query in the flags

#### How to register your domain name
- ICAN holds authority over all domain names
- godaddy, domain.com commericialize the domain names on behalf of ICAN
- first they ask if you have a name server
- if you're a big or small company
- if you have a name server, you have to give them your IP address
- if you're a small business you need to buy hosting from godaddy or whatever

## Day 7 - Jan 20, 2020

### Client Server vs P2P

#### File Distribution Time: Client Server
- server transmission = size of file x number of copies being sent / upload speed u
    - NF/u
- client - F/dmin where dmin is the minimum client download rate
- bottleneck will either be the client's download rate or the smallest client's download rate

#### File Distribution TIme: P2P
- server transmission - F/u
- client - F/dmin
- clients also contribute file content
- therefore, the max upload rate is us + sum of all u from other clients

#### P2P BitTOrrent
- file divided into 256Kb chunks
- cant set priorities of what peer you want to download from
    - only want file from peers who have complete file

#### Mulitmedia - Video
- one single second consists of 25-30 still images
- the images are then shown to us at a constant rate
- for every pixel, store the pixel number + colour values
- 1 second content = 25 Mb if each image takes 1 Mb
- to save space and time, usually store changing pixels (temporal coding example)
- another method is to send a pattern (i.e 42 black pixels, followed by n #???? pixels) but it's not as efficient

#### Content Distribution Networks
- storing multiple datas

#### Socket Programming
- lets you communicate with TCP or UDP
- A2 - basic socket python API

### Chapter 3 - Transport Layer

#### Transport services and protocols
- all OS by default implement UDP and TCP code provided by RFCs
- just like the app layer, the trasport layer assumes that we're connected directly
- sgement = app messages broken down into smaller parts that gets passed to netwrok layer after doing some processing
- one segment goes into 1 netwrok layer message

#### Transport vs network layer
- network layer takes care of logical communication between hosts

#### Internet transport layer protocols
- tcp or udp

#### Multiplexing/demultiplexing
- mulitplexing at sender: handle data from ultiple sockets, add transport header
- one entitiy, provide multiple doors (sockets) to handle mulitple inputs
- demultiplexing at receiver: user header to deilver recieved segments
- also sends port number of client in the msg so server can reply back

## Day 8 - Jan 22, 2020

### Sequence of Execution
- run proxy server
    - check if it's accepting connections on some port
- run client
- enter command at client: `ftp ftp.cdc.gov`
    - harcode proxy server port

#### Commands to implement
- list is given
    - USER, PASS, PWD, CWD, HELP

### Tunnel Vision
- encapsultion ftp commands inside http

###  UDP Segment Header
- checksum (16 bit number) based on content of msg
- during deliverry, if a certain bit is flipped, the checksum computed will be different
- reciever can recover from this 

### Principles of Reliable Data Transfer
- network layer provides no reliability

## Day 9 - Jan 23, 2020

### rdt2.0 fatal flaw
- the next packet is delivered upon acknowledgement that the packet before was successfully delivered
- if it's not delivered the sender gets a negative acknowledgement and you try sending the packet again
- if the ack/nak is corrupted you can retransmit current packet
- to know if its a duplicate you need to send a sequence number with the packet
- if you get a duplicate then resend acknowledgement and drop duplicate
- 2 sequence numbers are sufficient (2 bits) because you're only dealing with 1 packet at a time
- max bits for internet protocols is generally 16 bits
- when the data packet is receieved there are 3 possibilities
    - it's corrupt so u send the nak
    - it's not corrupt so u send an ack
    - you get a duplicate by checking sequence number (most likely due to lost acknowledgement) 
        - action: resend ack
        - sequence number is either 0 or 1 (stop and wait)

#### Parts of the Message
- checksum verified bit error
- sequence number is to check for duplicate
- acknowledgemt = confirmation
- retransmission is to see if we have to resend

#### Channels with errors and loss
- need to wait reasonable amount of time to wait for ACK
- negative ackonwledgement - when you get a sequence number you were't expecting

### Pipeline Protocols
- used to save overhead time from RTT
- allow you to send multiple packets
- allows time L/R to account for multiplr packets
- each packet needs unique sequence numbers so we can't use 0 and 1 anymore
    - number of sequence numbers for both depends on N

#### Go-back-N
- receiver only sends cumuative acknowledgements
- sender has timer for oldest unacked packet
- it sends N packets (each takes L/R time) 
    - timer is only started for the first packet
- receiver has to put out of sequene packets in a buffer and keep track of how many packets have been recieved
- sender has to track how many packets are out there
- less overhead but more retrasnmissions

##### Sender
- how many bits is N? - 2^k?? 
- once the window is completely transmitted (N packets in buffer) you send the cumulative acknowledgement
- send-bae = smallest sequence number
- nextseqnum = next packet that has not yet been transmitted

##### Receiver
- send one acknowledgment for the highest in-order sequence numbers successfully received

#### Selective Repeat
- sender can have up to N unacked packets in pipeline
- sender sends individual acknowledgements
- have the ability to selectively repeat packets
- timer for every packet
- less retransmissions and more overhead

## Day 10 - Jan 27, 2020

### COntinuation of reliable data transfer

#### GNB or whatver
- no buffer to store discarded packets
- when acks for packet 0 and 1 are recieved, new packets 

#### Selective repeat: sneder, reciever, windows
- yellow are transmitted
- blue have yet to be transmitted
- when the packet in gray on the left (first one after dotted line) is recieved, it skips 3
- basically, the window slides to the next gay packet

#### Selective Repeat Sender
- if n is the smallest unacknowledged packet, slide window to next unacknowledges sequence number

#### Selective Reapeat Reciever
- because of bit error, the sequence number can be unexpected
    - in this case, the packet is discarded

#### Sequence Example iwth 4 packets
- when sender recieves ack3, it marks (records) it
- reciever moves the winodw and delivers packet 2,3,4,5

#### Selective repeat dillema example
- we are sing 4 different sequene numbrs 0 1 2 3 (range is 4)
- size of window is 3
- note difference between range and window size^
- packet 1 is delivered, packet 2 has no acknowledgment, packet 3 is lost and then packet 0 is transmitted
- 0, 1, 2 si trasnmitted but acks for all are lost
- sender will retransmit all 3 since they all hit timeout
- reciever successfully recieves all 3 packets so it slies the window
- so the reciever is expected new packets starting fom 0 1 2 while the sender is still trying to send the old 0 1 2
- cant distinguish between old and new zero
    - solution: make a reasonable gap
    - thus size of window and range should be different
- what is the optimal difference
- want to add more numbers between 3 and 0 so 0 and 1 dont enter into the window
- the problem can be avoided by adding 
    - if we had 4 or 5 it'll be sufficient
    - size of window should be half of sequence number range so you can distinguish betwen old and new and they dont overlap

### TCP Overview
- tcp uses a smilar approach to selective repeat
    - it waits a bit and fills up the buffer to send packets in order
- full duplex - data travels in both directions
    - so far all the algirhtms we discussed have a snder and reciver (sender transmits msg and reciever sends acknowledgement)
    - TCP is like 2 parallel copies of the algorithm because it's bidrectional (sender transmits and also sends acnowledgements, vice versa)
- before startig to transmit data, it establishes connection and decides on some basic variables
- flow controlled
    - the rate at which data is coming through is fixd
- congestion control 
    - when tcp observes congestion it slows down speed

#### TCP segment structure
- similar to udp
- every segment has source port number and destination port number
- squence number is 32 bits
- so max sequence number would be 2^32 -1
- since its a sliding protocol, size of window should be half of the sequence number
- also has acknowlegdement number
- all tcp segments have the same header
    - the difference is in the acknowledgemnt number
- when you create a string of bits, there's no way to distinguis empty bits because 0000.. is a valid number
- no length field like udp but it has a header length field (which udp doesnt have)
- this means n udp the size of segment is variable but the size of the header is fixed
- in tcp the size is based on the link layer
- the tcp segment is picked in a way that a tcp segment can be fitted in the link layer
- tcp identifies whcih link the data will be transmitted through (wifi, wired network)
- both link layers have different size
- this means the same msg sent over wifi vs wired network will have a different number of tcp segments
- we dont have a length field because its based on link layer

### TCP seq numbers, ACKS
- zoned out

## Day 11 - Jan 29, 2020

### 
- sequence number + bit = 43

## Day 12 - Jan 30, 2020

### Connection Management
- handshake
    - agree on parameters (sequence numbers and value of recipient buffer)
- issues
    - first request is successfully recueved but the client side reaches timeout
    - if retransmitted request is really delayed, the client will stop waiting for it

#### TCP 3 way handshake
- synbit -> denotes if packet to establish connection has been sent
- syn recvd -> denotes if packet to establish connection has been recieved


#### Closing a tcp connection
- fin_wait
- fin_bit
    - 1 or 0
    - if the packet to close connection has been sent

#### Congestion Control
- initiated by reciever side basd on reciever window
- in 1 RTT, 1 data segment is sent
- additive increase
    - if it is successfully sent, it doubles the size of cwnd by 1 MSS (
        - MSS = frame size - data link layer header - more headers
        - max bound is reciever window thingy
        - cwnd is current window
- multiplicative decrease

#### Slow Start

#### Slow Start to CA
- in order to accomodate/avoid congestion, it slows down speed (as soon as cwindow touches ssthreth)
- linear congestion instead of exponential
- if there is a timeout error, the congestion window segments goes down to 1 in the next RTT

## Day 13 - Feb 3, 2020

### Quiz Overview
- 10-12 questions, 21 marks
- ch 1 - ch 2.2
- ignore security section in chapter 1

### Chapter 4 The Network Layer - Data Plane

#### NEtwork layer
- packets are called datagrams
- router examines header fields of every datagram passing through

#### Major Functions
1. forwarding
    - moves packets from router's input to appropriate output ports
2. routing
    - router decides wheich port a packet should be sent to
- router has at least 2 ports (incoming and outgoing)
- all ports work as incoming and outgoing (bidirectional)

#### Data Plane
- where actoins are performed
- determines how datagram is forwarded

#### Control Plane
- where router runs algorithms to decided mapping

#### Router Architecture Overview
- 

## Day 14 - Feb 5, 2020

#### Internet Network Layer
- when the packet is forwarded from transport layer to application layer, IP address is coming from the DNS server 
- at application layer - we have our domain name (google.com)
- transport layer ensures the IP address is available before transporting packets
- forwarding table
- IP protcol
    - governs how packet should be constructed (header + data)
- ICMP protocol - its job is to report errors
- IP protocols are impemented at routers but every host as its own lil forwarding table that forwards packets to gateway router
- a couple protocols that IP protocol requires help from (between IP and link layer)

#### IP Datagram Format
- 32 bits length for each row
- ip protocol version number (4 or 6)
- min IP header lenght = 20 bits
- length = total datgram length + data
- 16 bit identifier - sequence number (unique and random)
- time to live - after a certain number of hops, the datagram will be dropped
    - helps in terms of routing
    - if there is a loop in routing table then the datagram might keep travelling forever
    - if the router sees a 0 in this one, it'll automatically be dropped
- checksun - if the checksum doesn't match up, datagram is dropped (no acknowledgment will be provided)
- source and destination ip address (both 32 bit)
- 20 bytes of TCP
    - desination + source port number
- 20 bytes of IP header
- therefore 20 + 20 = 40 bytes of overhead + extra overhead

#### IP Fragmentation
- one datagram cant fit into one segment/fragment
- the datagram is split into fragments
- when an IP datagram goes to an ATM router, it is split into smaller fragments and theyll be encapsulated by the ATM datagram
- eg length 4000 and id x is split into 3 each with length 1500(1480), 1500(1480), 1040, each with id x 
    - the fragments will have an offset and all but the last one will have a fragflag indicating there are more fragments after this
- the offset is in bytes/8 (so the first has 1480/8) so 185 and the next will be 185 + 1480/8 = 370
- offset in bytes/8 because we don't have enough space to store it in bytes, so length has to be 
- each fragment is whatever bytes + 20 bytes?
- tcp header is only in the first fragment? <--- 

### How IP Addressing Works
- fixed and dynamic
- 32 bit number split into 4 8 bit numbers
- every link of a router will have its own IP address
- ethernet switch in the middle between devices and router
- higher order bits is the subnet part and then the host poart (lower order bits) identifies the device itself
- so every device in a network requires unique IP address (only in subnet)
- bigger enterprise system is divided into multiple subnets

#### How addressing is assigned
- in the beginning they were distinuished by classes (A, B, C)
- class A had 8 bits in the subnet part and the rest for host, B had 16 bits for subnet and rest for host (depended on devices in network)
    - rigid system
- modern appraoch
    - classless interdomain routing (CIDR)
        - any number of bits for subnet (23 bits for subnet and the rest 9 for host part)

### Midterm Glossary - Keywords and Definitions

#### 1.1 What is the Internet

##### 1.1.1 - nuts and bolts
- hosts/end systems
    - end users that are internet users, invluces PCs,laptops, smartphones, tablets, TVs, home appliances, smart watches, etc
- communication links
    - physical method through which data is transmitted
    - coaxial cable, copper wire, optic fiber, radio spectrum
- transmission rate
     - rate at which data ins transmitted
     - measured in bits/s
- packets
    - packages of information, segments of data with header bytes which are sent through the network to the destination and reassembled into original data
- packet switches
    - takes packet arriving from incoming communication link and forwards it to outgoing communication link
    - two types, router and link-layer switches 
- routers
    - forward packets to ultimate destination
    - typically for network core
    - route = ssequence of links and switches router takes to send data
- link-layer switches
    - forward packets to destination
    - typically for access networks
    - path = sequence of links and switches link-layer switch takes to send data
- Internet Service Providers (ISP)
    - how end systems access internt
    - is a network of packet switches and communication links
    - provide residential broadband access (cable modem/DSL), high-speed LAN access, mobile wireless access
    - ISPs are also interconnected
- Transmission Control Protocol (TCP)
- Internet Protocol (IP)
    - specifies format of packets sent and received among routers and end systems
- Internet Standards
    - agreement on what each protocol does
    - developed by Internet Engineering Task Force
- Request for comments (RFC)
    - standard documents written up by IETF
    - technical and detailed
    - define protocols TCP, IP, HTTP, SMTP
    - currently 7000 RFCs
- IEEE 802 LAN/MAN standards committee
    - define standards for Ethernet and WiFi

##### 1.1.2 - services description
- distributed application
    - applications that involve multiple systems exhacning data
- socket interface
    - specifies how program running on one end system will ask internet infrastructure to deliver data to destination
    - programming interface for hooks so apps can send and recieve using connection to internet

#### 1.2 Network Edge
- client
    - a type of end-system/host
    - tend to be desktops and moble PCs
- server
    - type of end-system/host
    - tend to be more powerful machines that store and distribute web pages, stream video, relay email
- data centers
    - where most servers reside and dstribute web pages, email, videos
    - google has 50-100, 15 of them with more than 100k servers

##### 1.2.1 Access Networks
- digital subscriber line (DSL)
    - type of broadband residential access
    - usually obtained from same company that does wired local phone
    - when DSL is used, ISP = telco
    - uses existing phone line (twisted-pair copper wire) to exchange data with digital access subscriber line acess multiplexor (DSLAM)
    - DSL modem on user end takes digital data and transates it to high frequency tones for transmission over telephone wire
    - go from analog signal at house to digital format at DSLAM
    - line can carry both data and phone signal simultaneously because of different frequency encoding
        - 0-4kHz band for phone (ordinary channel)
            - this is why phone is bad quality (big wavelength - lose data)
        - 4-50kHz band for upload (medium speed)
        - 50 kHz to 1MHz band for download (high speed)
- cable internet access
    - type of residential network access
    - makes use of cable televisoin company's existing infrastructure
    - fiber optics connect cable head end (cable modem termination system - CMTS) to neighbourhood junction (500-5000 homes), then coaxial cable connects homes to everything
    - since both fibre optic and coaxial are used, it's called hybrid fiber coax (HFC)
    - requires modem like DSL, but connects home PC through Ethernet port
    - CMTS is similar to DSLAM, turning analog signal from modem to digital
    - shared broadcase medium - every packet sent by head travels downstream on every link to every home 
    - so if multiple users are downloading same video, actual rate will be lower than aggregate cable downstream rate
    - upload is also shared so a distributd multiple access protocol is needed to avoid collisions
    - avg speed is 42.8 mbps down and 30.7 mbps up
- fiber to home (FTTH)
    - type of residential broadband access gaining popularity
    - provides higher speeds than DSL and cable
    - provides optical fiber path from CO directly to home
    - one fiber from CO to home (actually CO to homes but fibre splits)
    - two competing network architectures that do the splitting
        1. active optical networks (swithes ethernet)
        2. passive optical networks
    - each home has an ONT - optical network terminator, connected by optical fiber to neighbourhood splitter
    - fibre then goes from optical splitter to OLT (optical line terminator) - which provides conversion between optical and electric signals
    - average download is 20 mbps and 13 mbps up
- dial-up/satellite link
    - also residential
    - for rural areas - around 1mbps
    - dial-up = dsl but slower
- Internet of Things
    - devices that connect to internet wirelessly
    - in enterprise network, they transmit/receive packets to/from access point that is connected to wired ethernet, making it a wireless LAN setting
- 3G/LTE
    - for wide area access
    - mobile phones

##### 1.2.2 Phyical Media
- bit
    - propagates between transmiter/receiver pairs
- physical link
    - transmitter/receiver pairs
- guided media
    - signals propagate in solid media (copper, fiber, coaxial)
- unguided media
    - signals propagate freely
- unshielded twisted pair (UTP)
    - for LANs, frequently used for computer networks in a building
    - data rate depends on thiccness and distance between transmitter/reciever
- shared medium
    - number of end-systems connected to cable with each end system recieving whatever is sent
- geostationary satellites

- low-earth orbiting satellites

#### 1.3 Network Core

##### 1.3.1 Packet Switching
- messages - information in the form of data/ control function
- packet switches
- routers
- link-layer switches
- store-and-forward transmission
    - packet switch waits for entire packet to be transmitted, stores it until its done and then forwards
- output buffer/queue
- queuing delays
- packet loss
- forwarding table
- routing protocols
    - what sts the forwarding table values (automatically)
    - determines shortest path from each router destination 

##### 1.3.2 Circuit Switching
- circuit switching
- packet switching
- circuit
- end-to-end connection
- frequency-division multiplexing (FDM)
- time-division multiplexing (TDM)
- bandwidth
- silent periods
- customer
- provider
- regional ISP
- tier-1 ISPs
- PoP
- multi-home
- peer
- Internet Exchange Point (IXP)
- content-provider networks

- network archiecture - 5 layer model (fixed)

#### Chapter 2 - APplication Layer
- application architecture
    - dictates how application is structured over end system
- client-server architecture
    - always-on host called server with fixed address which services requests from clients
- P2P architecture
    - minimal or no reliance on servers
    - clients act as both server and client
    - hosts intermittently connected 'peers'
    - good for traffic intensive
- process
    - prgram running within end system
- client
    - process that initiates communication
- server
    - waits to be contacted to begin session
- socket
    - interface for processes to send and receive messages
- IP address
    - 32 bit number that is sent as part of process identifier
- port number
    - number to identify rocess running on host machine
    - also part of process identifier
- reliable data trasnfer
    - something that TCP does, UDP does not
- loss-tolerant applications
    - audio/video
    - not file sharing
- bandwdith sensitive apps
    - multimedia aps
    - telephone apps (32-36 kbps)
- elastic apps
    - not bandwidth sensitive
    - file sharing
    - email
    - messages?
    - web trasnfers 
- timing, throughput, security, data integrity = good protocol
- application layer protcol
    - defines how app's processs communicate

#### 2.2 Web and HTTP
- webpage
    - consists of object
- object
    - a file (html ,jpeg)
- base HTML file
    - primary page with references to other objects
- web browsers
    - implement client side of HTTP
- web server
    - implement server side of HTTP
    - apache, nginx
- stateless protocol
    - HTTP
- non-persistent connection
- persistent connection
- round trip time (RTT)
    - time for small packet to travel from client to server and abck to client
- request line
    - first line of HTTP request msg
- header lines
    - subsequent lines of HTTP request/response msg
- status line
    - first line of HTTP response msg
- entity body
    - contains requested object or post 
- cookie
    1. cookie header line in response from server
    2. cookie header line in request
    3. file containing cookie
    4. backend connection to db
- web cache/proxy server
    - satisfies HTTP requests on behalf of origin server
    - 40% hit this
- Content Dsitribution NEtworks (CDNs)
    - make it easier to use caches on internet and localize traffic
- conditional get
    - look at if-modified-since header line and only refresh cached copy is the last-modified date is more recent
    - else 304 not modified

#### 2.3 Electronic Mail
- user agent
    - allow users to ead, reply, forward, save, compose emails
- mail server
    - where messages go to be sent (queue)
- Simple Mail Transfer Protocol (SMTP)
    - application layer protocol for email
    - uses tcp
- mailbox
    - spot dedicated for each user agent in mail server
- message queue
    - where emails get put before they can be sent off
- pull protocol
    - HTTP, users pull info from server
- push protocol
    - primarily SMTP - mail server pushes mail to user agent (initiation by side who wants to send, not receive)
- Post Office Protocol Version 3 (POP3)
    - short and readable protocol that begins when user agent opens a TCP connection to mail server
    - does authorization, transactions (list, retr, dele, quit) and updates
- Internal Mail Access Protocol (IMAP)
    - associates each message with a folder
    - allows users to move messages around, delete them
    - keeps state

## Feb 6, 2020
- midterm

## Day 15 - Feb 10, 2020

### IP Addressing
- every end of a router is considered as a independent network
- IP address has 2 portions: network (LHS) and host (RHS)
- depends on how big the subnet is going to be
    - host portion depends on how many computers will be on that network (8 bits = 2^8 computers)
    - first few bits for those computers will be common (subnet address)
    - address of network itself = subnet address + all 0s
    - all 1s = broadcat address
    - therefore with 8 bits you can really only have 2^8 - 2

#### Subnets
- 
- /24 = 255.255.255.0 (first 24 are 1s)
- 23 bits: 255.255.254.0 (11111111 11111111 11111110 00000000)

##### CIDR
- classless interdomain routing
- class A - first 8 bits fixed
- class B - first 16 bits fixed
- 192.168 (class b reserved ranfe) and 10.x.x.x (class a reserved range)

#### DHCP
- dynamic host configuration protocol
- messages transmitted using UDP
- UDP is used by DNS and DHCP (discovery services)
    - because tcp requires connection establishment but to do that you need sufficient information
- goal: allow host to dynamically obtain its IP address from network server when it joins network

#### DHCP client server scenario
- temporary ientification for client
- permanent identification for server
- must know which port to reply to
    - 68 ?
- mac address = 48 bit
- ip address = 32 bit
- all 0s = unknown or network address
- how does network get subnet part of ip?
    - allocatd portion from ISP address space
