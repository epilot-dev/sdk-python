"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .appendvaluemapper import AppendValueMapper, AppendValueMapperTypedDict
from .copyvaluemapper import CopyValueMapper, CopyValueMapperTypedDict
from .setvaluemapper import SetValueMapper, SetValueMapperTypedDict
from typing import Union


MappingAttributeTypedDict = Union[SetValueMapperTypedDict, CopyValueMapperTypedDict, AppendValueMapperTypedDict]


MappingAttribute = Union[SetValueMapper, CopyValueMapper, AppendValueMapper]

