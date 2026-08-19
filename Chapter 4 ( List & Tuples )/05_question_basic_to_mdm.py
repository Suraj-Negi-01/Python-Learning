"""
================================================================================
                    LIST & TUPLE - IMPORTANT QUESTIONS
                      (Beginner to Medium Level)
================================================================================
This file contains 5 important questions on Lists and 5 on Tuples, 
each progressing from beginner-friendly to medium-level complexity.
================================================================================
"""

print("\n" + "="*80)
print("                        *** LIST QUESTIONS ***")
print("="*80)

"""
================================================================================
LIST QUESTION 1 - BEGINNER LEVEL
================================================================================
Question: Create a list of 5 numbers, then add a new number at the end using
append() method, and display the final list.

Concept: Basic list creation and append() method
"""
print("\nLIST QUESTION 1 - BEGINNER LEVEL: Using append() method")
print("-"*80)
print("Question: Create a list of 5 numbers, add a new number using append(),")
print("          and display the final list.")
print()

# Main Solution
numbers = [10, 20, 30, 40, 50]
print("Original list:", numbers)

numbers.append(60)  # Add 60 at the end
print("After append(60):", numbers)

print("\n✓ Concept: append() adds a single element at the end of the list")
print()


"""
================================================================================
LIST QUESTION 2 - BEGINNER-INTERMEDIATE LEVEL
================================================================================
Question: Given a list of numbers, find the maximum and minimum values, 
and calculate the sum of all elements.

Concept: Using built-in functions max(), min(), and sum()
"""
print("\nLIST QUESTION 2 - BEGINNER-INTERMEDIATE LEVEL: max(), min(), sum()")
print("-"*80)
print("Question: Find max, min, and sum of elements in a list")
print()

# Main Solution
scores = [45, 89, 23, 67, 92, 78, 56]
print("Scores list:", scores)

maximum = max(scores)
minimum = min(scores)
total = sum(scores)

print("Maximum score:", maximum)
print("Minimum score:", minimum)
print("Sum of all scores:", total)
print("Average score:", total / len(scores))

print("\n✓ Concept: max() returns largest, min() returns smallest, sum() adds all")
print()


"""
================================================================================
LIST QUESTION 3 - INTERMEDIATE LEVEL
================================================================================
Question: Given a list of numbers, remove duplicates and sort the list 
in ascending order. Display the cleaned and sorted list.

Concept: Using set() for removing duplicates, sort() for sorting
"""
print("\nLIST QUESTION 3 - INTERMEDIATE LEVEL: Remove duplicates and sort")
print("-"*80)
print("Question: Remove duplicate numbers from a list and sort it")
print()

# Main Solution
numbers = [5, 2, 8, 2, 9, 1, 5, 3, 2, 8]
print("Original list with duplicates:", numbers)

# Remove duplicates by converting to set, then back to list
unique_numbers = list(set(numbers))
print("After removing duplicates:", unique_numbers)

# Sort the list
unique_numbers.sort()
print("After sorting:", unique_numbers)

print("\n✓ Concept: set() removes duplicates, sort() arranges in order")
print("✓ Note: set() does not preserve order, so convert back to list")
print()


"""
================================================================================
LIST QUESTION 4 - INTERMEDIATE LEVEL
================================================================================
Question: Given a list of items, write code to:
1. Count how many times a specific item appears
2. Find the index position of an item
3. Remove the first occurrence of an item
4. Insert a new item at a specific position

Concept: count(), index(), remove(), insert() methods
"""
print("\nLIST QUESTION 4 - INTERMEDIATE LEVEL: Multiple list operations")
print("-"*80)
print("Question: Perform count(), index(), remove(), and insert() operations")
print()

# Main Solution
fruits = ["Apple", "Banana", "Orange", "Apple", "Grape", "Apple", "Banana"]
print("Original list:", fruits)
print()

# Count occurrences
apple_count = fruits.count("Apple")
print("Count of 'Apple':", apple_count)

# Find index
orange_index = fruits.index("Orange")
print("Index of 'Orange':", orange_index)

# Remove first occurrence
print("\nRemoving first 'Apple'...")
fruits.remove("Apple")
print("After remove('Apple'):", fruits)

