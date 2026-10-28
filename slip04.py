## Q1 (A): Explain Brute Force Attacks with an Example, Detailing Simple, Dictionary, and Hybrid Brute Force Types.

1. Definition of Brute Force Attack
A Brute Force Attack is a cybersecurity attack in which an attacker systematically tries different password combinations or possible keys until the correct one is found.
It is commonly used to guess weak passwords. The time required depends on password length, complexity, the number of possible combinations, and the system's security controls.

Example: If a password is a single digit from 0 to 9, an attacker may try 0, 1, 2, and so on until the correct digit is found.

2. Types of Brute Force Attacks

A. Simple Brute Force Attack

A simple brute force attack tries all possible combinations of characters until the correct password is found.

Working:
Select a possible password combination.
Compare it with the target password.
If it does not match, try another combination.
Repeat until a match is found or all possibilities are exhausted.

Example: For a four-digit numeric password, possible combinations range from 0000 to 9999, giving 10,000 possibilities.

Advantages:
1.Can find the password if the entire search space is explored.
2.Does not depend on knowing common password patterns.

Disadvantages:
1.Can require considerable time and computing resources.
2.Becomes impractical for long, complex passwords.

B. Dictionary Attack
A dictionary attack tries passwords from a predefined list of common passwords, words, and predictable combinations rather than testing every possible combination.

Working:
Prepare a list of likely passwords.
Select a password from the list.
Compare it with the target.
Continue until a match is found or the list ends.

Example: An attacker might try common passwords such as password123, welcome123, and admin123.

Advantages:
Faster than testing every possible combination when users choose common passwords.
Requires fewer attempts when the correct password is in the list.

Disadvantages:
Fails if the password is not included in the dictionary.
Its success depends on the quality of the password list.

C. Hybrid Brute Force Attack
A hybrid brute force attack combines dictionary-based guessing with additional characters, numbers, or symbols added to common passwords.

Working:
Select a common password from a dictionary.
Add likely numbers, symbols, or character variations.
Generate candidate passwords.
Test the candidates until a match is found or the search is exhausted.

Example: Starting with the common word student, possible variations include:
student123
student2026
student@123

Advantages:
Can identify predictable variations of common passwords.
Covers more possibilities than a basic dictionary attack.

Disadvantages:
Requires more attempts than testing the original dictionary alone.
May still fail against long, random passwords.



## Q2 (B): Write a Python Program to Demonstrate IP Tracking Simulation by Storing Fake IP Addresses and Printing Location Mapping Using a Dictionary.

ip_location = {
    "192.168.1.10": {"city": "Pune", "country": "India"},
    "192.168.1.20": {"city": "Mumbai", "country": "India"},
    "10.0.0.5": {"city": "Delhi", "country": "India"},
    "172.16.0.8": {"city": "Nagpur", "country": "India"},
    "192.168.2.15": {"city": "Chennai", "country": "India"}
}

print("Available IP Addresses:")

for ip in ip_location:
    print(ip)

target = input("\nEnter an IP address to track: ")

if target in ip_location:
    print("\nIP Address:", target)
    print("City:", ip_location[target]["city"])
    print("Country:", ip_location[target]["country"])
    print("Tracking Status: Location Found")
else:
    print("IP address not found in database!")

### Sample Output

Available IP Addresses:
192.168.1.10
192.168.1.20
10.0.0.5
172.16.0.8
192.168.2.15

Enter an IP address to track: 192.168.1.10

IP Address: 192.168.1.10
City: Pune
Country: India
Tracking Status: Location Found

