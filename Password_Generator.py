# Python code to genrate the password.
# Password should contain Alphabets, Numbers and Special characters.
# Ask for number of letters, number of numbers and number of special characters should password contain.
# Use random module to randomly select password characters.

import random

## code to generate the list of alphabets letters.
#char = []
#for i in range(65, 91):
#     if i in range(91, 97):     # also prints small case letters.
#        continue
#    char.append(chr(i))


letters =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '-', '_']

print("Welcome to the password generator !!!")
#Ask for the inputs.

let = int(input("\n\nEnter the number of alphabet characters you need in your password : "))
num = int(input("\nEnter the number of Numerals you need in your password: "))
sym = int(input("\nEnter the number of special characters you need in your password: "))

# Create an empty string to store the password.
password_list = []


#For getting random Letters.
for char in range(1, let+1):                        # +1 is because if range is from 1 to 5 then it will print only upto 4 but                                                          we want to get the exact input as user states.     
    password_list.append(random.choice(letters))               # (OR) password += random_char.
    

#For getting random numbers.
for char in range(1, num+1):
    password_list += random.choice(numbers)
    
    
# For Random Special characters.
for char in range(1, sym+1):
    password_list += random.choice(symbols)

# Shuffle all the characters in the password.

    
#print(password_list)

random.shuffle(password_list)
#print(password_list)


# Now to convert the list into string.
password = ""                   # Create an empty string.

for char in password_list:
    password += char

print(f"\nYour Password is : {password}")
