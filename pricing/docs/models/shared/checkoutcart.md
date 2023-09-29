# CheckoutCart

The cart checkout request payload


## Fields

| Field                                                                                         | Type                                                                                          | Required                                                                                      | Description                                                                                   |
| --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `cart`                                                                                        | [Optional[Union[str, shared.CartDtoInput]]](undefined/models/shared/checkoutcartcartinput.md) | :heavy_minus_sign:                                                                            | N/A                                                                                           |
| `mode`                                                                                        | [Optional[shared.CheckoutMode]](undefined/models/shared/checkoutmode.md)                      | :heavy_minus_sign:                                                                            | The checkout mode for the cart checkout.                                                      |