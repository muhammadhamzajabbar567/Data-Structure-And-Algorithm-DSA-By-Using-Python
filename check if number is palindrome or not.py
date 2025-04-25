def is_palindrom(n):
    num = n
    result = 0
    while n>0:
        ld = num // 10
        result = (result * 10) + ld
        num = num // 10
        return num == result


print(is_palindrom(1234))


# string

def is_sting_palindrom(s):
    str = s
    lower = str.lower()
    return lower == s[::-1]

print(is_sting_palindrom("madam"))
print(is_sting_palindrom("bat"))
print(is_sting_palindrom("radar"))