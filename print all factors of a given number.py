# brute force method
def find_factors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(i)
    return result

print(find_factors(120))

# optimize solution (Loop will execute Only For Half Number of Digits)

def find_factors_optimize(n):
    result = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            result.append(i)
            if i != n // i:  # check for perfect square
                result.append(n // i)
    return sorted(result)

print(find_factors_optimize(120))