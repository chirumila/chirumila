import re

def assess_password_strength(password):
    strength = 0
    feedback = []
    
    # Criteria 1: Length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    # Criteria 2: Uppercase and Lowercase Letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should include both uppercase and lowercase letters.")
        
    # Criteria 3: Numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one number.")
        
    # Criteria 4: Special Characters
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password should include at least one special character.")
    
    # Overall feedback
    if strength == 4:
        feedback.append("Your password is strong.")
    elif strength == 3:
        feedback.append("Your password is good, but could be stronger.")
    elif strength == 2:
        feedback.append("Your password is weak. Consider improving it.")
    else:
        feedback.append("Your password is very weak. Consider improving it significantly.")
    
    return strength, feedback

def main():
    while True:
        password = input("Enter a password to assess its strength (or 'q' to quit): ")
        if password.lower() == 'q':
            break
        
        strength, feedback = assess_password_strength(password)
        print(f"Password Strength: {strength}/4")
        for comment in feedback:
            print(comment)
        print()

if __name__ == "__main__":
    main()
