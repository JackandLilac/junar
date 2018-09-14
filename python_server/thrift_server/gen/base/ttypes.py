#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class TrafficEnv:
  """
  Attributes:
   - Open
   - Env
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'Open', None, False, ), # 1
    (2, TType.STRING, 'Env', None, "", ), # 2
  )

  def __init__(self, Open=thrift_spec[1][4], Env=thrift_spec[2][4],):
    self.Open = Open
    self.Env = Env

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.Open = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.Env = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TrafficEnv')
    if self.Open is not None:
      oprot.writeFieldBegin('Open', TType.BOOL, 1)
      oprot.writeBool(self.Open)
      oprot.writeFieldEnd()
    if self.Env is not None:
      oprot.writeFieldBegin('Env', TType.STRING, 2)
      oprot.writeString(self.Env)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.Open)
    value = (value * 31) ^ hash(self.Env)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class Base:
  """
  Attributes:
   - LogID
   - Caller
   - Addr
   - client
   - trafficEnv
   - extra
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'LogID', None, "", ), # 1
    (2, TType.STRING, 'Caller', None, "", ), # 2
    (3, TType.STRING, 'Addr', None, "", ), # 3
    (4, TType.STRING, 'client', None, "", ), # 4
    (5, TType.STRUCT, 'trafficEnv', (TrafficEnv, TrafficEnv.thrift_spec), None, ), # 5
    (6, TType.MAP, 'extra', (TType.STRING,None,TType.STRING,None), None, ), # 6
  )

  def __init__(self, LogID=thrift_spec[1][4], Caller=thrift_spec[2][4], Addr=thrift_spec[3][4], client=thrift_spec[4][4], trafficEnv=None, extra=None,):
    self.LogID = LogID
    self.Caller = Caller
    self.Addr = Addr
    self.client = client
    self.trafficEnv = trafficEnv
    self.extra = extra

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.LogID = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.Caller = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.Addr = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.client = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRUCT:
          self.trafficEnv = TrafficEnv()
          self.trafficEnv.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.MAP:
          self.extra = {}
          (_ktype1, _vtype2, _size0 ) = iprot.readMapBegin()
          for _i4 in xrange(_size0):
            _key5 = iprot.readString();
            _val6 = iprot.readString();
            self.extra[_key5] = _val6
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('Base')
    if self.LogID is not None:
      oprot.writeFieldBegin('LogID', TType.STRING, 1)
      oprot.writeString(self.LogID)
      oprot.writeFieldEnd()
    if self.Caller is not None:
      oprot.writeFieldBegin('Caller', TType.STRING, 2)
      oprot.writeString(self.Caller)
      oprot.writeFieldEnd()
    if self.Addr is not None:
      oprot.writeFieldBegin('Addr', TType.STRING, 3)
      oprot.writeString(self.Addr)
      oprot.writeFieldEnd()
    if self.client is not None:
      oprot.writeFieldBegin('client', TType.STRING, 4)
      oprot.writeString(self.client)
      oprot.writeFieldEnd()
    if self.trafficEnv is not None:
      oprot.writeFieldBegin('trafficEnv', TType.STRUCT, 5)
      self.trafficEnv.write(oprot)
      oprot.writeFieldEnd()
    if self.extra is not None:
      oprot.writeFieldBegin('extra', TType.MAP, 6)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.extra))
      for kiter7,viter8 in self.extra.items():
        oprot.writeString(kiter7)
        oprot.writeString(viter8)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.LogID)
    value = (value * 31) ^ hash(self.Caller)
    value = (value * 31) ^ hash(self.Addr)
    value = (value * 31) ^ hash(self.client)
    value = (value * 31) ^ hash(self.trafficEnv)
    value = (value * 31) ^ hash(self.extra)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class BaseResp:
  """
  Attributes:
   - StatusMessage
   - StatusCode
   - Extra
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'StatusMessage', None, "", ), # 1
    (2, TType.I32, 'StatusCode', None, 0, ), # 2
    (3, TType.MAP, 'Extra', (TType.STRING,None,TType.STRING,None), None, ), # 3
  )

  def __init__(self, StatusMessage=thrift_spec[1][4], StatusCode=thrift_spec[2][4], Extra=None,):
    self.StatusMessage = StatusMessage
    self.StatusCode = StatusCode
    self.Extra = Extra

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.StatusMessage = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.StatusCode = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.MAP:
          self.Extra = {}
          (_ktype10, _vtype11, _size9 ) = iprot.readMapBegin()
          for _i13 in xrange(_size9):
            _key14 = iprot.readString();
            _val15 = iprot.readString();
            self.Extra[_key14] = _val15
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('BaseResp')
    if self.StatusMessage is not None:
      oprot.writeFieldBegin('StatusMessage', TType.STRING, 1)
      oprot.writeString(self.StatusMessage)
      oprot.writeFieldEnd()
    if self.StatusCode is not None:
      oprot.writeFieldBegin('StatusCode', TType.I32, 2)
      oprot.writeI32(self.StatusCode)
      oprot.writeFieldEnd()
    if self.Extra is not None:
      oprot.writeFieldBegin('Extra', TType.MAP, 3)
      oprot.writeMapBegin(TType.STRING, TType.STRING, len(self.Extra))
      for kiter16,viter17 in self.Extra.items():
        oprot.writeString(kiter16)
        oprot.writeString(viter17)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.StatusMessage)
    value = (value * 31) ^ hash(self.StatusCode)
    value = (value * 31) ^ hash(self.Extra)
    return value

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)