#EXCEPTION:

try:
    a=int(input("enter num"))
    b=int(input("enter num"))
    print(a/b)
except:
    print("code has zero division error")
else:
    print("code doesn't have any error")
finally:
    print("code executed")

#whenever we know the which error is occur.then we use this method
#1.ZeroDivisionError
try:
    a=int(input("enter num"))
    b=int(input("enter num"))
    print(a/b)
except ZeroDivisionError as e:               
    print(e)
else:
    print("code doesn't have any error")
finally:
    print("code executed")
#2.ValueError
try:
    a=(input("enter num"))
    b=(input("enter num"))
    print(a/b)
except ValueError as e:               
    print(e)
else:
    print("code doesn't have any error")
finally:
    print("code executed")

#raise keyword:
def div(x,y):
    if y==0:
        raise ZeroDivisionError
    return x/y
div(3,0)
try:
    div(10,0)#error code
except:
    print("division with zero")

#custom Exception
#if user want to create an exception,we cal call it as custom exception
class NegativeBalanceError(Exception):
    pass

def withdraw(amount):
    balance = 10000
    if amount<0:
        raise NegativeBalanceError()
    balance -= amount
    return f'{amount} withdraw,current balance is {balance}'
#withdraw(-500)
try:
    withdraw(-300)
except:
    print("amount is negative")
#custom exception error for password spaces:
class SpaceError(Exception):
    pass

def password(password): 
    password=input("enter your password:")
    if " " in password:
        raise SpaceError()
    return
try:
    password(password)
except:
    print("password should not contain spaces")
    
#custom exception error for password length:--
class LenError(Exception):
    pass
def password(password): 
    password=input("enter your password:")
    if len(password)<8 or len(password)>8:
        raise LenError()
    return
try:
    password(password)
except:
    print("password len should contain only 8 characters")
else:
    print("valid password length")
finally:
    print("password is success")
