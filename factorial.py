def factorial(n):
    if n == 0:
        return (1)
    else:
        return (n*factorial(n-1))


x = int(input("Enter the number: ").strip())
print(factorial(x))
