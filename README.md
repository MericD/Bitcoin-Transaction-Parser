# Bitcoin-Transaction-Parser
A python3 script that searches the Bitcoin blockchain and filters the transactions which contains an OP_RETURN field.

## Motivation
This script was developed to analyze the content of op_return fields of bitcoin transactions on different contents.
## More Information

After the corresponding transactions have been filtered, the found transactions are saved in a SQLite3 Database with their corresponding information. Finally, the transactions can be graphically displayed with the seaborn library.

##  Installing
Further development requires python3 and pip3.

Instructions for installing Python3 for Linux and Mac OS operating systems:

https://realpython.com/installing-python/


Instructions for installing Pip3:

```
sudo apt-get install python3-pip
```

After installing/updating python and pip the following libraries are needed:

For decoding:
```
pip3 install hashlib
pip3 install base58
```

For displaying diagrams:
```
pip3 install seaborn
```

For used arrays:
```
pip3 install numpy
```

For plotting diagrams:
```
pip3 install -U matplotlib
```

For reading files:
```
pip3 install pandas
```

Conection to bitcoin server:
```
pip install python-bitcoinrpc
```

### Prerequisites

Befor running the script 

1. The Bitcoin blockchain are needed. They can be download in:
* [Bitcoin-Core](https://bitcoin.org/de/download)
#the *.dat Files are not pushed to the git-repository because their size are bigger than 100mb!

2. Before running the script the parameters for a full node connection in config.py must be set
- Desired block range ('start_block' :xxx  and  'end_block':xxx) 

```
.../bitcoin-0.16.2/bin$ ./bitcoind 
```

or 

 run a Bitcoin full Node with specific parameters in the downloaded file (here it is bitcoin-0.16.2):
 
```
.../bitcoin-0.16.2/bin$ ./bitcoind -server=1 -txindex=1 -rpcuser=rpc -rpcpassword=bitmaster -printtoconsole -testnet=0 
```
--> Attention the parameters for desired block range must be set in config.py

3. run the script in the file Python-Bitcoin-Transaction-Parser :
```
$ python3 main.py
```

4. The following Project is used: https://github.com/garethjns/PyBC to parse the .dat files, which has a BSD 3-Clause "New" or "Revised" License.

### Example outputs

- After running the script a database file is created that contains two tables. This file can be open with the tool [DB Browser for SQLite](https://sqlitebrowser.org)

- For statistic visualsation diagramms are plotted

## Built With

* [Visual Studio Code](https://code.visualstudio.com) - Programming tool
* [DB Browser for SQLite](https://sqlitebrowser.org) - Showing Database



## Authors

* **Emine Saracoglu** - *Initial work* - [Python-Bitcoin-Transaction-Parser](https://github.com/MericD/Python-Bitcoin-Transaction-Parser.git)

## License

