import dataclasses



@dataclasses.dataclass
class DeleteSavedViewPathParams:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    

@dataclasses.dataclass
class DeleteSavedViewRequest:
    path_params: DeleteSavedViewPathParams = dataclasses.field()
    

@dataclasses.dataclass
class DeleteSavedViewResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    
