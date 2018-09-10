from SQL import sqlite as sql
from BlockParser import parser
from ChainQueryCrawler import crwaler

print("The block analysis begins.")

#TODO starts the function for every .dat file in ./Blocks. also wie compare from the start number and finale number
block_trans = parser.read_hash('Blocks/blk00003.dat')
print("Hash Values:" + str(block_trans))

json_file = crwaler.start_crwaler("492fcdecf0803a458c0240b4947063d5496df6f9b95056f33de73e391110f805")

#TODO find OP_RESULT
sql.initTabel()
sql.addBlock(2,"1961-10-25")
sql.selectTable()