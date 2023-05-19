<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="YOUR_BEARER_TOKEN_HERE",
    ),
)

req = shared.WorkflowExecutionCreateReq(
    assigned_to=[
        'provident',
        'distinctio',
        'quibusdam',
    ],
    contexts=[
        shared.WorkflowContext(
            id='d8d69a67-4e0f-4467-8c87-96ed151a05df',
            schema='quo',
            title='Mr.',
        ),
        shared.WorkflowContext(
            id='ddf7cc78-ca1b-4a92-8fc8-16742cb73920',
            schema='ad',
            title='Miss',
        ),
        shared.WorkflowContext(
            id='29396fea-7596-4eb1-8faa-a2352c595590',
            schema='iure',
            title='Miss',
        ),
    ],
    trigger=shared.TriggerType.AUTOMATIC,
    workflow_id='sapiente',
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
```
<!-- End SDK Example Usage -->