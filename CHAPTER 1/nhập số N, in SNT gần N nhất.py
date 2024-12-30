def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 
def find_closest_prime(N):
    if is_prime(N):
        return N
 
    closest_prime = N - 1
    while True:
        if is_prime(closest_prime):
            return closest_prime
        closest_prime -= 1
 
# Ví dụ sử dụng:
N = int(input("Nhập số nguyên N: "))
result = find_closest_prime(N)
print(f"Số nguyên tố gần {N} nhất là: {result}")