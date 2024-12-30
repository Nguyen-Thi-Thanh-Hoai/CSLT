def tim_x(chuoi_so, x):
    so = [int(i) for i in chuoi_so.split()]
    indexes = [index for index, value in enumerate( so) if value == x]
    if indexes:
        return indexes
    else:
        return 0
chuoi_so= input("")
x = int(input(""))
indexes = tim_x(chuoi_so, x)
if indexes:
    for index in indexes:
        print(index + 1) 
else:
    print(0)