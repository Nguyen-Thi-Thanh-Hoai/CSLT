a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
max=a
if max<b:
   max=b
if max<c:
   max=c
min=a
if min>b:
   min=b
if min>c:
   min=c
print("SLN=",max,sep="")
print("SBN=",min,sep="")