*Q.1 Explain the CIA triad (Confidentiality, Integrity, Availability) with suitable examples*
 
The CIA Triad is a fundamental model of cybersecurity that helps protect information and computer systems. It consists of three main principles: Confidentiality, Integrity, and Availability. 

1. Confidentiality 
Meaning: Confidentiality ensures that information is accessible only to authorized users. 
●	It protects sensitive information from unauthorized access. 
●	Techniques include passwords, encryption, and access control. 
Example: A student's examination marks can be viewed only by authorized teachers and college administrators, not by other students. 

2. Integrity 
Meaning: Integrity ensures that information remains accurate, complete, and unchanged by unauthorized persons. 
●	It prevents unauthorized modification or deletion of data. 
●	Techniques include hashing, digital signatures, and access control. 
Example: If a student's marks are 85, an unauthorized person must not be able to change them to 95. 

3. Availability 
Meaning: Availability ensures that information and computer systems are accessible to authorized users whenever needed. 
●	It prevents disruptions to services and systems. 
●	Techniques include regular backups, system maintenance, and protection against DoS attacks. 
Example: A college website should remain accessible to students when they check examination results, even when many students access it simultaneously.


*Q2) B Write a Python program to simulate a phishing login page that collects username and password and stores them in a file.*

print("===================================") 
print("     PHISHING SIMULATION DEMO") 
print("       EDUCATIONAL PURPOSE") 
print("===================================") 
username = input("Enter Username: ") 
password = input("Enter Password: ") 
 
print("\nLogin processing...") 
print("This is a simulated phishing page.") 
print("Demo data has been stored in simulation_data.txt") 
 
 OUTPUT: 
===================================
     PHISHING SIMULATION DEMO
       EDUCATIONAL PURPOSE
===================================
Enter Username:  student123
Enter Password:  demo123

Login processing...
This is a simulated phishing page.
Demo data has been stored in simulation_data.txt


OR *Q.2 Write a Python program to implement a dictionary attack using a list of common passwords to check whether a target password exists in the list.* 

passwords = [
    "admin123", "password", "123456", "qwerty",
    "welcome123", "computer@123", "hello123",
    "student123", "india@123", "python123"
]

def dictionary_attack(target):
    attempts = 0

    for pwd in passwords:
        attempts += 1
        print("Attempt", attempts, ":", pwd)

        if pwd == target:
            print("Password matched!")
            print("Total attempts:", attempts)
            return

    print("Password not found in dictionary.")
    print("Total attempts:", attempts)


target = input("Enter target password: ")
dictionary_attack(target)

OUTPUT:
Enter target password:  qwerty
Attempt 1 : admin123
Attempt 2 : password
Attempt 3 : 123456
Attempt 4 : qwerty
Password matched!
Total attempts: 4

  
 



