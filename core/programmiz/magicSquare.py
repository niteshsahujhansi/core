# create magic square 
'''def magic_square(n):

    magicSquare = [[0 for i in range(n)]
                        for j in range(n)]

    # magicSquare = []
    # for i in range(0,n):
    #     l = []
    #     for j in range(0,n):
    #         l.append(0)
    #         magicSquare.append(l)   

    j = n-1
    i = n//2

    num = n*n 
    count = 1

    while (count<=num):
        if (i == -1 and j == n):
            j = n-2
            i = 0
        else:
            if (j == n):
                j = 0
                
            if (i < 0):
                i = n-1
        
        if magicSquare[i][j] != 0:
            j = j-2
            i = i+1
            continue
        else:
            magicSquare[i][j] = count 
            count += 1

        j = j + 1
        i = i - 1

    for i in range(0,n):
        for j in range(0,n):
            print(magicSquare[i][j], end=' ')

            if (j == n-1):
                print( )

magic_square(5)'''



'''n=5
i=n//2
j=n-1
num=1

lst = [[0 for i in range(n)] for j in range(n)]

while num<=n*n:
    if not lst[i][j]:
        lst[i][j] = num
        num += 1
        i = (i+n-1)%n
        j = (j+n-2)%n
    else:
        i = (i+n-2)%n
        j = (j+n-2)%n

print(lst)'''