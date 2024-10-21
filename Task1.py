"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

# Using set to create a list of unique values (phone numbers)
list_unique_numbers = set()

# Add phone numbers from texts
for text in texts:
    list_unique_numbers.add(text[0])  # Sending number
    list_unique_numbers.add(text[1])  # Receiving number

# Add phone numbers from calls
for call in calls:
    list_unique_numbers.add(call[0])  # Calling number
    list_unique_numbers.add(call[1])  # Receiving number

# Print the result
print(f"There are {len(list_unique_numbers)} different telephone numbers in the records.")
