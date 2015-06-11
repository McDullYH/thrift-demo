#!/usr/bin/env python



import sys
sys.path.append('gen-py')

import logging
logging.basicConfig()

from printer import PrinterService
from printer.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer



class PrinterServiceHanlder:
    def __init__(self):
        print "created!"

    def printBool(self,boolValue):
        print boolValue
        return not boolValue

    def printMap(self,mapValue):
        print mapValue
        mapValue[3]='f'
        return mapValue

    def printBox(self,boxValue):
        print boxValue
        boxValue.id=200
        return boxValue

    def verbose(self,cmd):
        print cmd




hanlder = PrinterServiceHanlder()

processor = PrinterService.Processor(hanlder)

socket=TSocket.TServerSocket(host='localhost',port=9090)

tFactory = TTransport.TBufferedTransportFactory()
pFactory = TBinaryProtocol.TBinaryProtocolFactory()

server=TServer.TSimpleServer(processor,socket,tFactory,pFactory)

server.serve()

