"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AutomationEntityMapping:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable automation entity mapping"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class AutomationPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable automation preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CentralInboxPreviewSetting:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable central inbox preview setting"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ContractsPreviewSetting:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable contracts preview setting"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DisableIvy:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable Ivy"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DoubleOptIn:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable double opt-in"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EcommerceCatalogPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable ecommerce catalog preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EcommerceOpportunitiesPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable ecommerce opportunities preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EcommercePreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable ecommerce preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EndCustomerPortal:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable end customer portal"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntitySchemaBuilder:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable entity schema builder"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InstallerPortal:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable installer portal"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LogicEditorPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable logic editor preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class NewNavigation:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable new navigation"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Partnering:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable partnering"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ProductAvailability:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable product availability"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Sso:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable single sign-on (SSO)"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SubmissionPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable submission preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UserRolesPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable user roles preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class OrganizationSettings:
    automation_entity_mapping: Optional[AutomationEntityMapping] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('automation_entity_mapping'), 'exclude': lambda f: f is None }})
    automation_preview: Optional[AutomationPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('automation_preview'), 'exclude': lambda f: f is None }})
    central_inbox_preview_setting: Optional[CentralInboxPreviewSetting] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('central_inbox_preview_setting'), 'exclude': lambda f: f is None }})
    contracts_preview_setting: Optional[ContractsPreviewSetting] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contracts_preview_setting'), 'exclude': lambda f: f is None }})
    disable_ivy: Optional[DisableIvy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disable_ivy'), 'exclude': lambda f: f is None }})
    double_opt_in: Optional[DoubleOptIn] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('double_opt_in'), 'exclude': lambda f: f is None }})
    ecommerce_catalog_preview: Optional[EcommerceCatalogPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecommerce_catalog_preview'), 'exclude': lambda f: f is None }})
    ecommerce_opportunities_preview: Optional[EcommerceOpportunitiesPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecommerce_opportunities_preview'), 'exclude': lambda f: f is None }})
    ecommerce_preview: Optional[EcommercePreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecommerce_preview'), 'exclude': lambda f: f is None }})
    end_customer_portal: Optional[EndCustomerPortal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_customer_portal'), 'exclude': lambda f: f is None }})
    entity_schema_builder: Optional[EntitySchemaBuilder] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_schema_builder'), 'exclude': lambda f: f is None }})
    installer_portal: Optional[InstallerPortal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('installer_portal'), 'exclude': lambda f: f is None }})
    logic_editor_preview: Optional[LogicEditorPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logic_editor_preview'), 'exclude': lambda f: f is None }})
    new_navigation: Optional[NewNavigation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_navigation'), 'exclude': lambda f: f is None }})
    partnering: Optional[Partnering] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('partnering'), 'exclude': lambda f: f is None }})
    product_availability: Optional[ProductAvailability] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product-availability'), 'exclude': lambda f: f is None }})
    sso: Optional[Sso] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sso'), 'exclude': lambda f: f is None }})
    submission_preview: Optional[SubmissionPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('submission_preview'), 'exclude': lambda f: f is None }})
    user_roles_preview: Optional[UserRolesPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_roles_preview'), 'exclude': lambda f: f is None }})
    
