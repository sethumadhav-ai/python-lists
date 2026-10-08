"""Tuple exercises 1-25: basics."""

# 1. Create and print a tuple containing 5 integers.
integers = (1, 2, 3, 4, 5)
print("1.", integers)

# 2. Create and print a tuple containing 5 strings.
words = ("red", "green", "blue", "yellow", "purple")
print("2.", words)

# 3. Create a tuple containing different data types.
mixed = (42, "Python", 3.14, True)
print("3.", mixed)

# 4. Create a tuple with only one element.
single = ("only item",)
print("4.", single)

# 5. A comma, not parentheses, makes a one-item tuple.
print("5. (10) is an int; (10,) is a tuple because the comma creates the tuple.")
print("   Types:", type((10)).__name__, type((10,)).__name__)

# 6. Find the length of a tuple.
sample = (10, 20, 30, 40, 50)
print("6.", len(sample))

# 7. Access the first element of a tuple.
print("7.", sample[0])

# 8. Access the last element using negative indexing.
print("8.", sample[-1])

# 9. Access the third element using positive indexing.
print("9.", sample[2])

# 10. Access the second-last element using negative indexing.
print("10.", sample[-2])

# 11. Print all elements of a tuple using a for loop.
print("11.")
for item in sample:
    print(item)

# 12. Print tuple elements with their indexes.
print("12.")
for index, item in enumerate(sample):
    print(index, item)

# 13. Check whether a value exists in a tuple.
print("13.", 30 in sample)

# 14. Check whether a value does not exist in a tuple.
print("14.", 99 not in sample)

# 15. Create a tuple containing numbers from 1 to 10.
one_to_ten = tuple(range(1, 11))
print("15.", one_to_ten)

# 16. Print the first three elements using slicing.
print("16.", one_to_ten[:3])

# 17. Print the last three elements using slicing.
print("17.", one_to_ten[-3:])

# 18. Print every second element from a tuple.
print("18.", one_to_ten[::2])

# 19. Reverse a tuple using slicing.
print("19.", one_to_ten[::-1])

# 20. Create an empty tuple.
empty = ()
print("20.", empty)

# 21. Convert a list into a tuple.
print("21.", tuple([1, 2, 3]))

# 22. Convert a tuple into a list.
print("22.", list((1, 2, 3)))

# 23. Create a tuple using the tuple() function.
print("23.", tuple(("a", "b", "c")))

# 24. Find the maximum value in a numeric tuple.
numbers = (8, 3, 12, 5, 9)
print("24.", max(numbers))

# 25. Find the minimum value in a numeric tuple.
print("25.", min(numbers))