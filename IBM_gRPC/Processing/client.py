from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import atexit
import logging
import multiprocessing
import sys
import time
# import the generated classes
import IBM_pb2
import IBM_pb2_grpc
import grpc
import aerospike

PROCESS_COUNT = multiprocessing.cpu_count()
MAXIMUM_RUNS = 10000

Channel = None
Stub = None
ctr = 0
# LOGGER = logging.getLogger(__name__)

# Configure the client
config = {
  'hosts': [ ('127.0.0.1', 3000) ]
}

# Create a client and connect it to the cluster
try:
  client = aerospike.client(config).connect()
except:
  import sys
  print("failed to connect to the cluster with", config['hosts'])
  sys.exit(1)

def shutdown_worker():
    # LOGGER.info('Shutting worker process down.')
    if Channel is not None:
        Channel.stop()

def initialize_worker(server_address):
    global Channel
    global Stub
    #LOGGER.info('Initializing worker process.')
    Channel = grpc.insecure_channel(server_address)
    Stub = IBM_pb2_grpc.PredictorStub(Channel)
    atexit.register(shutdown_worker)

def run_worker_query(x):
    global ctr
    ctr = ctr + 1
    #print(ctr)
    request = IBM_pb2.Request(Item_no = 15,Store_no = 11,Transactions = 12,Oil_Prices = 81,Holiday = True,Offer = False)
    response = Stub.Process(request = request)
    response = response.SerializeToString()
    return response

def start_servers(server_address):
    worker_pool = multiprocessing.Pool(processes=PROCESS_COUNT,initializer=initialize_worker,initargs=(server_address,))
    runs = range(2, MAXIMUM_RUNS)
    primality = worker_pool.map(run_worker_query, runs)
    return primality

def main():
    msg = ''
    parser = argparse.ArgumentParser(description=msg)
    parser.add_argument('server_address')
    args = parser.parse_args()
    response_list = start_servers(args.server_address)
    #print(response_list)

if __name__ == '__main__':
    start = time.time()
    # handler = logging.StreamHandler(sys.stdout)
    # formatter = logging.Formatter('[PID %(process)d] %(message)s')
    # handler.setFormatter(formatter)
    # LOGGER.addHandler(handler)
    # LOGGER.setLevel(logging.INFO)
    main()
    print("No. of requests made = ",MAXIMUM_RUNS)
    print(time.time() - start)
