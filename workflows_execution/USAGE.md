<!-- Start SDK Example Usage [usage] -->
```python
import epilot
from epilot.models import shared

s = epilot.Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)

req = shared.WorkflowExecutionCreateReq(
    workflow_id='j3f23fh23uif98',
    contexts=[
        shared.WorkflowContext(
            id='3fa3fa86-0907-4642-a57e-0fe30a19874d',
            schema='contact',
            title='<value>',
        ),
        shared.WorkflowContext(
            id='3a6d42fa-5070-4723-b90f-41ead4303e33',
            schema='opportunity',
            title='<value>',
        ),
    ],
    trigger=shared.TriggerType.AUTOMATIC,
)

res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->