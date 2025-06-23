import re
 
def extract_dates(text):
    pattern = r'\b\d{4}-\d{2}-\d{2}\b'
    dates = re.findall(pattern, text)
    return dates
 
# Example usage:
text = "Events on 2023-05-15 and 2023-06-20 are important."
print(extract_dates(text))  # Output: ['2023-05-15', '2023-06-20']
 
text2 = "No dates in this text."
print(extract_dates(text2)) # Output: []