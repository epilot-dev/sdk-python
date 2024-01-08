"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from .addressrelationattribute import AddressRelationAttribute
from .automationattribute import AutomationAttribute
from .booleanattribute import BooleanAttribute
from .computedattribute import ComputedAttribute
from .consentattribute import ConsentAttribute
from .countryattribute import CountryAttribute
from .currencyattribute import CurrencyAttribute
from .dateattribute import DateAttribute
from .entityaction import EntityAction
from .entitycapability import EntityCapability
from .entitydefaultcreate import EntityDefaultCreate
from .entitydefaultedit import EntityDefaultEdit
from .entitydefaulttable import EntityDefaultTable
from .entityviewdisabled import EntityViewDisabled
from .fileattribute import FileAttribute
from .internalattribute import InternalAttribute
from .internaluserattribute import InternalUserAttribute
from .invitationemailattribute import InvitationEmailAttribute
from .linkattribute import LinkAttribute
from .multiselectattribute import MultiSelectAttribute
from .numberattribute import NumberAttribute
from .orderedlistattribute import OrderedListAttribute
from .partnerorganisationattribute import PartnerOrganisationAttribute
from .partnerstatusattribute import PartnerStatusAttribute
from .paymentmethodrelationattribute import PaymentMethodRelationAttribute
from .purposeattribute import PurposeAttribute
from .redirectentityview import RedirectEntityView
from .relationattribute import RelationAttribute
from .repeatableattribute import RepeatableAttribute
from .searchmappings import SearchMappings
from .selectattribute import SelectAttribute
from .sequenceattribute import SequenceAttribute
from .statusattribute import StatusAttribute
from .summaryattribute import SummaryAttribute
from .tagsattribute import TagsAttribute
from .textattribute import TextAttribute
from .userrelationattribute import UserRelationAttribute
from dataclasses_json import Undefined, dataclass_json
from epilot import utils
from typing import Any, Dict, List, Optional, Union


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class InfoTooltipTitle:
    default: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default'), 'exclude': lambda f: f is None }})
    key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GroupSettings:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('label') }})
    purpose: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('_purpose'), 'exclude': lambda f: f is None }})
    expanded: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expanded'), 'exclude': lambda f: f is None }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feature_flag'), 'exclude': lambda f: f is None }})
    r"""This group should only be active when the feature flag is enabled"""
    info_tooltip_title: Optional[InfoTooltipTitle] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('info_tooltip_title'), 'exclude': lambda f: f is None }})
    order: Optional[int] = dataclasses.field(default=0, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('order'), 'exclude': lambda f: f is None }})
    r"""Render order of the group"""
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('render_condition'), 'exclude': lambda f: f is None }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('setting_flag'), 'exclude': lambda f: f is None }})
    r"""This group should only be active when the setting is enabled"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class LayoutSettings:
    r"""Custom grid definitions for the layout. These settings are composed by managed and un-managed properties:
    - Managed Properties: are interpreted and transformed into layout styles
    - Un-managed Properties: are appended as styles into the attribute mounting node
    """
    additional_properties: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'exclude': lambda f: f is None }})
    grid_gap: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grid_gap'), 'exclude': lambda f: f is None }})
    r"""Defines the grid gap for the mounting node of the attribute."""
    grid_template_columns: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('grid_template_columns'), 'exclude': lambda f: f is None }})
    r"""Defines the grid column template for the mounting node of the attribute."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class ListItem:
    quick_actions: Optional[List[EntityAction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('quick_actions'), 'exclude': lambda f: f is None }})
    summary_attributes: Optional[List[Union[SummaryAttribute, str]]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary_attributes'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Sharing:
    show_sharing_button: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('show_sharing_button'), 'exclude': lambda f: f is None }})
    r"""Show the sharing button in entity detail view"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UIConfig:
    create_view: Optional[Union[EntityDefaultCreate, RedirectEntityView, EntityViewDisabled]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('create_view'), 'exclude': lambda f: f is None }})
    edit_view: Optional[Union[EntityDefaultEdit, RedirectEntityView, EntityViewDisabled]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('edit_view'), 'exclude': lambda f: f is None }})
    list_item: Optional[ListItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('list_item'), 'exclude': lambda f: f is None }})
    sharing: Optional[Sharing] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sharing'), 'exclude': lambda f: f is None }})
    single_view: Optional[Union[EntityDefaultEdit, RedirectEntityView, EntityViewDisabled]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('single_view'), 'exclude': lambda f: f is None }})
    table_view: Optional[Union[EntityDefaultTable, RedirectEntityView, EntityViewDisabled]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('table_view'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class EntitySchema:
    r"""The \\"type\\" of an Entity. Describes the shape. Includes Entity Attributes, Relations and Capabilities."""
    attributes: List[Union[TextAttribute, LinkAttribute, DateAttribute, CountryAttribute, BooleanAttribute, SelectAttribute, MultiSelectAttribute, StatusAttribute, SequenceAttribute, RelationAttribute, UserRelationAttribute, AddressRelationAttribute, PaymentMethodRelationAttribute, CurrencyAttribute, RepeatableAttribute, TagsAttribute, NumberAttribute, ConsentAttribute, InternalAttribute, OrderedListAttribute, FileAttribute, ComputedAttribute, PartnerStatusAttribute, InvitationEmailAttribute, AutomationAttribute, InternalUserAttribute, PurposeAttribute, PartnerOrganisationAttribute]] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('attributes') }})
    r"""An ordered list of attributes the entity contains"""
    capabilities: List[EntityCapability] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('capabilities') }})
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""User-friendly identifier for the entity schema"""
    plural: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('plural') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('slug') }})
    r"""URL-friendly identifier for the entity schema"""
    blueprint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('blueprint'), 'exclude': lambda f: f is None }})
    r"""Reference to blueprint"""
    dialog_config: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dialog_config'), 'exclude': lambda f: f is None }})
    draft: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('draft'), 'exclude': lambda f: f is None }})
    enable_setting: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('enable_setting'), 'exclude': lambda f: f is None }})
    r"""This schema should only be active when one of the organization settings is enabled"""
    explicit_search_mappings: Optional[Dict[str, SearchMappings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('explicit_search_mappings'), 'exclude': lambda f: f is None }})
    r"""Advanced: explicit Elasticsearch index mapping definitions for entity data"""
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('feature_flag'), 'exclude': lambda f: f is None }})
    r"""This schema should only be active when the feature flag is enabled"""
    group_settings: Optional[List[GroupSettings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('group_settings'), 'exclude': lambda f: f is None }})
    r"""A dictionary of Group Titles and associated settings if present."""
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('icon'), 'exclude': lambda f: f is None }})
    layout_settings: Optional[LayoutSettings] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('layout_settings'), 'exclude': lambda f: f is None }})
    r"""Custom grid definitions for the layout. These settings are composed by managed and un-managed properties:
    - Managed Properties: are interpreted and transformed into layout styles
    - Un-managed Properties: are appended as styles into the attribute mounting node
    """
    published: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('published'), 'exclude': lambda f: f is None }})
    title_template: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title_template'), 'exclude': lambda f: f is None }})
    r"""Template for rendering the title field. Uses handlebars"""
    ui_config: Optional[UIConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('ui_config'), 'exclude': lambda f: f is None }})
    version: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('version'), 'exclude': lambda f: f is None }})
    

