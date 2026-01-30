import sys
sys.path.append("/Users/bhavy/Desktop/HackJNU/Project")

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.util.util import hash256
import time
import json


ZERO_HASH = '0'*64
VERSION = 1



class Blockchain:
    def __init__(self):
        self.chain = []
        self.GenesisBlock()                                                                                                                                                                                                                                                                                                                                    

    def GenesisBlock(self):
        BlockHeight = 0
        prev_block_hash = ZERO_HASH
        self.addBlock(BlockHeight, prev_block_hash)

    def addBlock(self, BlockHeight, prev_block_hash):                                                  
        timestamp = int(time.time())
        transactions = f"Codies Alert sent at {BlockHeight}"
        merkle_root = hash256(transactions.encode()).hex()
        bits = "ffff001f"
        blockheader = BlockHeader(VERSION, prev_block_hash, merkle_root, timestamp, bits)
        blockheader.mine()
        self.chain.append(Block(BlockHeight,1, blockheader.__dict__,1, transactions).__dict__)
        print(json.dumps(self.chain, indent=4))

    def main(self):
        while True:
            lastBlock = self.chain[::-1]
            BlockHeight = lastBlock[0]['Height'] + 1
            prev_block_hash = lastBlock[0]['BlockHeader']['blockHash']
            self.addBlock(BlockHeight, prev_block_hash)


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()


