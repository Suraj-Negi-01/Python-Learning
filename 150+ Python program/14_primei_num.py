a = int ( input("Enter the num :"))

flag = False

if (a == 1) :
    print(f"{a} is not a prime number")

for i in range(2 , a-1) :

    if (a % i) == 0 :
        flag = True
        break

if (flag == True) :
    print(f"{a} is not a prime number ")

else :
    print(f"{a} is a prime number ")