def kiem_tra_nguyen_to(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def in_nguyen_to_dau_tien(n):
    count = 0
    num = 1
    while count < n:
        if kiem_tra_nguyen_to(num):
            print(num, end=",")
            count += 1
        num += 1
n = int(input("Nhập số nguyên n: "))
in_nguyen_to_dau_tien(n)