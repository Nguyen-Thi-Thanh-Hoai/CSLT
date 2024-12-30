L=[]
while True:
    x=input()
    if x.isalpha():
        if x.lower()=="n":
            break
    elif x.isnumeric():
        L.append(int(x))
print(*L)