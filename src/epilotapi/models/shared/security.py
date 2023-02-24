from __future__ import annotations
import dataclasses



@dataclasses.dataclass
class SchemeEpilotAuth:
    authorization: str = dataclasses.field(metadata={'security': { 'field_name': 'Authorization' }})
    

@dataclasses.dataclass
class Security:
    epilot_auth: SchemeEpilotAuth = dataclasses.field(metadata={'security': { 'scheme': True, 'type': 'http', 'sub_type': 'bearer' }})
    