# Py-BitcoinTransactionFilter
Bitcoin transaction filter is a Python3 script that filters all Bitcoin transactions which contains an OP_RETURN field. The found transactions are stored in a SQLite3 database with additional transaction information. Finally, the transactions can be graphically displayed.


## Motivation
This script was developed to analyze the content of the OP_RETURN fields in the output script of Bitcoin transactions. 

# Requirements

## Bitcoin Blockchain Data

The Bitcoin blockchain data is loaded from binary .dat files. These were downloaded via the Bitcoin Core Wallet. The tool and the entire Bitcoin blockchain can be downloaded from the following website: https://bitcoincore.org/en/download/


##  Installation

### Python
* Instructions for installing Python3 for Linux and Mac OS operating systems:
https://realpython.com/installing-python/

* pip3
```
sudo apt-get install python3-pip
```

Following projects are used:

* https://github.com/garethjns/PyBC to parse the .dat files
* https://github.com/jgarzik/python-bitcoinrpc 

Following libraries are needed:

*  python-bitcoinrpc
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
* seaborn
```
pip3 install seaborn
```
* pandas
```
pip3 install pandas
```
* sqlite3
```
pip install pysqlite
```
* logging
```
pip install logging
```


### Prerequisites

* Before running the script the parameters for a full node connection in config.py must be set for the search range ('start_block' :xxx  and  'end_block':xxx) 

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


### Example outputs

- After running the script a database file is created that contains two tables. This file can be open with the tool [DB Browser for SQLite](https://sqlitebrowser.org)

- For statistic visualsation diagramms are plotted

## Built With

* [Visual Studio Code](https://code.visualstudio.com) - Programming tool
* [DB Browser for SQLite](https://sqlitebrowser.org) - Showing Database



## Authors

* **Emine Saracoglu** - *Initial work* - [Python-Bitcoin-Transaction-Parser](https://github.com/MericD/Python-Bitcoin-Transaction-Parser.git)

## Copyright and License Information
GNU Lesser General Public License v2.1 https://github.com/jgarzik/python-bitcoinrpc/blob/master/LICENSE

* https://github.com/garethjns/PyBC to parse the .dat files, which has a BSD 3-Clause "New" or "Revised" License.
