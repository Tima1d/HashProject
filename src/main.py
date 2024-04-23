# from sortings import bubble_sort, selection_sort
# from element_search import (
#     linear_find_reward_size_block,
#     binary_find_reward_size_block
# )
from load_blocks import load_transaction_blocks
from NewBlocks.generate_block import generate_block


def main():
    block_data = load_transaction_blocks()

    print(generate_block(block_data[-1]['index'], block_data[-1]['hash']))


if __name__ == "__main__":
    main()
