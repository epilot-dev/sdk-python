<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot(
    security=shared.Security(
        bearer_auth="Bearer YOUR_BEARER_TOKEN_HERE",
    ),
)


req = shared.WorkflowExecutionCreateReq(
    assigned_to=[
        "deserunt",
        "porro",
        "nulla",
    ],
    contexts=[
        shared.WorkflowContext(
            id="vero",
            schema="perspiciatis",
            title="Internal Group Orchestrator",
        ),
        shared.WorkflowContext(
            id="facilis",
            schema="eum",
            title="District Paradigm Agent",
        ),
        shared.WorkflowContext(
            id="inventore",
            schema="sapiente",
            title="Future Markets Architect",
        ),
    ],
    trigger="AUTOMATIC",
    workflow_id="vel",
)
    
res = s.workflows.create_execution(req)

if res.workflow_execution is not None:
    # handle response
```
<!-- End SDK Example Usage -->