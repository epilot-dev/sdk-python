"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .entityrelation import EntityRelation
from .opportunitysource import OpportunitySource
from .orderrelation import OrderRelation
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Dict, List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OpportunitySchemas1:
    entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_id'), 'exclude': lambda f: f is None }})
    r"""The id of the referenced entity"""
    path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path'), 'exclude': lambda f: f is None }})
    r"""The path to the target attribute being referenced"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OpportunityAddress:
    r"""A list of additional addresses"""
    dollar_relation_ref: Optional[List[DollarRelationRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$relation_ref'), 'exclude': lambda f: f is None }})
    r"""The relation from which a field is being referenced"""
    



@dataclasses.dataclass
class EmailNotificationSettings:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Assignee:
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'exclude': lambda f: f is None }})
    department: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('department'), 'exclude': lambda f: f is None }})
    display_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('display_name'), 'exclude': lambda f: f is None }})
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    email_notification_settings: Optional[EmailNotificationSettings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_notification_settings'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    image_uri: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('image_uri'), 'exclude': lambda f: f is None }})
    is_signature_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_signature_enabled'), 'exclude': lambda f: f is None }})
    organization_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization_id'), 'exclude': lambda f: f is None }})
    phone: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('phone'), 'exclude': lambda f: f is None }})
    preferred_language: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('preferred_language'), 'exclude': lambda f: f is None }})
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    token: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('token'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OpportunitySchemasBillingAddress1:
    entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_id'), 'exclude': lambda f: f is None }})
    r"""The id of the referenced entity"""
    path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path'), 'exclude': lambda f: f is None }})
    r"""The path to the target attribute being referenced"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BillingAddress:
    r"""The billing address"""
    dollar_relation_ref: Optional[List[OpportunityDollarRelationRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$relation_ref'), 'exclude': lambda f: f is None }})
    r"""The relation from which a field is being referenced"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OpportunityCustomer:
    r"""A list of customers related with the opportunity"""
    dollar_relation: Optional[List[EntityRelation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$relation'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Opportunity1:
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})
    r"""The date tags"""
    value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('value'), 'exclude': lambda f: f is None }})
    r"""The date value"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OpportunitySchemasDeliveryAddress1:
    entity_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_id'), 'exclude': lambda f: f is None }})
    r"""The id of the referenced entity"""
    path: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('path'), 'exclude': lambda f: f is None }})
    r"""The path to the target attribute being referenced"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeliveryAddress:
    r"""The delivery address"""
    dollar_relation_ref: Optional[List[OpportunitySchemasDollarRelationRef]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$relation_ref'), 'exclude': lambda f: f is None }})
    r"""The relation from which a field is being referenced"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Items:
    r"""The order relations items, representing quotes or orders associated with the opportunity"""
    dollar_relation: Optional[List[OrderRelation]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('$relation'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Opportunity:
    r"""The opportunity entity"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_created_at'), 'exclude': lambda f: f is None }})
    r"""The opportunity creation date"""
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_id'), 'exclude': lambda f: f is None }})
    r"""The opportunity id"""
    org_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_org_id'), 'exclude': lambda f: f is None }})
    r"""Organization Id the order belongs to"""
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})
    r"""An arbitrary set of tags attached to the opportunity"""
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_updated_at'), 'exclude': lambda f: f is None }})
    r"""The opportunity last update date"""
    address: Optional[OpportunityAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    r"""A list of additional addresses"""
    assignee: Optional[List[Assignee]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignee'), 'exclude': lambda f: f is None }})
    r"""The opportunity assignees"""
    billing_address: Optional[BillingAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    r"""The billing address"""
    customer: Optional[OpportunityCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer'), 'exclude': lambda f: f is None }})
    r"""A list of customers related with the opportunity"""
    dates: Optional[List[Dates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dates'), 'exclude': lambda f: f is None }})
    r"""A set of dates associated with the opportunity"""
    delivery_address: Optional[DeliveryAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delivery_address'), 'exclude': lambda f: f is None }})
    r"""The delivery address"""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""A description to frame this opportunity within its sales process"""
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_date'), 'exclude': lambda f: f is None }})
    r"""The expiration date"""
    items: Optional[Items] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    r"""The order relations items, representing quotes or orders associated with the opportunity"""
    opportunity_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('opportunity_number'), 'exclude': lambda f: f is None }})
    r"""The opportunity id number for the customer (autogenerated if left blank)"""
    opportunity_title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('opportunity_title'), 'exclude': lambda f: f is None }})
    r"""The opportunity title for the opportunity"""
    source: Optional[OpportunitySource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    r"""The opportunity generation source"""
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_id'), 'exclude': lambda f: f is None }})
    r"""Identifier for source e.g. journey ID"""
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_type'), 'exclude': lambda f: f is None }})
    r"""Type of source, e.g. journey or manual"""
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The opportunity status (defined by the opportunity workflow)"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OpportunityInput:
    r"""The opportunity entity"""
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    org_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_org_id'), 'exclude': lambda f: f is None }})
    r"""Organization Id the order belongs to"""
    tags: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_tags'), 'exclude': lambda f: f is None }})
    r"""An arbitrary set of tags attached to the opportunity"""
    address: Optional[OpportunityAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('address'), 'exclude': lambda f: f is None }})
    r"""A list of additional addresses"""
    assignee: Optional[List[Assignee]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignee'), 'exclude': lambda f: f is None }})
    r"""The opportunity assignees"""
    billing_address: Optional[BillingAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('billing_address'), 'exclude': lambda f: f is None }})
    r"""The billing address"""
    customer: Optional[OpportunityCustomer] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customer'), 'exclude': lambda f: f is None }})
    r"""A list of customers related with the opportunity"""
    dates: Optional[List[Dates]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dates'), 'exclude': lambda f: f is None }})
    r"""A set of dates associated with the opportunity"""
    delivery_address: Optional[DeliveryAddress] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delivery_address'), 'exclude': lambda f: f is None }})
    r"""The delivery address"""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""A description to frame this opportunity within its sales process"""
    due_date: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_date'), 'exclude': lambda f: f is None }})
    r"""The expiration date"""
    items: Optional[Items] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    r"""The order relations items, representing quotes or orders associated with the opportunity"""
    opportunity_number: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('opportunity_number'), 'exclude': lambda f: f is None }})
    r"""The opportunity id number for the customer (autogenerated if left blank)"""
    opportunity_title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('opportunity_title'), 'exclude': lambda f: f is None }})
    r"""The opportunity title for the opportunity"""
    source: Optional[OpportunitySource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    r"""The opportunity generation source"""
    source_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_id'), 'exclude': lambda f: f is None }})
    r"""Identifier for source e.g. journey ID"""
    source_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source_type'), 'exclude': lambda f: f is None }})
    r"""Type of source, e.g. journey or manual"""
    status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The opportunity status (defined by the opportunity workflow)"""
    


DollarRelationRef = Union[OpportunitySchemas1]

OpportunityDollarRelationRef = Union[OpportunitySchemasBillingAddress1]

Dates = Union[Opportunity1]

OpportunitySchemasDollarRelationRef = Union[OpportunitySchemasDeliveryAddress1]
