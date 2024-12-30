def add(L, x, k):
  if k > len(L):
    L.append(x)
  else:
    L.insert(k, x)
  return L
x=int(input(""))
k=int(input(""))
n= int(input(""))
L=[]  
for i in range(n):
    L.append(int(input()))
A = add(L, x, k)
print(A)
   