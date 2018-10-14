# Bitcoin-Transaction-Parser
A python3 script that searches the Bitcoin blockchain and filters the transactions which contains an OP_RETURN field.

## Motivation
This script was developed to analyze the op_return fields of bitcoin transactions on different contents and to find illegal activities.

## More Information

After the corresponding transactions have been filtered, the found transactions are saved in a SQLite Database with their corresponding information. Finally, the transactions can be graphically displayed with the seaborn library.

##  Installing
Further development requires python3 and pip3.

Instructions for installing Python3 for Linux and Mac OS operating systems:

https://realpython.com/installing-python/


Instructions for installing Pip3:

```
sudo apt-get install python3-pip
```

After installing/updating python and pip the following libraries are needed:

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

## Prerequisites

Befor running the script 

1. The blocks of the Bitcoin blockchain are needed. They can be download with:
* [Bitcoin-Core](https://bitcoin.org/de/download)

2. Before running the script the parameters for a full node connection in config.py must be set
- Desired block range ('start_block' :xxx  and  'end_block':xxx) 

```
.../bitcoin-0.16.2/bin$ ./bitcoind 
```

or 

 run a Bitcoin Full Node with specific parameters in the downloaded file (here it is bitcoin-0.16.2):
 
```
.../bitcoin-0.16.2/bin$ ./bitcoind -server=1 -txindex=1 -rpcuser=rpc -rpcpassword=bitmaster -printtoconsole -testnet=0 
```
--> Attention the parameters for desired block range must be set in config.py

## Built With

* [Visual Studio Code](https://code.visualstudio.com) - Programming tool
* [DB Browser for SQLite](https://sqlitebrowser.org) - Showing Database


## Authors

* **Emine Saracoglu** - *Initial work* - [Python-Bitcoin-Transaction-Parser](https://github.com/MericD/Python-Bitcoin-Transaction-Parser.git)

## License

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
