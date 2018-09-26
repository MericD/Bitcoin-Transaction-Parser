#Parameters that must be set before executing
#blockchain.db --> created database file 
# blocks that are analyzed from range start_block to end_block
# needed loggin parameters rpc_user and rpc_password befor running rpc 
# IP and port for rpc rpc_ip and rpc_port

CONFIG = {
    'database_file_name': 'blockchain.db',
    'start_block': 130001,
    'end_block':15000,
    'rpc_user':'rpc',
    'rpc_password':'bitmaster',
    'rpc_ip':'127.0.0.1',
    'rpc_port':'8332'
}



