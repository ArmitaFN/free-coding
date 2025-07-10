import re
user_pass = input("Please enter your password...")
num = len(user_pass)
if (re.search(r'[A-Z]', user_pass) and
    re.search(r'[a-z]', user_pass) and
    re.search(r'[0-9]', user_pass) and
    re.search(r'[!@#$%&]')):
      if num < 4:
        print("Too short!")
      elif 4 < num < 6: #now i should suggest something for renforcement 
        print("Weak")
      elif 6 < num < 8:
        print("Medium")
      elif 8 < num < 13:
        print("Strong")
      else:
        print("Too long!")
else:
  print("Please use both upper and lower case, numbers and symbols")
          

