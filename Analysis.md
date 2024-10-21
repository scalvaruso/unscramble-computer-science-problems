# Calculate Big O

## Task0

**Description**: The problem involves finding the first text message and the last call in the texts and calls lists.

**Approach**: Using indices to call the elements.  
Knowing that **0** is the index of the first element, the program calls `texts[0]` to get the details of the first text.  
Knowing that **-1** is the index of the last element, the program calls `calls[-1]` to get the details of the last call.

**Complexity Analysis**:

- **Algorithm**: The program calls the first and last elements of the two given lists.
- **Big O Notation**: $O(1)$
- **Justification**: The program always calls only two elements, therefore the running time is independent of the input size, this algorithm has constant time $O(1)$.

---

## Task1

**Description**: The task is to find the total different phone numbers in the given lists.

**Approach**: Creating a set, then looping through the two lists to add the numbers to the set.  
Finally printing the lenght of the set, this correspond to the total of different numbers in our lists.

**Complexity Analysis**:

- **Algorithm**: The programs execute two for loops one on the texts, and one on the calls.
In each loop the numbers are added to a set.
- **Big O Notation**: $O(n)$
- **Justification**: In spite of having two independent for loops that are dependent on the input $O(2*n)$, since coefficents are neglegible for large input, we can say that this algorithm has linear time complexity $O(n)$.

---

## Task2

**Description**:

**Approach**:

**Complexity Analysis**:

- **Algorithm**: ...
- **Big O Notation**: ...
- **Justification**: ...

---

## Task3

**Description**:

**Approach**:

**Complexity Analysis**:

- **Algorithm**: ...
- **Big O Notation**: ...
- **Justification**: ...

---

## Task4

**Description**:

**Approach**:

**Complexity Analysis**:

- **Algorithm**: ...
- **Big O Notation**: ...
- **Justification**: ...
