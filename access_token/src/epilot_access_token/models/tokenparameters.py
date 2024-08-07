"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from .accesstokenparameters import AccessTokenParameters, AccessTokenParametersTypedDict
from .journeytokenparameters import JourneyTokenParameters, JourneyTokenParametersTypedDict
from typing import Union


TokenParametersTypedDict = Union[AccessTokenParametersTypedDict, JourneyTokenParametersTypedDict]


TokenParameters = Union[AccessTokenParameters, JourneyTokenParameters]

