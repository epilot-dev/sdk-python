import dataclasses
from typing import Any,Optional
from dataclasses_json import dataclass_json
from epilotapi import utils
from ..shared import summaryattribute as shared_summaryattribute
from ..shared import entitydefaultcreate as shared_entitydefaultcreate
from ..shared import entitydefaultedit as shared_entitydefaultedit
from ..shared import entitydefaulttable as shared_entitydefaulttable
from ..shared import redirectentityview as shared_redirectentityview
from ..shared import entityparcelview as shared_entityparcelview
from ..shared import entityviewdisabled as shared_entityviewdisabled
from ..shared import textattribute as shared_textattribute
from ..shared import linkattribute as shared_linkattribute
from ..shared import dateattribute as shared_dateattribute
from ..shared import countryattribute as shared_countryattribute
from ..shared import booleanattribute as shared_booleanattribute
from ..shared import selectattribute as shared_selectattribute
from ..shared import multiselectattribute as shared_multiselectattribute
from ..shared import statusattribute as shared_statusattribute
from ..shared import sequenceattribute as shared_sequenceattribute
from ..shared import relationattribute as shared_relationattribute
from ..shared import userrelationattribute as shared_userrelationattribute
from ..shared import addressrelationattribute as shared_addressrelationattribute
from ..shared import paymentmethodrelationattribute as shared_paymentmethodrelationattribute
from ..shared import currencyattribute as shared_currencyattribute
from ..shared import repeatableattribute as shared_repeatableattribute
from ..shared import tagsattribute as shared_tagsattribute
from ..shared import numberattribute as shared_numberattribute
from ..shared import consentattribute as shared_consentattribute
from ..shared import internalattribute as shared_internalattribute
from ..shared import orderedlistattribute as shared_orderedlistattribute
from ..shared import fileattribute as shared_fileattribute
from ..shared import computedattribute as shared_computedattribute
from ..shared import partnerstatusattribute as shared_partnerstatusattribute
from ..shared import invitationemailattribute as shared_invitationemailattribute
from ..shared import automationattribute as shared_automationattribute
from ..shared import internaluserattribute as shared_internaluserattribute
from ..shared import purposeattribute as shared_purposeattribute
from ..shared import entitycapability as shared_entitycapability
from ..shared import searchmappings as shared_searchmappings


@dataclass_json
@dataclasses.dataclass
class EntitySchemaGroupSettingsInfoTooltipTitle:
    default: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('default') }})
    key: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('key') }})
    

@dataclass_json
@dataclasses.dataclass
class EntitySchemaGroupSettings:
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('id') }})
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    purpose: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('_purpose') }})
    expanded: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('expanded') }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag') }})
    info_tooltip_title: Optional[EntitySchemaGroupSettingsInfoTooltipTitle] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('info_tooltip_title') }})
    order: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('order') }})
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('render_condition') }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('setting_flag') }})
    

@dataclass_json
@dataclasses.dataclass
class EntitySchemaUIConfigListItem:
    summary_attributes: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('summary_attributes') }})
    

@dataclass_json
@dataclasses.dataclass
class EntitySchemaUIConfigSharing:
    show_sharing_button: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('show_sharing_button') }})
    

@dataclass_json
@dataclasses.dataclass
class EntitySchemaUIConfig:
    create_view: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('create_view') }})
    edit_view: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('edit_view') }})
    list_item: Optional[EntitySchemaUIConfigListItem] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('list_item') }})
    sharing: Optional[EntitySchemaUIConfigSharing] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('sharing') }})
    single_view: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('single_view') }})
    table_view: Optional[Any] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('table_view') }})
    

@dataclass_json
@dataclasses.dataclass
class EntitySchema:
    r"""EntitySchema
    The \"type\" of an Entity. Describes the shape. Includes Entity Attributes, Relations and Capabilities.
    """
    
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('name') }})
    plural: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('plural') }})
    slug: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('slug') }})
    attributes: Optional[list[Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('attributes') }})
    blueprint: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('blueprint') }})
    capabilities: Optional[list[shared_entitycapability.EntityCapability]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('capabilities') }})
    dialog_config: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('dialog_config') }})
    draft: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('draft') }})
    enable_setting: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('enable_setting') }})
    explicit_search_mappings: Optional[dict[str, shared_searchmappings.SearchMappings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('explicit_search_mappings') }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag') }})
    group_settings: Optional[list[EntitySchemaGroupSettings]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('group_settings') }})
    icon: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('icon') }})
    layout_settings: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('layout_settings') }})
    published: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('published') }})
    title_template: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('title_template') }})
    ui_config: Optional[EntitySchemaUIConfig] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('ui_config') }})
    version: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('version') }})
    
