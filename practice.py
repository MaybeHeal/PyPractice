from random import randint
from itertools import groupby


def list_generator():
    numbers = []
    while len(numbers) < 1000:
        x = randint(0, 3000)
        if x not in numbers:
            numbers.append(x)
    return sorted(numbers)


def converter():
    source_list = list_generator()
    print(source_list)
    inter_list = []
    id_list = []
    not_in_inter_list = []
    not_in_id_list = []

    for i in range(len(source_list) - 1):
        if source_list[i + 1] - source_list[i] <= 4:
            for j in range(source_list[i], source_list[i + 1] - 1):
                not_in_id_list.append(j + 1)
        elif source_list[i + 1] - source_list[i] > 4:
            not_in_inter_list.append([source_list[i] + 1, source_list[i + 1] - 1])
    for k, g in groupby(enumerate(source_list), lambda x: x[0] - x[1]):
        items = [i[1] for i in g]
        if len(items) > 2:
            inter_list.append([items[0], items[-1]])
        else:
            for i in items:
                id_list.append(i)
    print(id_list)
    print(inter_list)
    print(not_in_id_list)
    print(not_in_inter_list)

    res1 = ''
    res2 = ''
    res1 += f'not id in {not_in_id_list}'
    for i in not_in_inter_list:
        res1 += f' or ({i[0]}<=id<={i[1]})'
    res1 += f' or ({source_list[-1] + 1} <= id)'

    res2 += f'id in {id_list}'
    for i in inter_list:
        res2 += f' or ({i[0]}<=id<={i[1]})'

    print(res1)
    print(res2)



    '''not id in [1, 2, 3, 4, 5, 6] or (11<=id<=16) or or or'''


# def converter():
#     source_list = list_generator()
#     print(source_list)
#     # inter_list = []
#     # id_list = []
#     not_in_inter_list = []
#     not_in_id_list = []
#     res = ''
#     for i in range(len(source_list) - 1):
#         if source_list[i + 1] - source_list[i] <= 4:
#             for j in range(source_list[i], source_list[i + 1] - 1):
#                 not_in_id_list.append(j + 1)
#         elif source_list[i + 1] - source_list[i] > 4:
#             not_in_inter_list.append([source_list[i] + 1, source_list[i + 1] - 1])
#
#     print(not_in_id_list)
#     print(not_in_inter_list)
#     res += f'not id in {not_in_id_list}'
#     for i in not_in_inter_list:
#         res += f' or ({i[0]}<=id<={i[1]})'
#     res += f' or ({source_list[-1] + 1} <= id)'
#     print(res)
    '''not id in [1, 2, 3, 4, 5, 6] or (11<=id<=16) or or or'''


if __name__ == '__main__':
    converter()
