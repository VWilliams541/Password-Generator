import random
import string


#password generator

lower = []
upper = []
numbers = []
symbols = []
password = [lower, upper, numbers, symbols]

print("How many lowercase letters do you want in your password?")
userLower = int(input())

print("How many uppercase letters do you want in your password?")
userUpper = int(input())

print("How many numbers do you want in your password?")
userNumbers = int(input())

print("How many symbols do you want in your password?")
userSymbols = int(input())

i = 1
while i <= userLower:
    lower.append(random.choice(string.ascii_lowercase))
    i += 1

i = 1
while i <= userUpper:
    upper.append(random.choice(string.ascii_uppercase))
    i += 1

i = 1
while i <= userNumbers:
    numbers.append(random.choice(string.digits))
    i += 1

i = 1
while i <= userSymbols:
    symbols.append(random.choice(string.punctuation))
    i += 1

flatPassword = []
for entry in password:
    flatPassword.extend(entry)

random.shuffle(flatPassword)
finalPassword = ''.join(flatPassword)
print("Your new password is: " + finalPassword)
