from web3 import Web3
import json

setupContract = "0x1AC90AFd478F30f2D617b3Cb76ee00Dd73A9E4d3"
url = "https://eth-sepolia.g.alchemy.com/v2/SMfUKiFXRNaIsjRSccFuYCq8Q3QJgks8"
provider = Web3(Web3.HTTPProvider(url))

with open("setup.json") as f:       #json file with the contract ABI
    setup_json = json.load(f)

setup = provider.eth.contract(address=setupContract, abi = setup_json)

print(setup.functions.enterVenue().call())