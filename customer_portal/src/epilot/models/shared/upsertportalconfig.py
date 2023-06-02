"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import emailtemplates as shared_emailtemplates
from ..shared import entityslug as shared_entityslug
from ..shared import grant as shared_grant
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpsertPortalConfigCognitoDetails:
    r"""AWS Cognito Pool details for the portal"""
    
    cognito_user_pool_arn: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cognito_user_pool_arn'), 'exclude': lambda f: f is None }})
    r"""Cognito user pool ARN"""
    cognito_user_pool_client_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cognito_user_pool_client_id'), 'exclude': lambda f: f is None }})
    r"""Cognito user pool client ID"""
    cognito_user_pool_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cognito_user_pool_id'), 'exclude': lambda f: f is None }})
    r"""Cognito user pool ID"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpsertPortalConfigDefaultUserToNotify:
    r"""Default 360 user to notify upon an internal notification"""
    
    on_pending_user: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('onPendingUser'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpsertPortalConfigEntityActionsActionLabel:
    
    de: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('de'), 'exclude': lambda f: f is None }})
    en: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('en'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpsertPortalConfigEntityActions:
    
    action_label: Optional[UpsertPortalConfigEntityActionsActionLabel] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('action_Label'), 'exclude': lambda f: f is None }})
    journey_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('journey_id'), 'exclude': lambda f: f is None }})
    slug: Optional[shared_entityslug.EntitySlug] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug'), 'exclude': lambda f: f is None }})
    r"""URL-friendly identifier for the entity schema"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpsertPortalConfigEntityIdentifiersType:
    
    attributes: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes'), 'exclude': lambda f: f is None }})
    r"""Attributes used to identify an entity"""
    is_enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('isEnabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable the entity identifier"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpsertPortalConfigEntityIdentifiers:
    r"""Identifiers used to identify an entity by a portal user"""
    
    type: Optional[UpsertPortalConfigEntityIdentifiersType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpsertPortalConfigImages:
    r"""Teaser & Banner Image web links"""
    
    order_left_teaser: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orderLeftTeaser'), 'exclude': lambda f: f is None }})
    r"""URL of the order left teaser image"""
    order_right_teaser: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('orderRightTeaser'), 'exclude': lambda f: f is None }})
    r"""URL of the order right teaser image"""
    welcome_banner: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('welcomeBanner'), 'exclude': lambda f: f is None }})
    r"""URL of the welcome banner image"""
    

@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UpsertPortalConfig:
    r"""Portal payload"""
    
    design_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('design_id') }})
    r"""ID of the design used to build the portal"""
    cognito_details: Optional[UpsertPortalConfigCognitoDetails] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('cognito_details'), 'exclude': lambda f: f is None }})
    r"""AWS Cognito Pool details for the portal"""
    config: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('config'), 'exclude': lambda f: f is None }})
    r"""Stringified object with configuration details"""
    contact_secondary_identifier: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contact_secondary_identifier'), 'exclude': lambda f: f is None }})
    r"""Secondary identifier to identify a contact other than the email"""
    default_user_to_notify: Optional[UpsertPortalConfigDefaultUserToNotify] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_user_to_notify'), 'exclude': lambda f: f is None }})
    r"""Default 360 user to notify upon an internal notification"""
    domain: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('domain'), 'exclude': lambda f: f is None }})
    r"""The URL on which the portal is accessible"""
    email_templates: Optional[shared_emailtemplates.EmailTemplates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email_templates'), 'exclude': lambda f: f is None }})
    r"""Email templates used for authentication and internal processes"""
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable the portal access"""
    entity_actions: Optional[list[UpsertPortalConfigEntityActions]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_actions'), 'exclude': lambda f: f is None }})
    r"""Journey actions allowed on an entity by a portal user"""
    entity_identifiers: Optional[UpsertPortalConfigEntityIdentifiers] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_identifiers'), 'exclude': lambda f: f is None }})
    r"""Identifiers used to identify an entity by a portal user"""
    grants: Optional[list[shared_grant.Grant]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grants'), 'exclude': lambda f: f is None }})
    r"""Permissions granted to a portal user while accessing entities"""
    images: Optional[UpsertPortalConfigImages] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('images'), 'exclude': lambda f: f is None }})
    r"""Teaser & Banner Image web links"""
    is_epilot_domain: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_epilot_domain'), 'exclude': lambda f: f is None }})
    r"""Mark true if the domain is an Epilot domain"""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""A short name to identify your portal"""
    self_registration: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('self_registration'), 'exclude': lambda f: f is None }})
    r"""Allow portal user self-registration without a mapped contact"""
    