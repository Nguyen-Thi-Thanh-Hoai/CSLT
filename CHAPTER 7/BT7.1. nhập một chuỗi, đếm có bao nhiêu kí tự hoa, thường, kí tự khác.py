def dem_ky_tu(chuoi):
    in_hoa = 0
    in_thuong = 0
    chu_so = 0
    ky_tu_khac = 0
    for ky_tu in chuoi:
        if ky_tu.isupper():
            in_hoa += 1
        elif ky_tu.islower():
            in_thuong += 1
        elif ky_tu.isdigit():
            chu_so += 1
        else:
            ky_tu_khac += 1
    print("In hoa:", in_hoa)
    print("In thuong:", in_thuong)
    print("Chu so:", chu_so)
    print("Khac:", ky_tu_khac)
chuoi_input = input("")
dem_ky_tu(chuoi_input)