# CheckoutCart

The cart checkout request payload


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `cart`                                                               | [Optional[Union[str, shared.CartDto]]](../../models/shared/cart.md)  | :heavy_minus_sign:                                                   | N/A                                                                  |
| `mode`                                                               | [Optional[shared.CheckoutMode]](../../models/shared/checkoutmode.md) | :heavy_minus_sign:                                                   | The checkout mode for the cart checkout.                             |