def exp_mod(a, b, n):
    if b == 0:
        return 1
    if b % 2 == 0:
        return exp_mod((a*a) % n, b//2, n)
    return (a*(exp_mod(a, b - 1, n))) % n

def main():
    a = 12
    b = 34
    n = 56
    print(exp_mod(a, b, n))
main()
