from concurrent import futures
import logging

import grpc

import hellonerd_pb2
import hellonerd_pb2_grpc
import random
import re


class HelloNerd(hellonerd_pb2_grpc.HelloNerd):

    def SayHello(self, request, context):
        uname = str (request.name)
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:=]')
        if(regex.search(uname) == None):
            print ('Responding to ' + uname)
            messages = ['Where is my coffee?', 'Hello!', 'Hey, Whats up?', 'Is this legal?', 'Don\'t drink and root', 'I want to go to a mall' ]
            msg = uname +', ' + messages[random.randint(0,4)]
            return hellonerd_pb2.HelloReply(message= msg ) 
        else:
            return hellonerd_pb2.HelloReply(message = 'I see you dont follow by rules')
         
            


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hellonerd_pb2_grpc.add_HelloNerdServicer_to_server(HelloNerd(), server)
    server.add_insecure_port('[::]:50055')
    server.start()
    server.wait_for_termination()
   


if __name__ == '__main__':
    logging.basicConfig()
    serve()
    print('Server is ready to receive request !!')
