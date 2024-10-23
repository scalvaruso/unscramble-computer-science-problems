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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


# Function to return only the area code of a phone number.
def get_area_code(number):

    # Fixed lines start with an area code enclosed in brackets.
    # Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The prefix of a mobile number is its first four digits, and they always start with 7, 8 or 9.
    # Telemarketers' numbers have no parentheses or space, but they start with the area code 140.

    if number[0] == "1":
        return "140"
    elif number[0] == "(":
        a_code, _ = number.split(")")
        return a_code[1:]
    elif number[0] in ["7", "8", "9"]:
        return number[:4]


def find_area_codes(calls):
    list_of_codes = set()

    # Get list of unique area codes called by "(080)"
    for call in calls:
        # Calling telephone number (call[0]),
        # Receiving telephone number (call[1]),
        # Start timestamp of the telephone call (call[2]),
        # Duration of the telephone call in seconds (call[3]).
        if call[0][:5] == "(080)":
            area_code = get_area_code(call[1])
            list_of_codes.add(area_code)

    # Return the list of codes sorted in lexicographic order.
    return sorted(list_of_codes)


def percentage_local_calls(calls):
    # Initialise variable for total calls and local calls
    total_calls = 0
    local_calls = 0

    # Calculate the total numbers of calls made from "(080)", and total calls made from "(080)" to "(080)".
    for call in calls:
        if call[0][:5] == "(080)":
            total_calls += 1
            if call[1][:5] == "(080)":
                local_calls += 1

    # Calculating the percentage.
    percentage = (local_calls/total_calls) * 100

    # Returning the result with 2 decimal digits using f"{percentage:.2f}"
    return percentage


# Call function for Part A.
print("The numbers called by people in Bangalore have codes:")
for area_code in find_area_codes(calls):
        print(area_code)


# Call function for Part B.
print(f"{percentage_local_calls(calls):.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")