# list are mutable we can directly change directly in original

friend = ["Apple", "Mango", "Grapes", 3, 3.025, False, "Aakash", "Rohan"]
print(friend)

a = []            # This is a empty list
print(type(a))

friend[0] = "Changed apple"
print(friend)   # we directly change the original list idx value 0 = Apple

# Slicing also work in list just like string

print(friend[1:4])