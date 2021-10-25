import hashlib
import random
import names

'''
Example of blockchain created for digital ledger 

Automate random process of transactions and create chain given number of blocks to be viewed
Make it so that transactions are based on the previous (correct block) - if changed, do not accept transaction

'''

class BoriCoin:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        if len(transaction_list) == 1:
            self.block_data = transaction_list + "-" + previous_block_hash
        else:
            self.block_data =  transaction_list + "-" + previous_block_hash

        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()



def create_chain(block_amount):

    transaction_list = []
    history = []
    temp_block = 0
    first_string = "Initial block"

    for i in range(block_amount):
        transaction_list.append(names.get_full_name() + " sends " + str(round(random.uniform(0, 1000), 2)) + " BoriCoins to "
                                + names.get_full_name())

    return

    for j in range(block_amount):

        if j != 0:
            prev_block = temp_block
            temp_block = BoriCoin(prev_block.block_hash, transaction_list[j])

            if temp_block.previous_block_hash != prev_block.block_hash:
                print("Transaction Authentication Failed")
            else:
                history.append([temp_block.block_data, temp_block.block_hash])
        else:
            temp_block = BoriCoin(hashlib.sha256(first_string.encode()).hexdigest(), transaction_list[j])
            history.append([temp_block.block_data, temp_block.block_hash])


    print_transaction_history(history, block_amount)

    return


def print_transaction_history(history, block_amount):
    j = 0
    with open('ledger.txt', 'w') as f:
        print("Printing the history of the " + str(block_amount) + " transactions using BoriCoin in the following format:\n" \
                                                "['Current block data', 'Current block hash']", file=f)
        while j != block_amount:
            print(history[j], file=f)
            #j += 4
            j+=1

    return


def main():
    block_amount = input("Enter number of transactions to occur: ")
    create_chain(int(block_amount))

    return

if __name__ == '__main__':
    main()