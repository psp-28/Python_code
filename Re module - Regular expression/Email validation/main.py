import re
 
def is_valid_email(email):
    pattern = r'^[\w\.-]+@[a-zA-Z\d]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
 
# Example usage:
print(is_valid_email("example@email.com"))      # Output: True
print(is_valid_email("invalid.email@"))         # Output: False
print(is_valid_email("another.example@domain")) # Output: False
print(is_valid_email("user123@domain.uk"))   # Output: True