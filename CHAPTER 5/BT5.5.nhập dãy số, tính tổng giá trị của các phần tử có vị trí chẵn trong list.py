def Nhap():
    n=int(input("n="))
    global A,x
    A=[]
    for i in range(n):
        x=int(input(""))
        A.append(x)
    return A

def tong_gia_tri_phan_tu_chan():
    tong=0
    for i in range(1,len(A),2):
      tong+=A[i]
    print("Tong=",tong,sep="")

Nhap()
tong_gia_tri_phan_tu_chan()



