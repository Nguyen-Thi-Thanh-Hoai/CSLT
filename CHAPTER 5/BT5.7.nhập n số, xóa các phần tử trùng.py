def Nhap():
    n=int(input("n="))
    global L
    while n <= 0:
        n = int(input(""))

    L=[]
    for i in range(n):
        phan_tu = int(input(""))
        L.append(phan_tu)
    
def loai_phan_tu_trung():
    global M
    M=list(set(L))

def InKQ():
    for phan_tu in M:
        print(phan_tu, end=" ")

Nhap()
loai_phan_tu_trung()
InKQ()