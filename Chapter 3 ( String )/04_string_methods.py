# 01. .strip() method
# The .strip() method is used to remove any leading and trailing whitespace characters from a string    

raw_user_input = "  DataScientist_2024  "

# Remove whitespace and standardize to lowercase

clean_input = raw_user_input.strip().lower()
print(f"Original: '{raw_user_input}'")
print(f"Cleaned: '{clean_input}'")

# Output:
# Original: '  DataScientist_2024  '
# Cleaned: 'datascientist_2024'

# 02. .replace() method
# The .replace() method is used to replace occurrences of a substring with another substring

text = "Hello, World!"
new_text = text.replace("World", "Python")
print(f"Original: {text}")
print(f"Modified: {new_text}")

# Output:
# Original: 'Hello, World!'
# Modified: 'Hello, Python!'


# 03. Splitting and Joining Data

# A common raw log format
log_entry = "2023-10-01|USER_LOGIN|SUCCESS"

# Split by the pipe delimiter
parts = log_entry.split("|")
date, event, status = parts

# Reconstruct into a more readable format
formatted_log = f"{event} recorded on {date} with status: {status}"
print(formatted_log)

# Output:
# USER_LOGIN recorded on 2023-10-01 with status: SUCCESS


# 04. Formatting Strings for Analysis

accuracy = 0.94567
model_version = 2
# Format accuracy to 2 decimal places and include version
report = f"Model v{model_version} achieved accuracy: {accuracy:.2%}"
print(report)

# Output:
# Model v2 achieved accuracy: 94.57%


# 05. .upper() method
# The .upper() method converts all alphabetic characters in a string to uppercase

message = "welcome to python"
uppercase_message = message.upper()
print(f"Original: {message}")
print(f"Uppercase: {uppercase_message}")

# Output:
# Original: welcome to python
# Uppercase: WELCOME TO PYTHON


# 06. .count() method
# The .count() method counts how many times a substring appears in a string

sentence = "Python is easy, and Python is powerful."
python_count = sentence.count("Python")
print(f"The word 'Python' appears {python_count} times.")

# Output:
# The word 'Python' appears 2 times.


# 07. .startswith() method
# The .startswith() method checks whether a string begins with a specific substring

filename = "report_2024.pdf"
is_report = filename.startswith("report")
print(f"Is this a report file? {is_report}")

# Output:
# Is this a report file? True


# 08. .isdigit() method
# The .isdigit() method checks whether all characters in a string are digits

user_age = "25"
valid_age = user_age.isdigit()
print(f"Is '{user_age}' a valid number? {valid_age}")

# Output:
# Is '25' a valid number? True


# 09. .endswith() method
# The .endswith() method checks whether a string ends with a specific substring

file_name = "notes.txt"
is_text_file = file_name.endswith(".txt")
print(f"Is '{file_name}' a text file? {is_text_file}")

# Output:
# Is 'notes.txt' a text file? True


# 10. .find() method
# The .find() method returns the position of the first occurrence of a substring

email = "student@example.com"
at_position = email.find("@")
print(f"The @ symbol is at position {at_position}.")

# Output:
# The @ symbol is at position 7.


# 11. .title() method
# The .title() method converts the first letter of each word to uppercase

book_title = "learning python step by step"
formatted_title = book_title.title()
print(f"Formatted title: {formatted_title}")

# Output:
# Formatted title: Learning Python Step By Step


# 12. .join() method
# The .join() method combines elements of a list into one string

words = ["Python", "is", "fun"]
joined_sentence = " ".join(words)
print(joined_sentence)

# Output:
# Python is fun