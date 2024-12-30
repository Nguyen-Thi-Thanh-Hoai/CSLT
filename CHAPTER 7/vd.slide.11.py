# str="Python Programming"
# str1=str[:6]
# print(str1)
# str2=str[7:]
# print(str2)
# str3=str2[0:2]
# print(str3)
# str4=str1[-4:]
# print(str4)
# str5=str[:2]+str[-4:]
# print(str5)
def tim_vi_tri_xuat_hien(list_so, x):
    vi_tri = []
    for i, so in enumerate(list_so):
        if so == x:
            vi_tri.append(i + 1)
    return vi_tri
list_so = [1, 30, 44, 12, 15, 24, 93, 100, 24, 52, 15, 34]
x = 15

vi_tri = tim_vi_tri_xuat_hien(list_so, x)

print("Vị trí xuất hiện của X trong dãy số là:", vi_tri)