#LAMBDA FUNCTIONS:(Anonymous function)
def addition(a,b):
    return a+b
print(addition(10,20))

addition=lambda x,y:x+y
print(addition(10,20))
#higher order functions:
#filter():=
nums=[1,2,3,4,5,6,7,8]
even=filter(lambda x:x%2==0,nums)
print(even)
print(list(even))
#map():=
multiplication_by_2=map(lambda x:x*2,nums)
print(list(multiplication_by_2))
#reduce():=
from functools import reduce
summation=reduce(lambda x,y:x+y,nums)
print(summation)
nums=[1,2,3,4,5]
even_odd=map(lambda x:'even' if x%2==0 else 'odd',nums)
print(list(even_odd))