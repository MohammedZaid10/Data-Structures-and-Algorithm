# Question 1 :
# Print a Name n times

def namea(n):
    if n == 0:
        return
    print('Raj')
    namea(n-1)

# namea(5)

# (OR)

# ================================================================================

def nameb(i,n):
    if i>n:
        return
    print('Raj')
    nameb(i+1,n)

# nameb(1,7)

# ================================================================================
# ================================================================================

# Question 2 :
# Print 1 to n using recursion

def onetona(n):
    # Base case: stop when n drops below 1
    if n < 1:
        return
    
    onetona(n - 1)  # Recursive call with a smaller number
    print(n)       # Prints on the way back up the stack

# onetona(5)


# (OR)

# ================================================================================

def onetonb(n, i=1):
    # Base case: stop when current tracker exceeds n
    if i > n:
        return
        
    print(i)
    onetonb(n, i + 1)  # Pass the incremented value to the next call

# onetonb(5)

# ================================================================================

def onetonc(i,n):
    # Base case: stop when current tracker exceeds n
    if i > n:
        return
        
    print(i)
    onetonc(i + 1,n)  # Pass the incremented value to the next call

# onetonc(1,7)


# ================================================================================
# ================================================================================

# Question 3 :
# Print n to 1 using recursion

def ntoone(n):
    if n < 1:
        return
    print(n)
    ntoone(n - 1)

ntoone(5)

# ================================================================================
# ================================================================================
