"""Tuple exercises 71-85: advanced tuple problems."""

students = (
    ("Ava", 18, 92),
    ("Noah", 19, 75),
    ("Mia", 18, 88),
    ("Liam", 20, 65),
    ("Zoe", 19, 95),
)

# 71. Sort student records by marks (ascending).
print("71.", tuple(sorted(students, key=lambda record: record[2])))

# 72. Sort student tuples by age.
print("72.", tuple(sorted(students, key=lambda record: record[1])))

# 73. Sort student tuples alphabetically by name.
print("73.", tuple(sorted(students, key=lambda record: record[0])))

# 74. Find the top 3 students based on marks.
print("74.", tuple(sorted(students, key=lambda record: record[2], reverse=True)[:3]))

# 75. Find students whose marks are greater than 75.
print("75.", tuple(student for student in students if student[2] > 75))

# 76. Find duplicate elements in a tuple, once each, in first-seen order.
values = (1, 2, 3, 2, 4, 1, 1, 5)
seen = set()
duplicates = []
for value in values:
    if value in seen and value not in duplicates:
        duplicates.append(value)
    seen.add(value)
print("76.", tuple(duplicates))

# 77. Find elements that occur exactly once.
print("77.", tuple(value for value in values if values.count(value) == 1))

# 78. Find the frequency of every element in a tuple.
frequencies = {value: values.count(value) for value in dict.fromkeys(values)}
print("78.", frequencies)

# 79. Create a dictionary containing tuple element frequencies.
print("79.", frequencies)

# 80. Find the most frequently occurring element (first one in a tie).
print("80.", max(frequencies, key=frequencies.get))

# 81. Find the least frequently occurring element (first one in a tie).
print("81.", min(frequencies, key=frequencies.get))

# 82. Merge multiple tuples into one tuple.
groups = ((1, 2), (3,), (4, 5))
print("82.", tuple(item for group in groups for item in group))

# 83. Find common elements between two tuples, without duplicates.
first = (1, 2, 2, 3, 4)
second = (2, 4, 4, 5)
print("83.", tuple(value for value in dict.fromkeys(first) if value in second))

# 84. Find elements present in the first tuple but not the second.
print("84.", tuple(value for value in dict.fromkeys(first) if value not in second))

# 85. Find the union of elements from two tuples without duplicates.
print("85.", tuple(dict.fromkeys(first + second)))
