# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False
def MinMax(i,j,op,M,m):
    m_min = 0 
    m_max = 0
    flag = 1
    for k in range(i,j):
        
        a = evalt(M[i][k],M[k+1][j],op[k]) # send max and max
        b = evalt(M[i][k],m[k+1][j],op[k]) # send max and min
        c = evalt(m[i][k],M[k+1][j],op[k]) # send min and max
        d = evalt(m[i][k],m[k+1][j],op[k]) # send min and min
        #print(flag)
        if flag == 1:
            m_max = max(a,b,c,d) 
            m_min = min(a,b,c,d) 
        m_max = max(m_max,a,b,c,d)
        m_min = min(m_min,a,b,c,d)
        flag = flag+1
    return  (m_min, m_max)
def get_maximum_value(dataset):
    #write your code here
    #print(type(dataset))
    #dataset = str(dataset)
    str_len = len(dataset)
    # loop thru this string to find out the number of digits to construct the 2-D memo matrix
    
    d = []
    op = []
    # change this later it is redundant
    for x in dataset:
        if x.isdigit():
            d.append(int(x))
        else:
            op.append(x)
    
    actual_len = len(d)
    # array slicing doing the same thing as a for loop above
    #op = dataset[1:len(dataset):2]
    #d = dataset[0:len(dataset)+1:2]   
    #print(d,op)
    m = [[0 for x in range (actual_len)] for y in range(actual_len)]
    M = [[0 for x in range (actual_len)] for y in range(actual_len)]
    for i in range (actual_len):
        m[i][i] = int(d[i])
        M[i][i] = int(d[i])

    for s in range (1,actual_len):
        for i in range(actual_len-s):
            j = i+s
            #print(i,j)
            m[i][j], M[i][j] = MinMax(i,j,op,M,m)

    
    #print (M)
    return M[0][actual_len-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
