# Uses python3
import sys
import re

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def better(n,m):
    # find the period of m first
    # make a list of all fibos till 1 00000
    prev = 0
    curr = 1
    pattern = '-'
    factor = 0
    fibos = []
    fibos.append(0)
    fibos.append(1)
    for i in range (1000000):
        prev, curr = curr, prev + curr
        fibos.append(curr)

    for j in range(len(fibos)):
        pattern = pattern+str(fibos[j] % m)+str("-")

    result = re.search('-0-1-1-(.*)-0-1-1-',pattern)
    if(result!=None):

        seq = result.group(1)
        print(seq)
        mods = seq.split("-")
        factor = len(mods)+3
        

    new_n = n % factor
    return fibos[new_n] % m


def sampling(n,m):
    prev = 0
    curr = 1
    temp = prev+curr
    factor = 0
    for i in range (100000000):
        temp = (prev+curr)%m
        prev = curr
        curr = temp
        if(prev==0 and temp ==1):
            factor = i+1
            break

    a = 0
    b = 1
    new_n = n % factor
    t = new_n
    for i in range (1, t):
        new_n = (a+b)%m
        a = b
        b = new_n

    return new_n%m



    














if __name__ == '__main__':
    input = sys.stdin.readline()
    n, m = map(int, input.split())
    #print (n,m)
    print(sampling(n, m))
