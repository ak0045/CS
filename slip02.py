## Q1 Differences Between Virus, Worm, and Trojan Horse

| Basis                 | Virus                                                  | Worm                                               | Trojan Horse                                                    |
| --------------------- | ------------------------------------------------------ | -------------------------------------------------- | --------------------------------------------------------------- |
| 1. Definition         | Malware that attaches to a file or program.            | Malware that replicates and spreads independently. | Malware disguised as legitimate software.                       |
| 2. Host Requirement   | Requires a host file or program.                       | Does not require a host file.                      | Usually exists as a standalone program.                         |
| 3. Replication        | Replicates by infecting other files.                   | Replicates automatically.                          | Does not usually self-replicate.                                |
| 4. Spreading Method   | Through infected files, USB drives, or downloads.      | Through networks and vulnerable systems.           | Through deceptive downloads, attachments, or applications.      |
| 5. User Interaction   | Often requires execution of an infected file.          | Can spread without direct user action.             | Usually requires the user to install or run it.                 |
| 6. Main Purpose       | Infect files and potentially damage data.              | Spread rapidly and disrupt systems or networks.    | Trick users and perform malicious activities.                   |
| 7. Speed of Spreading | Depends on file sharing and execution.                 | Can spread rapidly across networks.                | Depends mainly on user installation or execution.               |
| 8. System Impact      | May corrupt, modify, or delete files.                  | May consume bandwidth and system resources.        | May steal data or enable unauthorized access.                   |
| 9. Detection          | Detected through antivirus scanning and file analysis. | Detected through antivirus and network monitoring. | Detected through antivirus and suspicious application analysis. |
| 10. Example           | File-infecting virus (e.g., CIH virus)                 | Conficker worm                                     | Fake antivirus containing malware                               |

##Q.2B Write a Python program to detect spam emails using predefined keywords. 

  spam_keywords = [
    "win",
    "winner",
    "free",
    "prize",
    "lottery",
    "urgent",
    "offer",
    "click here",
    "claim",
    "money",
    "congratulations"
]

email = input("Enter the email message: ")
email_lower = email.lower()

spam_words_found = []

for keyword in spam_keywords:
    if keyword in email_lower:
        spam_words_found.append(keyword)

print("\n---------- Result ----------")

if len(spam_words_found) >= 2:
    print("Email Status: SPAM")
    print("Spam keywords found:", spam_words_found)
else:
    print("Email Status: NOT SPAM")
    print("Spam keywords found:", spam_words_found)

print("----------------------------")

OUTPUT:
Enter the email message: Congratulations! You won a free prize. Click here to claim your money.

---------- Result ----------
Email Status: SPAM
Spam keywords found: ['free', 'prize', 'click here', 'claim', 'money', 'congratulations']
----------------------------


OR 
 
Q2) B Write a Python program to encrypt user input text using AES encryption  

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

plaintext = input("Enter the plaintext: ")

key = b"1234567890123456"

cipher = AES.new(key, AES.MODE_ECB)

data = pad(plaintext.encode(), AES.block_size)

encrypted_text = cipher.encrypt(data)

print("Original Text :", plaintext)
print("Encrypted Text:", encrypted_text.hex())


OUTPUT:
Enter the plaintext:  Hello World
Original Text : Hello World
Encrypted Text: c50017562e7683ec13ef1a15374f2cb1




 

