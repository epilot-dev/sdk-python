<!-- Start SDK Example Usage -->
```python
import epilot
from epilot.models import operations, shared

s = epilot.Epilot()

req = operations.AddEndCustomerRelationToEntityRequest(
    id='5da0a718-c822-403d-9f5d-20d4584e0528',
    slug=shared.EntitySlug.CONTACT,
)

res = s.ecp.add_end_customer_relation_to_entity(req, operations.AddEndCustomerRelationToEntitySecurity(
    portal_auth="YOUR_BEARER_TOKEN_HERE",
))

if res.add_end_customer_relation_to_entity_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->