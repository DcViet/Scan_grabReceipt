import os
import pytesseract
import json
from PIL import Image

# path file chứa ảnh
image_folder = '/home/grab_image/image1403'

# path thư mục xuất file
output_folder = '/home/output_grab'

# path xuất file Json
output_file = os.path.join(output_folder, 'output_1403.json')

# danh sách chứa những ký tự được trích xuất ra từ ảnh
text_list = []

# Đọc 1 lúc nhiều tấm ảnh, lặp qua tất cả các ảnh có trong thư mục
for filename in os.listdir(image_folder):
    # Check những file ảnh (đuôi .jpg, .jpeg, .png, ...)
    if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
        # Sử dụng PIL để tải các hình ảnh trong thư mục vào
        img = Image.open(os.path.join(image_folder, filename))
       
        # Sử dụng Tesseract để trích xuất chữ từ ảnh
        text = pytesseract.image_to_string(img)

        # Append những chữ trích xuất được vào danh sách
        text_list.append(text)
        
# Tạo 1 JSON object với danh sách chữ được trích xuất
data = {'text_list': text_list}

# Lưu JSON object ra 1 file
with open(output_file, 'w') as outfile:
    json.dump(data, outfile)
