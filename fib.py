def fibonacci(n):
    fib = []
    for x in range(0, n+1, 1):
        if x == 0 or x == 1:
            fib.append(x)
        else:
            fib.append(fib[x-1]+fib[x-2])
    return (fib[n])


n = int(input("Enter n: ").strip())
print(f"The fibonacci number at index {n} is {fibonacci(n)}")
