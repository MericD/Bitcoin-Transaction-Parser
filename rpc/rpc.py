from lib.bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging
import json
import config


# setted parameters in config.py needed for rpy-connection
rpc_user=config.CONFIG['rpc_user']
rpc_password=config.CONFIG['rpc_password']
rpc_ip=config.CONFIG['rpc_ip']
rpc_port=config.CONFIG['rpc_port']



#returns a dictionary ({key -> number of block : value -> {key -> transactionID : value -> decoded raw information of transaction}})
# and the created time of a block 
def get_transactions(block_number):
    block_trans_dec = {}

    rpc_connection= start_connection_to_rpc()
    block_hash = get_the_block_hash(rpc_connection, block_number)
    block_trans = get_all_transactions(rpc_connection, block_hash)[0]
    trans_decoded = decoded_transactions(rpc_connection, block_trans)
    block_trans_dec.update({block_number : trans_decoded})
    time=get_all_transactions(rpc_connection, block_hash)[1]
    return block_trans_dec, time



# start connection to rpc with corresponding information for loggin, IP and port
# set them in config.py
def start_connection_to_rpc():
    logging.basicConfig()
    logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)
    rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpc_user, rpc_password, rpc_ip, rpc_port))
    return rpc_connection



# returns hash of a block - input is the block-number of corresponding block
def get_the_block_hash(rpc_connection, block_number):
    #Step 1 Get the block hash
    block_hash = rpc_connection.getblockhash(block_number)
    return block_hash



# returns from block header all transaction that are stored in corresponding block
# returns created time of corresponding block
def get_all_transactions(rpc_connection,block_hash):
    
    # step 2 get transactions in a block
    # one block looks like this Example:
    #   {
	#	    ...
	#	    "merkleroot": "0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098",
	#	    "tx": [
	#		    "0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098"
	#	    ],
	#	    "time": 1231469665,
    #       ...
	#   }
    #
    block_json = rpc_connection.getblock(block_hash)
    block_trans = block_json['tx']
    block_time = str(block_json['time'])
    return block_trans, block_time


# returns decoded raw transaction that contains all information in a transaction script
# store it in a dictionary trans_decoded ({key -> transactionID: value -> decoded raw information of transaction})
def decoded_transactions(rpc_connection,block_trans):
    trans_decoded = {}
    #Step 3 get decode raw transactions
    for i in range(len(block_trans)):
        txid = block_trans[i]
        rawtx = rpc_connection.getrawtransaction(txid)
        decodedtx = rpc_connection.decoderawtransaction(rawtx)
        print(decodedtx)
        trans_decoded.update({txid : decodedtx})
    return trans_decoded
