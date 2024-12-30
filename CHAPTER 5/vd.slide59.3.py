x=int(input(""))
n = int(input(""))
L=[]  
for i in range(n):
    L.append(int(input()))
def delete(L, x):
  L_new = []
  for i in range(len(L)):
    if L[i] != x:
      L_new.append(L[i])
  return L_new
L_new = delete(L,x)
print(L_new)
