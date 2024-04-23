def linear_find_reward_size_block(block_data, find_number):
    counter = 0

    for i in range(len(block_data)):
        counter += 1

        if block_data[i]['index'] == find_number:
            return (block_data[i], counter)


def binary_find_reward_size_block(block_data, find_number):
    if not block_data:
        return 'Пустой массив'
    if block_data[-1]['index'] < find_number or find_number < 0:
        return 'Ничего не найдено'

    counter = 0
    low = 0
    high = len(block_data) - 1
    mid = len(block_data) // 2

    while block_data[mid]['index'] != find_number:
        counter += 1

        if find_number > block_data[mid]['index']:
            low = mid + 1
        else:
            high = mid - 1

        mid = (low + high) // 2

    return (block_data[mid], counter)
