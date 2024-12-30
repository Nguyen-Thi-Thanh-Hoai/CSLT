x=int(input(""))
n= int(input(""))
L=[]  
for i in range(n):
    L.append(int(input()))
def search(L, x):
  for i in range(len(L)):
    if L[i] == x:
      return i
  return None
i= search(L, x)
print(i)