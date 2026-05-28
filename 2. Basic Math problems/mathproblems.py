# Question1 :
# Count Digits of a number
def Q1(num):
    cnt = 0
    while num > 0:
        num = num//10
        cnt+=1
    return cnt


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

num = int(input())
ans = armstrong(num)
print(ans)