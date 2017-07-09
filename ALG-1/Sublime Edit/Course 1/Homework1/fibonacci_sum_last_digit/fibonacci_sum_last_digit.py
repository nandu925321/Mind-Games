# Uses python3
import sys
import math
import decimal  


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

# cant check this stuff by hand - do a stress test 
def better (n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    summ      = 1
    i = 0
    while(i<n - 1):
        previous, current = current,( previous + current)%10
        summ += current
        i = i + 1

    return summ % 10


def formula(n):

    a = decimal.Decimal((1+math.sqrt(5))/2)
    #a = math.pow(decimal.Decimal(a),decimal.Decimal(n+2))
    a = (decimal.Decimal(a)**decimal.Decimal(n+2))
    b = decimal.Decimal((1-math.sqrt(5))/2)
    #b = math.pow(decimal.Decimal(b),decimal.Decimal(n+2))
    b = (decimal.Decimal(b)**decimal.Decimal(n+2))
    factor = decimal.Decimal((1/math.sqrt(5)))
    s = decimal.Decimal((factor*decimal.Decimal(a-b)))
    return int(s-1)%10

def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':    v1, v2, v3 = v1+v2, v1, v2
    return v2
    

if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(better(n))
