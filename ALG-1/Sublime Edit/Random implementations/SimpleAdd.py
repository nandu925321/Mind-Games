# uses python3
import sys

print ("enter a number with space in between")
#input = sys.stdin.read()
tokens = input().split()
a = int(tokens[0])
b = int(tokens[1])
print(a + b)



