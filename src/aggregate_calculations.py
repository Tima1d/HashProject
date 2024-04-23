# from functools import reduce

from load_blocks import load_transaction_blocks


block_data = load_transaction_blocks()


def calculate_number_transactions_block(block_data):
    block_data.pop(0)

    return [
        (block['index'], len(block['transactions']))
        for block in block_data
    ]

# print(calculate_number_transactions_block(block_data))


def total_number_transactions_blocks(block_data):
    return sum([
        len(block['transactions'])
        for block in block_data
    ])

# print(total_number_transactions_blocks(block_data))


def calculate_total_number_rewards_for_miner(block_data):
    miners_and_their_rewards = {}

    for block in block_data:
        miner_name = block['transactions'][-1]['to']
        miner_reward = block['transactions'][-1]['value']

        if miner_name in miners_and_their_rewards.keys():
            miners_and_their_rewards[miner_name] += miner_reward
        else:
            miners_and_their_rewards[miner_name] = miner_reward

    return miners_and_their_rewards

# print(calculate_total_number_rewards_for_miner(block_data))


def get_max_reward(block_data):
    return max(
            block_data,
            key=lambda block: block['transactions'][-1]['value']
    )['transactions'][-1]['value']

# print(get_max_reward(block_data))


def get_min_reward(block_data):
    return min(
            block_data,
            key=lambda block: block['transactions'][-1]['value']
    )['transactions'][-1]['value']

# print(get_min_reward(block_data))


def get_avg_reward(block_data):

    sum_reward = 0

    for block in block_data:
        for transaction in block['transactions'][:-1:]:
            sum_reward += transaction['value']

    # return sum(*[block['transactions'] for block in block_data]) /
    # total_number_transactions_blocks(block_data)

    return sum_reward / total_number_transactions_blocks(block_data)

# print(get_avg_reward(block_data))


def group_blocks_time(block_data):
    blocks_by_time = {}

    for block in block_data:
        time_block = block['timestamp']

        if time_block in blocks_by_time.keys():
            blocks_by_time[time_block].append(block)
        else:
            blocks_by_time[time_block] = [block]

    return [
        (category, len(blocks_by_time[category]))
        for category in blocks_by_time.keys()
            ]

# print(group_blocks_time(block_data))
