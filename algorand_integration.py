from algosdk import account, mnemonic, transaction
from algosdk.v2client import algod

def connect_algorand():
    algod_token = "YourAlgodAPIToken"
    algod_address = "https://testnet-api.algonode.cloud"
    return algod.AlgodClient(algod_token, algod_address)

def write_to_blockchain(cert_hash):
    client = connect_algorand()
    print(f"🔗 Pretending to send certificate hash to Algorand blockchain...")
    print(f"Hash stored: {cert_hash}")

if __name__ == "__main__":
    sample_hash = "abc123def456..."
    write_to_blockchain(sample_hash)
