b=int(input())
T=['A','B','C','D','E','F','G','H','K','L']
for i in range(len(str(b))-1,-1,-1):
    a=int(b/10**i)
    b=b%10**i
    print(T[a],end='')