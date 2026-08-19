# Python Operators
# Operators are symbols or keywords used to perform operations on values.


# 1. Arithmetic Operators
# + addition, - subtraction, * multiplication, / division
# // floor division, % remainder (modulus), ** exponentiation
first_number = 17
second_number = 5

print("\nARITHMETIC OPERATORS")
print("Addition:", first_number + second_number)              # 22
print("Subtraction:", first_number - second_number)           # 12
print("Multiplication:", first_number * second_number)        # 85
print("Division:", first_number / second_number)               # 3.4
print("Floor division:", first_number // second_number)       # 3
print("Remainder:", first_number % second_number)             # 2
print("Exponentiation:", second_number ** 2)                  # 25

# @ is the matrix multiplication operator. It is used with matrix-like
# objects, such as lists of lists when using a library like NumPy.


# 2. Assignment Operators
print("\nASSIGNMENT OPERATORS")
score = 10
print("= :", score)                 # Assign 10 to score
score += 5
print("+=:", score)                 # score = score + 5 -> 15
score -= 3
print("-=:", score)                 # score = score - 3 -> 12
score *= 2
print("*=:", score)                 # score = score * 2 -> 24
score /= 4
print("/=:", score)                 # score = score / 4 -> 6.0
score //= 2
print("//=:", score)                # score = score // 2 -> 3.0
score %= 2
print("%=:", score)                 # score = score % 2 -> 1.0
score **= 3
print("**=:", score)                # score = score ** 3 -> 1.0

bitwise_value = 12                  # Binary: 1100
bitwise_value &= 10                 # 1100 & 1010 -> 1000
print("&=:", bitwise_value)        # 8
bitwise_value |= 3                  # 1000 | 0011 -> 1011
print("|=:", bitwise_value)        # 11
bitwise_value ^= 1                  # 1011 ^ 0001 -> 1010
print("^=:", bitwise_value)        # 10
bitwise_value <<= 1                 # 1010 << 1 -> 10100
print("<<=:", bitwise_value)       # 20
bitwise_value >>= 2                 # 10100 >> 2 -> 00101
print(">>=:", bitwise_value)       # 5

# @ is matrix multiplication and @= is augmented matrix multiplication.
# They are used with matrix-like objects, for example NumPy arrays:
# result = matrix_a @ matrix_b
# matrix_a @= matrix_b


# 3. Comparison Operators
left_value = 8
right_value = 5

print("\nCOMPARISON OPERATORS")
print("Equal (==):", left_value == right_value)                # False
print("Not equal (!=):", left_value != right_value)            # True
print("Greater than (>):", left_value > right_value)           # True
print("Less than (<):", left_value < right_value)              # False
print("Greater than or equal (>=):", left_value >= right_value) # True
print("Less than or equal (<=):", left_value <= right_value)    # False


# 4. Logical Operators
has_id = True
is_adult = False

print("\nLOGICAL OPERATORS")
print("and:", has_id and is_adult)     # True only when both are True
print("or:", has_id or is_adult)       # True when at least one is True
print("not:", not has_id)              # Reverses True to False


# 5. Bitwise Operators
# Bitwise operators work on the binary representation of integers.
bit_a = 6       # Binary: 110
bit_b = 3       # Binary: 011

print("\nBITWISE OPERATORS")
print("AND (&):", bit_a & bit_b)       # 2  (010)
print("OR (|):", bit_a | bit_b)        # 7  (111)
print("XOR (^):", bit_a ^ bit_b)       # 5  (101)
print("NOT (~):", ~bit_a)              # -7
print("Left shift (<<):", bit_a << 1)  # 12 (1100)
print("Right shift (>>):", bit_a >> 1) # 3  (011)


# 6. Membership Operators
languages = ["Python", "Java", "C++"]

print("\nMEMBERSHIP OPERATORS")
print("in:", "Python" in languages)         # True
print("not in:", "Ruby" not in languages)   # True


# 7. Identity Operators
# is checks whether two names refer to the same object. Use == to compare
# values instead of is.
first_list = [1, 2, 3]
second_list = first_list
third_list = [1, 2, 3]

print("\nIDENTITY OPERATORS")
print("is:", first_list is second_list)         # True
print("is not:", first_list is not third_list)   # True
print("Value comparison (==):", first_list == third_list)  # True


# 8. Walrus Operator (:=)
# It assigns a value and returns that value in the same expression.
print("\nWALRUS OPERATOR")
if (name_length := len("Python")) > 5:
	print("The word length is", name_length)     # 6

# Example of using the walrus operator in a while loop to get user input until "quit" is entered.
while (user_input := input("Enter a command: ")) != "quit":
    print(f"You entered: {user_input}")


# 9. Conditional (Ternary) Expression
# Syntax: value_if_true if condition else value_if_false
print("\nCONDITIONAL EXPRESSION")
number = 12
result = "even" if number % 2 == 0 else "odd"
print(number, "is", result)                       # 12 is even


# Operator precedence
# Parentheses can be used to make the intended order explicit.
answer = 2 + 3 * 4
parenthesized_answer = (2 + 3) * 4
print("\nOPERATOR PRECEDENCE")
print("2 + 3 * 4 =", answer)                       # 14
print("(2 + 3) * 4 =", parenthesized_answer)      # 20
