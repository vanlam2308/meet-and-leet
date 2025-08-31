def find_gcd_euclidean(a,b):
    """Find GCD using Euclidean algorithm, a,b > 0"""
    while b:
        a, b = b, a % b
    return a

print(find_gcd_euclidean(1,30))