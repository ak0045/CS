## Q1 (A): Define Denial of Service (DoS) Attack and Explain Its Working Principles Along with SYN Flood and HTTP Flood Attack Types.

1. Definition of DoS Attack
A Denial of Service (DoS) attack is a cyberattack in which an attacker sends a large number of requests or unwanted traffic to a server or network to make its services unavailable to legitimate users.

2. Working Principle of DoS Attack
The attacker targets a server or website.
The attacker sends a large number of requests to the target.
The server's resources, such as memory, CPU, or connection capacity, become overloaded.
The server becomes slow or stops responding.
Genuine users cannot access the service.

3. Types of DoS Attacks

A. SYN Flood Attack: 
A SYN flood is a type of DoS attack that misuses the TCP connection establishment process.

Working:
The attacker sends many TCP SYN requests to the server.
The server responds with SYN-ACK messages.
The attacker does not complete the TCP handshake by sending the final ACK.
The server keeps waiting for these connections to complete.
The server's connection queue fills up, preventing genuine users from connecting.

Example: A website cannot accept new connections because its connection queue is filled with incomplete TCP connections.

B. HTTP Flood Attack
An HTTP flood is a type of DoS attack in which an attacker sends a large number of HTTP requests to a web server.

Working:
The attacker sends repeated HTTP requests to a website.
The server attempts to process each request.
The server uses excessive CPU, memory, or processing capacity.
The website becomes slow or unavailable.
Genuine users experience delays or cannot access the website.

Example: An online shopping website becomes unavailable because it receives an unusually large number of requests to load pages.

4. Prevention of DoS Attacks
Use firewalls to filter suspicious traffic.
Apply rate limiting to restrict excessive requests.
Use IDS/IPS tools to detect malicious traffic.
Use SYN flood protection and connection timeouts.
Use a Web Application Firewall (WAF) to help filter HTTP floods.

5. Conclusion
A DoS attack makes a service unavailable by exhausting its resources. A SYN flood targets TCP connection handling, whereas an HTTP flood overloads a web server with HTTP requests.
Security controls and traffic monitoring help reduce these attacks.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  
## Q2 (B): Write a Python Program Using Scapy to Detect a Possible DoS Attack by Counting Packets Received from Each IP Address and Generating an Alert When Traffic Exceeds a Threshold.

from scapy.all import sniff, IP
from collections import defaultdict
import time

packet_counts = defaultdict(int)
start_time = time.time()

THRESHOLD = 100
TIME_WINDOW = 1


def report_traffic():
    global packet_counts

    print("\n--- Traffic Report ---")

    if not packet_counts:
        print("No IP packets observed.")
    else:
        for ip, count in sorted(
            packet_counts.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print(f"IP Address: {ip} | Packets: {count}")

            if count > THRESHOLD:
                print("ALERT: Possible DoS attack from", ip)

    packet_counts.clear()


def detect(packet):
    global start_time

    current_time = time.time()

    if current_time - start_time >= TIME_WINDOW:
        report_traffic()
        start_time = current_time

    if IP in packet:
        source_ip = packet[IP].src
        packet_counts[source_ip] += 1


print("Monitoring network traffic...")
print("Threshold:", THRESHOLD, "packets per second")
print("Press Ctrl+C to stop.")

try:
    sniff(prn=detect, store=False)

except KeyboardInterrupt:
    report_traffic()
    print("Monitoring stopped.")


Sample Output

The following is an illustrative example of what the program might display:

Monitoring network traffic...
Threshold: 100 packets per second
Press Ctrl+C to stop.

--- Traffic Report ---
IP Address: 192.168.1.10 | Packets: 125
ALERT: Possible DoS attack from 192.168.1.10
IP Address: 192.168.1.20 | Packets: 45
Monitoring stopped.

Required Library
Install Scapy using:
pip install scapy

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


OR
## Q2 (B): Write a Python Program to Implement Caesar Cipher for Both Encryption and Decryption of a Given Text.

text = input("Enter text: ")
key = int(input("Enter key: "))

enc = ""

for ch in text:
    if ch.isupper():
        enc += chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
    elif ch.islower():
        enc += chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    else:
        enc += ch

print("Encrypted text:", enc)

dec = ""

for ch in enc:
    if ch.isupper():
        dec += chr((ord(ch) - ord('A') - key) % 26 + ord('A'))
    elif ch.islower():
        dec += chr((ord(ch) - ord('a') - key) % 26 + ord('a'))
    else:
        dec += ch

print("Decrypted text:", dec)


Sample Output
Enter text: Hello World
Enter key: 3
Encrypted text: Khoor Zruog
Decrypted text: Hello World
