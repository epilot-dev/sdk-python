"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from epilot import utils
from epilot.models import components, errors, operations
from typing import Optional

class EntityImport:
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    
    def import_entities(self, entity_import_params: Optional[components.EntityImportParams] = None, job_id: Optional[str] = None) -> operations.ImportEntitiesResponse:
        r"""Import Entities
        This endpoint enables the import of entities into the platform.
        The entities should be provided in a CSV format inside an S3 bucket.
        This API will return the `job_id`` which can be used to fetch the status of the import process.
        """
        request = operations.ImportEntitiesRequest(
            entity_import_params=entity_import_params,
            job_id=job_id,
        )
        
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/v1/entity:import'
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, operations.ImportEntitiesRequest, "entity_import_params", False, True, 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.ImportEntitiesRequest, request)
        headers['Accept'] = '*/*'
        headers['user-agent'] = self.sdk_configuration.user_agent
        
        if callable(self.sdk_configuration.security):
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security())
        else:
            client = utils.configure_security_client(self.sdk_configuration.client, self.sdk_configuration.security)
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')
        
        res = operations.ImportEntitiesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            pass
        elif http_res.status_code >= 400 and http_res.status_code < 500 or http_res.status_code >= 500 and http_res.status_code < 600:
            raise errors.SDKError('API error occurred', http_res.status_code, http_res.text, http_res)

        return res

    