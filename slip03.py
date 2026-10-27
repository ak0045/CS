Q1 (A): What is Phishing? Explain the Step-by-Step Algorithm to Identify Phishing Emails.

1. Definition of Phishing
Phishing is a type of cyberattack in which an attacker sends fake emails, messages, or websites that appear to come from a trusted organization to trick users into revealing
sensitive information such as passwords, bank details, OTPs, or credit card numbers.

Example: A user receives an email claiming to be from a bank that says, "Your account will be blocked. Click here to verify your details." The link opens a fake website designed 
to steal the user's banking credentials.

2. Step-by-Step Algorithm to Identify Phishing Emails
Algorithm: Identify_Phishing_Email

Step 1: Start.
Step 2: Receive the email and examine the sender's email address.
Step 3: Check whether the sender's address or domain is suspicious or different from the official organization's domain.
Step 4: Examine the subject line and message for urgent or threatening language, such as "Your account will be blocked immediately."
Step 5: Check whether the email asks for sensitive information such as passwords, OTPs, or banking details.
Step 6: Inspect links without opening them. Check whether the displayed link matches the actual destination and official website.
Step 7: Check for unexpected attachments, especially executable files or suspicious documents.
Step 8: Look for spelling mistakes, grammatical errors, and unusual formatting.
Step 9: Determine the result:
         If several suspicious signs are present, classify the email as potentially phishing.
         Otherwise, classify it as no obvious phishing indicators found.
Step 10: Report the suspicious email to the IT or security team and delete it if appropriate. Verify important requests through an official communication channel.
Step 11: Stop.

3. Example
Consider the following email:
subject: Urgent! Your bank account will be blocked today.
Message: Click the link below and enter your account number, password, and OTP to reactivate your account.

Suspicious Indicators:
1.Creates urgency and fear.
2.Requests sensitive banking information.
3.May contain a fake website link.
4.Uses a threatening message to force immediate action.

Result: The email should be treated as potentially phishing. Do not click the link or provide any information.

4. Prevention Measures
Never share passwords or OTPs through email links.
Verify the sender's email address carefully.
Avoid clicking suspicious links or downloading unexpected attachments.
Use spam filters and updated security software.
Enable multi-factor authentication (MFA).


Q2) B Write a Python program to shift each alphabet by 2 positions. 

text = input("Enter a message: ")
result = ""

for ch in text:
    if ch.isalpha():
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + 2) % 26 + ord('A'))
        else:
            result += chr((ord(ch) - ord('a') + 2) % 26 + ord('a'))
    else:
        result += ch

print("Encrypted message:", result)


OUTPUT:
Enter a message: Hello World
Encrypted message: Jgnnq Yqtnf


OR 
 
Q2) B Write a Python program to simulate a phishing login page for educational purposes.  

print("================================")
print("           LOGIN PAGE")
print("     EDUCATIONAL SIMULATION")
print("================================")

correct_username = "student"
correct_password = "12345"

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == correct_username and password == correct_password:
    print("\nLogin Successful!")
    print("This is only a simulation.")
else:
    print("\nLogin Failed!")
    print("Invalid Username or Password.")

print("\n--- Security Awareness ---")
print("Do not enter your password on unknown websites.")
print("Always check the website address.")

OUTPUT:
================================
           LOGIN PAGE
     EDUCATIONAL SIMULATION
================================
Enter Username: student
Enter Password: 12345

Login Successful!
This is only a simulation.

--- Security Awareness ---
Do not enter your password on unknown websites.
Always check the website address.


 
