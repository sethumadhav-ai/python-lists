"""Tuple exercises 86-100: interview challenges."""

from collections import Counter

# 86. Remove duplicates without using set().
values = (10, 20, 10, 30, 20, 40)
unique_values = []
for value in values:
    if value not in unique_values:
        unique_values.append(value)
print("86.", tuple(unique_values))

# 87. Find the third-largest unique number in a tuple.
numbers = (10, 40, 20, 40, 30, 50, 30)
print("87.", sorted(set(numbers), reverse=True)[2])

# 88. Find the longest string in a tuple.
words = ("pear", "watermelon", "fig", "blueberry")
print("88.", max(words, key=len))

# 89. Find the shortest string in a tuple.
print("89.", min(words, key=len))

# 90. Sort a tuple of strings according to string length.
print("90.", tuple(sorted(words, key=len)))

# 91. Given student tuples, find the average marks of students who scored above 70.
students = (("Ava", 92), ("Noah", 70), ("Mia", 81), ("Liam", 65))
above_70 = tuple(marks for name, marks in students if marks > 70)
print("91.", sum(above_70) / len(above_70))

# 92. Find the employee with the highest salary.
employees = ((101, "Ava", 72000), (102, "Noah", 85000), (103, "Mia", 79000))
print("92.", max(employees, key=lambda employee: employee[2]))

# 93. Given employee tuples, find the average salary.
print("93.", sum(salary for employee_id, name, salary in employees) / len(employees))

# 94. Find products costing more than 1,000.
products = (("Keyboard", 850), ("Monitor", 12500), ("Mouse", 1200))
print("94.", tuple(product for product in products if product[1] > 1000))

# 95. Calculate the total transaction amount.
transactions = ((1, 250.0), (2, 125.5), (3, 400.0))
print("95.", sum(amount for transaction_id, amount in transactions))

# 96. Find the word with the highest frequency (first one in a tie).
words = ("red", "blue", "red", "green", "blue", "red")
word_counts = Counter(words)
print("96.", max(dict.fromkeys(words), key=word_counts.get))

# 97. Determine whether two tuples contain the same elements regardless of order.
first = (1, 2, 2, 3)
second = (3, 2, 1, 2)
print("97.", Counter(first) == Counter(second))

# 98. Find a pair of elements whose sum equals a given target.
numbers = (2, 7, 11, 15)
target = 9
pairs = tuple(
    (numbers[i], numbers[j])
    for i in range(len(numbers))
    for j in range(i + 1, len(numbers))
    if numbers[i] + numbers[j] == target
)
print("98.", pairs[0] if pairs else None)

# 99. Report highest, lowest, average, pass count, and fail count.
# This example uses 50 as the passing mark.
students = (("Ava", 92), ("Noah", 48), ("Mia", 75), ("Liam", 35))
marks = tuple(mark for name, mark in students)
print(
    "99.",
    {
        "highest": max(students, key=lambda student: student[1]),
        "lowest": min(students, key=lambda student: student[1]),
        "average": sum(marks) / len(marks),
        "pass_count": sum(mark >= 50 for mark in marks),
        "fail_count": sum(mark < 50 for mark in marks),
    },
)

# 100. Student Performance Analyzer using tuples.
# Grade bands: A >= 90, B >= 80, C >= 70, D >= 50, otherwise F.
# A mark of 50 or higher is a pass.
students = (
    ("Ava", 92),
    ("Noah", 48),
    ("Mia", 75),
    ("Liam", 35),
    ("Zoe", 88),
    ("Ethan", 67),
)
all_marks = tuple(mark for name, mark in students)
average = sum(all_marks) / len(students)


def grade_for(mark):
    if mark >= 90:
        return "A"
    if mark >= 80:
        return "B"
    if mark >= 70:
        return "C"
    if mark >= 50:
        return "D"
    return "F"


analysis = {
    "highest_scorer": max(students, key=lambda student: student[1]),
    "lowest_scorer": min(students, key=lambda student: student[1]),
    "average": average,
    "above_average_students": tuple(student for student in students if student[1] > average),
    "pass_count": sum(mark >= 50 for mark in all_marks),
    "fail_count": sum(mark < 50 for mark in all_marks),
    "top_3": tuple(sorted(students, key=lambda student: student[1], reverse=True)[:3]),
    "sorted_students": tuple(sorted(students, key=lambda student: student[0])),
    "total_students": len(students),
    "grades": tuple((name, mark, grade_for(mark)) for name, mark in students),
}
print("100.", analysis)
