import re

s = input("Enter a string: ")
s_clean = re.sub(r'[^a-zA-Z0-9]', '', s.lower())  # removes all non-alphanumerics

if s_clean == s_clean[::-1]:
    print(f"{s} is a Palindrome")
else:
    print(f"{s} is not a Palindrome")
