num = int (input ("Enter a number: "))

str_num = str(num)
length = len(str_num)

sum_of_powers = 0
temp_num = num

while temp_num > 0:
    digit = temp_num % 10
    sum_of_powers += digit ** length
    temp_num //= 10 

if sum_of_powers == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")