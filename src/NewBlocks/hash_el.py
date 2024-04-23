from hashlib import sha256
from copy import copy


def get_hash_transaction(transactions):
    while len(transactions) != 1:

        if len(transactions) % 2 != 0:
            transactions.append(transactions[-1])

        hash_1 = sha256()
        hash_2 = sha256()

        copy_transactions = copy(transactions)
        transactions = []

        for i in range(0, len(copy_transactions), 2):
            hash_1.update(str(copy_transactions[i]).encode('utf-8'))
            hash_2.update(str(copy_transactions[i + 1]).encode('utf-8'))

            transactions.append(hash_1.hexdigest() + hash_2.hexdigest())

    hash = sha256()
    hash.update(str(transactions[0]).encode('utf-8'))
    hash = hash.hexdigest()

    return hash


def get_hash(value):

    hash = sha256()
    hash.update(str(value).encode('utf-8'))
    hash = hash.hexdigest()

    return hash
