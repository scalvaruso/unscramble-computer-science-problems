"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

total_time_per_number = {}  # Dictionary to track total time spent by each phone number
total_time = 0  
telephone_number = None

# Add phone numbers and their call durations
for call in calls:

    # Update caller's total time
    total_time_per_number[call[0]] = total_time_per_number.get(call[0], 0) + int(call[3])
    # Update receiver's total time
    total_time_per_number[call[1]] = total_time_per_number.get(call[1], 0) + int(call[3])

    # Update the telephone number with the maximum time
    if total_time_per_number[call[0]] > total_time:
        total_time = total_time_per_number[call[0]]
        telephone_number = call[0]
    if total_time_per_number[call[1]] > total_time:
        total_time = total_time_per_number[call[1]]
        telephone_number = call[1]

print(f"{telephone_number} spent the longest time, {total_time} seconds, on the phone during September 2016.")
