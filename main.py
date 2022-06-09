import hashlib


class ZirconBlock:
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.data = "-".join(transaction_list) + "-" + previous_block_hash
        self.hash = hashlib.sha256(self.data.encode()).hexdigest()


t1 = "Andres sends 2 ZC to Will"
t2 = "Vero sends 4 ZC to Betza"
t3 = "Betza sends 0.5 ZC to Will"
t4 = "Betza sends 1 ZC to Gomito"
t5 = "Mateo sends 3 ZC to Andres"
t6 = "Gomito sends 1 ZC to Will"

initial_block = ZirconBlock("Hash Zero", [t1,t2])

print(initial_block.data)
print(initial_block.hash)

second_block = ZirconBlock(initial_block.hash, [t3,t4])

print(second_block.data)
print(second_block.hash)

third_block = ZirconBlock(second_block.hash, [t1,t2])

print(third_block.data)
print(third_block.hash)

    