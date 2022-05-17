from web3 import Web3, HTTPProvider, IPCProvider

# Ganache - fake blockchain (testing environment)
# Connecting to Ganache using Web3
# w3 = Web3(HTTPProvider('http://localhost:7545'))
# w3.eth.blockNumber
# w3.eth.getBlock('latest')

# Rinkeby network uses - PoA
# Ropsten network uses - PoW

# from web3 import Web3, IPCProvider
w3 = Web3(IPCProvider(""))