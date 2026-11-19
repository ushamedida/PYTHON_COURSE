#Loops:

lst=[10,20,30,40]
for num in lst:
    print(num,end=" ")

lst=[10,20,30,40,50]
for i in range(len(lst)):
    print(lst[i])

for index in range (len(lst)):
    print(lst[index],end=" ")
#even list and odd list:
even_lst=[]
odd_lst=[]
for i in range(1,11):
    if i%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print(even_lst)
print(odd_lst)

#JUMPING STATEMENTS:

# 1.BREAK:
for i in range(10):
    if i==4:
        break
    print(i)

#2.CONTINUE:(skip)
for i in range(10):
    if i==4:
        continue
    print(i,end=" ")

#3.PASS:(with out error execution)
if 10%2==0:
    pass

#ASSERT:will be used in testing
assert 10%2==0
print("error")

#WHILE LOOP:==

i=1
while i<=5:
    print(i)
    i+=1 

print(i)#i=6

i=5
while i>=1:
    print(i)
    i-=1
#for with else:=
for i in range(10):
    if i==15:
        break
    print(i)
else:
    print("loop completed")

#while with else:
i=0
while i<=10:
    print(i)
    i+=1
else:
    print("loop completed")


#factors:
num=int(input("enter your num"))
for factor in range(1,num+1):
    if num% factor==0:
        print(factor)

num1=int(input("enter your"))
count=0
for n in range(1,num1+1):
    if n%2!=0:
        count=count+1
print(count) 

#prime number:
num=int(input("enter your num"))
count=0
for i in range(1,num+1):
    if num % i == 0:
        count+=1
if count==2:
    print("prime")
else:
    print("not a prime")

#perfect number:
num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum += i

if sum == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")



for num in range(1, 100):
    sum = 0

    for i in range(1, num):
        if num % i == 0:
            sum += i

    if sum == num:
        print(num)

#find the minimum number
l=[10,26,2,4,45,-3]
mini=l[0] #float('inf')
for num in l:
    if num<mini:
        mini=num
print(mini)

#find maximum number:
l=[10,26,2,4,45,-3]
maxi=l[0]
for num in l:
    if num>maxi:
        maxi=num
print(maxi)
#sum of list in loops:
l=[1,2,3,4,5]
summation=0
for num in l:
    summation+=num
    print(summation)
#length of the list:
l=[10,20,30,40,50]
count=0
for num in l:
    count+=1
print(count)
    