from Blockchain.Backend.util.util import hash256


class BlockHeader:
    def __init__(self, version, prev_block_hash, merkle_root,timestamp,bits):
        self.version = version
        self.prev_block_hash = prev_block_hash
        self.timestamp = timestamp
        self.merkle_root = merkle_root
        self.bits = bits
        self.nonce = 0
        self.blockHash = ''  # Initialize blockHash to an empty string
    
    def mine(self):
        while (self.blockHash[0:4] != '0000'): # mine until the blockHash starts with 4 zeros
            self.blockHash = hash256((str(self.version) + self.prev_block_hash + str(self.timestamp) + self.merkle_root + str(self.bits) + str(self.nonce)).encode('utf-8')).hex()
            self.nonce += 1
            print(f"Missing Started {self.nonce}",end="\r")
