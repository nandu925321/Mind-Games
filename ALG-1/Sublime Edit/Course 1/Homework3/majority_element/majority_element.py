# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    return -1

def majority_in_dict(a,left,right):
    d  = {}
    for x in a:
        if(str(x) not in d):
            d[str(x)] = 1
        elif(str(x) in d):
            val = d[str(x)]
            val = val + 1
            #print(val)
            d[str(x)] = val

    vals = list(d.values())
    vals.sort(reverse=True)
    #print(vals)
    if(vals[0]>right/2):
        return 1
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n,p, *a = list(map(int, input.split()))
    print (n)
    print (p)
    print(a)
    if majority_in_dict(a, 0, n) != -1:
        print(1)
    else:
        print(0)
