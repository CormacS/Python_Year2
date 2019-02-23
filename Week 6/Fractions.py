def gcd(a,b):

    if b > a:
        if b % a == 0:
            return a
        else:
            return gcd(b % a, a)
    else:
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)


def lcm(a, b, x):

    return a * b / x


def addFrac(num1, dom1, num2, dom2, y):
    multiple = y / dom1
    num1 = num1 * multiple

    multiple = y / dom2
    num2 = num2 * multiple

    final = num1 + num2
    print("The two fractions added is:", final, y)


def subFrac(num1, dom1, num2, dom2, y):
    multiple = y / dom1
    num1 = num1 * multiple

    multiple = y / dom2
    num2 = num2 * multiple

    final = num1 - num2
    print("The two fractions subtracted is:", final, y)


def reduce(num, dom):

    x = gcd(num, dom)
    num = num / x
    dom = dom / x

    reduced = (num, dom)
    print("Fraction 1 reduced is: ", reduced)




numerator1 = int(input("Enter numerator of first fraction: "))
denominator1 = int(input("Enter denominator of first fraction: "))

frac1 = (numerator1, denominator1)

numerator2 = int(input("Enter numerator of second fraction: "))
denominator2 = int(input("Enter denominator of second fraction: "))

frac2 = (numerator2, denominator2)


x = gcd(frac1[1], frac2[1])

y = lcm(frac1[1], frac2[1], x)

print("The GCD of ", frac1[1], "and ", frac2[1], "is ", x)
print("The LCM of ", frac1[1], "and ", frac2[1], "is ", y)


addFrac(*frac1, *frac2, y)

subFrac(*frac1, *frac2, y)

reduce(*frac1)