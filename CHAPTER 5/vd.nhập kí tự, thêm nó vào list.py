
#Cach 1
L=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(L)):
    # range(3) --> range(0,3,1)
    # i=(0,1,2)
    for j in range(len(L[i])):
        # j=(0,1,2)
        if (L[i][j]%2==0):
            L[i][j]="x"


print(L)




#Cach2
L=[[1,2,3],[4,5,6],[7,8,9]]
for X in L:
    for j in range(len(X)):
        if (X[j] %2==0):
            X[j]="x"
print(L)




