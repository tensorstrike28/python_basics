import math


def is_prime(n):
    if n == 0 or n == 1:
        return ("prime")
    else:
        for x in range(2, int(math.sqrt(n)+1)):
            if n % x == 0:
                return ("not prime")
                break
        else:
            return ("prime")


n = int(input("Enter number: ").strip())
print(f"The input number is {is_prime(n)}")
