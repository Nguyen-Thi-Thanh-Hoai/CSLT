def kiemtra_ho_ten(ho_ten):
    for i in range(len(ho_ten)):
        if i == 0 or ho_ten[i-1] == " ":
            if not ho_ten[i].istitle():
                return False
        else:
            if ho_ten[i].istitle():
                return False
    return True

ho_ten = input("Ho ten: ")

if kiemtra_ho_ten(ho_ten):
        print("Hop le!!!")
else:
        print("Khong hop le!!!")

