<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations

s = epilot.Epilot()


req = operations.AddEndCustomerRelationToEntityRequest(
    id='89bd9d8d-69a6-474e-8f46-7cc8796ed151',
    slug='contact',
)

res = s.ecp.add_end_customer_relation_to_entity(req, operations.AddEndCustomerRelationToEntitySecurity(
    portal_auth="Bearer YOUR_BEARER_TOKEN_HERE",
))

if res.add_end_customer_relation_to_entity_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->