## Q1) A) Describe the Different Types of Distributed Denial of Service (DDoS) Flooding Attacks. (8 Marks)

Definition
A Distributed Denial of Service (DDoS) attack is a cyberattack in which multiple compromised computers or devices send a large amount of traffic to a target server or network,
making its services unavailable to legitimate users.

Types of DDoS Flooding Attacks

1. SYN Flood Attack
The attacker sends a large number of TCP SYN requests to a server.
The server waits for connections to be completed.
Incomplete connections consume server resources.
Legitimate users may be unable to connect.

2. UDP Flood Attack
The attacker sends a large number of UDP packets to the target.
The server spends resources processing these packets.
Network bandwidth and system resources become overloaded.
Legitimate users may experience service disruption.

3. ICMP Flood Attack
The attacker sends a large number of ICMP packets, such as ping requests.
The target spends resources processing or responding to them.
Network bandwidth may become exhausted.
The service may become slow or unavailable.

4. HTTP Flood Attack
The attacker sends a large number of HTTP requests to a website.
The server attempts to process every request.
CPU and memory resources become overloaded.
The website may become slow or unavailable.

5. DNS Amplification Attack
The attacker misuses publicly accessible DNS servers to direct large responses toward a victim.
The victim receives much more traffic than the attacker directly sends.
Network bandwidth becomes overloaded.
Legitimate network communication is disrupted.

6. TCP Flood Attack
The attacker generates excessive TCP traffic toward the target.
The target must process incoming packets and connections.
Network and server resources become exhausted.
Genuine users may lose access to the service.

7. Volumetric Flooding Attack
Multiple compromised devices send huge amounts of traffic to the victim.
The traffic consumes available network bandwidth.
Legitimate data cannot reach the target properly.
Network services may become unavailable.

Prevention of DDoS Attacks:
Use firewalls and intrusion prevention systems.
Apply traffic filtering and rate limiting.
Use reliable DDoS protection services.
Monitor unusual network traffic.
Configure servers to handle sudden increases in traffic.

Conclusion
DDoS flooding attacks attempt to make online services unavailable by overwhelming network bandwidth or system resources. SYN, UDP, ICMP, HTTP, DNS amplification, 
TCP, and volumetric flooding are common types. Proper filtering, monitoring, and DDoS protection help reduce their impact.
________________________________________________________________________________________________________________________________________________________________________________________________________________

## Q2) B) Option 1: Write a Python Program to Detect Spam Emails Using Predefined Keywords.

email = input("Enter email message: ")

keywords = ["win", "free", "prize", "offer", "lottery"]

email = email.lower()
spam = False

for word in keywords:
    if word in email:
        spam = True

if spam:
    print("Spam Email")
else:
    print("Not a Spam Email")

SAMPLE OUTPUT
Enter email message: You have won a free prize
Spam Email

Enter email message: Hello, how are you?
Not a Spam Email
_______________________________________________________________________________________________________________________________________________________________________________________________________________________

## Q2) B) Option 2: Write a Python Program to Display ASCII Values of Characters Before Encryption.

text = input("Enter a message: ")

print("Characters and ASCII values:")

for ch in text:
    print(ch, "=", ord(ch))

OUTPUT
Enter a message: CAT
Characters and ASCII values:
C = 67
A = 65
T = 84
