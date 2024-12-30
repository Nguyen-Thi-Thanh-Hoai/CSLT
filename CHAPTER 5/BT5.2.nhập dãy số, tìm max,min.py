def Input():
    n=int(input("n="))
    global L
    L=[]
    for i in range(n):
        so_nguyen = int(input(""))
        L.append(so_nguyen)
    return L

def Output():
    print(max(L),min(L))
 
Input()
Output()