import string
import random

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation

s=[]

passgen=int(input("Enter the length of password required : "))

complex=input("Enter the complexity required (low,med,high) :")

if complex=="low":
    s.extend(list(s1))
elif complex=="med":
    s.extend(list(s1))
    s.extend(list(s2))
elif complex=="high":
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))

spchar=int(input("Do you want to include special characters?If yes then enter 1 else 2 :"))

if spchar==1:
    s.extend(list(s4))
random.shuffle(s)

print("".join(s[0:passgen]))
