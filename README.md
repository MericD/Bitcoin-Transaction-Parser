# Py-BitcoinTransactionFilter
Bitcoin transaction filter is a Python3 script that filters all Bitcoin transactions which contains an OP_RETURN field. The found transactions are stored in a SQLite3 database with additional transaction information. Finally, the transactions can be graphically displayed.


## Motivation
This script was developed to analyze the content of the OP_RETURN fields in the output script of Bitcoin transactions. 

# Requirements

## Bitcoin Blockchain Data

The Bitcoin blockchain data is loaded from binary .dat files. These were downloaded via the Bitcoin Core Wallet. The tool and the entire Bitcoin blockchain can be downloaded for Windows, Linux and Mac OS from the following website: https://bitcoincore.org/en/download/


##  Installation

### Python
* Instructions for installing Python3 for Windows, Linux and Mac OS operating systems:
https://realpython.com/installing-python/

* pip3
```
sudo apt-get install python3-pip
```

Following liebraries are needed:

* https://github.com/garethjns/PyBC to parse the .dat files
* https://github.com/jgarzik/python-bitcoinrpc 
```
pip install python-bitcoinrpc
```

* base58
```
pip3 install base58
```
* hashlib
```
pip3 install hashlib
```
* numpy
```
pip3 install numpy
```
* matplotlib
```
pip3 install -U matplotlib
```
* seaborn: https://github.com/mwaskom/seaborn
```
pip3 install seaborn
```
* pandas
```
pip3 install pandas
```
* sqlite3: https://github.com/ghaering/pysqlite
```
pip install pysqlite 
```
* logging
```
pip install logging
```

## Built With

* [Visual Studio Code](https://code.visualstudio.com) - Programming tool
* [DB Browser for SQLite](https://sqlitebrowser.org) - Showing Database


### Prerequisites

* Before running the script, the parameters for a full node connection in config.py must be set. Mainly the searchrange of the blocks and the database name:

```ruby
'database_file_name': 'db1.db',
'start_block': 1,
'end_block':546000,
```

* Run the full node
```
.../bitcoin-0.16.2/bin$ ./bitcoind 
```

or 
 
```
.../bitcoin-0.16.2/bin$ ./bitcoind -server=1 -txindex=1 -rpcuser=rpc -rpcpassword=bitmaster -printtoconsole -testnet=0 
```

* Run the Python script
```
$ python3 main.py
```


# Examples

* The script creates two basic tables for the SQLite3 database. The first table contains all block numbers containing OP_RETURN transactions with their created data. The second table lists all transactions with the corresponding transaction information.


![bildschirmfoto 2019-02-17 um 22 16 09](https://user-images.githubusercontent.com/23129546/52919404-748f2480-3302-11e9-8a7d-1b98f29e839c.png)

![bildschirmfoto 2019-02-17 um 22 16 29](https://user-images.githubusercontent.com/23129546/52919417-87095e00-3302-11e9-86b3-69382015d119.png)

* In hex_converting.py, adding the code lines can create an additional table with transaction information for the corresponding category. The default category is 'Non-ASCII decodable strings'

```ruby
i.append(len(j)/2)
hf.save_op_sql(i)
```

ReadBlocks
Reading binary data from disk
HashBlock
Compile the relevant information in a block header
Hash it to verify it's valid
HashTransaction
Compile the relevant transaction data
Hash it to verify it's valid
DecodeOutputScripts
Process transaction output script to list of OP_CODES and data
GetOuputAddress
Convert data in output script to a bitcoin address
BlockChainInfoAPI
How to query Blockchain.info's api
And use it to verify transactions and blocks
Export
Explorting blocks to other formats indlucing dicts and Pandas DataFrames.



- After running the script a database file is created that contains two tables. This file can be open with the tool [DB Browser for SQLite](https://sqlitebrowser.org)

- For statistic visualsation diagramms are plotted

![time](https://user-images.githubusercontent.com/23129546/46921047-d5c28680-cff6-11e8-8192-abefaee24a82.png)



![bildschirmfoto 2019-02-17 um 22 17 44](https://user-images.githubusercontent.com/23129546/52919423-9ab4c480-3302-11e9-8c21-18aad8d392f1.png)



## Authors

* **Emine Saracoglu** - *Initial work* - [Py-BitcoinTransactionFilter](https://github.com/MericD/Python-Bitcoin-Transaction-Parser.git)

## Copyright and License Information
The file "LICENSE" contains information on the history of this software, terms & conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.

