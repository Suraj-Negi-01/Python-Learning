# tuple are immutable we can not directly change it make chenges on copy

a = (2, False ,676,8,8, "rohan", 45.33)
print(a)
print(type(a))

b = ()          # This is empty tuple 
print(type(b))

# make one eliment tuple 

a = (1)     # this is the wrong way to make one eliment tuple 
print(a)
print(type(a)) 


a = (1,)       # this is the right way to right way to write single eliment tuple
print(a)
print(type(a)) 


