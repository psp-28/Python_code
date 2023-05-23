char = []
for i in range(65, 91):
     if i in range(91, 97):     # also prints small case letters.
        continue
    char.append(chr(i))         # "chr()" is used to generate character from ascii value, vise versa "ord()".
    
print(char)
    