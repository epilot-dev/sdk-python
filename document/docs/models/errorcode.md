# ErrorCode

Error codes for document generation:
- PARSE_ERROR - Error while parsing the document. Normally related with a bad template using the wrong DocxTemplater syntax.
- DOC_TO_PDF_CONVERT_ERROR - Error while converting the document to PDF. Normally related with a ConvertAPI failure.
- INTERNAL_ERROR - Internal error. Please contact support.
- INVALID_TEMPLATE_FORMAT - Invalid template format (only .docx is supported). This can happen due to a bad word file or an unsupported file extension.



## Values

| Name                       | Value                      |
| -------------------------- | -------------------------- |
| `PARSE_ERROR`              | PARSE_ERROR                |
| `DOC_TO_PDF_CONVERT_ERROR` | DOC_TO_PDF_CONVERT_ERROR   |
| `INTERNAL_ERROR`           | INTERNAL_ERROR             |
| `INVALID_TEMPLATE_FORMAT`  | INVALID_TEMPLATE_FORMAT    |