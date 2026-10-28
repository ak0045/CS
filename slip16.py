## Q1 (A): Describe the Different Types of Distributed Denial of Service (DDoS) Flooding Attacks. 

### 1. Definition
A Distributed Denial of Service (DDoS) attack is a cyberattack in which multiple compromised computers or devices send a large amount of traffic to a target server or network 
to make its services unavailable to legitimate users.

### 2. Types of DDoS Flooding Attacks

1. SYN Flood Attack
* The attacker sends a large number of TCP SYN requests to the target server.
* The server waits for the connections to complete.
* Many incomplete connections consume server resources.
* Genuine users may be unable to establish connections.

2. UDP Flood Attack
* The attacker sends a large number of User Datagram Protocol (UDP) packets to the target.
* The server spends resources processing the packets.
* This can overload the target system and reduce service availability.

3. ICMP Flood Attack
* The attacker sends a large number of Internet Control Message Protocol (ICMP) packets, such as ping requests.
* The target consumes network bandwidth and processing resources handling the packets.
* Legitimate network traffic may be delayed or blocked.

4. HTTP Flood Attack
* The attacker sends a large number of HTTP requests to a web server.
* The server attempts to process the requests and generate responses.
* CPU, memory, and application resources may become overloaded.
* The website becomes slow or unavailable.

5. DNS Amplification Attack
* The attacker abuses publicly accessible DNS servers to send large responses toward a victim.
* The victim receives more traffic than the attacker directly sends.
* This can consume the victim's bandwidth and disrupt network services.

6. SYN-ACK or TCP Flooding**
* The target receives excessive TCP traffic, including SYN-ACK packets.
* The system must process and filter the incoming packets.
* The resulting traffic can consume network and processing resources.

7. Volumetric Flooding Attack
* The attacker generates a very large volume of traffic from multiple devices.
* The victim's network bandwidth becomes saturated.
* Legitimate users cannot access the service.

### 3. Working of a DDoS Attack

1. The attacker gains control of multiple compromised devices, often called a botnet.
2. These devices send traffic toward the target simultaneously.
3. The target receives more traffic than it can handle.
4. Network bandwidth or server resources become exhausted.
5. Legitimate users experience slow service or complete service disruption.

Prevention of DDoS Attacks:
* Use firewalls and intrusion prevention systems.
* Apply traffic filtering and rate limiting.
* Use DDoS protection services and traffic scrubbing.
* Monitor network traffic for unusual patterns.
* Configure servers and network infrastructure to handle traffic spikes.

Conclusion

DDoS flooding attacks attempt to make online services unavailable by overwhelming their bandwidth or resources. Common types include SYN, UDP, ICMP, HTTP, DNS 
amplification, and volumetric flooding attacks. Proper traffic filtering, monitoring, and DDoS protection help reduce their impact.
_________________________________________________________________________________________________________________________________________________________________________________________________________________

## Q2 (B): Write a Program Using Both ord() and chr() Functions for Caesar Cipher

text = input("Enter a message: ")
key = int(input("Enter key: "))
enc = ""

for ch in text:
    if ch.isalpha():
        enc = enc + chr((ord(ch.upper()) - 65 + key) % 26 + 65)
    else:
        enc = enc + ch
print("Encrypted message:", enc)

OUTPUT
Enter a message:  hello
Enter key:  2
Encrypted message: JGNNQ
___________________________________________________________________________________________________________________________________________________________________________________________________________________

OR
## Q2 (B): Write a Program to Implement the RSA Algorithm (Generate Public and Private Keys, Encrypt a Message, and Decrypt It)
p = 3
q = 11

n = p * q
phi = (p - 1) * (q - 1)

e = 7
d = 3

print("Public key:", e, n)
print("Private key:", d, n)

M = int(input("Enter message number (0 to 32): "))

C = (M ** e) % n
print("Encrypted message:", C)

M = (C ** d) % n
print("Decrypted message:", M)

OUTPUT
Public key: 7 33
Private key: 3 33
Enter message number (0 to 32): 5
Encrypted message: 14
Decrypted message: 5
