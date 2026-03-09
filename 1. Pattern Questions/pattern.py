# Question 1 :
# *****
# *****
# *****
# *****
# *****

def Question1():
    n = 5
    for i in range(n):
        for j in range(n):
            print("*", end ="")
        print()

# Question 2 :
# *
# **
# ***
# ****
# *****

def Question2():
    n = 5
    for i in range(n):
        for j in range(i+1):
            print("*", end ="")
        print()

# Question 3 :
# 1
# 12
# 123
# 1234
# 12345

def Question3():
    n = 5
    for i in range(n):
        for j in range(i+1):
            print(j+1, end ="")
        print()

# Question 4 :
# 1
# 22
# 333
# 4444
# 55555

def Question4():
    n = 5
    for i in range(n):
        for j in range(i+1):
            print(i+1, end ="")
        print()

# Question 5 :
# *****
# ****
# ***
# **
# *

def Question5():
    n = 5
    for i in range(n):
        for j in range(n-i):
            print("*", end ="")
        print()

# Question 6 :
# 12345
# 1234
# 123
# 12
# 1

def Question6():
    n = 5
    for i in range(n):
        for j in range(n-i):
            print(j+1, end ="")
        print()

# Question 7 :
#     *
#    ***
#   *****
#  *******
# *********

def Question7():
    n = 5
    for i in range(n):
        for j in range(n-1-i):
            print(" ", end ="")
        for j in range(2*i+1):
            print("*", end ="")
        print()

# Question 8 :
# *********
#  *******
#   *****
#    ***
#     *
def Question8():
    n = 5
    for i in range(n):
        for j in range(i):
            print(" ", end ="")
        for j in range(2*(n-1-i)+1):
            print("*", end ="")    
        print()

# Question 9a :
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

def Question9a():
    n = 5
    for i in range(2*n-1):
        if i < n:
            for j in range(n-1-i):
                print(" ", end="")
            for j in range(i*2+1):
                print("*", end="")
            print()
        else:
            for j in range(i-(n-1)):
                print(" ", end="")
            for j in range((2*n-1-i)*2-1):
                print("*", end="")
            print()

# (OR)

def Question9b():
    n = 5
    for i in range(2*n):  # Changed from 2*n-1 to 2*n
        if i < n:
            for j in range(n-1-i):
                print(" ", end="")
            for j in range(i*2+1):
                print("*", end="")
            print()
        else:
            for j in range(i-n):  # Changed from i-(n-1) to i-n
                print(" ", end="")
            for j in range((2*n-i)*2-1):  # Changed from (2*n-1-i)*2-1 to (2*n-i)*2-1
                print("*", end="")
            print()

# Question 10 :
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


def Question10a():
    n = 5
    for i in range(n):
        for j in range(i+1):
            print("*", end="")
        print()

    for i in range(n):
        for j in range(n-i-1):
            print("*", end="")
        print()

# (OR)

def Question10b():
    n = 5
    for i in range(2*n-1):
        if (i<n):
            for j in range(i+1):
                print("*", end="")
        else:
            for j in range(2*n-i-1):
                print("*", end="")
        print()

# Question 11 :
# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *

def Question11():
    n = 5
    for i in range(2*n):
        if (i<n):
            for j in range(i+1):
                print("*", end="")
        else:
            for j in range(2*n-i):
                print("*", end="")
        print()

# Question 12 :
# 1
# 01
# 101
# 0101
# 10101

def Question12a():
    n = 5
    for i in range(n):
        for j in range(i+1):
            if (i+j)%2==0:
                print(1, end="")
            else:
                print(0, end="")
        print()

# (OR)

def Question12b():
    n = 5
    for i in range(n):
        for j in range(i+1):
            print((i+j+1)%2, end="")
        print()

# Question 13 :
# 1      1
# 12    21
# 123  321
# 12344321

# if i = 0 then 6 , if i = 1 then 4, 2 then 2, 3 then 0

def Question13():
    n = 4
    for i in range(n):
        for j in range(i+1):
            print(j+1, end="")
        for j in range((n-i-1)*2):
            print(" ", end="")
        for j in range(i+1,0,-1):
            print(j, end="")
        print()

