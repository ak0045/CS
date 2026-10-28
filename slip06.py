## Q1 (A): Explain the Key Behaviors of Cyber Stalkers and Discuss the Misuse of Social Networking Features.

Cyber stalking is the repeated use of the internet, social media, email, or other digital technologies to harass, threaten, monitor, or intimidate a person. 
Cyber stalkers may cause emotional stress and create fear in the victim.

2. Key Behaviors of Cyber Stalkers
  1.Repeated Unwanted Messages: Sending continuous messages, emails, or comments even after the victim requests them to stop.
  2.Online Monitoring: Regularly checking the victim's social media profiles, posts, activities, and online status to gather personal information.
  3.Threatening Messages: Sending abusive, frightening, or threatening messages to create fear and mental pressure.
  4.Impersonation: Creating fake accounts using the victim's name, photographs, or personal details to damage their reputation.
  5.Collecting Personal Information: Gathering private details such as phone numbers, home addresses, workplace information, and daily routines.
  6.Spreading False Information: Sharing rumours, edited photographs, or misleading content to embarrass or defame the victim.
  7.Unwanted Contact Through Others: Contacting the victim's friends, relatives, or colleagues to obtain information or continue harassment.
  8.Tracking Online Activities: Misusing location-sharing features, check-ins, or tagged posts to discover the victim's whereabouts.

3. Misuse of Social Networking Features
Social networking platforms provide several features that can be misused by cyber stalkers.
  1.Fake Profiles: Attackers create fake accounts to hide their identity and communicate with victims deceptively.
  2.Private Messaging: Direct messages and chat features may be used to send repeated unwanted, abusive, or threatening messages.
  3.Location Sharing and Check-ins: Location tags and check-ins can reveal a person's current location or regular movements.
  4.5.Photo and Video Sharing: Personal photographs or videos may be copied, edited, or shared without permission to harass or embarrass someone.
  6.Friend Requests and Followers: Attackers may send repeated requests or use fake accounts to gain access to private posts and personal information.
  7.Comments and Public Posts: Comment sections and public posts may be misused to spread rumours, insults, threats, or defamatory content.
  8.Tagging and Mentions: Repeatedly tagging a victim in unwanted posts or offensive content can draw unwanted attention and cause distress.
  9.Personal Information Exposure: Publicly available contact details, workplace information, and family details may be collected and misused for harassment.

    
4. Preventive Measures
    Keep social media accounts private.
    Avoid sharing personal details and live locations publicly.
    Block and report suspicious accounts.
    Use strong passwords and two-factor authentication.
    Save screenshots and other evidence of harassment.
    Inform trusted people and contact the police or appropriate cybercrime authorities when necessary.

5. Conclusion
Cyber stalking is a serious cybercrime that affects a person's privacy, safety, and mental well-being. Misuse of social networking features makes it easier for stalkers to monitor 
and harass victims. Privacy settings, safe online practices, and timely reporting can help reduce cyber stalking.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Q2 (B): Write a Python Program to Check Password Strength: Length ≥ 8 and Password Must Contain Digits and Special Characters.

import string

password = input("Enter your password: ")

length_valid = len(password) >= 8

digit_valid = any(char.isdigit() for char in password)

special_valid = any(char in string.punctuation for char in password)

print("\n----- Password Strength Report -----")

print("Length >= 8:", length_valid)
print("Contains digit:", digit_valid)
print("Contains special character:", special_valid)

if length_valid and digit_valid and special_valid:
    print("\nPassword Strength: STRONG")
else:
    print("\nPassword Strength: WEAK")

    if not length_valid:
        print("- Password must contain at least 8 characters.")

    if not digit_valid:
        print("- Password must contain at least one digit.")

    if not special_valid:
        print("- Password must contain at least one special character.")


Sample Output 1: Strong Password
Enter your password: Hello@123

----- Password Strength Report -----
Length >= 8: True
Contains digit: True
Contains special character: True

Password Strength: STRONG
Sample Output 2: Weak Password
Enter your password: hello

----- Password Strength Report -----
Length >= 8: False
Contains digit: False
Contains special character: False

Password Strength: WEAK
- Password must contain at least 8 characters.
- Password must contain at least one digit.
- Password must contain at least one special character.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  

OR
## Q2 (B): Write a Python Program to Implement Caesar Cipher for Both Encryption and Decryption of a Given Text.

def caesar_cipher(text, shift):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch

    return result


text = input("Enter text: ")
key = int(input("Enter key: "))

enc = caesar_cipher(text, key)
print("Encrypted text:", enc)

dec = caesar_cipher(enc, -key)
print("Decrypted text:", dec)


Sample Output
Enter text: Hello World
Enter key: 3
Encrypted text: Khoor Zruog
Decrypted text: Hello World
