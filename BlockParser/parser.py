from pybit.py3.chain import Dat

def read_hash(file):
    dat = Dat(file)
    dat.read_next_block()

    block_trans = {}
    for block_nr, block in dat.blocks.items():
        for trans_nr, trans in block.trans.items():
            hashValue = str(trans.hash)
            print('find block: ' + str(block_nr)+ ' with the transaction hash value: ' + hashValue)
            block_trans.update({block_nr : hashValue})
    
    return block_trans