"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum
from epilot_message.types import BaseModel, Nullable, OptionalNullable, UNSET, UNSET_SENTINEL
from epilot_message.utils import FieldMetadata, PathParamMetadata, QueryParamMetadata
import pydantic
from pydantic import model_serializer
from typing import List, Optional, TypedDict, Union
from typing_extensions import Annotated, NotRequired


class GetInfoRequestTypedDict(TypedDict):
    thread_id: str
    r"""Thread ID"""
    message_id: NotRequired[str]
    r"""Message ID, If not passed defaults to latest message ID in the thread"""
    

class GetInfoRequest(BaseModel):
    thread_id: Annotated[str, pydantic.Field(alias="threadId"), FieldMetadata(path=PathParamMetadata(style="simple", explode=False))]
    r"""Thread ID"""
    message_id: Annotated[Optional[str], pydantic.Field(alias="messageId"), FieldMetadata(query=QueryParamMetadata(style="form", explode=True))] = None
    r"""Message ID, If not passed defaults to latest message ID in the thread"""
    

class GetInfoGenAIStatus(str, Enum):
    r"""Status of the GenAI job"""
    INITIATED = "INITIATED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class GetInfoGenAIPayloadTypedDict(TypedDict):
    created_at: NotRequired[float]
    r"""Job created date"""
    error: NotRequired[Nullable[str]]
    r"""Error message if the job failed"""
    feedback: NotRequired[Nullable[str]]
    r"""Feedback of the suggested reply"""
    next_steps: NotRequired[Nullable[List[str]]]
    r"""Recommended next steps"""
    progress: NotRequired[float]
    r"""Progress of the GenAI job in percentage"""
    rating: NotRequired[Nullable[str]]
    r"""Rating of the suggested reply"""
    status: NotRequired[GetInfoGenAIStatus]
    r"""Status of the GenAI job"""
    summary: NotRequired[Nullable[List[str]]]
    r"""Generated summary"""
    tags: NotRequired[Nullable[List[str]]]
    r"""Tags"""
    topics: NotRequired[Nullable[List[str]]]
    r"""Topics of the email thread"""
    updated_at: NotRequired[float]
    r"""Job last updated date"""
    

