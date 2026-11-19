#LIST COMPREHENSION:==list comprehension is a short and simple way to create a new list using loop.
#instead of writing multiple lines using a for loop,we can write the code in a single line.
# 1. Create a list from 1 to 10
numbers= [i for i in range(1, 11)]
print("Numbers:", numbers)


# 2. Squares of numbers
squares = [i ** 2 for i in range(1, 6)]
print("Squares:", squares)


# 3. Even numbers
evens = [i for i in range(1, 11) if i % 2 == 0]
print("Even numbers:", evens)


# 4. Odd numbers
odds = [i for i in range(1, 11) if i % 2 != 0]
print("Odd numbers:", odds)


# 5. Multiplication by 2
doubled = [i * 2 for i in range(1, 6)]
print("Doubled:", doubled)


# 6. Convert words into uppercase
names = ["python", "java", "html"]
uppercase = [i.upper() for i in names]
print("Uppercase:", uppercase)


# 7. Convert words into lowercase
names = ["PYTHON", "JAVA", "HTML"]
lowercase = [i.lower() for i in names]
print("Lowercase:", lowercase)


# 8. Extract characters from a string
word = "Python"
characters = [i for i in word]
print("Characters:", characters)


# 9. Convert characters into uppercase
word = "python"
characters = [i.upper() for i in word]
print("Uppercase characters:", characters)

#conditional statements in list comprehension:=
# 10. Find positive numbers
numbers = [-2, 5, -8, 10, 3, -1]
positive = [i for i in numbers if i > 0]
print("Positive:", positive)


# 11. Find negative numbers
numbers = [-2, 5, -8, 10, 3, -1]
negative = [i for i in numbers if i < 0]
print("Negative:", negative)


# 12. Find numbers greater than 5
numbers = [2, 4, 6, 8, 10, 3]
greater = [i for i in numbers if i > 5]
print("Greater than 5:", greater)


# 13. Find vowels
word = "python programming"
vowels = [i for i in word if i in "aeiou"]
print("Vowels:", vowels)


# 14. Find consonants
word = "python"
consonants = [i for i in word if i not in "aeiou"]
print("Consonants:", consonants)


# 15. Even numbers with their squares
numbers = [1, 2, 3, 4, 5, 6]
even_squares = [i ** 2 for i in numbers if i % 2 == 0]
print("Even squares:", even_squares)


# 16. If-else: Even or Odd
numbers = [1, 2, 3, 4, 5]
result = ["Even" if i % 2 == 0 else "Odd" for i in numbers]
print("Even or Odd:", result)


# 17. Find the length of each word
words = ["apple", "banana", "kiwi"]
lengths = [len(i) for i in words]
print("Lengths:", lengths)

#range in list comprehension:=
# 18. Extract even-positioned elements from a tuple
numbers = (-2, 45, 72, 1, 3, 8, 14, 6)
result = [numbers[i] for i in range(1, len(numbers), 2)]
print("Even-positioned elements:", result)


# 19. Extract odd-positioned elements from a tuple
numbers = (-2, 45, 72, 1, 3, 8, 14, 6)
result = [numbers[i] for i in range(0, len(numbers), 2)]
print("Odd-positioned elements:", result)


# 20. Remove spaces from a string
word = "Python is fun"
result = [i for i in word if i != " "]
print("Without spaces:", result)
#21.true_expression condition and false_expression condition for items in iterable
arr=[1,2,3,4,5,6,7,7,8]



















































