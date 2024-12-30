print("Nhap 3 so nguyen")
def Nhap():
   a=int(input("a="))
   b=int(input("b="))
   c=int(input("c="))
   return a,b,c

def SLN(a,b,c=None):
    if c==None:
        max=a
        if max<b:
            max=b
    else:
        max=a
        if max<b:
            max=b
        if max<c:
            max=c      
    return max
def InKQ(max):
    print("So lon nhat la:",max)
a,b,c=Nhap()
solonnhat=SLN(a,b,c)
InKQ(solonnhat)  