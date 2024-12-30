x= float(input("x="))
y= float(input("y="))
pheptoan=input("Phep toan:")
if pheptoan == '+':
    print (x,pheptoan,y,"=",x+y,sep="")
elif pheptoan=='-':
    print (x,pheptoan,y,"=",x-y,sep="")
elif pheptoan=='*':
    print (x,pheptoan,y,"=",x*y,sep="") 
elif pheptoan=='/' and y!=0 :  
    print (x,pheptoan,y,"=",x/y,sep="")
elif pheptoan=='/' and y==0 :
    print("Khong hop le")
else:
    print("Khong hop le")