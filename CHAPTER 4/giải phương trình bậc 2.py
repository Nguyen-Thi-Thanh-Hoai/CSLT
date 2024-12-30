import math

# Nhập số a, b và kiểm tra điều kiện khác 0
print("Nhap 3 so nguyen:")
a = float(input("a="))
while True:
    if a == 0:
        a = float(input("Số a phải khác 0. Mời nhập lại số a: "))
    else:
        break
    
b = float(input("b="))
while True:
    if b == 0:
        b = float(input("Số b phải khác 0. Mời nhập lại số b: "))
    else:
        break
    
# Nhập số c
c = float(input("c="))

# Tính Delta
delta = b**2 - 4 * a * c

# Tìm nghiệm của phương trình
if delta < 0:
    print("Phuong trinh vo nghiem")
elif delta == 0:
    print("Phuong trinh co nghiem kep")
    print("x1=x2=", -(b / (2 * a)),sep="")
else:
    print("Phuong trinh co hai nghiem")
    print("x1=",(-(b)+math.sqrt(delta))/(2*a),sep="")
    print("x2=",(-(b)-math.sqrt(delta))/(2*a),sep="")