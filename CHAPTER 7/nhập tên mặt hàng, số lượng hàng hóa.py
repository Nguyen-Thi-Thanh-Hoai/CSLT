TenHang=[]
SoLuong=[]
#Nhap ten hang va so luong
print("Moi nhap ten hang va so luong: ")
for i in range(0,4): # i=(0,1,2,3)
    print("+ Mat hang",i+1,":")
    ten=input(" - Ten hang:")
    TenHang.append(ten)
    sl=input(" - So luong:")    
    SoLuong.append(sl)


#In len man hinh
for i in range(0,4):
    ten=TenHang[i]
    sl=SoLuong[i]
    print(ten.ljust(20,"."),end="")
    print(sl.rjust(6," "))