def calculate_power(P, n):
    if n == 0:
        return 1
    else:
        return P * calculate_power(P, n - 1)

print(calculate_power(20, 5))
