# Question1 :
# Count Digits of a number
import math 

def Q1a(num):
    cnt = 0
    while num > 0:
        num = num//10
        cnt+=1
    return cnt

# (OR)

def Q1b(num):
    return math.floor(math.log10(num))+1


# Question2:
# Reverse a number
def Q2(num):
    rev = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        rev = rev * 10 + rem
    return rev

# Question3:
# Palindrome
def Q3(num) :
    rev = 0
    while num > 0:
        rem = num % 10
        num = num // 10
        rev = rev * 10 + rem
    return rev

def palindrome(num):
    if num == Q3(num):
        return f"{num} is a Palindrome"
    else :
        return f"{num} is not a Palindrome"

# Question 4:
# GCD or HCF
def gcd(a,b):
    divisor = min(a,b)
    dividend = max(a,b)

    while dividend % divisor !=0:
        temp = dividend
        dividend = divisor
        divisor = temp % divisor
    return divisor

# Question 5:
# LCM 


# Question 6:
# Armstrong number
def count(num):
    count = 0
    while num > 0:
        num = num // 10
        count = count + 1
    return count

def armstrong(num):
    original_num = num
    total_digits = count(num) 
    arm = 0
    while num > 0:
        rem = num % 10
        digit_power = rem ** total_digits
        arm = arm + digit_power
        num = num // 10

    if arm == original_num:
        return f"{original_num} is an Armstrong number"
    else:
        return f"{original_num} is not an Armstrong number"


# Question 7:
# Print all Divisors
def Divisorsa(num):
    for i in range (1, num+1):
        if num % i == 0:
            print (i)

# (OR)

def Divisorsb(num):
    # COMMENT: Loop only up to the square root of num (int(num**0.5) + 1)
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            print(i)  # COMMENT: Prints the smaller divisor of the pair
            
            # COMMENT: Prints the matching larger divisor if it is not a duplicate (like 6*6)
            if i != num // i:
                print(num // i)

#     Left Side (Small)           Middle             Right Side (Large)
# [ Checks 1 to 9 via Loop ]   [ Check 10 ]   [ Instantly calculated via num // i ]

#        1  ------------------------> 6 <------------------------ 36

# (OR) to print in order

def Divisorsc(num):
    divisors_list = []  # Step 1: Create an empty list to store divisors
    
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_list.append(i)  # Step 2: Add the smaller divisor
            
            if i != num // i:
                divisors_list.append(num // i)  # Step 2: Add the larger divisor
                
    # Step 3: Sort the list in ascending order
    divisors_list.sort()
    
    # Step 4: Print each divisor from the sorted list
    for divisor in divisors_list:
        print(divisor)


# (OR) to print in order but without sort

def Divisors(num):
    small_divisors = []  # Naturally grows smallest to largest (1, 2, 3...)
    large_divisors = []  # Naturally grows largest to smallest (...12, 6, 4)
    
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            small_divisors.append(i)          # Left side goes here
            if i != num // i:
                large_divisors.append(num // i) # Right side goes here
                
    # TWEAK: Reverse the large list and print everything sequentially
    # large_divisors[::-1] turns [12, 6, 4] into [4, 6, 12]
    all_divisors = small_divisors + large_divisors[::-1]
    
    for divisor in all_divisors:
        print(divisor)

# time complexity is root n

# Question 8:
# Check for Prime

def prime(num):
    if num < 2:
        return f"{num} is not a prime"
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"{num} is not a prime"
    
    return f"{num} is a prime"

# time complexity is root n

# num = int(input())
# ans = Q1b(num)
# print(ans)

# Question 9:
# Given a series of number print it is a prime or not

def primea(num):
    if num < 2:
        return f"{num} is not a prime"
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"{num} is not a prime"
    
    return f"{num} is a prime"

# 1. Read the input line, split by spaces, convert to integers, and create a list
# series = list(map(int, input("Enter your numbers separated by spaces: \n").split()))

# 2. Directly grab each actual number from the list and pass it to the function
# for num in series:
#     print(prime(num))

# (OR)

import sys

def primeb(num):
    if num < 2:
        return f"{num} is not a prime"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"{num} is not a prime"
    return f"{num} is a prime"

# print("Enter your numbers (Press Ctrl+D or Ctrl+Z when finished):")

# 1. sys.stdin.read() grabs all text across all lines
# 2. .split() cleanly extracts numbers ignoring ALL spaces and newlines
# raw_input = sys.stdin.read()
# series = list(map(int, raw_input.split()))

# 3. Process the cleanly separated numbers
# for num in series:
#     print(primeb(num))

# (OR)

# user input in multiple lines or spaces

import sys
def primec(num):
    if num < 2:
        return f"{num} is not a prime"
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return f"{num} is not a prime"
    return f"{num} is a prime"

content = sys.stdin.read()
series = list(map(int, content.split()))

for num in series:
    print(primec(num))

