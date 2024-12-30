n=int(input("n="))

def nhap_so_nguyen():
    global A
    A=[]
    for i in range(n):
        so_nguyen=int(input(""))
        A.append(so_nguyen)
    return A

def dao_xep():
    B=[]
    for i in range(n-1,-1,-1):
        B.append(A[i])
    print(B)
    B.sort()
    print(B)

nhap_so_nguyen()
dao_xep()