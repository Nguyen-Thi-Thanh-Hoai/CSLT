def NhapSo(tb):
    print(tb)
    while True:
        x=input()
        if x.isnumeric():
            return int(x)
        else:
            print("Khong hop le!!!")
         
a=NhapSo("Nhap so a")
b=NhapSo("Nhap so b")
print("a+b=",a+b)
