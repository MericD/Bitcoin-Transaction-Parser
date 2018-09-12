from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
import logging

logging.basicConfig()
logging.getLogger("BitcoinRPC").setLevel(logging.DEBUG)

rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:8332"%('rpc', 'bitmaster'))
print(rpc_connection.getblockchaininfo())

txid = '0e3e2357e806b6cdb1f70b54c3a3a17b6714ee1f0e68bebb44a74b1efd512098'
rawtx = rpc_connection.getrawtransaction(txid)
decodedtx = rpc_connection.decoderawtransaction(rawtx)

print(decodedtx)
