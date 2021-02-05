"""-*- coding: utf-8 -*-
@ author: Zhang Chi
@ e-mail: 220200785@mail.seu.edu.cn
@ file: question_1.py
@ project: code
"""
"""part-1: check invalidation"""
inputs = input("Please input a string:")
char_list = list(inputs)  # 将输入的字符串拆分成字符列表
for item in char_list:
    temp = ord(item)  # ord将字符转换为ASCII码形式，ord默认输入是字符（将字符转换为ASCII），chr默认输入是ASCII码（将ASCII码转换为相应的字符）
    if temp < 48 or temp > 57:
        if item != '-':
            print("This input is not valid")
            break

input_list = inputs.split("-")
if '' in input_list:
    print("This input is not valid")
for item in input_list:
    if int(item) < 33 or int(item) > 126:
        print("This input is not valid")
        break
"""part-2:convert to string"""
email_string = ""
for item in input_list:
    email_string += chr(int(item))
print("Email is:", email_string)
"""part-3:check email validation"""
import re
re_email = re.compile(r'^[a-zA-Z\.]+@[a-zA-Z0-9]+\.[a-zA-Z]{3}$')
if re_email.match(email_string):
    print((email_string, True))
else:
    print('False')









