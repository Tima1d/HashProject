from os import listdir
from json import load

from itertools import takewhile
from functools import reduce


def load_transaction_blocks(directory='./transactions'):
    block_data = [
        load(open(f"{directory}/{filename}", 'r'))
        for filename in listdir(directory)
    ]

    # Предварительная сортировка по индексам и удаление первого элемента(у него странное вознаграждение)
    block_data.sort(key = lambda block: block['index'])
    block_data.pop(0)

    return block_data

block_data = load_transaction_blocks()

#print(*load_transaction_blocks(), sep="\n")


def find_special_block(blocks):
    for block in blocks:
        if block['hash'][-3::] == '000':
            return block['index'], block['transactions'][-1]['to']

#print(find_special_block(block_data))


def find_smallest_fork(blocks):
    indices = sorted([block['index'] for block in blocks])

    # Поиск индексов блоков, которые входят в форк
    gap_between_indices = [indices[i] for i in range(len(indices) - 1) if indices[i] - indices[i + 1] == 0]

    fork_length = []
    count = 0
    # Создание массива с длинами форков
    for i in range(len(gap_between_indices) - 1):
        count += 1
        if gap_between_indices[i] - gap_between_indices[i + 1] != -1:
             fork_length.append(count)
             count = 0

    return min(fork_length)

#print(find_smallest_fork(block_data))


def find_first_block_of_shortest_fork(blocks):
    indices = sorted([block['index'] for block in blocks])

    # Поиск индексов блоков, которые входят в форк
    gap_between_indices = [indices[i] for i in range(len(indices) - 1) if indices[i] - indices[i + 1] == 0]

    # Добавление форка в конец массива для чтения последнего настоящего форка циклом
    gap_between_indices.append(gap_between_indices[-1]+2)

    first_blocks_and_lengh_forks = []
    start_of_the_fork = gap_between_indices[0]
    # Создание массива кортежей с индексом начального блока и длиной форка
    for i in range(len(gap_between_indices) - 1):
        if gap_between_indices[i] - gap_between_indices[i + 1] != -1:
            # Блок с индексом start_of_the_fork тоже входит в форк, поэтому +1
            first_blocks_and_lengh_forks.append((start_of_the_fork, gap_between_indices[i] - start_of_the_fork + 1))

            start_of_the_fork = gap_between_indices[i + 1]

    minimum_fork_data = reduce(lambda x,y: x if x[1] < y[1] else y, first_blocks_and_lengh_forks)

    return minimum_fork_data[0]

#print(find_first_block_of_shortest_fork(block_data))


def find_largest_block(blocks):
    indices = sorted([block['index'] for block in blocks])

    # Другой способ решения
    # a = [indices[i] - indices[i+1] for i in range(len(indices)-1)]
    # a = [a[i] for i in range(1, len(a)) if a[i-1] != 0]
    # a = [list(group) for _, group in groupby(a)]
    # a = [i for i in a if 0 in i]
    # return len(max(a))

    # Индексы блоков, которые входят в форк
    gap_between_indices = [indices[i] for i in range(len(indices) - 1) if indices[i] - indices[i + 1] == 0]

    fork_length = []
    count = 0
    # Создание массива с длинами форков
    for i in range(len(gap_between_indices) - 1):
        count += 1
        if gap_between_indices[i] - gap_between_indices[i + 1] != -1:
             fork_length.append(count)
             count = 0

    return max(fork_length)

#print(find_largest_block(block_data))


def find_last_block_hash_of_longest_fork(block_data):
    sorted_blocks = [(block['timestamp'], block['index'], block['hash']) for block in block_data]
    sorted_blocks.sort()

    # Определение пропущенных блоков (начало форков)
    forks_start_data = []
    expected_next_index = sorted_blocks[0][1]
    for block in sorted_blocks:
        if block[1] == expected_next_index:
            expected_next_index += 1
        else:
            forks_start_data.append((block[1], block[2]))  # Сохранение индекса и хэша блока

    # Анализ длины форков и выбор последнего блока самого длинного форка
    longest_fork_details = []
    min_block_index_of_current_fork = forks_start_data[0][0]
    for i in range(len(forks_start_data) - 1):
        if forks_start_data[i + 1][0] - forks_start_data[i][0] != 1:
            fork_length = forks_start_data[i][0] - min_block_index_of_current_fork
            longest_fork_details.append((fork_length, forks_start_data[i][1]))

            min_block_index_of_current_fork = forks_start_data[i + 1][0]

    # Возвращение хэша последнего блока в наиболее длинной отброшенной ветке
    return max(longest_fork_details)[1]

