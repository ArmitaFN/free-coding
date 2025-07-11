import re
import random
user_pass = input("Please enter your password...")
num = len(user_pass)
length = random.randint(7, 10)
missing = []
upper = bool(re.search(r'[A-Z]', user_pass))
lower = bool(re.search(r'[a-z]', user_pass))
digit = bool(re.search(r'[0-9]', user_pass))
symbol = bool(re.search(r'[!@#$%&]', user_pass))
extra1 = ''.join(random.choice(user_pass) for _ in range(length))
extra2 = ''.join(random.choice(user_pass) for _ in range(length))
if all(upper, lower, digit, symbol):
    if num < 4:
        print("Too short!")
    elif num < 6: 
        print(f"Weak, how about {extra1} or {extra2} ?") 
    elif num < 8:
        print("Medium")
    elif num < 13:
        print("Strong")
    else:
        print("Too long!")
else: 
    if upper == 0:
        missing.append("an uppercase letter")
    if lower == 0:
        missing.append("a lowercase letter")
    if digit == 0:
        missing.append("a digit")
    if symbol == 0:
        missing.append("a special symbol (!@#$%&)")
    print("Your password is missing:", ", ".join(missing))
