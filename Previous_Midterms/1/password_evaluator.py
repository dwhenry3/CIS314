import string 
import pwinput  # Import the pwinput library to hide the password with asterisk 
from common_password_checker import check_common_password

def evaluate_password():
    # Prompt the user to enter a password and hide the input
    password = pwinput.pwinput("Enter a Password: ")

    # Length checker: Check if the password is at least 8 characters long
    if len(password) < 8:
        print("Warning: Password must be at least 8 characters long.")
        return  # Exit the function if the password is too short

    # Space checker: Check if the password contains any spaces
    if ' ' in password:
        print("Warning: Password should not contain spaces.")
        return  # Exit the function if the password contains spaces
    
    # Initialize password strength and feedback
    strength = 0
    feedback = ''
    
    # Initialize counters for character types
    lower_case_count = 0
    upper_case_count = 0
    num_count = 0
    special_char_count = 0

    if check_common_password(password):
        print("Warning: This is a commonly used password and is not secure.")
        return  # Exit the function if the password is common
    
    # Count the types of characters in the password
    for char in password:
        if char in string.ascii_lowercase:
            lower_case_count += 1  # Increment count for lowercase letters
        elif char in string.ascii_uppercase:
            upper_case_count += 1  # Increment count for uppercase letters
        elif char in string.digits:
            num_count += 1  # Increment count for digits
        else:
            special_char_count += 1  # Increment count for special characters

    # Determine password strength based on character type counts
    if lower_case_count >= 1:
        strength += 1  # At least one lowercase letter contributes to strength
    if upper_case_count >= 1:
        strength += 1  # At least one uppercase letter contributes to strength
    if num_count >= 1:
        strength += 1  # At least one digit contributes to strength
    if special_char_count >= 1:
        strength += 1  # At least one special character contributes to strength

    # Adjust the feedback based on the calculated strength
    if strength == 1:
        feedback = "Very weak. Change immediately!"
    elif strength == 2:
        feedback = "Weak. Add a mix of characters."
    elif strength == 3:
        feedback = "Moderate. Consider changing."
    elif strength == 4:
        feedback = "Strong"

    # Display the counts of different character types in the password
    print('Your password has: ')
    print(f"{lower_case_count} lowercase characters")
    print(f"{upper_case_count} uppercase characters")
    print(f"{num_count} numeric characters")
    print(f"{special_char_count} special characters")

    # Display the strength and feedback of the password
    print(f"Password Strength: {strength}")
    print(f"Feedback: {feedback}")
