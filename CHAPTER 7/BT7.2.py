def clean_string(input):
    # Loại bỏ khoảng trắng ở đầu và cuối chuỗi
    input = input.strip()
    # Chuyển chữ cái đầu tiên của chuỗi thành chữ thường
    input = input.capitalize()
    # Loại bỏ khoảng trắng trước dấu câu
    input = input.replace(' ,', ',').replace(' ;', ';').replace(' .', '.')
    return input
def xoa_cach(result): 
  words = result.split()
  return " ".join(words)
input = input("")
result = clean_string(input)
print(xoa_cach(result))
