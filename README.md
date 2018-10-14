# Bitcoin-Transaction-Parser
A python3 script that searches the Bitcoin blockchain and filters the transactions which contains an OP_RETURN field. The found transactions are saved in a SQLite Database with their corresponding information. Finally, the transactions can be graphically displayed with the seaborn library.

## Motivation
This script was developed to analyze the op_return fields of bitcoin transactions on different contents and to find illegal activities.

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


from lib.bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


### More Information

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
