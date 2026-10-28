Q1 (A): What Specific Digital Evidence Can Be Obtained from Browser History Analysis in Digital Forensics?
Browser History Analysis in Digital Forensics

1. Introduction
Browser history analysis is a digital forensic technique used to examine web browser records to identify a user's online activities. Investigators analyze browser history, 
cache, cookies, downloads, and related records to collect digital evidence during cybercrime investigations.

2. Digital Evidence Obtained from Browser History Analysis
  1.Visited Websites: Records of websites and URLs visited by the user. These help identify websites accessed during an investigation.
  2.Date and Time of Visits: Timestamps showing when a website was accessed. These help establish a timeline of online activities.
  3.Search History: Records of searches made using search engines. These may provide information about the user's activities relevant to a case.
  4.Downloaded Files: Information about downloaded files, including file names, download locations, source URLs, and download times, when recorded by the browser.
  5.Cookies: Small data files stored by websites that may contain session identifiers, preferences, or tracking information.
  6.Cached Data: Copies of website resources, images, and other content stored temporarily by the browser. These may help reconstruct previously accessed web pages.
  7.Login and Session Evidence: Browser records may reveal evidence of website access and active sessions. Passwords are not necessarily stored or recoverable.
  8.Bookmarks and Saved Pages: Saved website links and web pages that may indicate websites of interest or provide evidence related to an investigation.

3. Importance in Digital Forensics
  1.Helps reconstruct a user's online activity timeline.
  2.May identify access to suspicious or malicious websites.
  3.Can support investigations involving fraud, cyberstalking, or unauthorized access.
  4.Helps correlate browsing activity with other digital evidence.

4. Precautions
Investigators should preserve the original evidence, maintain a proper chain of custody, use forensic tools, and verify findings with other evidence. Browser records may be deleted, 
incomplete, shared between users, or affected by private browsing modes. A browser history entry alone does not prove who performed the activity or establish criminal intent.

5. Conclusion
Browser history analysis provides valuable evidence such as visited URLs, timestamps, search queries, downloads, cookies, and cached content. These records help investigators
reconstruct online activities and support digital forensic investigations.
________________________________________________________________________________________________________________________________________________________________________________________________________

## Q2) B Write a simple Python program to hide a text message inside an image and display the hidden message again. 

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

SAMPLE OUTPUT:
Enter the original image name: original.png
Enter the secret message: Hello World
Enter name for stego image (use .png): secret.png
Message successfully hidden!
Stego image: secret.png
Enter the stego image name: secret.png
Retrieved Message: Hello World

Required libraries:
pip install Pillow stepic
_______________________________________________________________________________________________________________________________________________________________________________________________________

Or 
algorithm given 𝑝 = 3, 𝑞 = 11, and 𝑒 = 7.𝑀 = 5 Q2) B Calculate and encrypt the number  using the RSA  

p = 3
q = 11
e = 7
M = 5

n = p * q

C = (M ** e) % n

print("Public key:", e, n)
print("Original message:", M)
print("Encrypted message:", C)

SAMPLE OUTPUT:
Public key: 7 33
Original message: 5
Encrypted message: 14
