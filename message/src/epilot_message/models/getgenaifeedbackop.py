"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from epilot_message.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from epilot_message.utils import FieldMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict
from typing_extensions import Annotated, NotRequired


class GetGenAIFeedbackRequestTypedDict(TypedDict):
    from_: NotRequired[float]
    size: NotRequired[float]
    r"""Number of feedback to return"""
    

class GetGenAIFeedbackRequest(BaseModel):
    from_: Annotated[Optional[float], pydantic.Field(alias="from"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 0
    size: Annotated[Optional[float], FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = 10
    r"""Number of feedback to return"""
    

class GetGenAIFeedbackType(str, Enum):
    r"""Job type"""
    INFO = "INFO"
    REPLY = "REPLY"

class GetGenAIFeedbackResultsTypedDict(TypedDict):
    created_at: NotRequired[datetime]
    r"""Created date"""
    feedback: NotRequired[Nullable[str]]
    r"""Feedback of the suggested reply"""
    last_updated_at: NotRequired[datetime]
    r"""Updated date"""
    message_id: NotRequired[str]
    r"""Message ID"""
    org_id: NotRequired[str]
    r"""Organization ID"""
    org_name: NotRequired[str]
    r"""Name of the org"""
    rating: NotRequired[Nullable[str]]
    r"""Rating of the suggested reply"""
    thread_id: NotRequired[str]
    r"""Thread ID"""
    type: NotRequired[GetGenAIFeedbackType]
    r"""Job type"""
    

class GetGenAIFeedbackResults(BaseModel):
    created_at: Optional[datetime] = None
    r"""Created date"""
    feedback: OptionalNullable[str] = UNSET
    r"""Feedback of the suggested reply"""
    last_updated_at: Optional[datetime] = None
    r"""Updated date"""
    message_id: Optional[str] = None
    r"""Message ID"""
    org_id: Optional[str] = None
    r"""Organization ID"""
    org_name: Optional[str] = None
    r"""Name of the org"""
    rating: OptionalNullable[str] = UNSET
    r"""Rating of the suggested reply"""
    thread_id: Optional[str] = None
    r"""Thread ID"""
    type: Optional[GetGenAIFeedbackType] = None
    r"""Job type"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["created_at", "feedback", "last_updated_at", "message_id", "org_id", "org_name", "rating", "thread_id", "type"]
        nullable_fields = ["feedback", "rating"]
        null_default_fields = []

        serialized = handler(self)

        m = {}

        for n, f in self.model_fields.items():
            k = f.alias or n
            val = serialized.get(k)

            optional_nullable = k in optional_fields and k in nullable_fields
            is_set = (self.__pydantic_fields_set__.intersection({n}) or k in null_default_fields) # pylint: disable=no-member

            if val is not None and val != UNSET_SENTINEL:
                m[k] = val
            elif val != UNSET_SENTINEL and (
                not k in optional_fields or (optional_nullable and is_set)
            ):
                m[k] = val

        return m
        

class GetGenAIFeedbackResponseBodyTypedDict(TypedDict):
    r"""Success"""
    
    hits: NotRequired[float]
    r"""Total hits"""
    results: NotRequired[List[GetGenAIFeedbackResultsTypedDict]]
    

class GetGenAIFeedbackResponseBody(BaseModel):
    r"""Success"""
    
    hits: Optional[float] = None
    r"""Total hits"""
    results: Optional[List[GetGenAIFeedbackResults]] = None
    
