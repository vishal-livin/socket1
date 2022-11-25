python -m thrift_compiler.main --gen py calculator.thrift

thrift -gen py calculator.thrift

import sys

sys.path.append('gen-py')

from calculator import Calculator

from thrift import Thrift

from thrift.transport import TSocket

from thrift.transport import TTransport

from thrift.protocol import TCompactProtocol


# Make socket

transport = TSocket.TSocket('localhost', 8081)

transport = TTransport.TBufferedTransport(transport)

# Wrap in a protocol

protocol = TCompactProtocol.TCompactProtocol(transport)

# Create a client to use the protocol encoder

client = Calculator.Client(protocol)

# Connect!

transport.open()

result = client.add(18, 24)

print("add result: {}".format(result))

result = client.multiply(18, 24)

print("multiply result: {}".format(result))

# Close