#print(find_last_block_hash_of_longest_fork(block_data))


def find_number_forks(block_data):
    indices = sorted([block['index'] for block in block_data])

    # Поиск индексов блоков, которые входят в форк
    gap_between_indices = [indices[i] for i in range(len(indices) - 1) if indices[i] - indices[i + 1] == 0]

    number_forks = 0
    # Поиск количества форков
    for i in range(len(gap_between_indices) - 1):
        if gap_between_indices[i] - gap_between_indices[i + 1] != -1:
            number_forks += 1

    return number_forks

#print(find_number_forks(block_data))


def find_reward_size_block_71(block_data):
    return next((block['transactions'][-1]['value'] for block in block_data if block['index'] == 71), None)

#print(find_reward_size_block_71(block_data))


def searching_remuneration_reduction_period(block_data):
    block_data.sort(key = lambda block: block['index'])

    # # Удаление индесков блоков форков(Можно просто заменить функциями set(list()) )
    # block_data = [block_data[i] for i in range(len(block_data) - 1) if block_data[i]['index'] != block_data[i + 1]['index']]

    # Удалене первого блока(У него странное вожнаграждение)
    block_data.pop(0)

    reward_for_first_block = block_data[0]['transactions'][-1]['value']

    # Почти равносильно takewhile
    # mass = []
    # for block in block_data:
    #     if block['transactions'][-1]['value'] < reward_for_first_block:
    #         mass.append(block['index'])
    #     else:
    #         break

    pre_halving_and_fork_blocks = takewhile(lambda block: block['transactions'][-1]['value'] == reward_for_first_block, block_data)
    pre_halving_and_fork_block_indices = (block['index'] for block in pre_halving_and_fork_blocks)

    # Подсчет количства блоко до халвинга без учета блоков форков
    return len(set(pre_halving_and_fork_block_indices))

#print(searching_remuneration_reduction_period(block_data))


def finding_remuneration_reduction_factor(block_data):
    initial_reward_price = block_data[0]['transactions'][-1]['value']

    reward_price_after_halving = next((
        block['transactions'][-1]['value'] 
        for block in block_data 
        if block['transactions'][-1]['value'] != initial_reward_price
    ), None)

    return round(initial_reward_price / reward_price_after_halving, 2)

#print(finding_remuneration_reduction_factor(block_data))


def find_block_with_reward_of_0_09(block_data):
    remuneration_reduction_factor = finding_remuneration_reduction_factor(block_data)
    reward_price = block_data[0]['transactions'][-1]['value']
    block_number = 0

    while reward_price > 0.09:
        reward_price /= remuneration_reduction_factor
        block_number += 16

    return block_number

#print(find_block_with_reward_of_0_09(block_data))


def find_blocks_with_secret_info(block_data):
    block_data_without_forks = [block_data[0]]

    # Утсечение форков
    for i in range(len(block_data) - 1):
        if block_data[i + 1]['index'] - block_data[i]['index'] == 0:

            # Нахождение timestamp блока после окончания форка
            timestamp_fork_winning_branch = next((
                block_data[j]['timestamp'] 
                for j in range(i, len(block_data) - 1, 2) 
                if block_data[j + 1]['index'] - block_data[j]['index'] != 0
            ), None)

            if block_data[i]['timestamp'] == timestamp_fork_winning_branch:
                block_data_without_forks.append(block_data[i])
            else:
                block_data_without_forks.append(block_data[i + 1])

        else:
            if block_data[i]['index'] != block_data_without_forks[-1]['index']:
                block_data_without_forks.append(block_data[i])

    str_with_all_secret_info = ''

    for block in block_data_without_forks:
        if block['secret_info'] != '':
            str_with_all_secret_info += block['secret_info']

    return str_with_all_secret_info

#print(find_blocks_with_secret_info(block_data))


def conversion_from_hex_to_str(hex_string):
    bytes_from_hex = bytes.fromhex(hex_string)
    text = bytes_from_hex.decode('utf-8')

    return text

hex_key_string = find_blocks_with_secret_info(block_data)
print(conversion_from_hex_to_str(hex_key_string))