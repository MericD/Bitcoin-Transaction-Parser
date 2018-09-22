from lib.bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging
import json
import config

rpc_user=config.CONFIG['rpc_user']
rpc_password=config.CONFIG['rpc_password']
rpc_ip=config.CONFIG['rpc_ip']
rpc_port=config.CONFIG['rpc_port']

def get_transactions(block_number):
    block_trans_dec = {}

    rpc_connection= start_connection_to_rpc()
    
    block_hash = get_the_block_hash(rpc_connection, block_number)

    block_trans = get_all_transactions(rpc_connection, block_hash)

    trans_decoded = decoded_transactions(rpc_connection, block_trans)

    block_trans_dec.update({block_number : trans_decoded})

    return block_trans_dec

def start_connection_to_rpc():
    logging.basicConfig()
    logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)

    rpc_connection = AuthServiceProxy("http://%s:%s@%s:%s"%(rpc_user, rpc_password, rpc_ip, rpc_port))
    return rpc_connection

def get_the_block_hash(rpc_connection, block_number):
    #Step 1 Get the block hash
    block_hash = rpc_connection.getblockhash(block_number)
    return block_hash

def get_all_transactions(rpc_connection,block_hash):
    #Step 2 get transactions of the block
    #One trancation look like this Example:
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
    print("\n" + "-----------------------------------------------------" + block_json[time] + "\n")
    block_trans = block_json['tx']
    return block_trans

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
