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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# Initialise two sets: 
# "list_of_numbers" for the list of possible telemarketers 
# "list_of_non_telemarketers" for the list of numbers that are not telemarketers
list_of_numbers = set()
list_of_non_telemarketers = set()

# Iterate through calls list to extract callers and receivers.
for call in calls:
    list_of_numbers.add(call[0])
    list_of_non_telemarketers.add(call[1])

# Iterate through texts list to extract numbers that sent and/or received a text.
for text in texts:
    list_of_non_telemarketers.add(text[0])
    list_of_non_telemarketers.add(text[1])

# Using the ".difference_update" method of "set" to remove those numbers
# that appear in the list of numbers that received a call, and/or sent or received a text.
list_of_numbers.difference_update(list_of_non_telemarketers)

# Print the result in lexicographic order.
print("These numbers could be telemarketers: ")
for number in sorted(list_of_numbers):
    print(number)
