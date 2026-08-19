"""
================================================================================
                    IMPORTANT LIST METHODS IN PYTHON
================================================================================
List is a mutable, ordered collection of elements. Here are 12+ important
and very useful methods for working with lists.
================================================================================
"""

print("="*80)
print("1. append() - Add a single element at the end of the list")
print("="*80)
friend = ["Apple", "Mango", "Grapes", 3, 3.025, False, "Aakash", "Rohan"]
print("Original list:", friend)
friend.append("Suraj")  # Adds single element at the end
print("After append('Suraj'):", friend)
print()


print("="*80)
print("2. extend() - Add multiple elements from an iterable to the list")
print("="*80)
colors = ["Red", "Blue"]
print("Original list:", colors)
colors.extend(["Green", "Yellow", "Black"])  # Adds multiple elements
print("After extend(['Green', 'Yellow', 'Black']):", colors)
print()


print("="*80)
print("3. insert() - Insert an element at a specific index")
print("="*80)
ls = [15, 45, 5, 3, 25, 7, 95, 3]
print("Original list:", ls)
ls.insert(0, 3333)  # Insert 3333 at index 0
print("After insert(0, 3333):", ls)
print()


print("="*80)
print("4. remove() - Remove the first occurrence of a value (no return)")
print("="*80)
ls = [15, 45, 5, 3, 25, 7, 95, 3]
print("Original list:", ls)
ls.remove(15)  # Removes first occurrence of 15
print("After remove(15):", ls)
print()


print("="*80)
print("5. pop() - Remove and return element at index (default: last element)")
print("="*80)
ls = [15, 45, 5, 3, 25, 7, 95, 3]
print("Original list:", ls)
removed_value = ls.pop(0)  # Remove and return element at index 0
print("Popped value:", removed_value)
print("After pop(0):", ls)
print()


print("="*80)
print("6. sort() - Sort the list in ascending order (modifies original list)")
print("="*80)
ls = [15, 45, 5, 3, 25, 7, 95, 3]
print("Original list:", ls)
ls.sort()  # Sort in ascending order
print("After sort():", ls)
ls.sort(reverse=True)  # Sort in descending order
print("After sort(reverse=True):", ls)
print()


print("="*80)
print("7. reverse() - Reverse the order of elements in the list")
print("="*80)
ls = [15, 45, 5, 3, 25, 7, 95, 3]
print("Original list:", ls)
ls.reverse()  # Reverse the list
print("After reverse():", ls)
print()


print("="*80)
print("8. index() - Return the index of the first occurrence of a value")
print("="*80)
ls = [15, 45, 5, 3, 25, 7, 95, 3]
print("List:", ls)
idx = ls.index(25)  # Find index of 25
print("Index of 25:", idx)
idx = ls.index(3)  # Returns index of first occurrence
print("Index of first occurrence of 3:", idx)
print()


print("="*80)
print("9. count() - Return the number of times a value occurs in the list")
print("="*80)
ls = [15, 45, 5, 3, 25, 7, 95, 3]
print("List:", ls)
count_3 = ls.count(3)  # Count occurrences of 3
print("Number of times 3 appears:", count_3)
count_99 = ls.count(99)  # Value not in list
print("Number of times 99 appears:", count_99)
print()


print("="*80)
print("10. clear() - Remove all elements from the list")
print("="*80)
ls = [15, 45, 5, 3]
print("Original list:", ls)
ls.clear()  # Remove all elements
print("After clear():", ls)
print()


print("="*80)
print("11. copy() - Create a shallow copy of the list")
print("="*80)
original = [10, 20, 30, 40]
print("Original list:", original)
copied = original.copy()  # Create a copy
copied.append(50)  # Modify the copy
print("Copied list:", copied)
print("Original list (unchanged):", original)
print()


print("="*80)
print("12. del - Delete elements at specific index or slice (operator, not method)")
print("="*80)
ls = [10, 20, 30, 40, 50]
print("Original list:", ls)
del ls[0]  # Delete element at index 0
print("After del ls[0]:", ls)
ls2 = [10, 20, 30, 40, 50]
del ls2[1:3]  # Delete slice from index 1 to 2
print("After del ls2[1:3]:", ls2)
print()


print("="*80)
print("BONUS: sum() - Calculate sum of all numeric elements")
print("="*80)
numbers = [5, 5, 8, 8, 4, 10]
print("List:", numbers)
total = sum(numbers)  # Sum all elements
print("Sum of all elements:", total)
print()


print("="*80)
print("BONUS: len() - Get the number of elements in the list")
print("="*80)
items = ["Apple", "Banana", "Cherry", "Date"]
print("List:", items)
length = len(items)  # Get length
print("Length of list:", length)
print()


print("="*80)
print("BONUS: min() & max() - Find minimum and maximum values")
print("="*80)
values = [15, 45, 5, 3, 25, 7, 95, 3]
print("List:", values)
print("Minimum value:", min(values))
print("Maximum value:", max(values))
print()


print("="*80)
print("SUMMARY TABLE OF LIST METHODS")
print("="*80)
summary = """
Method          | Purpose                                  | Returns    | Modifies List
----------------------------------------------------------------------------------------------
append()        | Add single element at end               | None       | Yes
extend()        | Add multiple elements from iterable     | None       | Yes
insert()        | Insert element at specific index        | None       | Yes
remove()        | Remove first occurrence of value        | None       | Yes
pop()           | Remove and return element at index      | Element    | Yes
sort()          | Sort list in ascending/descending order | None       | Yes
reverse()       | Reverse order of elements              | None       | Yes
index()         | Find index of first occurrence         | Index      | No
count()         | Count occurrences of a value           | Count      | No
clear()         | Remove all elements                    | None       | Yes
copy()          | Create shallow copy of list            | New List   | No
del             | Delete element(s) at index/slice       | None       | Yes
len()           | Get number of elements                 | Length     | No
sum()           | Sum of numeric elements                | Sum        | No
min()           | Find minimum value                     | Min Value  | No
max()           | Find maximum value                     | Max Value  | No
"""
print(summary)