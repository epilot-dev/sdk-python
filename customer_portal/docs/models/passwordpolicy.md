# PasswordPolicy

Password policy for the portal


## Fields

| Field                        | Type                         | Required                     | Description                  | Example                      |
| ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- | ---------------------------- |
| `minimum_length`             | *Optional[int]*              | :heavy_minus_sign:           | Minimum password length      | 8                            |
| `require_lowercase`          | *Optional[bool]*             | :heavy_minus_sign:           | Require lowercase characters | true                         |
| `require_numbers`            | *Optional[bool]*             | :heavy_minus_sign:           | Require numbers              | true                         |
| `require_symbols`            | *Optional[bool]*             | :heavy_minus_sign:           | Require symbols              | true                         |
| `require_uppercase`          | *Optional[bool]*             | :heavy_minus_sign:           | Require uppercase characters | true                         |