st1=input("st1: ").lower()
st2=input("st2: ").lower()
dem=0
i=0
while True:
    i=st1.find(st2,i)
    if i>=0:      
        print("Vi tri:",i)
        dem=dem+1
        i=i+1
    else:
        break
   
print("So lan xuat hien:",dem)
