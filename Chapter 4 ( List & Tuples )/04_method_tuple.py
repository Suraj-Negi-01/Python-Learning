"""
================================================================================
                    IMPORTANT TUPLE METHODS IN PYTHON
================================================================================
Tuple is an immutable, ordered collection of elements. Although tuples have
fewer methods than lists (due to immutability), they provide several important
and very useful operations. Here are 12+ important tuple methods and operations.
================================================================================
"""

print("="*80)
print("1. count() - Count occurrences of a value in the tuple")
print("="*80)
t = (25, 56, 5, 5, 89, 4, 4, 4, 58, 6)
print("Tuple:", t)
count = t.count(4)  # Count how many times 4 appears
print("Count of 4 in tuple:", count)
count = t.count(5)  # Count another value
print("Count of 5 in tuple:", count)
print()


print("="*80)
print("2. index() - Find the index of first occurrence of a value")
print("="*80)
t = (25, 56, 5, 5, 89, 4, 4, 4, 58, 6)
print("Tuple:", t)
idx = t.index(89)  # Find index of 89
print("Index of 89:", idx)
idx = t.index(5)  # Returns index of first occurrence
print("Index of first occurrence of 5:", idx)
print()


print("="*80)
print("3. len() - Get the number of elements in the tuple")
print("="*80)
t = (25, 56, 5, 5, 89, 4, 4, 4, 58, 6)
print("Tuple:", t)
length = len(t)  # Get length
print("Length of tuple:", length)
print()


print("="*80)
print("4. sum() - Calculate sum of all numeric elements")
print("="*80)
numbers = (5, 5, 8, 8, 10, 4)
print("Tuple:", numbers)
total = sum(numbers)  # Sum all elements
print("Sum of all elements:", total)
print()


print("="*80)
print("5. min() - Find minimum value in the tuple")
print("="*80)
values = (25, 56, 5, 5, 89, 4, 4, 4, 58, 6)
print("Tuple:", values)
minimum = min(values)  # Find minimum
print("Minimum value:", minimum)
print()


print("="*80)
print("6. max() - Find maximum value in the tuple")
print("="*80)
values = (25, 56, 5, 5, 89, 4, 4, 4, 58, 6)
print("Tuple:", values)
maximum = max(values)  # Find maximum
print("Maximum value:", maximum)
print()


print("="*80)
print("7. sorted() - Return a sorted list from tuple elements")
print("="*80)
t = (25, 56, 5, 5, 89, 4, 4, 4, 58, 6)
print("Original tuple:", t)
sorted_list = sorted(t)  # Returns sorted list
print("Sorted list:", sorted_list)
sorted_desc = sorted(t, reverse=True)  # Sorted in descending order
print("Sorted descending:", sorted_desc)
print()


print("="*80)
print("8. in operator - Check if value exists in tuple (membership test)")
print("="*80)
t = (25, 56, 5, 5, 89, 4, 4, 4, 58, 6)
print("Tuple:", t)
print("Is 58 present in tuple:", 58 in t)
print("Is 68 present in tuple:", 68 in t)
print("Is 4 present in tuple:", 4 in t)
print()


print("="*80)
print("9. Tuple Unpacking - Assign tuple elements to variables")
print("="*80)
tupp = (5, 6, 1)
print("Tuple:", tupp)
a, b, c = tupp  # Unpack tuple into variables
print("After unpacking: a =", a, ", b =", b, ", c =", c)

# Extended unpacking with *
extended = (1, 2, 3, 4, 5)
x, *middle, y = extended  # Unpack with * to capture multiple values
print("From tuple (1,2,3,4,5): x =", x, ", middle =", middle, ", y =", y)
print()


print("="*80)
print("10. enumerate() - Get index and value pairs from tuple")
print("="*80)
fruits = ("Apple", "Banana", "Cherry", "Date")
print("Tuple:", fruits)
print("Using enumerate:")
for index, value in enumerate(fruits):
    print(f"  Index {index}: {value}")
print()


