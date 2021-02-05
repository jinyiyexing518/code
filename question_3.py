"""-*- coding: utf-8 -*-
@ Time: 10:47
@ author: Zhang Chi
@ e-mail: 220200785@mail.seu.edu.cn
@ file: question_3.py
@ project: code
"""
purchase_price = eval(input("Enter purchase price($):"))
down_payment = purchase_price * 0.12
month_repayment = purchase_price * 0.06
init_opening_balance = purchase_price - down_payment
closing_balance = 0.0
if month_repayment - 0.01 < 0:
    print("The loan might never paid off!")
else:
    print('-'*96)
    # print Header
    space1 = " "
    space2 = "|"
    print("{:<7}{}".format(space1 + "Month" + space1, space2), end="")
    print("{:<13}{}".format(space1 + "Opening Bal" + space1, space2), end="")
    print("{:<10}{}".format(space1 + "Interest" + space1, space2), end="")
    print("{:<11}{}".format(space1 + "Principal" + space1, space2), end="")
    print("{:<11}{}".format(space1 + "Repayment" + space1, space2), end="")
    print("{:<13}{}".format(space1 + "Closing Bal" + space1, space2), end="")
    print("{:<12}{}".format(space1 + "Percentage" + space1, space2), end="")
    print("{:<12}".format(space1 + "Progress" + space1))
    print('-'*96)

    month = 1
    opening_balance = init_opening_balance
    interest = round(opening_balance * 0.15 / 12, 2)
    principal = month_repayment - interest
    closing_balance = round(opening_balance - principal, 2)
    percentage = closing_balance / init_opening_balance
    num = round(10*percentage)
    progress = num * '*'
    while opening_balance > 0:
        print("{}{:<5}{}{}".format(space1, month, space1, space2), end="")
        print("{}{:<11.2f}{}{}".format(space1, opening_balance, space1, space2), end="")
        print("{}{:<8.2f}{}{}".format(space1, interest, space1, space2), end="")
        print("{}{:<9.2f}{}{}".format(space1, principal, space1, space2), end="")
        print("{}{:<9.2f}{}{}".format(space1, month_repayment, space1, space2), end="")
        print("{}{:<11.2f}{}{}".format(space1, closing_balance, space1, space2), end="")
        print("{}{:>10.2%}{}{}".format(space1, percentage, space1, space2), end="")
        print("{}{:<10}{}".format(space1, progress, space1))
        month += 1
        opening_balance = closing_balance
        interest = round(opening_balance * 0.15 / 12, 2)
        if opening_balance <= month_repayment:
            principal = opening_balance
            month_repayment = principal + interest
        else:
            principal = month_repayment - interest
        closing_balance = round(opening_balance - principal, 2)
        percentage = closing_balance / init_opening_balance
        num = round(10 * percentage)
        progress = num * '*'





















