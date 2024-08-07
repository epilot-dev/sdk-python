# ConvertDocumentRequest


## Fields

| Field                                              | Type                                               | Required                                           | Description                                        | Example                                            |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| `input_document`                                   | [models.InputDocument](../models/inputdocument.md) | :heavy_check_mark:                                 | Input document                                     |                                                    |
| `output_format`                                    | [models.OutputFormat](../models/outputformat.md)   | :heavy_check_mark:                                 | Output format of the document                      |                                                    |
| `output_filename`                                  | *Optional[str]*                                    | :heavy_minus_sign:                                 | Filename of the output document (optional)         | converted.pdf                                      |