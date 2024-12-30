import re
def kiemtra_password(password):
    # Kiểm tra độ dài của mật khẩu
    if 6 <= len(password) <= 17:
        # Kiểm tra chữ cái thường
        if re.search("[a-z]", password):
            # Kiểm tra số
            if re.search("[0-9]", password):
                # Kiểm tra chữ cái hoa
                if re.search("[A-Z]", password):
                    # Kiểm tra ký tự đặc biệt trong [$ # @]
                    if re.search("[$#@]", password):
                        return True
    return False

password1 =  input("")
print(kiemtra_password(password1)) 