print("="*80)
print("11. zip() - Combine multiple tuples element-wise")
print("="*80)
names = ("Alice", "Bob", "Charlie")
ages = (25, 30, 35)
print("Names tuple:", names)
print("Ages tuple:", ages)
combined = list(zip(names, ages))  # Combine tuples
print("Combined using zip:", combined)
print()


print("="*80)
print("12. any() - Check if any element is True/Truthy")
print("="*80)
t1 = (0, 0, 0, 0)
t2 = (0, 0, 1, 0)
t3 = (False, False, True, False)
print("Tuple (0, 0, 0, 0):", any(t1))
print("Tuple (0, 0, 1, 0):", any(t2))
print("Tuple (False, False, True, False):", any(t3))
print()


print("="*80)
print("13. all() - Check if all elements are True/Truthy")
print("="*80)
t1 = (1, 2, 3, 4)
t2 = (1, 2, 0, 4)
t3 = (True, True, True, True)
print("Tuple (1, 2, 3, 4):", all(t1))
print("Tuple (1, 2, 0, 4):", all(t2))
print("Tuple (True, True, True, True):", all(t3))
print()


print("="*80)
print("14. reversed() - Get reversed iterator of tuple")
print("="*80)
t = (1, 2, 3, 4, 5)
print("Original tuple:", t)
reversed_list = list(reversed(t))  # Convert reversed iterator to list
print("Reversed tuple:", reversed_list)
print()


print("="*80)
print("15. tuple() - Convert other iterables to tuple")
print("="*80)
lst = [1, 2, 3, 4, 5]
print("List:", lst)
t = tuple(lst)  # Convert list to tuple
print("Converted to tuple:", t)
string = "Hello"
t_str = tuple(string)  # Convert string to tuple
print("String 'Hello' converted to tuple:", t_str)
print()


print("="*80)
print("BONUS: Slicing - Extract portion of tuple")
print("="*80)
t = (10, 20, 30, 40, 50, 60, 70)
print("Original tuple:", t)
print("t[1:4]:", t[1:4])  # Elements from index 1 to 3
print("t[::2]:", t[::2])  # Every 2nd element
print("t[::-1]:", t[::-1])  # Reversed (all elements, step -1)
print()


print("="*80)
print("SUMMARY TABLE OF TUPLE METHODS")
print("="*80)
summary = """
Method/Operation | Purpose                                    | Returns    | Modifies Tuple
----------------------------------------------------------------------------------------------
count()          | Count occurrences of a value               | Count      | No
index()          | Find index of first occurrence            | Index      | No
len()            | Get number of elements                    | Length     | No
sum()            | Sum of numeric elements                   | Sum        | No
min()            | Find minimum value                        | Min Value  | No
max()            | Find maximum value                        | Max Value  | No
sorted()         | Return sorted list from tuple             | List       | No
in operator      | Check if value exists in tuple            | Boolean    | No
Unpacking        | Assign tuple elements to variables        | Variables  | No
enumerate()      | Get index and value pairs                 | Iterator   | No
zip()            | Combine multiple tuples                   | Tuples     | No
any()            | Check if any element is truthy            | Boolean    | No
all()            | Check if all elements are truthy          | Boolean    | No
reversed()       | Get reversed iterator                     | Iterator   | No
tuple()          | Convert iterable to tuple                 | Tuple      | No
Slicing         | Extract portion of tuple using [:]        | Tuple      | No
"""
print(summary)

print("="*80)
print("KEY DIFFERENCES: TUPLE vs LIST")
print("="*80)
differences = """
Feature              | Tuple           | List
----------------------------------------------------------------------------------------------
Mutability           | Immutable       | Mutable
Syntax               | (a, b, c)       | [a, b, c]
Can modify elements  | No              | Yes
Can add elements     | No              | Yes
Can remove elements  | No              | Yes
Performance          | Faster          | Slower
Memory               | Less memory     | More memory
Hashable (dict key)  | Yes             | No
Methods available    | Few (count, index) | Many (append, remove, sort, etc.)
Use case             | Fixed collections, dictionary keys | Dynamic collections
"""
print(differences)