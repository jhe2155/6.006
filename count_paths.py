

def count_paths(F):
    n= len(F[0]) 
    dp = [[[0 for k in range(2)] for j in range(n)] for i in range(n)]

    # defining DP 
    # last index  0 = paths 
    # last index  1 = mushrooms 
    dp[0][0][0] = 1
    dp[0][0][1] = 0

    # fill in x edge 
    for x in range(1, n):
        dp[x][0][0]= 1 
        dp[x][0][1]= dp[x-1][0][1]
        if F[x][0] == 'm':
            dp[x][0][1] += 1 
            print("after:", dp[x][0][1])

    # fill in y edge
    for y in range(1, n):
        dp[0][y][0]= 1 
        dp[0][y][1]= dp[0][y-1][1]
        if F[0][y] == 'm':
            dp[0][y][1] += 1 
    
    #fill the grid 
    for x in range(1, n):
        for y in range(1, n):
            m1 = dp[x-1][y][1]
            m2 = dp[x][y-1][1]
            k1 = dp[x-1][y][0]
            k2 = dp[x][y-1][0]

            k= 0 
            m= 0
            if m1 == m2:
                k = k1 + k2 
                m = m1
            elif m1 > m2: 
                m = m1  
                k = k1 
            elif m2 > m1: 
                m = m2 
                k = k2 

            if F[x][y]=='m':
                m +=  1
        
            if F[x][y]=='t':
                k = 0 
                m = 0

            dp[x][y][0] = k 
            dp[x][y][1] = m 

    return(dp[n-1][n-1][0])

    '''
    Input:  F | size-n direct access array of size-n direct access arrays
              | each F[i][j] is either 't', 'm', or 'x'
              | for tree, mushroom, empty respectively
    Output: p | the number of distinct optimal paths in F
              | starting from (0,0) and ending at (n-1,n-1)
    '''




    
    
