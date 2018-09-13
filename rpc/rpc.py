from Lib.bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging
import json

def get_transactions():
    block_trans_dec = {}
    block_number = 1

    rpc_connection= start_connection_to_rpc()
    
    block_hash = get_the_block_hash(rpc_connection, block_number)

    block_trans = get_all_transactions(rpc_connection, block_hash)

    trans_decoded = decoded_transactions(rpc_connection, block_trans)

    block_trans_dec.update({block_number : trans_decoded})

    return block_trans_dec

def start_connection_to_rpc():
    logging.basicConfig()
    logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)

    rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%('rpc', 'bitmaster'))
    return rpc_connection

def get_the_block_hash(rpc_connection, block_number):
    #Step 1 Get the block hash
    block_hash = rpc_connection.getblockhash(block_number)
    return block_hash

def get_all_transactions(rpc_connection,block_hash):
    #Step 2 get transactions of the block
    #One trancation look like this Example:
    #   {
	#	    "hash": "00000000839a8e6886ab5951d76f411475428afc90947ee320161bbf18eb6048",
	#	    "confirmations": 541152,
	#	    "strippedsize": 215,
	#	    "size": 215,
	#	    "weight": 860,
	#	    "height": 1,
	#	    "version": 1,
	#	    "versionHex": "00000001",
	#	    "merkleroot": "0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098",
	#	    "tx": [
	#		    "0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098"
	#	    ],
	#	    "time": 1231469665,
	#	    "mediantime": 1231469665,
	#	    "nonce": 2573394689,
	#	    "bits": "1d00ffff",
	#	    "difficulty": 1,
	#	    "chainwork": "0000000000000000000000000000000000000000000000000000000200020002",
	#	    "previousblockhash": "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f",
	#	    "nextblockhash": "000000006a625f06636b8bb6ac7b960a8d03705d1ace08b1a19da3fdcc99ddbd"
	#   }
    #
    block_json = rpc_connection.getblock(block_hash)
    block_trans = block_json['tx']
    return block_trans

def decoded_transactions(rpc_connection,block_trans):
    trans_decoded = {}
    #Step 3 get decode raw transactions
    for i in range(len(block_trans)):
        txid = block_trans[i]
        #txid = '0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098'
        rawtx = rpc_connection.getrawtransaction(txid)
        decodedtx = rpc_connection.decoderawtransaction(rawtx)
        print(decodedtx)
        trans_decoded.update({txid : decodedtx})
    return trans_decoded