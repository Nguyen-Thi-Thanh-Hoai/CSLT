def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

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

# In ra các số nguyên tố nhỏ hơn số đã nhập
print(f"Các số nguyên tố nhỏ hơn {so_nguyen_to} là:")
for i in range(2, so_nguyen_to):
    if la_so_nguyen_to(i):
        print(i, end=' ')