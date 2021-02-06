
"""Below is the code for bitcoin mining"""
from hashlib import sha256
import time

#? Based on amount of power your computer has. Higher the power, higher the number.
maxNonce = 100000000000
# text = "abc"

#? Finding the hexdigit using sha256 library.
def code(text):
    return sha256(text.encode("ascii")).hexdigest()

#? Getting data of a block and inputing for mining.
def mine(blockNumber, transactions, previousHash, prefixZero):
    prefixStr = "0" * prefixZero
    for nonce in range(maxNonce):
        txt = str(blockNumber) + transactions + previousHash + str(nonce)
        newHash = code(txt)
        if newHash.startswith(prefixStr):
            print(f"Successfully mined the block with nonce {nonce}")
            return newHash

    raise BaseException(f"Unable to nine the block.")

#? Main Steps.
if __name__ == "__main__":
    transactions = """
    batman to superman - 20 btc
    ironman to cap - 60 btc
    """
    start = time.time()
    #? Current difficulty
    difficulty = 5
    newHash = mine(5, transactions, "00000000000000000003e1f49e9d32fbdfb2f081babbad9de82942b8e620e345", difficulty)
    end = time.time()

    #? printing total time taken.
    totalTime = end - start
    print(f"Mining time = {totalTime}")
    print(newHash)