import dataclasses



@dataclasses.dataclass
class RemoveJourneyPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class RemoveJourneyRequest:
    path_params: RemoveJourneyPathParams = dataclasses.field()
    

@dataclasses.dataclass
class RemoveJourneyResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    
