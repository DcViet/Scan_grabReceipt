import re
import csv
import os
import json

with open ('/home/namtran/ITKHTN/output_grab/output_1403.json', 'r') as file:
    data = json.load(file)
    text = data['text_list']

messages = (text) 
#print(text)
#text = '"Ban mu6n goi ai?\n\nKhach hang: Pham Thi Thao Nguy\u00e9n\n+84 3322 28975\n\nTai x\u00e9: Tran Ti\u00e9n Thanh\n+84 7967 72707\n\n", "Ban mu6n goi ai?\n\nod 0) Khach hang: Trung Tran Anh\n\n+84 9699 99038\n\nTai x\u00e9: Phan Thanh Long\n881 2315 3\n\n", "Ban mu\u00e9n goi ai?\n\nKhach hang: V6 Hoang Di\u00e9m\nB +84 3834 44:\n\n3 Thdng tin nay kh\u00e9ng con ton tai.\n\n", "Ban mu\u00e9n goi ai?\n\nKhach hang: Quynh Ngan\n+84 9372 85876\n\nTai x\u00e9: Pham Thanh Tri\u00e9u\n+84 9330 6756 2\n\n", "Ban mu6n goi ai?\n\nlod Khach hang: H6\u00e9 Qu\u00e9c Binh\nfr +84 8689 30121\n\nTai x\u00e9: Nguy\u00e9n Hoang Nam\n+84 8283 02398\n\n", "Ban mu6n goi ai?\n\nfe \u00b0 Khach hang: Ng6 Minh Phic\n\n+84 9070 1012 8\n\n", "Ban mu6n goi ai?\n\ne Khach hang: Carrot Ngoc\nfr +84 9073 0109 1_16 3939 1924 030_R\n\nTai x\u00e9: Lam Quach Ngoc Lot\n+84 7788 6969 6\n\n", "Ban mu6n goi ai?\n\nlod Khach hang: Vu Thi Ha Chau\nfr +84 9837 7688 7\n\nTai x\u00e9: L\u00e9 Qu\u00e9c Thai\n+84 9068 41320\n\n", "Ban mu\u00e9n goi ai?\n\nod 0) Khach hang: Kim Phugng\n\n+84 9722 06969\n\n@ Tai x\u00e9: Va Van Truy\u00e9n\n\n", "Ban mu\u00e9n goi ai?\n\nload \u00b0 Khach hang: Thuy Loan\n\n+84 9818 12479\n\nTai x\u00e9: Nguy\u00e9n Hitu Truc\n\n"' 

#messages = re.findall(r'"([^"]+)"', text)
#print(text)
#print(messages)
'''
for message in messages:
    # extract customer name and phone number using regex
    name = re.findall(r'Khach hang: (.*?)\n', message)
    phone = re.findall(r'\+84 \d{4} \d{5}', message)
    if name and phone:
        print(f"{name[0]}: {phone[0]}")

lines = text.split('\n')
formatted_lines = [line + '\n' for line in lines if line.strip()]
formatted_string = ''.join(formatted_lines)
print(formatted_string)
'''

name_pattern = r"Khach hang: (.+?)\n"
#phone_pattern = r"\+\d{2} \d{4} \d{4,5}"
#phone_pattern = r"\+?\d{2} \d{4} \d{4} \d{1}"
phone_pattern = r"\+?\d{2} [0-9\s]{7,16}"
#phone_pattern = r"\+?\d{2} \d{4} \d{5}|\+?\d{2} \d{4} \d{4} \d{1}"


#phone_pattern = r"(\+84|0)\d{9,10}"

#taixe_pattern = r"Tai x\u00e9: (.+?)\n"

output_dir = '/home/namtran/ITKHTN/output_grab'
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
