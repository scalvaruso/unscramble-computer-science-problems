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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

# texts[0] is the first element in the list of texts which has three columns:
# Sending telephone number (texts[0][0]), Receiving telephone number (texts[0][1]), Timestamp of the text message (texts[0][2]).
# Using indices to call these elements.

print(f"First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}")

# calls[-1] is the last element in the list of calls which has four columns:
# Calling telephone number (calls[-1][0]), Receiving telephone number (calls[-1][1]), Start timestamp of the telephone call (calls[-1][2]), Duration of the telephone call in seconds (calls[-1][3]).
# Using indices to call these elements.

print(f"Last record of calls, {calls[-1][0]} calls {calls[-1][1]} at time {calls[-1][2]}, lasting {calls[-1][3]} seconds")
