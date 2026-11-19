def addition(x,y):
    return x+y
z=addition(10,20)
print(z)
#2.alphabet checker:
def alphabet_count(str1):
    vowels_count=0
    consonents_count=0
    for ch in str1:
        if ch in "aeiouAEIOU":
            vowels_count+=1
        else:
            consonents_count+=1
    return [vowels_count,consonents_count]
result=alphabet_count("python program")
print(result)
#types of parameters:
#ADDITION
#1.with parameter and with return type:
def add1(x,y):
    return x+y
z=add1(20,10)
print(z)
#2.with parameter and without return type:
def add2(x,y):
    print(x+y)          #out put=6
add2(2,4)
#####
def add_2(x,y):
    print(x+y)           #output=none 
z=add_2(2,4)
print(z)
#3.with out parameter and with return type:
def add3():
    x=200
    y=100
    return x+y
z=add3()
print(z)
#4.without parameter and without return type:
def add4():
    x=int(input())
    y=int(input())
    print(x+y)
add4()
#DIVISION:
#1.
def division1(x,y):
    return x % y
z=division1(25,5)
print(z)
#2.
def division2(x,y):
    print(x % y) 
division2(25,5)
#3.
def division3():
    x=15
    y=3
    return x % y
z=division3()
print(z)
#4.
def division4():
    x=int(input())
    y=int(input())
    if y!=0:
        print(x % y)
    else:
        print(" division with zero can't be possible.take another num")
division4()
###############################################

#PRACTICING PROBLEMS:==
# 1.FIND THE PRIME NUMBER FROM 2 TO 100:
def prime_num():
    for n in range (2,101):
        count=0
        for i in range(1,n+1):
            if n % i==0:
                count+=1
        if count==2:
            print(n,end=" ")
prime_num()
print
#2.get all square patterns,right triangle patterns,pyramid patterns,rhombus patterns using functions:
def squares():
    def square(n):
        for i in range(n):
            for j in range(n):
                print("*", end=" ")
            print()
    square(5)

    def hollow_square(n):
        for i in range(n):
            for j in range(n):
                if i == 0 or i == n-1 or j == 0 or j == n-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    hollow_square(5)

    def diagonal_square(n):
        for i in range(n):
            for j in range(n):
                if i == j or i+j == n-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
            print()
    diagonal_square(5)

    def number_square(n):
        for i in range(1, n+1):
            for j in range(n):
                print(i, end=" ")
            print()
    number_square(5)
    
    def  even_odd(n):
        for r in range(4):                        
            for c in range(4):                    
                if r%2==0:                        
                    print(r*4+(c+1)*2,end=" ")    
                else:
                    print(r*4+(c*2)-3,end=" ")
            print()
    even_odd(5)
squares()
#right triangle:
def triangles():
    def right_triangle(n):
        for i in range(1, n+1):
            for j in range(i):
                print("*", end=" ")
            print()
    right_triangle(5)

    def decreasing_triangle(n):
        for i in range(n, 0, -1):
            for j in range(i):
                print("*", end=" ")
            print()
    decreasing_triangle(5)

    def right_aligned(n):
        for i in range(1, n+1):
            print("  " * (n-i), end="")
            print("* " * i)
    right_aligned(5)

    def number_triangle(n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()
    number_triangle(5)

    def inverted_number(n):
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(j, end=" ")
            print()
    inverted_number(5)
triangles()
#Pyramid patterns:=
def pyramids():
    def pyramid(n):
        for i in range(n):                         
            for j in range(n-i-1):    
                print(" ",end=" ")    
            for j in range(2*i+1):
                print("*",end=" ")
            print()

    pyramid(5)
    def inverted_pyramid(n):
        for i in range(n):                    
            for j in range(i):                
                print(" ",end=" ")           
            for j in range(2*n-(2*i+1)):
                print("*",end=" ")
            print()

    inverted_pyramid(5)
    def number_pyramid(n):
        for i in range(1, n+1):
            print("  " * (n-i), end="")

            for j in range(1, i+1):
                print(j, end=" ")

            for j in range(i-1, 0, -1):
                print(j, end=" ")

            print()

    number_pyramid(5)
pyramids()


#rhombus patterns:==
def rhombus():
    n=5
    for i in range(n):                      
        for j in range(n-i-1):    
            print(" ",end=" ")    

        for j in range(2*i+1):    
            print("*",end=" ")    
        print()                
    n=4                           
    for i in range(n):
    
        for j in range(i+1):
            print(" ",end=" ")
        for j in range(2*n-(2*i+1)):
            print("*",end=" ")
        print()
rhombus()


#squares()
#triangles()
#pyramids()
#rhombus()


#3.add all the values in the dictionary and find maximum,minimum,average,among all the values:==


def dictionary_operations():
    marks = {
        "Python": 85,
        "Java": 90,
        "SQL": 75,
        "HTML": 80,
        "CSS": 70
    }

    values = marks.values()

    total = sum(values)
    maximum = max(values)
    minimum = min(values)
    average = total / len(marks)

    print("Dictionary:", marks)
    print("Sum of values:", total)
    print("Maximum value:", maximum)
    print("Minimum value:", minimum)
    print("Average value:", average)


dictionary_operations()


#4.reverse the string -"hello"
def reverse_string():
    s = "hello"
    print(s[::-1])

reverse_string()

#5.search the target in the given list if target is present, return its position otherwise return-1

def search_target():
    numbers = [10, 20, 30, 40, 50]

    target = int(input("Enter target value: "))

    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1


result = search_target()
print("Position:", result)
