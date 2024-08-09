"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .erroroutput import ErrorOutput, ErrorOutputTypedDict
from .executionstatus import ExecutionStatus
from .mapentityconfig import MapEntityConfig, MapEntityConfigTypedDict
from .retrystrategy import RetryStrategy
from enum import Enum
from epilot_automation.types import BaseModel
from typing import Any, Dict, Optional, TypedDict
from typing_extensions import NotRequired


class MapEntityActionReasonTypedDict(TypedDict):
    message: NotRequired[str]
    r"""Why the action has to be skipped/failed"""
    payload: NotRequired[Dict[str, Any]]
    r"""Extra metadata about the skipping reason - such as a certain condition not met, etc."""
    

class MapEntityActionReason(BaseModel):
    message: Optional[str] = None
    r"""Why the action has to be skipped/failed"""
    payload: Optional[Dict[str, Any]] = None
    r"""Extra metadata about the skipping reason - such as a certain condition not met, etc."""
    

class MapEntityActionType(str, Enum):
    MAP_ENTITY = "map-entity"

class MapEntityActionTypedDict(TypedDict):
    allow_failure: NotRequired[bool]
    r"""Whether to stop execution in a failed state if this action fails"""
    condition_id: NotRequired[str]
    r"""Condition Id to be checked before executing the action"""
    config: NotRequired[MapEntityConfigTypedDict]
    created_automatically: NotRequired[bool]
    r"""Flag indicating whether the action was created automatically or manually"""
    error_output: NotRequired[ErrorOutputTypedDict]
    execution_status: NotRequired[ExecutionStatus]
    flow_action_id: NotRequired[str]
    id: NotRequired[str]
    is_bulk_action: NotRequired[bool]
    r"""Flag indicating whether the same action can be in bulk in a single execution. e.g; send-email / map-entity"""
    name: NotRequired[str]
    outputs: NotRequired[Dict[str, Any]]
    reason: NotRequired[MapEntityActionReasonTypedDict]
    retry_strategy: NotRequired[RetryStrategy]
    r"""different behaviors for retrying failed execution actions."""
    started_at: NotRequired[str]
    type: NotRequired[MapEntityActionType]
    updated_at: NotRequired[str]
    

class MapEntityAction(BaseModel):
    allow_failure: Optional[bool] = None
    r"""Whether to stop execution in a failed state if this action fails"""
    condition_id: Optional[str] = None
    r"""Condition Id to be checked before executing the action"""
    config: Optional[MapEntityConfig] = None
    created_automatically: Optional[bool] = None
    r"""Flag indicating whether the action was created automatically or manually"""
    error_output: Optional[ErrorOutput] = None
    execution_status: Optional[ExecutionStatus] = None
    flow_action_id: Optional[str] = None
    id: Optional[str] = None
    is_bulk_action: Optional[bool] = None
    r"""Flag indicating whether the same action can be in bulk in a single execution. e.g; send-email / map-entity"""
    name: Optional[str] = None
    outputs: Optional[Dict[str, Any]] = None
    reason: Optional[MapEntityActionReason] = None
    retry_strategy: Optional[RetryStrategy] = None
    r"""different behaviors for retrying failed execution actions."""
    started_at: Optional[str] = None
    type: Optional[MapEntityActionType] = None
    updated_at: Optional[str] = None
    
