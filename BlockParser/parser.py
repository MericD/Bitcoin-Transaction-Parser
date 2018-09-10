from pybit.py3.chain import Dat

def read_hash():
    f = 'Blocks/blk00003.dat'
    dat = Dat(f)
    dat.read_next_block()

    hashValue = str(dat.blocks[0].trans[0].hash)

    print(dat.blocks[0].trans[0])
    print("Hash Value:" + hashValue)
    return hashValue