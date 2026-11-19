#SCOPE:scope refers to the region of a program where a variable can be accessed.
#TYPES OF SCOPE:
#1.LOCAL SCOPE:-A variable created inside a function is called a local variable.it can be accessed only inside that function.
def student():
    name="ush"
    print(name)
student()
#2.enclosed scope:-a variable create inside an outer function can be accessed by an inner function.
# this is called enclosed scope.
def outer():
    x=10
    def inner():
        print(x)
    inner()
a=outer()
#3.global scope:-a variable create outside a function is called a global variable.
# it can be accessed both inside and outside function.
x=10
def display():
    print(x)
display()
print(x)
#4.built in scope:-
numbers=[10,20,30]
print(len(numbers))
print(sum(numbers))
print(max(numbers))

#GLOBAL AND NON-GLOBAL KEYWORDS:-
#1.GLOBAL KEYWORDS:-the global keyword us to modify a global variable from inside a function.
x=10
def change():
    global x
    x=x+1
change()
print(x)
#2.NON-GLOBAL KEYWORDS:-use inside a nested function to modify a variable belonging to the enclosing function.
def outer():
    x=10
    def inner():
        nonlocal x
        x=x+5
    inner()
    print(x)
outer()

#RECURSION:-recursion is a process in which a function case itself until a base condition is reached.
def factorial(n):
    if n==1:
        return 1
    return n* factorial(n-1)
print(factorial(5))

#sum of natural numbers using recursion.
def natural_sum(n):
    if n==1:
        return 1
    return n+ natural_sum(n-1)
print(natural_sum(5))