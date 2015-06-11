#!/usr/bin/env python


import sys
sys.path.append('gen-py')

from printer import PrinterService
from printer.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


transport = TSocket.TSocket('localhost',9090)
transport = TTransport.TBufferedTransport(transport)
protocol  = TBinaryProtocol.TBinaryProtocol(transport)

client = PrinterService.Client(protocol)


transport.open()

boolReturn = client.printBool(True)
print boolReturn

mapValue = {1:"b",2:"d"}
mapReturn = client.printMap(mapValue)
print mapReturn

boxValue = Box(100,65.5,'magic box',Usage.PACK)
boxReturn = client.printBox(boxValue)
print boxReturn

client.verbose("run!")

transport.close()
