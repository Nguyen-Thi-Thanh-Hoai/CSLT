n=int(input(("n=")))
i=1
while i<=n:
    print(i,end=" ")
    #chia hết cho 10 thì xuống dòng, mỗi dòng chỉ có 10 số
    if (i%10==0):
    #lệnh xuống dòng
        print("")
    i=i+1