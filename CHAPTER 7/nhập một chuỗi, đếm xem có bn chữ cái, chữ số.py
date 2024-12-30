st=input()
so=0
chucai=0
for x in st:
    if x.isnumeric():
        so+=1
    elif x.isalpha():
        chucai+=1


print("Chu cai:",chucai)
print("Chu so:",so)


