from thrift_server.gen.ad.audcache.CacheRefreshServer import *
from thrift_server.gen.ad.audcache.ttypes import CacheRefreshNotifyReq
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:
    transport = TSocket.TSocket('10.17.19.15', 7980)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = Client(protocol)
    transport.open()

    print 'start'
    cacheRefreshNotifyReq = CacheRefreshNotifyReq(uniq_id="1")
    ret = client.cache_refresh_notify(cacheRefreshNotifyReq)
    print ret
    transport.close()
except Thrift.TException as e:
    print 'exception'
    print e
