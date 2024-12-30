n=int(input(""))
for i in range(2,n,1):
       if n % i == 0:
        print(n,"khong la SNT")
        break
else:
    print(n,"la SNT")
