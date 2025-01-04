# Status

Status of the bulk trigger automation job
* approval: Waiting for user approval to start the bulk trigger automation
* starting: Starting automation executions
* in_progress: Automation execution are currently running
* send_report: Automation executions finished running. Report is being created & sent to the user who initiated the bulk trigger automation
* finished: Automation executions finished running. Some may have failed. Check the status of each entity.
* failed: Bulk trigger automation execution failed. Some executions might have started. Check the status of each entity.
* cancelled: Bulk trigger automation execution was cancelled



## Values

| Name          | Value         |
| ------------- | ------------- |
| `APPROVAL`    | approval      |
| `STARTING`    | starting      |
| `IN_PROGRESS` | in_progress   |
| `SEND_REPORT` | send_report   |
| `FINISHED`    | finished      |
| `FAILED`      | failed        |
| `CANCELLED`   | cancelled     |