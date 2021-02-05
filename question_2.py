"""-*- coding: utf-8 -*-
@ Time: 20:58
@ author: Zhang Chi
@ e-mail: 220200785@mail.seu.edu.cn
@ file: question_2.py
@ project: code
"""


def count_birds_num(bird_num, predator_num, week_num):
    # bird_num = 50
    # predator_num = 5
    # week_num = 13

    # 对应存活了多少周的鸟的数量统计列表
    # 从0周到17周
    bird_live_week_num = [0] * 9  # [0, 0, 0, 0, 0, 0, 0, 0, 0]
    bird_live_week_num[0] = bird_num
    bird_alive = bird_num
    # print(bird_alive)
    bird_alive_list = []

    for week in range(week_num + 1):
        if (week % 2 != 0) and week >= 3:
            group = bird_alive // 3
            bird_alive += group * 2
            bird_live_week_num[0] += group * 2

        elif week % 2 == 0 and week > 0:
            index1 = 0
            index2 = -1
            bird_alive -= predator_num * 2
            if bird_alive <= 0:  # 不够吃的
                bird_alive = 0
                for s in range(len(bird_live_week_num)):
                    bird_live_week_num[s] = 0
            else:  # 够吃的
                for p in range(predator_num):
                    # for (i, temp) in enumerate(bird_live_week_num):
                    #     if temp != 0:
                    #         index1 = i
                    #         break
                    index_i = 0
                    for temp in bird_live_week_num:
                        if temp != 0:
                            index1 = index_i
                            break
                        index_i += 1
                    index_j = 0
                    for temp in bird_live_week_num[::-1]:
                        if temp != 0:
                            index2 = len(bird_live_week_num) - index_j - 1
                            break
                        index_j += 1
                    bird_live_week_num[index1] -= 1  # 吃掉年轻的
                    # if bird_live_week_num[index1] < 0:
                    #     bird_live_week_num[index1] = 0
                    bird_live_week_num[index2] -= 1  # 吃掉年老的
                    # if bird_live_week_num[index2] < 0:
                    #     bird_live_week_num[index2] = 0

        # 减去自然8周死亡的数量
        bird_alive -= bird_live_week_num[-1]
        bird_live_week_num[-1] = 0
        # 每进行新的一周，则存活时间整体后移动
        def ahead_one():
            b = bird_live_week_num.pop(0)  # 这个列表把索引是0的元素丢掉
            bird_live_week_num.append(b)
            return bird_live_week_num
        for m in range(len(bird_live_week_num) - 1):
            ahead_one()

        # print(bird_alive)
        bird_alive_list.append(bird_alive)
    print(bird_alive_list)


count_birds_num(50, 5, 13)








