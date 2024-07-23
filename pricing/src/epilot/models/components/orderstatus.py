"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class OrderStatus(str, Enum):
    r"""| status      | description |
    |-------------|-------|
    | `draft`     | \u200B\u200BStarting state for all orders, at this point we can still edit the order |
    | `quote`     | The order is in a quoting phase, bound to an expiration date |
    | `placed`    | The order has been paid and can now be fulfilled (shipped, delivered, complete) or canceled |
    | `cancelled` | The order has been cancelled |
    | `completed` | The order is now closed and finalized |
    """
    DRAFT = 'draft'
    QUOTE = 'quote'
    PLACED = 'placed'
    CANCELLED = 'cancelled'
    COMPLETED = 'completed'
