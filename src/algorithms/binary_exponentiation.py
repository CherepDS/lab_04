# Рекурсивный подход
def binary_exp_recursive(a, n):
    if n < 0:
        return 1/binary_exp_recursive(a, -n)
    elif n == 0:
        return 1
    elif n%2 == 0:
        return binary_exp_recursive(a*a, n/2)
    elif n%2 != 0:
        return a*binary_exp_recursive(a*a, (n-1)/2)

print(binary_exp_recursive(2, -4))

# Итератиный подход
def binary_exp_iterative(a, n):
    if n < 0:
        if a == 0:
            raise ZeroDivisionError("Zero cannot have a negative exponent")

        a = 1 / a
        n = -n

    result = 1
    while n > 0:
        if n % 2 == 1:
            result *= a

        a *= a
        n //= 2

    return result

print(binary_exp_iterative(2, -4))