# Uses python3
import sys


def merge(a,b,left,ave,right):
    i = left
    j = ave
    k = left
    count = 0
    while ((i<=ave-1) and (j<=right)):
        if(a[i]<=a[j]):
            b[k+1] = a[i+1]
        else:
            b[k+1] = a[j+1]
            #this is tricky
            count = count + (ave - i)
    if(len(a[i:ave])>0):
        b.append(a[i:ave])
    if(len(a[j:right])>0):
        b.append(a[j:right])
    return count


def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    number_of_inversions = number_of_inversions + merge(a,b,left,ave,right)
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
