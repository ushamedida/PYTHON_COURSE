#ATM machine program
withdraw_amount=int(input("Enter the amount to withdraw: "))
balance=10000
if withdraw_amount <= balance:
    balance=balance-withdraw_amount
    print(f"{withdraw_amount} withdrawn successfully.")
    print(f"balance in your acount {balance}")
else:
    print("Insufficient funds.")

#updated code
withdraw_amount = int(input("Enter the amount to withdraw: "))
balance=10000
if(withdraw_amount%100==0)or (withdraw_amount%200==0) or  (withdraw_amount%500==0):
    if withdraw_amount<= balance:
        balance=balance-withdraw_amount
        print(f"{withdraw_amount} withdrawn successfully.")
        print(f"Balance in your account: {balance}")
    else:
        print("Insufficient funds.")
else:
    print("Please enter the correct number.")

# 2. DISCOUNT CALCULATOR
bill=float(input("Enter the price of the product: "))
discount=0
if bill >= 2000:
    discount = bill * 0.2
    print(f'you are eligible for a discount of: {discount}')
    amount_to_pay=bill - discount
    print(f"Amount to pay after discount: {amount_to_pay}")
    
else:
    print("No discount available.")
    print("please pay the full amount: ", bill)

#PASSWORD VALIDATION
password=input("Enter your password: ")
print("Password must contain at least 8 characters, one uppercase letter, one lowercase letter, and one digit.")
if len(password) >= 8:
    if any(char.isupper() for char in password):
        if any(char.islower() for char in password):
            if any(char.isdigit() for char in password):
                print("Password is valid.")
            else:
                print("Password must contain at least one digit.")
        else:
            print("Password must contain at least one lowercase letter.")
    else:
        print("Password must contain at least one uppercase letter.")
else:
    print("Password must be at least 8 characters long.")


#time 24 hour format to 12 hour format
hours=int (input("hour : "))
minutes=int(input("minutes : "))
if hours <=12:
    print(f'time is {hours}:{minutes}')
    
else:
    hour = hours%12
    print(f'time is {hours}:{minutes}')

#positive even or positive odd:
num = int(input("Enter a number: "))

if num > 0 :
    if num%2==0:
        print("positive even")
    else:
        print("positive odd")
elif num<0:
    if num %2==0:
        print("negative even")
    else:
        print("negative odd")
else:
    print("zero")

#another method:
number=int(input("enter the m=number"))
if number>0 and number %2==0:
    print("positive even")
elif number>0 and number%2!=0: 
    print("positive odd")
elif number<0 and number%2==0:
    print("negative even")
elif number<0 and number%2!=0:
    print("negative odd")
else:
    print("zero")


l=[]
if l:
    print("")
