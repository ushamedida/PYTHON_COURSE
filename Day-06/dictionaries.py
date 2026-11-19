#DICTIONARIES:=
# A dictionary is an unordered collection of key-value pairs.
# Dictionaries are mutable, meaning that their contents can be changed after they are created.
# Dictionaries are defined using curly braces {} and each key-value pair is separated by a colon :.
dict1={'a':1,
    'b':2,
    'c':3}
print(dict1)
print(type(dict1))
print(dict1['a'])
print(dict1.get('b'))
print(dict1.values())
print(dict1.keys())
print(dict1.items())
print(dict1.get('d'))#returns none if the key is not present in the dictionary.

# Adding and modifying elements in a dictionary:=
dict1['d']=4
print(dict1)
dict1['a']=10
print(dict1)
dict1.update({"d":4})
print(dict1)
dict1.update(e=5)
print(dict1)

# Removing elements from a dictionary:=
del dict1['a']
print(dict1)
dict1.pop('b')
print(dict1)
dict1.popitem()
print(dict1)
dict1.clear()
print(dict1)