# Insert at specific position
print("\nInserting 'Mango' at index 2...")
fruits.insert(2, "Mango")
print("After insert(2, 'Mango'):", fruits)

print("\n✓ Concept: count() counts, index() finds position,")
print("           remove() deletes first occurrence, insert() adds at position")
print()


"""
================================================================================
LIST QUESTION 5 - MEDIUM LEVEL
================================================================================
Question: Given two lists - one with names and one with scores, 
merge them to create pairs, find the highest score with corresponding name,
and filter names with scores above 75.

Concept: zip(), max() with key, list comprehension or filtering
"""
print("\nLIST QUESTION 5 - MEDIUM LEVEL: Working with multiple lists")
print("-"*80)
print("Question: Merge two lists, find top scorer, and filter by threshold")
print()

# Main Solution
names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"]
scores = [85, 92, 78, 88, 95, 72]

print("Names:", names)
print("Scores:", scores)
print()

# Create pairs using zip
pairs = list(zip(names, scores))
print("Pairs (name, score):", pairs)
print()

# Find highest score with name
highest_pair = max(pairs, key=lambda x: x[1])
print("Highest scorer:", highest_pair[0], "with score", highest_pair[1])
print()

# Filter scores above 75
print("Students with score > 75:")
high_scorers = [(name, score) for name, score in pairs if score > 75]
for name, score in high_scorers:
    print(f"  - {name}: {score}")

print("\n✓ Concept: zip() combines lists, max() with key finds maximum,")
print("           list comprehension filters with conditions")
print()


# ============================================================================
# TUPLE QUESTIONS START HERE
# ============================================================================

print("\n" + "="*80)
print("                        *** TUPLE QUESTIONS ***")
print("="*80)

"""
================================================================================
TUPLE QUESTION 1 - BEGINNER LEVEL
================================================================================
Question: Create a tuple of 5 fruits, check if a specific fruit exists in it,
and find its position (index).

Concept: Tuple creation, 'in' operator, index() method
"""
print("\nTUPLE QUESTION 1 - BEGINNER LEVEL: Membership and indexing")
print("-"*80)
print("Question: Check if fruit exists in tuple and find its position")
print()

# Main Solution
fruits = ("Apple", "Banana", "Cherry", "Date", "Elderberry")
print("Fruits tuple:", fruits)
print()

# Check membership
if "Banana" in fruits:
    print("'Banana' is in the tuple")
else:
    print("'Banana' is NOT in the tuple")

# Find index
banana_index = fruits.index("Banana")
print("Index of 'Banana':", banana_index)

# Check non-existing item
if "Mango" in fruits:
    print("'Mango' is in the tuple")
else:
    print("'Mango' is NOT in the tuple")

print("\n✓ Concept: 'in' operator checks membership (returns True/False),")
print("           index() returns position of first occurrence")
print()


"""
================================================================================
TUPLE QUESTION 2 - BEGINNER-INTERMEDIATE LEVEL
================================================================================
Question: Given a tuple of numbers, count how many even and odd numbers exist,
and find the sum of all numbers.

Concept: count(), sum(), and basic filtering logic
"""
print("\nTUPLE QUESTION 2 - BEGINNER-INTERMEDIATE LEVEL: Counting and summing")
print("-"*80)
print("Question: Count even/odd numbers and find sum of all numbers")
print()

# Main Solution
numbers = (10, 15, 22, 33, 44, 51, 60, 77, 88, 99)
print("Numbers tuple:", numbers)
print()

# Count sum
total_sum = sum(numbers)
print("Sum of all numbers:", total_sum)
print("Count of numbers:", len(numbers))
print("Average:", total_sum / len(numbers))
print()

# Count even numbers
even_count = sum(1 for num in numbers if num % 2 == 0)
odd_count = sum(1 for num in numbers if num % 2 != 0)

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)

print("\n✓ Concept: sum() adds all elements, len() gets count,")
print("           generator expression filters even/odd")
print()


