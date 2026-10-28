## Q1 (A): Define Steganography and Distinguish It Clearly from Cryptography. (8 Marks)

1. Definition of Steganography
Steganography is the technique of hiding secret information inside an ordinary file, such as an image, audio, video, or text file, so that the existence of the secret message remains hidden.

Example: Hiding a secret message inside a photograph and sending the photograph to another person.


2. Definition of Cryptography
Cryptography is the technique of converting readable information (plaintext) into an unreadable form (ciphertext) to protect it from unauthorized access.

Example: Converting the message HELLO into an encrypted message such as KHOOR using a Caesar cipher with a key of 3.

3. Difference Between Steganography and Cryptography

Basis	                                                        Steganography	                                                                                 Cryptography
1. Main                                             Purpose	Hides the existence of a message.	                                              Hides the meaning of a message.
2. Technique	                                      Secret data is embedded inside an ordinary file.	                                      Data is converted into ciphertext using an algorithm.
3. Appearance	                                      The carrier file may look normal.	                                                      The encrypted message may look unreadable or meaningless.
4. Media                                            Used	Uses images, audio, videos, or text as carriers.	                                Uses encryption algorithms and keys.
5. Goal	                                            Conceals the existence of communication.	                                              Protects information from unauthorized reading.
6. Example	                                        Hiding a message inside an image.	                                                      Encrypting a message using AES.
7. Security	                                        The hidden message may be readable if discovered, unless separately encrypted.	        The message generally remains unreadable without the required decryption key.
8. Detection or Attack	                            Detection focuses on finding hidden information.	                                      Attacks may attempt to break the encryption or obtain the key.

4. Simple Diagram

Steganography:

Secret Message + Image
          |
          v
  Steganography Process
          |
          v
Image Containing Hidden Message


Cryptography:

Plaintext: HELLO
      |
      v
Encryption (Key = 3)
      |
      v
Ciphertext: KHOOR


5. Conclusion
Steganography hides the existence of a secret message, whereas cryptography hides the meaning of a message. Both techniques help protect information, and they can also be used
together for stronger security.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Q2 (B): Write a Python Program That Accepts a Sentence from the User and Encrypts It Using Caesar Cipher.

text = input("Enter a sentence: ")
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
Sample Output
Enter a sentence: Hello World
Enter key: 3
Encrypted text: Khoor Zruog
______________________________________________________________________________________________________________________________________________________________________________________________________________

OR
Q2 (B): Write a Python Program to Implement a Dictionary Attack Using a List of Common Passwords to Check Whether a Target Password Exists in the List.

def dictionary_attack(target):
    passwords = [
        "admin123",
        "password",
        "123456",
        "qwerty",
        "welcome123",
        "computer@123",
        "hello123",
        "student123",
        "india@123",
        "python123"
    ]

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


Sample Output 1: Password Found
Enter target password: qwerty
Attempt 1 : admin123
Attempt 2 : password
Attempt 3 : 123456
Attempt 4 : qwerty
Password matched!
Total attempts: 4

Sample Output 2: Password Not Found
Enter target password: mysecurepass
Attempt 1 : admin123
Attempt 2 : password
Attempt 3 : 123456
Attempt 4 : qwerty
Attempt 5 : welcome123
Attempt 6 : computer@123
Attempt 7 : hello123
Attempt 8 : student123
Attempt 9 : india@123
Attempt 10 : python123
Password not found in dictionary.
Total attempts: 10
