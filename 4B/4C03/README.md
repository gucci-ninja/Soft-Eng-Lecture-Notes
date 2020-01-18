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
    - server cannot handle all the traffic and can't serve actual users

## Day 4 - Jan 13, 2020

### Creating network app
- write programs that run on different end systems
- just focus on application layer
- if the application inteacts with some third-party hosts then you need some extra protocols?
- we will be workng on generic structure application layer programs
- network core devices don't run user apps
    - each layer provides a generic interface to the neighbouring layer (in API form)
- 2 variations
    - client-server
    - P2P

### Client Server
- one node requests for a service and the other provides a service
- communication is inititated by client
- server has a permanent IP address
- if a huge number of nodes are being serviced, need multiple copies of server node (data centers)
- clint has dynamic IP addresses

### P2P architecture
- no fixed role
- both devices are switching roles (either can initiate and either can respond to requests)
- usually there is a server which holds a list of nodes which can participate in communication
    - each 'peer' needs to register itself to the server to be added to the list
- there is no 'always-on' servicing node
- useful for file-sharing, content-sharing

### Interprocess communication
- network communication is communcation between a process running on ne machine and a process running on another
- dealt with by OS

#### Socket
- the communcation point through which communciation layer sends messages to transport layer
- usually every socket is bound to some port
- OS provides multiple sockets to communicate with trasnport layer
- circuit programming
    - process controlled by app developer

#### Addressing Processes
- every app is identified by 2 things
    1. IP addres (host)
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
    - data integrity 
    - want to make sure data is securely and successfully transferred
    - timing
    - throughput
- different requirements for different types of applications

#### TCP service vs UDP service
- guarantees that data will reach the other end
    - udp doesn't do that
    - app deveoper can decide which protocol to use and use the interface provided by the OS for that protocol
- tcp
    - reliability
    - congestion control
- throughput and timing are not guaranteed by either protocol
    - solution: app dev has to add those additional features
- for video streaming apps, there is additional code that gaurantees min throughput and min delay
    - buffering: start to download data but don't service it until there is enough data to service
- tcp is connection oriented
    - before data is transferred, you need to establish connection between host and end-user 
- udp does not require connection setup
    - good solution for a "no frills attached" app
- if you want to send a huge amount of data as quickly as possible and not care about congestion then UDP is your best bet
    - will only work if there is not a lot of traffic
- most apps use TCP (mail, remote access, web, file tranfer) and some use either (streaming, video/online call)

#### Securing TCP
- tcp and udp have no encryption
- SSL sits between app layer and transport layer
    - takes info from HTTP and secuely sends it to tcp layer
    - encrypts data
    - denoted by lock sign in browser window (HTTPS = HTTP + SSL)

### Web and HTTP
- web is a network of computers with specialzed web service available
- http is the protocol that makes this service possible (defines rules for www)
- webpage consists of objects
    - html file, jpeg, java applets, audio files..
    - webpage is identified by URL (server host + path to obejct)

#### HTTP overview
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

### Types of HTTP

#### Non-Persistant HTTP
- when you requeest a new document, a new TCP connection is made
- all audio/video/image files are independent objects
- separate requests are made for each object
- new TCP connection for each object

#### Persistent HTTP
- keeps TCP connection open
- multiple objects can be sent over one TCP connection
- this is the default in the current model of HTTP

#### Response Time
- RTT 
    - time for a small packet to travel from client to server and back (round trip time)
    - can never be preciely measured because factors such as network congestion affects the value
- RTT = time from TCP request initiation to file request
- RTT = time from file request to when the file is received
- the two steps above are assumed to have the same RTT
- depending on file size, the RTT will vary
- 2RTT + file transmission time = non-persistant HTTP response time
    - 2RTT means more overhead

### HTTP Status Codes
- 1st line in server-to-client response message
- 200 - OK
- 301 - moved permanently
    - new location specified later in msg
    - sometimes do automatic redirection
- 400 - bad request
- 404 - not found

#### Trying out HTTP
1. Telnet
    - command prompt utility (network based)
    - allows remote connection to machines
    - `telnet url port_number`
    - one of the default original services of internet
2. type in a GET HTTP request
    - `GET /page HTTP/1.1 Host: base_url`

### Cookies
- small text-based pieces of info stored on the client side in a small file
- server sends client a message saying they want to store cookies
- the browser checks to see if client has cookies enabled
- if yes then some information is stored in some text file locally
- next time you visit the same url the browser will look for a cookie file

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

### Electronic Mail servers
- client sends a request and server responds

#### Mail Access Protocols
- SMTP
- mail access protocol
    - IMAP
    - POP
    - HTTP (browser email - gmail, Hotmail)
- tunneling
    - messages of one protocol can be sent through another protocol

#### POP3
- pull new mail messages every 10 seconds

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