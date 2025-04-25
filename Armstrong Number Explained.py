def is_armstrong(n):
    num = n
    result = 0
    while n > 0:
        digit = n % 10
        result += digit ** 3
        n = n // 10
    return num == result

# Test cases:
print(is_armstrong(371))  # True
print(is_armstrong(123))  # False
print(is_armstrong(153))  #True
