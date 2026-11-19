#SETS:=
# A set is an unordered collection of unique items.
# Sets are mutable, meaning that their contents can be changed after they are created.
# Sets are defined using curly braces {} or the set() function.
#no indexing or slicing is allowed in sets because they are unordered collections.
set1={1,2,3,5}
s1=set()
s2={}
print(set1,type(s1),type(s2))#s2 is a dictionary not a set.
#SET METHODS:==
#1.ADDING ELEMENTS TO A SET:=
set1.add(4)
print(set1)
#2.REMOVING ELEMENTS FROM A SET:=
set1.remove(2)
print(set1)
#3.DISCARD METHOD:=
set1.discard(10)#if the element is not present in the set then it will not give an error.
print(set1)
#4.copy() method:=
s5=set1.copy()#creates a shallow copy of the set.
print(s5)
#5.clear() method:=
s5.clear()#removes all the elements from the set.
#SET OPERATIONS:==
s1={10,20,30,40}
s2={40,50,60}
#1.union of two sets:=
print(s1.union(s2))#returns a new set containing all unique elements from both sets.
print(s1 | s2)
#2.intersection of two sets:=
print(s1.intersection(s2))
print(s1 & s2)
#3.difference of two sets:=
print(s1.difference(s2))
print(s1 - s2)
print(s2.difference(s1))
print(s2 - s1)
#4.symmetric difference of two sets:=
print(s1.symmetric_difference(s2))
print(s1 ^ s2)
#5.subset and superset:=
s3={26,45,18,1,4}
s4={26}
print(s3.issuperset(s4))#returns True if s3 is a superset of s4.
print(s3.issuperset(s1))#returns False if s3 is not a superset of s1.
print(s4.issubset(s3))#returns True if s4 is a subset of s3.















