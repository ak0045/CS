Q1) A) What Is Phishing? Explain the Step-by-Step Algorithm to Identify Phishing Emails. (8 Marks)

Definition of Phishing
Phishing is a type of cyberattack in which an attacker sends fake emails or messages pretending to be a trusted organization, such as a bank, to steal sensitive information 
like passwords, OTPs, bank details, and credit card numbers.

Example: An attacker sends an email saying, “Your bank account will be blocked. Click here to update your account details.” The link opens a fake banking website that attempts to steal the user's information.

Step-by-Step Algorithm to Identify Phishing Emails

Algorithm: Identify_Phishing_Email
Step 1: Start.
Step 2: Receive the email from the sender.
Step 3: Check the sender's email address. If the address is suspicious or different from the official address, mark it as suspicious.
Step 4: Check the subject line. If it contains urgent or threatening words such as "Account Blocked," "Urgent Action," or "Verify Now," increase suspicion.
Step 5: Check the email content for spelling mistakes, grammatical errors, and requests for passwords, OTPs, or banking details.
Step 6: Check the links in the email. If a link leads to an unknown or suspicious website, mark the email as suspicious. Do not click the link.
Step 7: Check attachments. If an unexpected attachment is received, especially an executable file, do not open it.
Step 8: If multiple suspicious signs are found, classify the email as a potential phishing email. Otherwise, classify it as not identified as phishing and continue to exercise caution.
Step 9: Report the suspicious email to the email service provider or IT administrator.
Step 10: Stop.

Common Signs of Phishing Emails
    Unknown or fake sender address.
    Urgent or threatening language.
    Suspicious links or fake websites.
    Spelling and grammatical mistakes.
    Requests for passwords, OTPs, or bank details.
    Unexpected or suspicious attachments.

Conclusion
Phishing emails can be identified by carefully checking the sender, subject, message content, links, and attachments. Users should never share confidential information through suspicious emails.
________________________________________________________________________________________________________________________________________________________________________________________________________________

Q2) B) Option 1: Write a Python Program to Hide a Text Message Inside an Image and Display the Hidden Message Again.
Program

from PIL import Image
import stepic

def hide_data():
    image_name = input("Enter the original image name: ")
    img = Image.open(image_name)

    secret_msg = input("Enter the secret message: ")
    data = secret_msg.encode("utf-8")

    stego_img = stepic.encode(img, data)

    output_name = input("Enter name for stego image (use .png): ")
    stego_img.save(output_name, format="PNG")

    print("Message successfully hidden!")
    print("Stego image:", output_name)

def retrieve_data():
    image_name = input("Enter the stego image name: ")
    stego_img = Image.open(image_name)

    decoded_data = stepic.decode(stego_img)
    print("Retrieved Message:", decoded_data.decode("utf-8"))

hide_data()
retrieve_data()

Sample Output
Enter the original image name: image.png
Enter the secret message: Hello World
Enter name for stego image (use .png): secret.png
Message successfully hidden!
Stego image: secret.png
Enter the stego image name: secret.png
Retrieved Message: Hello World
__________________________________________________________________________________________________________________________________________________________________________________________________________________

OR
Q2) B) Option 2: Write a Python Program to Simulate a Phishing Login Page for Educational Purposes.

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
print("Always check the website address before logging in.")
print("Never share your password or OTP with others.")


###### Sample Output 1: Successful Login
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
Always check the website address before logging in.
Never share your password or OTP with others.


###### Sample Output 2: Failed Login
Enter Username: user
Enter Password: 11111

Login Failed!
Invalid Username or Password.

--- Security Awareness ---
Do not enter your password on unknown websites.
Always check the website address before logging in.
Never share your password or OTP with others.
