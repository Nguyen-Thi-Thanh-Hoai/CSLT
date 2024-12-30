so_am = 0
so_duong = 0
while True:
     n = int(input(""))
     if n == 0:
          break
     elif n < 0:
          so_am += 1
     else:
          so_duong += 1
print(so_duong,"so duong")
print(so_am,"so am")
