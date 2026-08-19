# dict store key value pair it is mutable can't contain duplicate key

marks = {
    "Suraj" : 100,
    "Harry" : 50,
    "Rohan" : 45,
    "list"  : [1,2,9],
    45 : "Shivang"
}

print(marks,type(marks))
print(marks["list"])
print(marks["Rohan"], "This is the marks of Rohan")
print(marks[45], "'s marks is 45")