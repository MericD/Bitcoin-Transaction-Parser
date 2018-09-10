from SQL import sqlite as sql
from BlockParser import parser

print("The block analysis begins.")

sql.initTabel()

sql.addBlock(4,"1961-10-25")

sql.selectTable()

parser.read_hash()