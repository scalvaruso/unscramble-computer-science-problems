# Calculate Big O

## Task0

**Description**: The problem involves extracting specific records from two datasets (texts and calls): specifically the first record from texts and the last record from calls.

**Approach**: The program accesses the first record in texts and the last record in calls using their respective indices.  
Beeing **0** the index of the first element, `texts[0]` correspond to the first text.  
Beeing **-1** the index of the last element, `calls[-1]` correspond to the last call.

**Complexity Analysis**:

- **Algorithm**: Accessing the two elements (first text, and last call) at a specific index in the lists, then printing the results.
- **Big O Notation**: $O(1)$
- **Justification**: For the purpose of this task, we are only analysing the complexity of accessing and printing the specific records, ignoring the complexity of reading the CSV files into lists that would be $O(n)$. The reason for this is that the task explicitly focuses on printing specific records after they have been read into memory. Index-based access in a list takes constant time, independent of the list size, which justifies the $O(1)$ complexity for accessing and printing these records.

---

## Task1

**Description**: The problem involves counting the number of unique telephone numbers in two records: texts and calls. Each record contains sending and receiving phone numbers.

**Approach**: A set is utilized to automatically handle and count unique phone numbers. Each phone number from both texts and calls is added to the set.
The size of the set (the number of unique telephone numbers) is then determined and printed.

**Complexity Analysis**:

- **Algorithm**: The solution uses two loops to iterate through the records: one for texts and one for calls. In each iteration, sending and receiving numbers are added to a set, which automatically handles duplicates.
- **Big O Notation**: $O(n)$, where $n$ is $t$+$c$, and $t$ is the number of records in the texts file and $c$ is the number of records in the calls file.
- **Justification**: Each record from both texts and calls is processed once $O(t+c)$, and each unique number is inserted into the set, which handles duplicates in constant average time $O(1)$. Thus, the overall complexity depends linearly on the combined size of the records.

---

## Task2

**Description**: The problem involves finding the telephone number that spent the longest total time on the phone during a given period. The data is provided as a list of call records, each containing a caller, receiver, and call duration.

**Approach**: Iterate through the list of calls and maintain a dictionary that tracks the total time spent on calls for each phone number. Simultaneously, keep track of the phone number with the maximum total time.

**Complexity Analysis**:

- **Algorithm**: A single loop runs through each call in the calls list. For each call, the caller's and receiver's total time is updated in the dictionary. Then, a check is performed to see if either the caller or receiver has exceeded the current maximum time.
- **Big O Notation**: $O(n)$, where $n$ is the number of calls in the calls list.
- **Justification**: The algorithm iterates over the calls list once. During each iteration, the algorithm performs constant-time operations for dictionary updates and maximum time checks. Since all these operations take $O(1)$ time for each call, the overall time complexity is directly proportional to the number of calls in the list.

---

## Task3

**Description**: The problem involves identifying and analyzing phone calls made by people in Bangalore (calls with area code 080). The task is to find unique area codes and mobile prefixes called by these Bangalore-based callers and calculate the percentage of calls made to other Bangalore-based fixed lines.

**Approach**:

- Part A: Iterated through the call records to extract unique area codes or mobile prefixes called by Bangalore callers (area code 080). These codes are then sorted lexicographically.
- Part B: Iterated through the call records to count calls made from Bangalore (area code 080) and calculated the percentage of those made inside the same area (area code 080).

**Complexity Analysis**:

- **Algorithm**:
  - Part A involves iterating over the entire call dataset once. For each call record, the program performs a check to see if the calling number starts with 080 (Bangalore area code). If it does, it extracts the relevant area code or prefix and stores them in a set (which allows for constant time insertions on average). Finally, the program sorts the set of codes.
  - Part B also involves a single iteration over the dataset to calculate the percentage of calls made from Bangalore to Bangalore (area code 080).
- **Big O Notation**: $O(n \log n)$, where $n$ is the number of call records.
- **Justification**:
  - Part A, iterating through all calls takes $O(n)$, where $n$ is the number of call records, and collecting unique codes into a set is $O(1)$ on average. Sorting these codes takes $O(k \log k)$, where $k$ is the number of unique area codes, which can be at most $n$. Thus, the time complexity for Part A is $O(n \log n)$ in the worst case.  
  - Part B involves a single loop over the records with $O(n)$ complexity.  

  Combining the two, the overall complexity is $O(n \log n)$, as sorting in Part A dominates the runtime.

---

## Task4

**Description**:

**Approach**:

**Complexity Analysis**:

- **Algorithm**: ...
- **Big O Notation**: ...
- **Justification**: ...
