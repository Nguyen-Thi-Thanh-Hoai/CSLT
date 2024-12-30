def tach_email(input_str):
    # Tìm vị trí của chuỗi "Email:"
    email= input_str.find("Email:")
    # Nếu có "Email:" trong chuỗi
    if email!= -1:
        # Tách phần của chuỗi sau "Email:"
        phan_email = input_str[email + len("Email:"):].strip()
        # Nếu email_part không rỗng, in ra email
        if phan_email:
            print(phan_email)
        else:
            print("")
    else:
        print("")
input_string = input("Ho ten:")
tach_email(input_string)