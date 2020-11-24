from __future__ import print_function
import logging
import sys

import grpc

import hellonerd_pb2
import hellonerd_pb2_grpc


def run():
    try:
        uname = sys.argv[1]
        server = sys.argv[2]
        port = sys.argv[3]
        detonate = sys.argv [4]
    except:
        detonate = "no"
        print('usage: python client.py username ip  port  --normal/--detonate ')
        sys.exit(0)
       

    with grpc.insecure_channel(server+':'+port) as channel:
        stub = hellonerd_pb2_grpc.HelloNerdStub(channel)
        if (detonate == '--detonate'):
            while True:
                response = stub.SayHello(hellonerd_pb2.HelloRequest(name=uname))
                print ("Server Says : " + response.message)
        response = stub.SayHello(hellonerd_pb2.HelloRequest(name=uname))
        print("Server Says: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
