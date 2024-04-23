from json import load
from random import randint, choice
from datetime import datetime

from NewBlocks.hash_el import get_hash


def get_names_from_file(path):
    try:
        names = load(open(path, 'r'))

        return names['names']
    except FileNotFoundError:
        print('Неверный путь')

    return None


def generate_transaction(min_transfer_amount=0,
                         max_transfer_amount=400,
                         names=None, path='../Data/names.json'):
    if not names:
        names = get_names_from_file(path)

    transfer_amount = randint(min_transfer_amount,
                              max_transfer_amount * 1000) / 1000

    from_transfer = choice(names)
    to_transfer = choice(names)

    while from_transfer == to_transfer:
        to_transfer = choice(names)

    return {
        'from': from_transfer,
        'to': to_transfer,
        'value': transfer_amount
                   }


def generate_block(index_last_block, pre_hash_last_block, difficulty='0',
                   min_transfer_amount=0,
                   max_transfer_amount=400,
                   names=None, path='../Data/names.json'):

    count_transactions_in_block = randint(3, 12)
    transactions = [
        generate_transaction()
        for _ in range(count_transactions_in_block)
                ]

    index = index_last_block + 1
    pre_hash = pre_hash_last_block
    timestamp = int(datetime.timestamp(datetime.now()))
    transactions = transactions

    i = 0
    hash = '1'

    while hash[0] != difficulty:

        hash = get_hash({
            'index': index,
            'pre_hash': pre_hash,
            'timestamp': timestamp,
            'transactions': transactions,
            'nonce': i})

        i += 1

    return {
        'index': index,
        'pre_hash': pre_hash,
        'timestamp': timestamp,
        'transactions': transactions,
        'nonce': i,
        'hash': hash
    }


# generate_block(block_data['index'], block_data['hash'])
