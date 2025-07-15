'''
Write a function fizzbuzz_twist(n) that:
Takes an integer n
Prints numbers from 1 to n
For multiples of 3, print "Fizz"
For multiples of 5, print "Buzz"
For multiples of both, print "FizzBuzz"
But:
If the number contains a 3, print "Three"
If the number contains a 5, print "Five"
If it contains both → "ThreeFive" (regardless of divisibility)
"ThreeFive" overrides everything
"Three" and "Five" override FizzBuzz
'''


def fizzbuzz_twist(n):
    for i in range(1, n+1):
        x = str(i)
        if i % 3 == 0 and i % 5 == 0:
            x = "FizzBuzz"
        elif i % 3 == 0:
            x = "Fizz"
        elif i % 5 == 0:
            x = "Buzz"
        if ("3" in str(i) and "5" in str(i)):
            x = "ThreeFive"
        elif ("3" in str(i)):
            x = "Three"
        elif ("5" in str(i)):
            x = "Five"
        print(x)


n = int(input())
fizzbuzz_twist(n)
