M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
S =int(input("S="))
if S<=100:
 print("Phai tra=",S*M1,sep="")
if 100<S<151:
 print("Phai tra=",100*M1+(S-100)*M2,sep="")
if S>=151:
 print("Phai tra=",100*M1+50*M2+(S-150)*M3,sep="")