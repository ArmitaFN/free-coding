import re
import random
user_pass = input("Please enter your password...")
num = len(user_pass)
length = random.randint(7, 10)
extra = ''.join(random.choice(user_pass) for _ in range(length))
if (re.search(r'[A-Z]', user_pass) and
    re.search(r'[a-z]', user_pass) and
    re.search(r'[0-9]', user_pass) and
    re.search(r'[!@#$%&]')):
      if num < 4:
        print("Too short!")
      elif 4 < num < 6: 
        print(f"Weak, how about {extra} ?")
      elif 6 < num < 8:
        print("Medium")
      elif 8 < num < 13:
        print("Strong")
      else:
        print("Too long!")
else:
  print("Please use both upper and lower case, numbers and symbols")
          

