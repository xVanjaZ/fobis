from server import server
from ndov.connector import connect

import threading


ndov_thread = threading.Thread(target=connect)
ndov_thread.start()

server_thread = threading.Thread(target=server)
server_thread.start()

