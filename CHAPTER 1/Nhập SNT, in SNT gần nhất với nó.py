def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def so_nguyen_to_gan_nhat(n):
    n -= 1
    while n >= 2:
        if la_so_nguyen_to(n):
            return n
        n -= 1
    return None

# Nhập vào một số nguyên tố từ người dùng
while True:
    try:
        so_nguyen_to = int(input("Nhập vào một số nguyên tố: "))
        if la_so_nguyen_to(so_nguyen_to):
            break
        else:
            print("Vui lòng nhập một số nguyên tố.")
    except ValueError:
        print("Vui lòng nhập một số nguyên tố.")

# Tìm và in ra số nguyên tố gần nhất và nhỏ hơn số đã nhập
so_nguyen_to_gan_nhat = so_nguyen_to_gan_nhat(so_nguyen_to)
if so_nguyen_to_gan_nhat is not None:
    print(f"Số nguyên tố gần nhất và nhỏ hơn {so_nguyen_to} là: {so_nguyen_to_gan_nhat}")
else:
    print(f"Không có số nguyên tố nhỏ hơn {so_nguyen_to}.")