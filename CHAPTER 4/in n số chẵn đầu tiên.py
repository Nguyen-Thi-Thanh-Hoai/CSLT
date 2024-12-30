def nhap():
    while True:
        try:
            n = int(input("n="))
            if n >= 2:
                return n
            else:
                print("Khong hop le, nhap lai")
        except ValueError:
            print("Khong hop le, nhap lai")

def inkq(n):
    for i in range(2, n + 1, 2):
        print(i, end=' ')

while True:
    n = nhap()
    inkq(n)
    chon = input("\nTiep tuc khong?")
    if chon.lower() == 'k' or chon.lower() == 'K' :
        break