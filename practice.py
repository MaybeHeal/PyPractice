from itertools import groupby
import time
import numpy as np


def list_generator(scope: int, sampling: int):
    rand_list = np.random.choice(scope, sampling, replace=False)
    return sorted(rand_list)


def converter_in(source_list):
    inter_list = []
    id_list = []
    start = time.time()
    for k, g in groupby(enumerate(source_list), lambda x: x[0] - x[1]):
        items = [i[1] for i in g]
        if len(items) > 2:
            inter_list.append([items[0] - 1, items[-1] + 1])
        else:
            for i in items:
                id_list.append(i)

    # print('Ids:', id_list)
    # print('Intervals:', inter_list)

    res = ''
    res += f'id in {id_list}'
    for i in inter_list:
        res += f' or ({i[0]}<id<{i[1]})'
    end = time.time() - start

    # print('Result:', res)
    return end, len(res)


def converter_not_in(source_list):
    not_in_inter_list = []
    not_in_id_list = []

    start = time.time()
    if source_list[0] != 0:
        if source_list[0] - 0 <= 4:
            for j in range(0, source_list[0]):
                not_in_id_list.append(j)
        elif source_list[0] - 0 > 4:
            not_in_inter_list.append([-1, source_list[0]])
    for i in range(len(source_list) - 1):
        if source_list[i + 1] - source_list[i] <= 4:
            for j in range(source_list[i], source_list[i + 1] - 1):
                not_in_id_list.append(j + 1)
        elif source_list[i + 1] - source_list[i] > 4:
            not_in_inter_list.append([source_list[i], source_list[i + 1]])

    # print('Ids:', not_in_id_list)
    # print('Intervals:', not_in_inter_list)

    res = ''
    res += f'not id in {not_in_id_list}'
    for i in not_in_inter_list:
        res += f' or ({i[0]}<id<{i[1]})'
    res += f' or ({source_list[-1] + 1} <= id)'
    end = time.time() - start

    # print('Result:', res)
    return end, len(res)


def scope_sampling():
    scope_list = [100000000]
    sampling_list = [80]
    for i in scope_list:
        for p in sampling_list:
            script(i, i // 100 * p, p)


def script(scope, sampling, sampling_percent):
    st = time.time()
    l_st = time.time()
    num_list = list_generator(scope=scope, sampling=sampling)
    l_en = time.time()
    # print('Array:', num_list)

    # conv_in = converter_in(num_list)
    conv_not_in = converter_not_in(num_list)

    en = time.time()

    # time_results = {'Converter_in': conv_in[0], 'Converter_not_in': conv_not_in[0]}
    # compr_results = {'Converter_in': conv_in[1], 'Converter_not_in': conv_not_in[1]}

    with open('results.txt', 'a', encoding='utf-8') as file:
        file.write(f'Scope: {scope}\nSampling_percent: {sampling_percent}\n\n')
        file.write(f'List generating time: {l_en - l_st}\n')
        # file.write(f'Converter_in time: {conv_in[0]}\n')
        file.write(f'Converter_not_in time: {conv_not_in[0]}\n')
        file.write(f'General time: {en - st}\n\n')
        # file.write(f'List len: {len(str(num_list))}\nConverter_in len: {conv_in[1]}\nConverter_not_in len: {conv_not_in[1]}\n\n')
        # file.write(f'Best time result: {min(time_results, key=time_results.get)}\n')
        # file.write(f'Best compression: {min(compr_results, key=compr_results.get)}\n\n')
        file.write('============================================\n\n')


if __name__ == '__main__':
    scope_sampling()
