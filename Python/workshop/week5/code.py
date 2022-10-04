'''
#Q3
def price():
    m = float(input("What's the mass of the coffee?(in pounds)"))
    p = m * 10.5 + 0.86 * m + 1.5
    print(p)

price()

#Q4
def area():
    a = float(input("enter a length of the triangle: "))
    b = float(input("enter a length of the triangle: "))
    c = float(input("enter a length of the triangle: "))
    s = (a + b + c) / 2
    S = s * (s - a) * (s - b) * (s - c)
    A = pow(S,0.5)
    print(A)

area()
'''
#Q5
def sumcubes():
    m = int(input("What's the number of n"))
    k = 0
    for i in range(m):
        k = k + i ** 3
    print(k,"the sum of the cubes of", m, "natural numbers")

sumcubes()


#06
def fibonacci():
    n = int(input("What's the number of n"))
    m = n - 1
    n1 = 1
    n2 = 1
    for i in range(1,m):
        fib = n1 + n2
        n1 = n2
        n2 = fib
    print(fib)

fibonacci()
