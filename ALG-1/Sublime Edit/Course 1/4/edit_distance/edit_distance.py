# Uses python3
def edit_distance(s, t):
    #write your code here
    #print(s,t)
    m = len(s)
    n = len(t)
    # create 2-d array
    DP = [[0 for x in range (m+1)] for y in range(n+1)]
    # m*n for loop
    for i in range (m+1):
    	for j in range (n+1):
    		# if i==0 then fill i,j with all j's[first row]
    		if i == 0:
    			DP[i][j] = j
    		# fill first column
    		elif j == 0:
    			DP[i][j] = i
    		# if last character is same 
    		elif s[i-1] == t[j-1]:
    			DP[i][j] = DP[i-1][j-1]
    		# else consider all possibilities to find min
    		else:
    			DP[i][j] = 1 + min(DP[i][j-1],DP[i-1][j],DP[i-1][j-1])

    return DP[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
