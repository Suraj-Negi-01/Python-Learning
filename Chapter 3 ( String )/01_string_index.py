a = "surajnegi"
print(a)

# String slicing

b = a[0:5] # Go 0 to 3 means len - 1
print(b)

d = a[1] # print single char according to index
print(d)

# Negative indexing
# Negative indexing not includes 0 start with -1 at last

z = "surajsingh"

c = z[-10:-5] # Print from -10 to len - 1 means -4
print(c)

# Slicing with single value

a = "surajnegi"

g = a[1:] # Go from 1 to last print all accept 0
print(g)

h = a[:5] # Same logic start to idx 5
print(h)

# Slicing with jump

s = "rahulsharma"

e = s[0:11:2] # rhlhra prints cause jumping 2 step
print(e)