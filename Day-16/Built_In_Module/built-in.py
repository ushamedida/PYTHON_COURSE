#BUILT-IN MODULE:
#Built in modules are already available in python.we can directly import and use them.
# MODULE                   PURPOSE
# math          -         mathematic operations
# random        -         generate random values
# datetime      -         work with date and Time
# os            -         interact with operating System
# sys           -         work with python interpreter
# statistics    -         statistical calculation

#1.math module:
import math
print(math.sqrt(25))
print(math.factorial(5))
print(math.pi)
print(math.pow(2,3))
print(math.ceil(4.2))
print(math.floor(4.8))
print(math.log(10))
print(math.sin(90))
print(math.cos(90))
print(math.tan(180))

radius=5
area=math.pi*math.pow(radius,2)
print(area)

#2.random module:
import random
print(random.randint(1,10))

raki=['designed','home_made','silver_raki','thread']
print(random.choice(raki))

num=[10,20,30,40,50]
print(random.sample(num,3))

num1=[10,20,30,40,50]
print(random.shuffle(num1))

#3.sys module:
import sys
print(sys.version)
print(sys.platform)
# print(sys.argv)

import sys
age = 15
if age<18:
    print("not eligible")
    sys.exit()
print("eligible")

print(sys.path)
print(sys.version)

#4.platform module
import platform
print(platform.system())
print(platform.release())
print(platform.machine())
print(platform.processor())
print(platform.python_version())

#5.collections 
import collections
from collections import Counter
name = "Codegnan"
r = Counter(name)
print(r)
nums = [1, 2, 3, 4, 1, 3, 10, 2, 2]
n = Counter(nums)
print(n)
# d = {} 
# for ch in name:
#     if ch in d:
#         d[ch] += 1
#     else:
#         d[ch] = 1

from collections import defaultdict
d = defaultdict(int)
d["apple"] = 1
print(d["name"])
# dic = {'a':2,'b':5,'c':10}
# print(dic['x'])
# d = {}
# print(d["name"])

from collections import deque
d = deque([1,2,3])
d.append(4)
d.appendleft(10)
d.pop()
d.popleft()
print(d)

#6.itertools
from itertools import permutations
numbers = [1,2,3,5] 
print(list(permutations(numbers)))

from itertools import combinations
numbers = [1,2,3,4] 
print(list(combinations(numbers,3)))

from itertools import product
a = [1,2,4]
b = ['A','B','C']
print(list(product(a,b)))
#7.datetime
from datetime import datetime
now = datetime.now()
print(now)
print()
print(now.year)
print(now.month)
print(now.day)
print()
print(now.hour)
print(now.minute)
print(now.second)

from datetime import date
today = date.today()
print(today)

# manual creation of a date
d = date(2026, 2, 22)
print(d)

from datetime import date, timedelta
today = date.today()
future = today+timedelta(days=30)
print(future)

past = today - timedelta(days=100)
print(past)

from datetime import datetime
now = datetime.now()
print(now.strftime("%H:%M:%S")) # %H, %M, %S, %y
print(now.strftime("%d/%m/%Y"))
print(now.strftime("%d-%m-%Y"))

#random password generation:=
import random

characters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
characters+= "abcdefghijklmnopqrstuvwxyz"
characters += "0123456789"
characters += "!@#$%^&*?"

password = ""
password_length = int(input("Enter password length: "))

for i in range(password_length):
    password += random.choice(characters)

print("Generated Password:", password)


characters="aedRTG@#%"
print(random.choice(characters))

upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case= "abcdefghijklmnopqrstuvwxyz"
digits= "0123456789"
special_chars= "!@#$%^&*?"
all_chars=upper_case+lower_case+digits+special_chars
password=[]
password.append(random.choice(upper_case))
password.append(random.choice(lower_case))
password.append(random.choice(digits))
password.append(random.choice(special_chars))
length=8
for i in range(length -4):
    password.append(random.choice(all_chars))
random_Password="".join(password)
print(random_Password)

#frequency:
name="Codegnan"
d={}
for ch in name:
    if ch in d:
        d[ch]+=1
    else:
        d[ch]=1
print(d)

from collections import Counter
f=Counter(name)
print(f)
print(d)
#print(d['z'])#key error
print(f['z'])

#snake and ladder:
import random
count=0
rolls=0
while True:
    input("click enter to throw the dice")
    dice=random.randint(1,6)
    if count+dice<=100:
        count+=dice
    print(f"your dice value is {dice}")
    print(f"you are at {count} position")
    rolls+=1
    if count==100:
        print(f"you win at {rolls} ")

#snake and ladder with two players:-
import random

# Snake and Ladder positions

##########
import random 
count1=0
count2=0
rolls1=0
rolls2=0
while True:
    input("player1 Click enter to throw the dice:")
    dice = random.randint(1,6)
    if count1+dice <= 100:
        count1 += dice
    print(f'player1 your dice value is {dice}')
    print(f"player1 your are at {count1} position")
    rolls1+=1  
    input("player2 Click enter to throw the dice:")
    dice = random.randint(1,6)
    if count2+dice <= 100:
        count2 += dice
    print(f'player2 your dice value is {dice}')
    print(f"player2 your are at {count2} position")
    rolls2+=1
    if count1 == 100:
        print(f"player1 you win at {rolls1} rolls")
        break
    elif count2 == 100:
        print(f"player2 you win at {rolls2} rolls")
        break