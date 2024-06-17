from web3 import Web3

# Assuming 'w3' is the Web3 instance
w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))
block = w3.eth.get_block('latest')
transaction_count = len(block['transactions'])
print(transaction_count)
