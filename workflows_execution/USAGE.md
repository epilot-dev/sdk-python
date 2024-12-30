<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
import epilot_workflows_execution
from epilot_workflows_execution import Epilot

with Epilot(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
) as epilot:

    res = epilot.workflows.create_execution(workflow_id="j3f23fh23uif98", contexts=[
        {
            "id": "3fa3fa86-0907-4642-a57e-0fe30a19874d",
            "schema_": "contact",
            "title": "<value>",
        },
        {
            "id": "3a6d42fa-5070-4723-b90f-41ead4303e33",
            "schema_": "opportunity",
            "title": "<value>",
        },
    ], trigger=epilot_workflows_execution.TriggerType.AUTOMATIC)

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
import epilot_workflows_execution
from epilot_workflows_execution import Epilot

async def main():
    async with Epilot(
        bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
    ) as epilot:

        res = await epilot.workflows.create_execution_async(workflow_id="j3f23fh23uif98", contexts=[
            {
                "id": "3fa3fa86-0907-4642-a57e-0fe30a19874d",
                "schema_": "contact",
                "title": "<value>",
            },
            {
                "id": "3a6d42fa-5070-4723-b90f-41ead4303e33",
                "schema_": "opportunity",
                "title": "<value>",
            },
        ], trigger=epilot_workflows_execution.TriggerType.AUTOMATIC)

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->