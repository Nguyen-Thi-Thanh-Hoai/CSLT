def tiền_xử_lý(đoạn_văn):
  # Thay thế các kí tự đặc biệt bằng khoảng trắng
  đoạn_văn = đoạn_văn.replace("--", " ")
  đoạn_văn = đoạn_văn.replace("----", " ")

  # Ghép các từ liền kề với nhau
  đoạn_văn = đoạn_văn.replace(" ", "")

  # Xóa bỏ các khoảng trống thừa
  đoạn_văn = đoạn_văn.strip()

  return đoạn_văn


đoạn_văn = """--Người---đâu-gặp---gỡ-làm-chi---
Trăm----năm-biết-có---duyên---gì--hay--không.
Ngổn-ngang---trăm-mối---bên---lòng----
----Nên-câu---tuyệt--diệu-ngụ-trong-tính-tình."""

đoạn_văn_xử_lý = tiền_xử_lý(đoạn_văn)
.
print(đoạn_văn_xử_lý)
