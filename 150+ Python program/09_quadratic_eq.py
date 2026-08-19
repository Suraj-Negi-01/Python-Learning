import math 

print("Enter the cofficient for the standard form of quadratic equation")
print("which is = ax^2 + bx +c")

a = float ( input("Enter the cofficient of a :"))
b = float ( input("Enter the cofficient of b :"))
c = float ( input("Enter the cofficient of c :"))

discriminent = b**2 - 4*a*c

if discriminent > 0 :
    root1 = (-b + math.sqrt(discriminent) / (2*a))
    root2 = (-b - math.sqrt(discriminent) / (2*a))

    print(f"Root 1 : {root1}")
    print(f"Root 2 : {root2}")

elif discriminent == 0 :
    root = -b / (2*a)

    print(f"Root : {root}")

else : 
    real_part = -b / (2*a)
    imag_part = math.sqrt(abs(discriminent)) / (2*a)

    print(f"Root 1 : {real_part} + {imag_part}i")
    print(f"Root 2 : {real_part} - {imag_part}i")