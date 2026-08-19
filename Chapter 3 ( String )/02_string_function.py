a = "suraj negi is aa legit aa aa" # lenght = 10

# 1. len function
print("the length is :",len(a))

# 2. Check str end or start with 
print("Is the name ends with gi :", a.endswith("gi"))
print("Is the name start with su :", a.startswith("su"))

# 3. Do str upper and lower case
print("the first letter is in uppercase :", a.capitalize() ) # Do first letter capital
print("the  word is in uppercase :", a.upper() )             # Do all in uppercase
print("the first letter is in lowercase :", a.lower() )      # Do all in lowercase
print("the every first word is in uppercase :", a.title() )  # Do every words first letter in captal

# 4. Count occurence of char and world in senternce
print("the word aa is", a.count("aa"),"times in the senterce" )

# 5. find the word and return the index of first char in sentence
print("the  word aa is in the index :", a.find("aa"))

# 6. Replace the world from the string 
print("the  word aa is now replaced to pp in the sentence :", a.replace("aa","pp") )