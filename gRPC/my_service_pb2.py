# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: my_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10my_service.proto\x12\nmy_service\"!\n\x0e\x43ommandRequest\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\")\n\x0f\x43ommandResponse\x12\x16\n\x0e\x63ommand_output\x18\x01 \x01(\t2P\n\tMyService\x12\x43\n\x07\x43ommand\x12\x1a.my_service.CommandRequest\x1a\x1a.my_service.CommandRequest\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'my_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _COMMANDREQUEST._serialized_start=32
  _COMMANDREQUEST._serialized_end=65
  _COMMANDRESPONSE._serialized_start=67
  _COMMANDRESPONSE._serialized_end=108
  _MYSERVICE._serialized_start=110
  _MYSERVICE._serialized_end=190
# @@protoc_insertion_point(module_scope)
