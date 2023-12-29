import pyfiglet
import random, string



banner = pyfiglet.figlet_format("PASSWORD MANAGER")
print(banner)

def first():
    # length = GLineEdit_780.get()
    length = input("enter length of your password")
    if length.isdigit():
        length = int(length)
        chars = string.digits + "!@#$%_-[{^&*()`~}].,:" + string.ascii_letters
        return ''.join(random.choice(chars) for _ in range(length))
    else:
        return "check, Is your input is correct"
def check_password_strength(password):
    # Check length
    length = len(password)
    if length < 8:
        return "[Weak] : Password length should be at least 8 characters"
    
    # Check for uppercase, lowercase, digits, and special characters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(not char.isalnum() for char in password)

    # Determine strength
    if has_upper and has_lower and has_digit and has_special:
        return "Your Password is : [Strong] "
    elif (has_upper and has_lower and has_digit) or (has_upper and has_lower and has_special) or (has_upper and has_digit and has_special) or (has_lower and has_digit and has_special):
        return "Your Password is : [Medium]: "
    else:
        return "Your Password is : [Weak] "

# Get user input for the password
print(first())
user_password = input("Enter your password for checking strength : ")
print(check_password_strength(user_password))
exit = input("press any key to exit")
print(exit)

