def LaSoNguyenTo(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def SoHopLe(x):
    return x <= 1

def NhapVaDem():
    count = 0
    print("Nhap day so:")
    while True:
        x = int(input(""))
        if SoHopLe(x):
            break
        if LaSoNguyenTo(x):
            count += 1
    return count

def InKQ(kq):
    print("Co {} so nguyen to".format(kq))

def Main():
    kq = NhapVaDem()
    InKQ(kq)

Main()