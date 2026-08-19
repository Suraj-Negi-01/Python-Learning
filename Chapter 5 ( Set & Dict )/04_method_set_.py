s = {1, 5, 5, 5, 86, 87, 25, 36, "harry", "harry"}

# 01. Adding the eliments in a set in assending order
s.add(111)
s.add(11)
print(s)

# 02. Clears the set and throw the empty set
s.clear()
print(s , "This happend after s.clear throws an empty set")

s = {1, 5, 5, 5, 86, 87, 25, 36, "harry", "harry"}

# 03. coping the set in another set
ss = set()
ss = s.copy()

print(ss, "Eliment of set s in ss copied succesfully !")

# 03. Diff between two set a-b

a = {1, 2, 3}
b = {3, 4, 5}

print(a.difference(b)) # Returns a new set

# 04. Diff between two set a-b

a = {1, 2, 3}
b = {3, 4, 5}
a.difference_update(b)
print(a)

# 05. Union and intersaction in a set

a = {1, 2, 3}
b = {3, 4, 5}

c = a.union(b) # prints all eliment present in both set
print(c)

d = a.intersection(b)
print(d) # prints the common eliment in both set

# 06. Removing methods

a = {9, 5, 2, 4, 5, 6, 7}  # remove rendom eliment generally smallest one and return also
b = a.pop()
print(b)
print(a)

b = a.remove(9)
print(b)  # returns nothing only removes the eliment
print(a)