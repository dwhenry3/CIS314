import re

password_file = "Password_file.txt" # variable storing a text file where weak passwords will be written

def password_strength(password):
    strength = 0 # intialize the password strength
    feedback = [] # empty list to store feedback


    if len(password) >=8: # check if password is 8 characters long
        strength +=1 # if true increase strength by 1
    else:
        feedback.append("Password should be at least 8 characters long.")  # if not return this
    
    if re.search(r'[a-z]', password): # uses regular expressions to check if password includes a lowercase letter
        strength+=1 
    else: 
        feedback.append("Password needs at least one lowercase letter.")
    
    if re.search(r'[A-Z]', password):
        strength+=1
    else:
        feedback.append("Passowrd needs at least one uppercase letter.")
    
    if re.search(r'[0-9]', password):
        strength+=1
    else:
        feedback.append("Password needs at least one digit.")
    
    if re.search(r'[!@#$%^&*(),.?":{}|<>]',password):
        strength+=1
    else:
        feedback.append("Password needs at least one special character.")
    
    if not re.search(r'(password|123|admin|forget)',password, re.IGNORECASE): # ignorecase recognizes patterns no matter the capitalization
        strength+=1
    else:
        feedback.append("Avoid using common passwords like password, 123, admin, and forget")
    
    if strength >= 6: # Determine overall strength of password
        return "Strong Password!", feedback
    
    elif strength >= 4: # Determine if it's moderate
        return "Moderate password, could use some strengthing.", feedback
    else:  # Determine if it's weak
        return "Weak password, needs improvement.",feedback 
    
def save_feedback(feedback):
    # append feedback to password file
    with open(password_file, "a") as f: # open with the append mode
        f.write("Password Feedback: " + "".join(feedback) + "\n")  # Join feedback with a comma


if __name__ ==  "__main__": # Driver code
    password = input("Create a password:") # Have the user enter a password
    result, suggestions = password_strength(password) # call the password function and run password through
    print(result)

    if suggestions: # print suggestions for strengthing password
        print("Suggestions to improve:") 
        for suggestions in suggestions:
            print(f"-{suggestions}") # Print each suggestions
    
    # if password is weak save to password file
    if result.startswith("Weak"):
        print(f"Saving feedback to {password_file}")
        save_feedback(suggestions) # call save function to store suggestions 

    


    


