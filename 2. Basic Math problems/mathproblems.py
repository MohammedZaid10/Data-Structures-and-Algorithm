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
def Q3(num):
    num = num % 10
    return num

num = int(input())
ans = Q2(num)
print(ans)