# Question 14 :
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15

def Question14():
    n = 5
    K = 1
    for i in range (n):
        for j in range (i+1):
            print(K, end=" ")
            K = K + 1
        print()

# Question 15 :
# A
# A B
# A B C
# A B C D
# A B C D E

def numtoChr(num):
    return chr(num+65)

def Question15():
    n = 5
    for i in range (n):
        for j in range (i+1):
            print(numtoChr(j), end=" ")
        print()

# Question 16 :
# A B C D E
# A B C D
# A B C
# A B
# A

def numtoChr(num):
    return chr(num+65)

def Question16():
    n = 26
    for i in range (n):
        for j in range (n):
            print(numtoChr(j), end=" ")
        n = n - 1
        print()

# Question 17 :
# A
# B B
# C C C
# D D D D
# E E E E E

def numtoChr(num):
    return chr(num+65)

def Question17():
    n = 5
    for i in range (n):
        for j in range (i+1):
            print(numtoChr(i), end=" ")
        print()

# Question 18 :
#       A
#     A B A
#   A B C B A
# A B C D C B A

def numtoChr(num):
    return chr(num+65)

def Question18():
    n = 4
    for i in range (n):
        for j in range (n):
            print(" ", end = " ")
        n = n - 1
        for j in range (i+1):
            print(numtoChr(j), end=" ")
        for j in range (i, 0 , -1):
            print (numtoChr(j-1), end= " ")
        print()

# Question 19 :
# E 
# D E 
# C D E 
# B C D E 
# A B C D E 

def numtoChr(num):
    return chr(num+65)

def Question19():
    n = 5
    for i in range (n):
        for j in range (i+1, 0 , -1):
            print(numtoChr(n-j), end = " ")
        print()

# Question 20 :
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

def Question20a():
    n = 5;
    for i in range(2 * n):    
        if (i<n):
            for j in range(n - i):
                print("*", end = "")
            for j in range (2 * i):
                print(" ", end = "")
            for j in range(n - i):
                print("*", end = "")
            print()
        else :
            for j in range(i - n + 1):
                print("*", end = "")
            for j in range((2*n - i - 1)* 2):
                print(" ", end = "")
            for j in range(i- n + 1):
                print("*", end = "")
            print()

# (OR)

def Question20b():
    n = 5
    
    # Top Half: Stars decrease, Pipes increase
    for i in range(n):
        stars = "*" * (n - i)
        pipes = "|" * (2 * i)
        print(stars + pipes + stars)

    # Bottom Half: Stars increase, Pipes decrease
    for i in range(n):
        # We use (i + 1) so the first row starts at 1 star
        # We use (2 * (n - i - 1)) to shrink the pipes
        stars = "*" * (i + 1)
        pipes = "|" * (2 * (n - i - 1))
        print(stars + pipes + stars)

# Question 21 :
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********

def Question21():
    n = 5;
    for i in range(2 * n - 1):    
        if (i<n):
            for j in range(i+1):
                print("*", end = "")
            for j in range (n * 2 - i * 2 - 2):
                print(" ", end = "")
            for j in range(i+1):
                print("*", end = "")
            print()
        else :
            for j in range(n * 2  - i - 1):
                print("*", end = "")
            for j in range ((i - n) * 2 + 2):
                print(" ", end="")
            for j in range (n * 2 - i - 1):
                print("*", end = "")
            print()

# Question 22 :
# ****
# *  *
# *  *
# ****

def Question22a():
    n = 4
    for i in range(n):
        for j in range((i == 0) or (i == n-1)):
            print("*" * n, end="")
        for j in range(n * (i > 0 and i < n-1)):
            if j == 0 or j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# (OR)

def Question22b():
    n = 4
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n-1 or j == 0 or j == n-1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Question 23 :

def Question23():
    n = 4;
    for i in range(2*n-1):
        for j in range (2*n-1):
            row = min(i, 2*n-2-i)
            col = min(j, 2*n-2-j) 
            ans = min(row,col)
            print(n-ans, end= "")
        print()

Question23()