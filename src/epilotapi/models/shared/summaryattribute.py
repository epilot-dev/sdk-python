import dataclasses
from typing import Optional
from dataclasses_json import dataclass_json
from epilotapi import utils


@dataclass_json
@dataclasses.dataclass
class SummaryAttribute:
    r"""SummaryAttribute
    Represents an expanded version of an attribute to be displayed in the list item summary.
    This configuration can be used in the following way:
    ```js
    {
      \"label\": \"Price components\"
      \"value\": \"{{item.prices.length}} price components\"
      \"show_as_tag\": true
      \"render_condition\": \"is_composite_price = \"true\"\"
    }
    ```
    The value field supports handlebar expressions from which you can pick any field from the entity state.
    
    """
    
    label: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('label') }})
    value: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.field_name('value') }})
    feature_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('feature_flag') }})
    render_condition: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('render_condition') }})
    setting_flag: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('setting_flag') }})
    show_as_tag: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('show_as_tag') }})
    tag_color: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.field_name('tag_color') }})
    
