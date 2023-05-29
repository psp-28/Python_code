# Create a list of alphabets so that we can match the alphabets, and also copy the alphabet list and paste the same so that the list of alphabets repeats 2 time because if shift of letter z occurs then it will start from letter 'a' next to z.


alpha = []
alphabet = []
for i in range(97, 123):                            # 97 to 123 is an ascii value to get small case alphabets.
    alphabet.append(chr(i))
alpha = alphabet.copy()

for j in range(1):          
    alphabet += alpha
#print(alphabet)
#--------------------------------------------------------

## Create a single function name "Caesar" instead of using 2 different function encrypt and decrypt.
#def caesar(start_text, shift_number, cipher_option):

#    end_text = ""
#    if cipher_option == "decode":
#        shift_number * = -1                 # It wil be like - 5 *(-1) = -5
#        
#    for letter in start_text:
#        position = alphabet.index(letter)
#        if cipher_option == "encode:
#            new_position = position + shift_number
#        elif cipher_option == "decode":
#            new_position = position - shift_number
#        else:
#            print("\n\t\t\t\t\tError!!! \nAccepted options are 'encode' and 'decode' only.")
            

##        new_position = position = shift_number
##        
#        new_letter = alphabet[new_position]
#        end_text += new_letter
#    print("\nYour {cipher_option}d text is: {}".format(end_text))



def encrypt(plain_text, shift_number):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        cipher_text += new_letter
#    print(f"The encoded text is : {cipher_text}")
    return cipher_text
    
    
def decrypt(cipher, shift_number):
    plain_msg = ""
    for letter1 in cipher:
        position1 = alphabet.index(letter1)
        new_position1 = position1 - shift_number
        new_letter1 = alphabet[new_position1]
        plain_msg += new_letter1
    return plain_msg    
    
    
      
# take input as plain_text, and number of shift to be performed.
option = input("\n Type'encode' to encrypt and 'decode' to decrypt : ").lower()

# Use this variable when using Caesar function.
#text2 = input("\nType your message here: \n").lower()
#shift2 = int(input("\nEnter the shift number: "))
#caesar(start_text = text2, shift_number = shift2, cipher_option = option)

    
    
if option == 'encode':
    check = ""
    message = input("Type your message here \n")
    text = message.lower()
    shift = int(input("\nType the shift number : "))
    encrypted = encrypt(text, shift)
    check = encrypted
    print("\nEncrypted text is also : {}".format(encrypted))
    if check == "":                                             # check if the the message is empty or not.
        print("\nEmpty Message")
    else:
        print("\nEncrypted message")
    
elif option == 'decode':
    message1 = input("Type your message here \n")
    text1 = message1.lower()
    shift1 = int(input("\nType the shift number : "))
    decrypted = decrypt(cipher = text1, shift_number = shift1)
    print("\nDecrypted text is : {}".format(decrypted))
    
else:
    print("\nThe typed option is not available, please select 'encode' or 'decode' only.")