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

# Question 9 :
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *

def Question9():
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

# Question 10 :
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

def Question10():
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

# Question 11 :
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


def Question11a():
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

def Question11b():
    n = 5
    for i in range(2*n-1):
        if (i<n):
            for j in range(i+1):
                print("*", end="")
        else:
            for j in range(2*n-i-1):
                print("*", end="")
        print()

# Question 12 :
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

def Question12():
    n = 5
    for i in range(2*n):
        if (i<n):
            for j in range(i+1):
                print("*", end="")
        else:
            for j in range(2*n-i):
                print("*", end="")
        print()

# Question 13 :
# 1
# 01
# 101
# 0101
# 10101

def Question13a():
    n = 5
    for i in range(n):
        for j in range(i+1):
            if (i+j)%2==0:
                print(1, end="")
            else:
                print(0, end="")
        print()

# (OR)

def Question13b():
    n = 5
    for i in range(n):
        for j in range(i+1):
            print((i+j+1)%2, end="")
        print()

# Question 14 :
# 1      1
# 12    21
# 123  321
# 12344321

def Question14():
    n = 4
    for i in range(n):
        for j in range(i+1):
            print(j+1, end="")
        for j in range((n-i-1)*2):
            print(" ", end="")
        for j in range(i+1,0,-1):
            print(j, end="")
        print()

Question4()