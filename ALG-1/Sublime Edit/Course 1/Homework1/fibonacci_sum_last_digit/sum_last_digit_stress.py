# Uses python3
import sys
from random import randint


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


def fibonacci_sum_naive1(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    summ      = 1

    for i in range(n - 1):
        previous, current = current,( previous + current)%10
        summ += current

    return summ % 10

# cant check this stuff by hand - do a stress test 
def better (n):
    prev = 0
    curr = 1
    s=0

    for i in range (2,n):
        s = (prev+curr)%10
        prev = curr
        curr = s

    if (n==0):
        return 0
    else:
        return s 

    

if __name__ == '__main__':
    #input = sys.stdin.readline()
    #n = int(input)
    c=100000
    while(True):
        c = c+1
        inp = randint(0,c)
        print ("input is ", inp)
        naive = fibonacci_sum_naive(inp)
        print("answer from naive is ", naive)
        bet = fibonacci_sum_naive1(inp)
        print("answer form better is ", bet)
        if(naive == bet):
            print("all okies, continue")
        elif(naive != bet or counter>c):
            print("answer mismatch ")
            break

    
