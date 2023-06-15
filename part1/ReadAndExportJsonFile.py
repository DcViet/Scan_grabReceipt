import re
import csv
import os
import json

with open ('/home/.../output_grab/output_1403.json', 'r') as file:
    data = json.load(file)
    text = data['text_list']

messages = (text) 

# sau khi check file json, nhận thấy nội dung file có 1 số nhận dạng -> sử dụng patern để clear data
name_pattern = r"Khach hang: (.+?)\n"
#phone_pattern = r"\+\d{2} \d{4} \d{4,5}"
#phone_pattern = r"\+?\d{2} \d{4} \d{4} \d{1}"
phone_pattern = r"\+?\d{2} [0-9\s]{7,16}"

#phone_pattern = r"\+?\d{2} \d{4} \d{5}|\+?\d{2} \d{4} \d{4} \d{1}"
#phone_pattern = r"(\+84|0)\d{9,10}"
#taixe_pattern = r"Tai x\u00e9: (.+?)\n"

# xuất những data đã lọc ra 1 file và xử lý nó 
output_dir = '/home/namtran/ITKHTN/output_grab'
# tạo 1 file json mới để lưu các dữ liệu đã đọc được và trình bày 
with open(os.path.join(output_dir, 'outputdone.csv'), mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Customer name', 'Phone name'])         

    for message in messages:
        name_match = re.search(name_pattern, message)
        if name_match:
            customer_name = name_match.group(1)
        else:
            customer_name = ""

        phone_match = re.search(phone_pattern, message)
        if phone_match:
            phone_number = phone_match.group(0)
        else:
            phone_number = ""
# test thử xem cái code ở trên có in ra đúng ý mình muốn k , nếu okie thì ghi vào file 
#       print("Customer name:", customer_name)
#       print("Phone number:", phone_number)
#       print("------------------------")
        writer.writerow([customer_name, phone_number])
'''    for message in messages:
        taixename_match = re.search(taixe_pattern, message)
        if taixename_match:
            taixe_name = taixename_match.group(1)
        else:
            taixe_name = ""
    
#    print("Taixe name:", taixe_name)
#    print("------------------------")
#
