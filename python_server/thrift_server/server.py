# coding=utf-8
from thrift_server.gen.hello.Hello import Processor
from thrift_server.gen.hello.ttypes import *
from thrift.Thrift import TType, TMessageType, TException
from thrift.Thrift import TProcessor
from thrift.transport import TSocket
from thrift.protocol import TBinaryProtocol, TProtocol
from thrift.server import TServer
import logging


class HelloHandler:
    def get(self):
        return "hello world"

def run():
    handler = HelloHandler()
    processor = Processor(handler)
    # 监听端口
    transport = TSocket.TServerSocket('localhost', 9234)
    # 选择传输层
    tfactory = TTransport.TBufferedTransportFactory()
    # 选择传输协议
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()
    # 创建服务端
    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    server.setNumThreads(5)
    logging.info('start thrift serve in python')
    server.serve()


if __name__ == '__main__':
    run()
