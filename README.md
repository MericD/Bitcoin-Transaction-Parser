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
![bildschirmfoto 2019-02-17 um 21 42 40](https://user-images.githubusercontent.com/23129546/52919363-03e80800-3302-11e9-939c-8b5d7f91873d.png)

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

- After running the script a database file is created that contains two tables. This file can be open with the tool [DB Browser for SQLite](https://sqlitebrowser.org)

- For statistic visualsation diagramms are plotted

![time](https://user-images.githubusercontent.com/23129546/46921047-d5c28680-cff6-11e8-8192-abefaee24a82.png)





## Authors

* **Emine Saracoglu** - *Initial work* - [Py-BitcoinTransactionFilter](https://github.com/MericD/Python-Bitcoin-Transaction-Parser.git)

## Copyright and License Information
The file "LICENSE" contains information on the history of this software, terms & conditions for usage, and a DISCLAIMER OF ALL WARRANTIES.

