def nhap_10_so_nguyen():
    global L
    L=[]
    for i in range(10):
        so_nguyen = int(input(""))
        L.append(so_nguyen)
    return L

def hoan_vi():
  B=[]
  for i in range(0, len(L), 2):
    B.append(L[i + 1])
    B.append(L[i])
  for x in B:
   print(x,end=" ")

nhap_10_so_nguyen()
hoan_vi()
