# OrderStatus


| status      | description |
|-------------|-------|
| `draft`     | ​​Starting state for all orders, at this point we can still edit the order |
| `quote`     | The order is in a quoting phase, bound to an expiration date |
| `placed`    | The order has been paid and can now be fulfilled (shipped, delivered, complete) or canceled |
| `cancelled` | The order has been cancelled |
| `completed` | The order is now closed and finalized |



## Values

| Name        | Value       |
| ----------- | ----------- |
| `DRAFT`     | draft       |
| `QUOTE`     | quote       |
| `PLACED`    | placed      |
| `CANCELLED` | cancelled   |
| `COMPLETED` | completed   |