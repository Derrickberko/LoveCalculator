# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is your girlfriend/ boyfriend name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine_string = name1 + name2
lower_string = combine_string.lower()

t = lower_string.count("t")
r = lower_string.count("r")
u = lower_string.count("u")
e = lower_string.count("e")

true = t + r + u + e

l = lower_string.count("l")
o = lower_string.count("o")
v = lower_string.count("v")
e = lower_string.count("e")

love = l + o + v + e
total = int(str(true) + str(love))

if (total <  10) or (total  > 90):
  print(f"Your score {total}% you guy might or might not be together")

elif (total >= 40) and (total <= 50):
  print(f"Your score is {total}%, you are alright together")

else:
  print(f"Your dcore is {total}%")
