"""-*- coding: utf-8 -*-
@ Time: 18:13
@ author: Zhang Chi
@ e-mail: 220200785@mail.seu.edu.cn
@ file: question_4.py
@ project: code
"""


# first form
def first_form(inputs):
    # inputs = input("Please input a string:")
    word_list = inputs.split(' ')
    new_word_list = []
    for word in word_list:
        chr_list = list(word)
        if chr_list[0] in ['a', 'e', 'i', 'o', 'u']:
            new_word_list.append(word + 'key')
        elif chr_list[0] not in ['a', 'e', 'i', 'o', 'u'] and chr_list[0].isalpha():
            consonant_string = ''
            index = 0
            index_i = 0
            for item in chr_list:
                if item not in ['a', 'e', 'i', 'o', 'u'] and item.isalpha():
                    consonant_string += item
                    index = index_i
                else:
                    break
                index_i += 1
            new_word_list.append(word[index+1:] + consonant_string + 'ey')
        elif not chr_list[0].isalpha():
            new_word_list.append(word)
    new_form = " ".join(new_word_list)
    # print(new_form)
    return new_form


def second_form(inputs):
    # inputs = input("Please input a string:")
    inputs_list = list(inputs)
    new_form_list = []
    for item in inputs_list:
        if (item in ['a', 'e', 'i', 'o', 'u']) or (not item.isalpha()):
            new_form_list.append(item)
        elif item in ['B', 'b', 'S', 's', 'L', 'l', 'T', 't', 'D', 'd', 'M', 'm', 'V', 'v', 'N', 'n', 'G', 'g']:
            new_form_list.append(item.upper())
            new_form_list.append('u')
            new_form_list.append(item.lower())
        elif item in ['C', 'c', 'H', 'h']:
            new_form_list.append(item.upper())
            new_form_list.append('ash')
        elif item in ['P', 'p', 'Y', 'y', 'Z', 'z']:
            new_form_list.append(item.upper())
            new_form_list.append('ub')
        elif item in ['K', 'k']:
            new_form_list.append('Kuck')
        elif item in ['F', 'f']:
            new_form_list.append('Fud')
        elif item in ['W', 'w']:
            new_form_list.append('Wack')
        elif item in ['X', 'x']:
            new_form_list.append('Ex')
        elif item in ['Q', 'q']:
            new_form_list.append('Quack')
        elif item in ['J', 'j']:
            new_form_list.append('Jay')
        elif item in ['R', 'r']:
            new_form_list.append('Rug')
    new_form = "".join(new_form_list)

    # print(new_form)
    return new_form


def convert2funny_language():
    inputs = input("Please input a string:")
    new_form1 = first_form(inputs)
    new_form2 = second_form(inputs)

    print((new_form1, new_form2))


if __name__ == '__main__':
    convert2funny_language()





