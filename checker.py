password = input("Enter a password to check: ")

has_number = False
has_upper = False
has_lower = False
has_special = False

for char in password:
    if char.isdigit():
        has_number = True
    if char.isupper():
        has_upper = True
    if char.islower():
        has_lower = True
    if not char.isalnum():
        has_special = True

if len(password) < 8:
    print("Result: Weak (Password is too short.)")
elif "123" in password or "password" in password.lower():
    print("Result: Weak (Too common or easy to guess.)")
elif not (has_number and has_upper and has_lower and has_special):
    print("Result: Weak (Use a mix of uppercase, lowercase, numbers, and symbols.)")
else:
    print("Result: Strong! Good job.")
