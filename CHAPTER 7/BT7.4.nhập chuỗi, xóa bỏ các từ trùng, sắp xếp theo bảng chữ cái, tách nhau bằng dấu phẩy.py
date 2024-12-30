def sap_xep_va_loai_bo_trung_lap(chuoi):
    # Tách chuỗi thành danh sách các từ
    danh_sach_tu = chuoi.split(',')

    # Loại bỏ từ trùng lặp
    danh_sach_tu = list(set(danh_sach_tu))

    # Sắp xếp danh sách các từ theo thứ tự bảng chữ cái
    danh_sach_tu.sort()
    print(",".join(danh_sach_tu))

chuoi_input = input("")
sap_xep_va_loai_bo_trung_lap(chuoi_input)