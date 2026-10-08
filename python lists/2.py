"""Tuple exercises 26-50: methods and operations."""

# 26. Find the sum of all numbers in a tuple.
numbers = (5, 10, 15, 20)
print("26.", sum(numbers))

# 27. Count how many times 10 occurs in a tuple.
values = (10, 5, 10, 20, 10, 30)
print("27.", values.count(10))

# 28. Find the index of a particular element.
print("28.", values.index(20))

# 29. Concatenate two tuples.
print("29.", (1, 2, 3) + (4, 5))

# 30. Repeat a tuple 3 times.
print("30.", ("go", "!",) * 3)

# 31. Compare two tuples using ==.
print("31.", (1, 2, 3) == (1, 2, 3))

# 32. Compare two tuples using < (lexicographic comparison).
print("32.", (1, 2, 4) < (1, 3, 0))

# 33. Check whether two tuples contain the same elements, regardless of order.
first = (3, 1, 2)
second = (2, 3, 1)
print("33.", sorted(first) == sorted(second))

# 34. Find the length of a nested tuple (the number of outer elements).
nested = ((1, 2), (3, 4), (5, 6))
print("34.", len(nested))

# 35. Sort a tuple and return the result as a list.
unsorted = (4, 1, 3, 2)
print("35.", sorted(unsorted))

# 36. Sort a tuple and convert the result back to a tuple.
print("36.", tuple(sorted(unsorted)))

# 37. Find the second-largest distinct number in a tuple.
numbers = (10, 5, 8, 10, 3)
print("37.", sorted(set(numbers))[-2])

# 38. Find the second-smallest distinct number in a tuple.
print("38.", sorted(set(numbers))[1])

# 39. Remove duplicate values from a tuple, preserving first-occurrence order.
duplicates = (1, 2, 2, 3, 1, 4)
print("39.", tuple(dict.fromkeys(duplicates)))

# 40. Count the number of unique elements in a tuple.
print("40.", len(set(duplicates)))

# 41. Create a tuple containing numbers and calculate their average.
scores = (70, 80, 90)
print("41.", sum(scores) / len(scores))

# 42. Find all even numbers from a tuple.
numbers = (1, 2, 3, 4, 5, 6)
print("42.", tuple(number for number in numbers if number % 2 == 0))

# 43. Find all odd numbers from a tuple.
print("43.", tuple(number for number in numbers if number % 2 != 0))

# 44. Create a new tuple containing only positive numbers.
signed = (-3, 0, 4, -1, 8)
print("44.", tuple(number for number in signed if number > 0))

# 45. Create a new tuple containing only negative numbers.
print("45.", tuple(number for number in signed if number < 0))

# 46. Multiply every element of a numeric tuple by 2.
print("46.", tuple(number * 2 for number in numbers))

# 47. Create a tuple containing squares of numbers from another tuple.
print("47.", tuple(number**2 for number in numbers))

# 48. Create a tuple containing cubes of numbers from another tuple.
print("48.", tuple(number**3 for number in numbers))

# 49. Find the difference between the maximum and minimum values.
print("49.", max(signed) - min(signed))

# 50. Check whether all elements in a tuple are integers.
mixed = (1, 2, 3.0)
print("50.", all(isinstance(item, int) for item in mixed))
