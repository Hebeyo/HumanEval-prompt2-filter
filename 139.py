def special_factorial(n):
    fact = 1
    special_fact = 1
    for i in range(1, n+1):
        fact *= i
        special_fact *= fact
    return special_fact
