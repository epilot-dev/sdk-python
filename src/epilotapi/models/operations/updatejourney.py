import dataclasses
from datetime import date, datetime
from marshmallow import fields
import dateutil.parser
from typing import Any,Optional


@dataclasses.dataclass
class UpdateJourneyRequest:
    request: Optional[dict[str, Any]] = dataclasses.field(default=None, metadata={'request': { 'media_type': 'application/json' }})
    

@dataclasses.dataclass
class UpdateJourneyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    journey_response: Optional[dict[str, Any]] = dataclasses.field(default=None)
    
