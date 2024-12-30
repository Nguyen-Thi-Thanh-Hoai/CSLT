def Nhap():
    global n
    n=int(input("n="))
    return n
def so_nguyen_to(n):
    global KQ
    laSNT=1 
    for i in range(2,n,1):
       if n % i==0:
        laSNT=0 
        break
    if (laSNT==1):
       KQ= "la SNT"
    else:
       KQ="khong la SNT"
def InKQ():
    print(n,KQ)
Nhap()
so_nguyen_to(n)
InKQ()