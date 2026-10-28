Q1 (A): What Is Digital Evidence? Explain the Role and Purpose of Write Blockers, FTK Imager, and EnCase Imager in Forensic Acquisition.

1. Digital Evidence
Digital evidence is any information stored or transmitted in digital form that can be used during an investigation or in a court of law.

Examples:
* Emails and chat messages
* Computer files and documents
* Browser history
* Call logs and mobile data
* Images, videos, and network logs

2. Write Blocker
A write blocker is a hardware or software tool that prevents data from being written to a digital storage device during forensic examination.

Role and Purpose:
  1.Prevents accidental modification of the original evidence.
  2.Allows investigators to read data without changing it.
  3.Maintains the integrity and reliability of digital evidence.
  4.Helps preserve the original storage device for investigation.

Example: Connecting a suspect's hard disk through a hardware write blocker before creating a forensic image.

3. FTK Imager
FTK Imager is a digital forensic tool used to create forensic images and examine digital evidence.

Role and Purpose:
1.Creates forensic copies of hard disks, USB drives, and other supported media.
2.Allows investigators to preview files and folders.
3.Supports examination of deleted files and file-system information where available.
4.Can calculate hash values, such as MD5 and SHA-1, to help verify data integrity.
5.Saves forensic images in supported formats, such as E01 and raw formats.

Example: Creating a forensic image of a USB drive and calculating its hash value to help verify the image.

4. EnCase Imager
EnCase Imager is a forensic acquisition tool associated with EnCase forensic products. It is used to acquire and preserve digital evidence for further examination.

Role and Purpose:
1.Creates forensic images of hard disks and other supported storage media.
2.Supports acquisition of digital evidence while preserving the original source.
3.Helps verify acquired data using hash values.
4.Records acquisition-related information for documentation.
5.Produces forensic image files that can be examined using compatible forensic tools.

Example: Creating a forensic image of a suspect's hard disk for later analysis in a digital investigation.

6. Importance in Digital Forensics
  * Integrity: Helps ensure evidence remains unchanged.
  * Accuracy: Creates forensic copies for examination.
  * Verification: Hash values help detect changes to acquired data.
  * Documentation: Acquisition records support the chain of custody.
  * Legal Reliability: Proper procedures help establish the authenticity and reliability of evidence.
_________________________________________________________________________________________________________________________________________________________________________________________________________________

Q2) B Write a Python program that accepts a sentence from the user and encrypts it using Caesar Cipher

text = input("Enter a sentence: ")
key = int(input("Enter key: "))
enc = ""

for ch in text:
    if ch.isalpha():
        enc = enc + chr((ord(ch.upper()) - 65 + key) % 26 + 65)
    else:
        enc = enc + ch

print("Encrypted text:", enc)

OUTPUT
Enter a sentence: HELLO WORLD
Enter key: 3
Encrypted text: KHOOR ZRUOG
________________________________________________________________________________________________________________________________________________________________________________________________________________

Q2) B Write a program to implement RSA algorithm.(Generate public and private keys, encrypt a message, and decrypt it.) 

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
