"""-*- coding: utf-8 -*-
@ Time: 23:09
@ author: Zhang Chi
@ e-mail: 220200785@mail.seu.edu.cn
@ file: test1.py
@ project: code
"""


def is_valid_input(inputs):
    m = inputs.split("-")
    for i in m:
        if not i.isdigit() or not 33 <= int(i) < 126:
            return False, None
    return True, inputs


def convert_to_str(s):
    m = s.split('-')
    n = ""
    for i in m:
        n = n + chr(int(i))
    return n


def is_valid_email(n):
    n_1 = n.find("@")
    n_2 = n.find('.')
    a = n[: n_1]
    b = n[n_1 + 1: n_2]
    c = n[n_2 + 1:]
    if len(a) >= 1 and (a.isdigit() or a.isalpha()) and \
            len(b) >= 1 and (b.isdigit() or b.isalpha()) and len(c) >= 1 and (c.isdigit() or c.isalpha()):
        return (n, True)
    else:
        return (n, False)


inputs = input("Please input a string:")
valid, valid_str = is_valid_input(inputs)
if not valid:
    print('This input is not valid')
elif valid:
    email_str = convert_to_str(valid_str)
    print(is_valid_email(email_str))




