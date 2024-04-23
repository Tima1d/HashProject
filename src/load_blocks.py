from os import listdir
from json import load


def load_transaction_blocks(directory='../Transactions'):
    block_data = [
        load(open(f"{directory}/{filename}", 'r'))
        for filename in listdir(directory)
    ]

    return sorted(block_data, key=lambda block: block['index'])
