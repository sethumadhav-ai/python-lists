"""Tuple exercises 51-70: unpacking and nested tuples."""

# 51. Unpack (10, 20, 30) into three variables.
a, b, c = (10, 20, 30)
print("51.", a, b, c)

# 52. Swap two variables using tuple unpacking.
left, right = "left", "right"
left, right = right, left
print("52.", left, right)

# 53. Unpack a tuple using *.
first, *middle, last = (1, 2, 3, 4, 5)
print("53.", first, middle, last)

# 54. Extract the first element and store the remaining elements separately.
first, *remaining = (10, 20, 30, 40)
print("54.", first, tuple(remaining))

# 55. Extract the last element and store all previous elements separately.
*previous, last = (10, 20, 30, 40)
print("55.", tuple(previous), last)

# 56. Unpack five elements into three variables using *.
first, *middle, last = (1, 2, 3, 4, 5)
print("56.", first, middle, last)

# 57. Use tuple unpacking inside a for loop.
pairs = (("apple", 2), ("pear", 4), ("plum", 3))
print("57.")
for fruit, quantity in pairs:
    print(fruit, quantity)

# 58. Create student records and unpack each record.
student_records = (("Ava", 18, 92), ("Noah", 19, 85))
print("58.")
for name, age, mark in student_records:
    print(name, age, mark)

# 59. Create a nested tuple and access an inner element.
nested = ((1, 2), (3, 4))
print("59.", nested[1][0])

# 60. Create a 3-level nested tuple and access a deeply nested value.
three_levels = (("group", (("target", 42),)),)
print("60.", three_levels[0][1][0][1])

# 61. Find the maximum value inside a nested tuple.
nested_numbers = ((4, 9), (2, 15), (7, 3))
print("61.", max(number for row in nested_numbers for number in row))

# 62. Find the total number of leaf elements in a nested tuple.
nested_values = ((1, 2), (3, (4, 5)))


def count_leaves(items):
    return sum(count_leaves(item) if isinstance(item, tuple) else 1 for item in items)


print("62.", count_leaves(nested_values))

# 63. Flatten a tuple containing tuples (one level deep).
rows = ((1, 2), (3, 4), (5,))
print("63.", tuple(item for row in rows for item in row))

# 64. Convert a nested tuple into a nested list (one level deep).
print("64.", [list(row) for row in rows])

# 65. Convert a nested list into a nested tuple (one level deep).
nested_list = [[1, 2], [3, 4]]
print("65.", tuple(tuple(row) for row in nested_list))

# 66. Create a tuple containing student details (name, age, marks).
student = ("Ava", 18, 92)
print("66.", student)

# 67. Create 5 student tuples and print each student's name.
students = (
    ("Ava", 18, 92),
    ("Noah", 19, 85),
    ("Mia", 18, 78),
    ("Liam", 20, 88),
    ("Zoe", 19, 95),
)
print("67.")
for name, age, marks in students:
    print(name)

# 68. Find the student with the highest marks.
print("68.", max(students, key=lambda record: record[2]))

# 69. Find the student with the lowest marks.
print("69.", min(students, key=lambda record: record[2]))

# 70. Calculate the average marks of students stored as tuples.
print("70.", sum(marks for name, age, marks in students) / len(students))
