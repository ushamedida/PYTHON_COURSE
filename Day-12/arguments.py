#TYPES OF ARGUMENTS:
#1.POSITIONAL ARGUMENTS:--Positional arguments are arguments passed to a function in the order of the parameters.
def student(name,age):
    print("Name:",name)
    print("age:",age)
student("greeshma",22) 
#2.KEYWORD ARGUMENTS:-keyword arguments are arguments passed to a function using parameter names.the order of arguments does not matter.
def student(name,age):
    print("name:",name)
    print("age:",age)
student(age=22,name="usha")
#3.DEFAULT ARGUMENTS:-default arguments are arguments that have default values assigned to them in them in the function definition.
#if we don't pass a value while calling the function.python uses the default value.
def student(name,age=22):
    print("name:",name)
    print("age:",age)
student("ush")

def student(name,age=22):
    print("name:",name)
    print("age:",age)
student("ush",23)
#4.VARIABLE-LENGTH ARGUMENTS(*args):-variable-length allow a function to accept any number of positional arguments.
# we use *args when we don't know in advance how many arguments will be passed to a function.
def add(*args):
    total=0
    for i in args:
        total=total+i
        return total
result=add(10,20,30,40)
print(result)
#5.KEY WORD VARIABLE-LENGTH ARGUMENTS(*kwargs):-*kwargs allows a function to accept any number of keyword arguments inside the function.
# these arguments are stored as a dictionary.
def student(**kwargs):
    print(kwargs)

student(name="Ush", age=21, course="Python")


    