"""
================================================================================
TUPLE QUESTION 3 - INTERMEDIATE LEVEL
================================================================================
Question: Given a tuple, unpack its elements into separate variables and 
also demonstrate extended unpacking with * to capture multiple values.

Concept: Tuple unpacking, extended unpacking with *
"""
print("\nTUPLE QUESTION 3 - INTERMEDIATE LEVEL: Tuple unpacking")
print("-"*80)
print("Question: Unpack tuple elements into variables (with and without *)")
print()

# Main Solution - Basic unpacking
print("Basic Unpacking:")
student = ("Alice", 95, "A+", "Physics")
print("Student tuple:", student)

name, score, grade, subject = student
print(f"Name: {name}, Score: {score}, Grade: {grade}, Subject: {subject}")
print()

# Extended unpacking with *
print("Extended Unpacking with *:")
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Numbers tuple:", numbers)

first, *middle, last = numbers
print(f"First: {first}")
print(f"Middle: {middle}")
print(f"Last: {last}")
print()

# Another example
a, *rest = (10, 20, 30, 40)
print(f"a = {a}, rest = {rest}")

print("\n✓ Concept: Direct unpacking assigns each element to a variable,")
print("           * captures multiple elements into a list")
print()


"""
================================================================================
TUPLE QUESTION 4 - INTERMEDIATE LEVEL
================================================================================
Question: Given two tuples, combine them, find common elements, 
and count occurrences of a specific value.

Concept: Concatenation, set operations, count() method
"""
print("\nTUPLE QUESTION 4 - INTERMEDIATE LEVEL: Tuple operations")
print("-"*80)
print("Question: Combine tuples, find common elements, and count values")
print()

# Main Solution
tuple1 = (1, 2, 3, 4, 5, 3, 2)
tuple2 = (3, 4, 5, 6, 7, 5, 3)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print()

# Concatenate tuples
combined = tuple1 + tuple2
print("Combined tuple:", combined)
print()

# Find common elements using set intersection
common = tuple(set(tuple1) & set(tuple2))
print("Common elements:", common)
print()

# Count occurrences
count_3_t1 = tuple1.count(3)
count_3_t2 = tuple2.count(3)
count_3_combined = combined.count(3)

print(f"Count of 3 in tuple1: {count_3_t1}")
print(f"Count of 3 in tuple2: {count_3_t2}")
print(f"Count of 3 in combined: {count_3_combined}")

print("\n✓ Concept: + concatenates tuples, set operations find common elements,")
print("           count() works on combined tuples")
print()


"""
================================================================================
TUPLE QUESTION 5 - MEDIUM LEVEL
================================================================================
Question: Given multiple tuples with student data (name, score1, score2, score3),
calculate average score for each student, find the topper, 
and sort by average score in descending order.

Concept: zip(), enumerate(), list comprehension, sorting with key parameter
"""
print("\nTUPLE QUESTION 5 - MEDIUM LEVEL: Working with data tuples")
print("-"*80)
print("Question: Calculate averages, find topper, and sort by performance")
print()

# Main Solution
students = (
    ("Alice", 85, 90, 88),
    ("Bob", 78, 82, 80),
    ("Charlie", 92, 88, 95),
    ("Diana", 88, 91, 89),
    ("Eve", 95, 94, 96)
)

print("Student data (name, score1, score2, score3):")
for student in students:
    print(f"  {student}")
print()

# Calculate average for each student
print("Averages for each student:")
student_averages = []
for name, s1, s2, s3 in students:
    average = (s1 + s2 + s3) / 3
    student_averages.append((name, average))
    print(f"  {name}: {average:.2f}")
print()

# Find the topper (highest average)
topper = max(student_averages, key=lambda x: x[1])
print(f"Topper: {topper[0]} with average {topper[1]:.2f}")
print()

# Sort by average in descending order
sorted_students = sorted(student_averages, key=lambda x: x[1], reverse=True)
print("Ranking (by average score, descending):")
for rank, (name, avg) in enumerate(sorted_students, 1):
    print(f"  {rank}. {name}: {avg:.2f}")

print("\n✓ Concept: Unpacking tuple elements in loops,")
print("           max() with key parameter finds maximum,")
print("           sorted() with key and reverse parameters sorts data")
print()

print("\n" + "="*80)
print("                    ✓ END OF QUESTIONS")
print("="*80)
