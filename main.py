from SQL import sqlite as sql
from BlockParser import parser

print("The block analysis begins.")

sql.initTabel()
sql.addBlock(2,"1961-10-25")
sql.selectTable()

#TODO starts the function for every .dat file in ./Blocks. also wie compare from the start number and finale number
block_trans = parser.read_hash('Blocks/blk00003.dat')
print("Hash Values:" + str(block_trans))