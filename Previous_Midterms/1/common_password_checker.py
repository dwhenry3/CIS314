# Function to check if it is a commonly used password
def check_common_password(password):
    try:
        # Open the file containing common passwords for reading
        with open('CommonPasswords.txt', 'r') as f:
            # Read all lines and store them as a list
            common = f.read().splitlines()
        # Check if the password entered by user is in the list of common passwords
        if password in common:
            return True  # Return True if it is a common password
    except FileNotFoundError:
        # Warn if the file is not found
        print("Warning: 'CommonPasswords.txt' file not found.")
    return False  # Return False if the password is not common or the file was not found