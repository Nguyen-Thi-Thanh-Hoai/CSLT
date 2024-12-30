L = [1, 2, 3, 5, 5, 5, 8, 9, 5]
x=int(input("x="))
#xóa tất cả các kí tự x trong list
def remove_5(L):
    while x in L:
     L.remove(x)
    return L
L_new = remove_5(L)
print(L_new)