class GetInfoGenAIPayload(BaseModel):
    created_at: Optional[float] = None
    r"""Job created date"""
    error: OptionalNullable[str] = UNSET
    r"""Error message if the job failed"""
    feedback: OptionalNullable[str] = UNSET
    r"""Feedback of the suggested reply"""
    next_steps: OptionalNullable[List[str]] = UNSET
    r"""Recommended next steps"""
    progress: Optional[float] = None
    r"""Progress of the GenAI job in percentage"""
    rating: OptionalNullable[str] = UNSET
    r"""Rating of the suggested reply"""
    status: Optional[GetInfoGenAIStatus] = None
    r"""Status of the GenAI job"""
    summary: OptionalNullable[List[str]] = UNSET
    r"""Generated summary"""
    tags: OptionalNullable[List[str]] = UNSET
    r"""Tags"""
    topics: OptionalNullable[List[str]] = UNSET
    r"""Topics of the email thread"""
    updated_at: Optional[float] = None
    r"""Job last updated date"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["created_at", "error", "feedback", "next_steps", "progress", "rating", "status", "summary", "tags", "topics", "updated_at"]
        nullable_fields = ["error", "feedback", "next_steps", "rating", "summary", "tags", "topics"]
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
        

class GetInfoGenAIType(str, Enum):
    r"""Job type"""
    INFO = "INFO"
    REPLY = "REPLY"

class GetInfoGenAIResponseBodyTypedDict(TypedDict):
    r"""Accepted"""
    
    message_id: NotRequired[str]
    r"""Message ID"""
    org_id: NotRequired[str]
    r"""Organization ID"""
    payload: NotRequired[GetInfoGenAIPayloadTypedDict]
    thread_id: NotRequired[str]
    r"""Thread ID"""
    type: NotRequired[GetInfoGenAIType]
    r"""Job type"""
    

class GetInfoGenAIResponseBody(BaseModel):
    r"""Accepted"""
    
    message_id: Optional[str] = None
    r"""Message ID"""
    org_id: Optional[str] = None
    r"""Organization ID"""
    payload: Optional[GetInfoGenAIPayload] = None
    thread_id: Optional[str] = None
    r"""Thread ID"""
    type: Optional[GetInfoGenAIType] = None
    r"""Job type"""
    

class GetInfoStatus(str, Enum):
    r"""Status of the GenAI job"""
    INITIATED = "INITIATED"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"

class GetInfoPayloadTypedDict(TypedDict):
    created_at: NotRequired[float]
    r"""Job created date"""
    error: NotRequired[Nullable[str]]
    r"""Error message if the job failed"""
    feedback: NotRequired[Nullable[str]]
    r"""Feedback of the suggested reply"""
    next_steps: NotRequired[Nullable[List[str]]]
    r"""Recommended next steps"""
    progress: NotRequired[float]
    r"""Progress of the GenAI job in percentage"""
    rating: NotRequired[Nullable[str]]
    r"""Rating of the suggested reply"""
    status: NotRequired[GetInfoStatus]
    r"""Status of the GenAI job"""
    summary: NotRequired[Nullable[List[str]]]
    r"""Generated summary"""
    tags: NotRequired[Nullable[List[str]]]
    r"""Tags"""
    topics: NotRequired[Nullable[List[str]]]
    r"""Topics of the email thread"""
    updated_at: NotRequired[float]
    r"""Job last updated date"""
    

class GetInfoPayload(BaseModel):
    created_at: Optional[float] = None
    r"""Job created date"""
    error: OptionalNullable[str] = UNSET
    r"""Error message if the job failed"""
    feedback: OptionalNullable[str] = UNSET
    r"""Feedback of the suggested reply"""
    next_steps: OptionalNullable[List[str]] = UNSET
    r"""Recommended next steps"""
    progress: Optional[float] = None
    r"""Progress of the GenAI job in percentage"""
    rating: OptionalNullable[str] = UNSET
    r"""Rating of the suggested reply"""
    status: Optional[GetInfoStatus] = None
    r"""Status of the GenAI job"""
    summary: OptionalNullable[List[str]] = UNSET
    r"""Generated summary"""
    tags: OptionalNullable[List[str]] = UNSET
    r"""Tags"""
    topics: OptionalNullable[List[str]] = UNSET
    r"""Topics of the email thread"""
    updated_at: Optional[float] = None
    r"""Job last updated date"""
    
    @model_serializer(mode="wrap")
    def serialize_model(self, handler):
        optional_fields = ["created_at", "error", "feedback", "next_steps", "progress", "rating", "status", "summary", "tags", "topics", "updated_at"]
        nullable_fields = ["error", "feedback", "next_steps", "rating", "summary", "tags", "topics"]
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
        

class GetInfoType(str, Enum):
    r"""Job type"""
    INFO = "INFO"
    REPLY = "REPLY"

class GetInfoResponseBodyTypedDict(TypedDict):
    r"""Success"""
    
    message_id: NotRequired[str]
    r"""Message ID"""
    org_id: NotRequired[str]
    r"""Organization ID"""
    payload: NotRequired[GetInfoPayloadTypedDict]
    thread_id: NotRequired[str]
    r"""Thread ID"""
    type: NotRequired[GetInfoType]
    r"""Job type"""
    

class GetInfoResponseBody(BaseModel):
    r"""Success"""
    
    message_id: Optional[str] = None
    r"""Message ID"""
    org_id: Optional[str] = None
    r"""Organization ID"""
    payload: Optional[GetInfoPayload] = None
    thread_id: Optional[str] = None
    r"""Thread ID"""
    type: Optional[GetInfoType] = None
    r"""Job type"""
    

GetInfoResponseTypedDict = Union[GetInfoResponseBodyTypedDict, GetInfoGenAIResponseBodyTypedDict]


GetInfoResponse = Union[GetInfoResponseBody, GetInfoGenAIResponseBody]

