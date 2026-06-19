import re

mystr = "Hello Riya Jivani @Python_2026 Welcome to Python Programming 456"

print("Word Characters:", re.findall(r'\w', mystr))
print("Non Word Characters:", re.findall(r'\W', mystr))

print("Digits:", re.findall(r'\d', mystr))
print("Non Digits:", re.findall(r'\D', mystr))

print("Spaces:", re.findall(r'\s', mystr))
print("Non Spaces:", re.findall(r'\S', mystr))

print("One or More Digits:", re.findall(r'\d+', mystr))
print("Zero or More Digits:", re.findall(r'\d*', mystr))
print("Zero or One Digit:", re.findall(r'\d?', mystr))

print("Exactly 2 Digits:", re.findall(r'\d{2}', mystr))
print("2 to 4 Digits:", re.findall(r'\d{2,4}', mystr))

print("Start with Hello:", re.findall(r'^Hello', mystr))
print("End with 456:", re.findall(r'456$', mystr))

print("Any Character:", re.findall(r'.', mystr))

print("Words:", re.findall(r'\b\w+\b', mystr))
print("Words Starting with Capital:", re.findall(r'\b[A-Z]\w*', mystr))

print("Vowels:", re.findall(r'[aeiouAEIOU]', mystr))
print("Non Vowels:", re.findall(r'[^aeiouAEIOU ]', mystr))