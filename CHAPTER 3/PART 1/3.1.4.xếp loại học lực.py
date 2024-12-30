Toan=int(input(""))
Ly= int(input(""))
Hoa= int(input(""))
DTB=(Toan*2+Ly*3+Hoa)/6
if DTB<3:
    print('Kem')
elif 3<=DTB<5:
   print('Yeu')
elif 5<=DTB<6:
    print('Trung binh')
elif 6<=DTB<7:
    print('Trung binh Kha')
elif 7<=DTB<8:
    print('Kha')
elif 8<=DTB<9:
    print('Gioi')
elif 9<=DTB<10:
    print('Xuat sac')   
