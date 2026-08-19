marks = {
    "Suraj" : 100,
    "Harry" : 50,
    "Rohan" : 45,
    "list"  : [1,2,9],
    45 : "Shivang"
}

# 01. Return the list of (key , value ) touple 
print(marks.items())

# 02. Return list containing dictionary's key or values according to the context
print(marks.keys())
print(marks.values())

# 03. Update the dictionary with supplies key-value pairs if new then added them in dict
marks.update({"Suraj" : 90 ,"Harry" : 56})
print(marks)

# 04. len of dict
print("The len of dict is",len(marks) )

# 05. Returns the value of specific keys of the given value
print(marks.get("Harry")," this is harry's marks")
print(marks["Harry"], " this is harry's marks")

    # diffrence is 
                    # if the key is not present in the dict it shows none insted of error

print(marks.get("arry")," this is arry's marks")
print(marks["arry"], " this is arry's marks")   # throws error
