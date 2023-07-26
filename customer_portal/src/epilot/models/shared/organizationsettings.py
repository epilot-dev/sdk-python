"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsAutomationEntityMapping:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable automation entity mapping"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsAutomationPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable automation preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsCentralInboxPreviewSetting:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable central inbox preview setting"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsContractsPreviewSetting:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable contracts preview setting"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsDisableIvy:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable Ivy"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsDoubleOptIn:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable double opt-in"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsEcommerceCatalogPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable ecommerce catalog preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsEcommerceOpportunitiesPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable ecommerce opportunities preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsEcommercePreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable ecommerce preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsEndCustomerPortal:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable end customer portal"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsEntitySchemaBuilder:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable entity schema builder"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsInstallerPortal:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable installer portal"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsLogicEditorPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable logic editor preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsNewNavigation:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable new navigation"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsPartnering:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable partnering"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsProductAvailability:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable product availability"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsSso:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable single sign-on (SSO)"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsSubmissionPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable submission preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettingsUserRolesPreview:
    enabled: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enabled'), 'exclude': lambda f: f is None }})
    r"""Enable/Disable user roles preview"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class OrganizationSettings:
    automation_entity_mapping: Optional[OrganizationSettingsAutomationEntityMapping] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('automation_entity_mapping'), 'exclude': lambda f: f is None }})
    automation_preview: Optional[OrganizationSettingsAutomationPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('automation_preview'), 'exclude': lambda f: f is None }})
    central_inbox_preview_setting: Optional[OrganizationSettingsCentralInboxPreviewSetting] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('central_inbox_preview_setting'), 'exclude': lambda f: f is None }})
    contracts_preview_setting: Optional[OrganizationSettingsContractsPreviewSetting] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contracts_preview_setting'), 'exclude': lambda f: f is None }})
    disable_ivy: Optional[OrganizationSettingsDisableIvy] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('disable_ivy'), 'exclude': lambda f: f is None }})
    double_opt_in: Optional[OrganizationSettingsDoubleOptIn] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('double_opt_in'), 'exclude': lambda f: f is None }})
    ecommerce_catalog_preview: Optional[OrganizationSettingsEcommerceCatalogPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecommerce_catalog_preview'), 'exclude': lambda f: f is None }})
    ecommerce_opportunities_preview: Optional[OrganizationSettingsEcommerceOpportunitiesPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecommerce_opportunities_preview'), 'exclude': lambda f: f is None }})
    ecommerce_preview: Optional[OrganizationSettingsEcommercePreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ecommerce_preview'), 'exclude': lambda f: f is None }})
    end_customer_portal: Optional[OrganizationSettingsEndCustomerPortal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_customer_portal'), 'exclude': lambda f: f is None }})
    entity_schema_builder: Optional[OrganizationSettingsEntitySchemaBuilder] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('entity_schema_builder'), 'exclude': lambda f: f is None }})
    installer_portal: Optional[OrganizationSettingsInstallerPortal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('installer_portal'), 'exclude': lambda f: f is None }})
    logic_editor_preview: Optional[OrganizationSettingsLogicEditorPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('logic_editor_preview'), 'exclude': lambda f: f is None }})
    new_navigation: Optional[OrganizationSettingsNewNavigation] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_navigation'), 'exclude': lambda f: f is None }})
    partnering: Optional[OrganizationSettingsPartnering] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('partnering'), 'exclude': lambda f: f is None }})
    product_availability: Optional[OrganizationSettingsProductAvailability] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product-availability'), 'exclude': lambda f: f is None }})
    sso: Optional[OrganizationSettingsSso] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sso'), 'exclude': lambda f: f is None }})
    submission_preview: Optional[OrganizationSettingsSubmissionPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('submission_preview'), 'exclude': lambda f: f is None }})
    user_roles_preview: Optional[OrganizationSettingsUserRolesPreview] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_roles_preview'), 'exclude': lambda f: f is None }})
    

