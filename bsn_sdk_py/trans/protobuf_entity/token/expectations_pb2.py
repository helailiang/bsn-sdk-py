# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: token/expectations.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from bsn_sdk_py.trans.protobuf_entity.token import transaction_pb2 as token_dot_transaction__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='token/expectations.proto',
  package='protos',
  syntax='proto3',
  serialized_options=b'\n#org.hyperledger.fabric.protos.tokenZ*github.com/hyperledger/fabric/protos/token',
  serialized_pb=b'\n\x18token/expectations.proto\x12\x06protos\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17token/transaction.proto\"X\n\x10TokenExpectation\x12\x35\n\x11plain_expectation\x18\x01 \x01(\x0b\x32\x18.protos.PlainExpectationH\x00\x42\r\n\x0b\x45xpectation\"\x99\x01\n\x10PlainExpectation\x12;\n\x12import_expectation\x18\x01 \x01(\x0b\x32\x1d.protos.PlainTokenExpectationH\x00\x12=\n\x14transfer_expectation\x18\x02 \x01(\x0b\x32\x1d.protos.PlainTokenExpectationH\x00\x42\t\n\x07payload\"6\n\x15PlainTokenExpectation\x12\x1d\n\x07outputs\x18\x01 \x03(\x0b\x32\x0c.PlainOutputBQ\n#org.hyperledger.fabric.protos.tokenZ*github.com/hyperledger/fabric/protos/tokenb\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,token_dot_transaction__pb2.DESCRIPTOR,])




_TOKENEXPECTATION = _descriptor.Descriptor(
  name='TokenExpectation',
  full_name='protos.TokenExpectation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='plain_expectation', full_name='protos.TokenExpectation.plain_expectation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='Expectation', full_name='protos.TokenExpectation.Expectation',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=94,
  serialized_end=182,
)


_PLAINEXPECTATION = _descriptor.Descriptor(
  name='PlainExpectation',
  full_name='protos.PlainExpectation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='import_expectation', full_name='protos.PlainExpectation.import_expectation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='transfer_expectation', full_name='protos.PlainExpectation.transfer_expectation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='payload', full_name='protos.PlainExpectation.payload',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=185,
  serialized_end=338,
)


_PLAINTOKENEXPECTATION = _descriptor.Descriptor(
  name='PlainTokenExpectation',
  full_name='protos.PlainTokenExpectation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='outputs', full_name='protos.PlainTokenExpectation.outputs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=340,
  serialized_end=394,
)

_TOKENEXPECTATION.fields_by_name['plain_expectation'].message_type = _PLAINEXPECTATION
_TOKENEXPECTATION.oneofs_by_name['Expectation'].fields.append(
  _TOKENEXPECTATION.fields_by_name['plain_expectation'])
_TOKENEXPECTATION.fields_by_name['plain_expectation'].containing_oneof = _TOKENEXPECTATION.oneofs_by_name['Expectation']
_PLAINEXPECTATION.fields_by_name['import_expectation'].message_type = _PLAINTOKENEXPECTATION
_PLAINEXPECTATION.fields_by_name['transfer_expectation'].message_type = _PLAINTOKENEXPECTATION
_PLAINEXPECTATION.oneofs_by_name['payload'].fields.append(
  _PLAINEXPECTATION.fields_by_name['import_expectation'])
_PLAINEXPECTATION.fields_by_name['import_expectation'].containing_oneof = _PLAINEXPECTATION.oneofs_by_name['payload']
_PLAINEXPECTATION.oneofs_by_name['payload'].fields.append(
  _PLAINEXPECTATION.fields_by_name['transfer_expectation'])
_PLAINEXPECTATION.fields_by_name['transfer_expectation'].containing_oneof = _PLAINEXPECTATION.oneofs_by_name['payload']
_PLAINTOKENEXPECTATION.fields_by_name['outputs'].message_type = token_dot_transaction__pb2._PLAINOUTPUT
DESCRIPTOR.message_types_by_name['TokenExpectation'] = _TOKENEXPECTATION
DESCRIPTOR.message_types_by_name['PlainExpectation'] = _PLAINEXPECTATION
DESCRIPTOR.message_types_by_name['PlainTokenExpectation'] = _PLAINTOKENEXPECTATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TokenExpectation = _reflection.GeneratedProtocolMessageType('TokenExpectation', (_message.Message,), {
  'DESCRIPTOR' : _TOKENEXPECTATION,
  '__module__' : 'token.expectations_pb2'
  # @@protoc_insertion_point(class_scope:protos.TokenExpectation)
  })
_sym_db.RegisterMessage(TokenExpectation)

PlainExpectation = _reflection.GeneratedProtocolMessageType('PlainExpectation', (_message.Message,), {
  'DESCRIPTOR' : _PLAINEXPECTATION,
  '__module__' : 'token.expectations_pb2'
  # @@protoc_insertion_point(class_scope:protos.PlainExpectation)
  })
_sym_db.RegisterMessage(PlainExpectation)

PlainTokenExpectation = _reflection.GeneratedProtocolMessageType('PlainTokenExpectation', (_message.Message,), {
  'DESCRIPTOR' : _PLAINTOKENEXPECTATION,
  '__module__' : 'token.expectations_pb2'
  # @@protoc_insertion_point(class_scope:protos.PlainTokenExpectation)
  })
_sym_db.RegisterMessage(PlainTokenExpectation)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
