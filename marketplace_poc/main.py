import json
from web3 import Web3
import os

rpc_url = os.environ.get("RPC_URL")
ipfs_api_url = os.environ.get("IPFS_API_URL")
w3 = Web3(Web3.HTTPProvider(rpc_url))

if w3.is_connected():
    print("Connected to blockchain")
else:
    print("Failed to connect")
    exit()

contract_address = "0x5FbDB2315678afecb367f032d93F642f64180aa3" 

contract_abi = "./contracts/OaseesMarketplace.json"

with open(contract_abi, "r") as f:
    contract_abi = json.load(f)

try:
    checksummed_address = w3.to_checksum_address(contract_address)
    contract = w3.eth.contract(address=checksummed_address, abi=contract_abi)
except Exception as e:
    print(f"Error creating contract object: {e}")
    if "YOUR_CONTRACT_ADDRESS_HERE" in contract_address:
         print("Please update 'contract_address' with a valid Ethereum address.")
    exit()

try:
    result = contract.functions.getListedNfts().call()
    
    import requests

    def fetch_from_ipfs(ipfs_hash):
        local_gateway = f"{ipfs_api_url}/ipfs/" 
        url = f"{local_gateway}{ipfs_hash}"
        
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return f"Error fetching from local node: {e}"

    for res in result:
        ipfs_hash = res[5]

        if ipfs_hash:
            data = fetch_from_ipfs(ipfs_hash)
            data = json.loads(data)
            print(f"ID: {res[1]}\t IPFS Hash: {ipfs_hash}\tTitle: {data['title']}")

except Exception as e:
    print(f"Error calling contract method: {e}")
