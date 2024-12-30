def Nhap():
    L=[]
    for i in range(10):
        L=L + [int(input())]
    x=int(input("x="))
    return L,x


def InKQ(L):
    for x in L:
        print(x,end=", ")
    print()


def CauA(L,x):
    for i in range(len(L)):
        if L[i]==5:
            L[i]=x
    InKQ(L)


def CauB(L,x):
    i=0
    while (i<len(L)):
        if L[i]==x:
            del(L[i])
        else:
            i=i+1
    InKQ(L)


L,x=Nhap()
CauA(L,x)
CauB(L,x)

