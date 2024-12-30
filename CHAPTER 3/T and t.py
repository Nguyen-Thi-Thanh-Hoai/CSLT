while (True):
    a=float(input('a='))
    b=float(input('b='))
    toantu=input('Toan tu:')
    if toantu=='+':
        print (a,toantu,b,'=',a+b,sep='')
    elif toantu=='-':
        print (a,toantu,b,'=',a-b,sep='')
    elif toantu=='*':
        print (a,toantu,b,'=',a*b,sep='') 
    elif toantu=='/' :  
        if b!=0:
            print (a,toantu,b,'=',a/b,sep='')
        else:
            print ("Khong thuc hien bieu thuc nay")
    tt=input("Tiep tuc:")
    if ((tt=="T") or (tt=="t")):
        break
    