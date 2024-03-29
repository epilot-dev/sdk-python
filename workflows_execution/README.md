# epilot-workflows-execution

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/epilot-dev/sdk-python.git#subdirectory=workflows_execution
```
<!-- End SDK Installation -->

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
## SDK Available Operations


### workflows

* `create_execution` - createExecution
* `create_step` - createStep
* `delete_execution` - deleteExecution
* `delete_step` - deleteStep
* `get_closing_reason_execution` - getClosingReasonExecution
* `get_execution` - getExecution
* `get_executions` - getExecutions
* `search_executions` - searchExecutions
* `search_steps` - searchSteps
* `update_execution` - updateExecution
* `update_step` - updateStep
<!-- End SDK Available Operations -->

### SDK Generated by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
