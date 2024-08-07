# EntityOperationTrigger

- If provides filter_config, executes an automation based on the filtered configuration when an entity event occurs.
- The conditions on a filter follows the event bridge patterns - `https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html`
  | Comparison             | Example                                             | Rule syntax                                              |
  |------------------------|-----------------------------------------------------|----------------------------------------------------------|
  | Null                   | first_name is null                                  | `"first_name": [ null ]`                                 |
  | Empty                  | last_name is empty                                  | `"last_name": [""]`                                      |
  | Equals                 | email is "j.doe@email.com"                          | `"email": [ "j.doe@email.com" ]`                         |
  | Equals (ignore case)   | first_name is "John"                                | `"first_name": [ { "equals-ignore-case": "john" } ]`     |
  | And                    | fist_name is "John" and last_name is "Doe"          | `"first_name": [ "John" ], "last_name": ["Doe"]`         |
  | Or                     | PaymentType is "Invoice" or "SEPA"                  | `"PaymentType": [ "invoice", "sepa"]`                    |
  | Or (multiple fields)   | first_name is "John", or last_name is "Doe".        | `"$or": [ { "first_name": [ "John" ] }, { "last_name": [ "Doe" ] } ]` |
  | Not                    | status is anything but "cancelled"                  | `"status": [ { "anything-but": [ "cancelled" ] } ]`      |
  | Numeric (equals)       | Price is 100                                        | `"Price": [ { "numeric": [ "=", 100 ] } ]`               |
  | Numeric (range)        | Price is more than 10, and less than or equal to 20 | `"Price": [ { "numeric": [ ">", 10, "<=", 20 ] } ]`      |
  | Exists                 | ProductName exists                                  | `"ProductName": [ { "exists": true } ]`                  |
  | Does not exist         | ProductName does not exist                          | `"ProductName": [ { "exists": false } ]`                 |
  | Begins with            | OpportunityNumber starts with OPP-                  | `"opportunity_number": [ { "prefix": "OPP-" } ]`         |
  | Ends with              | FileName ends with a .png extension                 | `"filename": [ { "suffix": ".png" } ]`                   |
  | Wildcard               | search a string using a wildcard                    | `"email": [ { "wildcard": "*@doe.com" } ]`               |
  - To run the execution on all update events
    ```
      {
        "type": "filter_entity_event",
        "configuration": {
          "operation": {
            "operation": ["updateEntity"]
          }
        }
      }
    ```
  - To run the execution only when the updates are from a portal user
    ```
      {
        "type": "filter_entity_event",
        "configuration": {
          "operation": {
            "operation": ["updateEntity"]
          },
          "activity": {
            "type": "EntityUpdatedFromPortal"
          }
        }
      }
    ```
  - To run the execution only when there is an update on a specific attribute
    ```
      Only starts the automation when the email on a contact is changed
      {
        "type": "filter_entity_event",
        "configuration": {
          "operation": {
            "operation": ["updateEntity"],
            "payload": {
              "_schema": ["contact"]
            },
            "diff": {
              "updated": {
                "email": [{ "exists": true }]
              }
            }
          }
        }
      }
    ```
    - To run the execution only when a specific attribute is altered(created/updated/deleted)
      ```
        Only starts the automation when a price is altered on a contract
        {
          "type": "filter_entity_event",
          "configuration": {
            "operation": {
              "payload": {
                "_schema": ["contract"]
              },
              "diff": {
                // Whether he first_name has been added, updated, or removed
                $or: [
                  {
                    'added.first_name': [{ exists: true }]
                  },
                  {
                    'updated.first_name': [{ exists: true }]
                  },
                  {
                    'deleted.first_name': [{ exists: true }]
                  }
                ]
              }
            }
          }
        }
      ```
    - To run the execution if an attribute is changed from one state to another
      ```
        Only starts the automation when the order status changes from `open_for_acceptance` to `placed`
        {
          "type": "filter_entity_event",
          "configuration": {
            "operation": {
              "operation": ["updateEntity"],
              "payload": {
                "_schema": ["order"],
                "status": ["placed"]
              },
              "diff": {
                "updated": {
                  "status": ["open_for_acceptance"]
                }
              }
            }
          }
        }
      ```



## Fields

| Field                                                                                          | Type                                                                                           | Required                                                                                       | Description                                                                                    | Example                                                                                        |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `configuration`                                                                                | [models.EntityOperationTriggerConfiguration](../models/entityoperationtriggerconfiguration.md) | :heavy_check_mark:                                                                             | N/A                                                                                            |                                                                                                |
| `type`                                                                                         | [models.EntityOperationTriggerType](../models/entityoperationtriggertype.md)                   | :heavy_check_mark:                                                                             | N/A                                                                                            |                                                                                                |
| `id`                                                                                           | *Optional[str]*                                                                                | :heavy_minus_sign:                                                                             | N/A                                                                                            | 12d4f45a-1883-4841-a94c-5928cb338a94                                                           |