from password_evaluator import evaluate_password

def get_password(another_password=False):
    # Ask the user if they want to enter another password
    if another_password:
        choice = input('Do you want to enter another pwd (y/n): ')
    else:
        choice = input('Do you want to check pwd (y/n): ')

    # Return True if the user wants to continue, otherwise return False
    if choice.lower() == 'y':
        return True
    elif choice.lower() == 'n':
        return False
    else:
        # If the input is invalid, ask again
        print('Invalid, Try Again')
        return get_password(another_password)

    
password_check = get_password()  # Ask the user if they want to check a password
while password_check:  # Repeat until the user chooses to stop
    evaluate_password()  # Call the password check function
    password_check = get_password(True)  # Ask again if they want to enter another password