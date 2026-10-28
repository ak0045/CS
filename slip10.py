## Q1 (A): Compare AES with RSA and Explain Key AES Applications

1. Difference Between AES and RSA

| Basis           | AES                                                       | RSA                                                                                      |
| --------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| 1. Full Form    | Advanced Encryption Standard                              | Rivest–Shamir–Adleman                                                                    |
| 2. Type         | Symmetric encryption                                      | Asymmetric encryption                                                                    |
| 3. Keys         | Same secret key for encryption and decryption             | Public key and private key                                                               |
| 4. Key Size     | 128, 192, or 256 bits                                     | Commonly 2048 or 3072 bits                                                               |
| 5. Speed        | Very fast                                                 | Slower than AES                                                                          |
| 6. Security     | Secure with a suitable mode and proper key management     | Security depends on the difficulty of factoring large numbers and correct implementation |
| 7. Key Sharing  | Secret key must be shared securely                        | Public key can be shared openly                                                          |
| 8. Applications | File encryption, disk encryption, and database protection | Digital signatures, key establishment, and public-key encryption                         |

## 2. Key Applications of AES
AES (Advanced Encryption Standard) is widely used to protect sensitive data because it provides strong security and fast encryption.
1. **File and Folder Encryption:** AES protects confidential documents and files from unauthorized access.
2. **Disk Encryption:** It protects data stored on laptops, computers, and external storage devices.
3. **Network Security:** AES is used in secure communication protocols and VPNs to protect transmitted data.
4. **Wireless Security:** AES is used in modern Wi-Fi security standards, including WPA2 and WPA3.
5. **Database Security:** AES encrypts sensitive information, such as personal records and financial data.
6. **Cloud Security:** AES helps protect files and backups stored in cloud services.
7. **Mobile Applications:** AES can protect sensitive information stored locally by mobile applications.

## 3. Conclusion
AES is a fast symmetric encryption algorithm suitable for encrypting large amounts of data. RSA is an asymmetric cryptographic algorithm that uses public and private keys 
for operations such as digital signatures and key establishment. In practice, both algorithms can be used together: RSA can help establish or protect a secret key, while AES encrypts the actual data.
__________________________________________________________________________________________________________________________________________________________________________________________________________________
## Q2) B Write a Python program to perform secure message communication using AES encryption and decryption 

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key = get_random_bytes(16)

print("----- SENDER -----")

message = input("Enter message: ")

cipher = AES.new(key, AES.MODE_GCM)

ciphertext, tag = cipher.encrypt_and_digest(message.encode())

print("Encrypted Message:", ciphertext.hex())

print("\n----- RECEIVER -----")

decipher = AES.new(
    key,
    AES.MODE_GCM,
    nonce=cipher.nonce
)

decrypted_message = decipher.decrypt_and_verify(
    ciphertext, tag
)

print("Decrypted Message:", decrypted_message.decode())

----- SENDER -----
Enter message: Hello World
Encrypted Message: [encrypted hexadecimal data]

----- RECEIVER -----
Decrypted Message: Hello World
________________________________________________________________________________________________________________________________________________________________________________________________________________

OR  
## Q2) B Write a Python program to generate MD5, SHA-1, and SHA-256  hashes of a file and verify its integrity. 

import hashlib

original_file = input("Enter original file name: ")
check_file = input("Enter file to verify: ")

f = open(original_file, "rb")
data1 = f.read()
f.close()

f = open(check_file, "rb")
data2 = f.read()
f.close()

md5_1 = hashlib.md5(data1).hexdigest()
sha1_1 = hashlib.sha1(data1).hexdigest()
sha256_1 = hashlib.sha256(data1).hexdigest()

md5_2 = hashlib.md5(data2).hexdigest()
sha1_2 = hashlib.sha1(data2).hexdigest()
sha256_2 = hashlib.sha256(data2).hexdigest()

print("\nOriginal File:")
print("MD5    :", md5_1)
print("SHA-1  :", sha1_1)
print("SHA-256:", sha256_1)

print("\nFile to Verify:")
print("MD5    :", md5_2)
print("SHA-1  :", sha1_2)
print("SHA-256:", sha256_2)

if md5_1 == md5_2 and sha1_1 == sha1_2 and sha256_1 == sha256_2:
    print("\nFile Integrity Verified")
    print("File is not modified.")
else:
    print("\nFile Integrity Failed")
    print("File is modified.")

SAMPLE OUTPUT
Enter original file name: original.txt
Enter file to verify: copy.txt

Original File:
MD5    : 5d41402abc4b2a76b9719d911017c592
SHA-1  : aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
SHA-256: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

File to Verify:
MD5    : 5d41402abc4b2a76b9719d911017c592
SHA-1  : aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
SHA-256: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824

File Integrity Verified
File is not modified.
