
"""Simple password length checker (unsercured) using variables, user input, math & f strings"""

username = input("USERNAME: ")
password = input("PASSWORD: ")

password_length = len(password)
hidden_password = "*" * int(password_length)

print(
    f"{username} your password {hidden_password} is {password_length} characters long"
)
