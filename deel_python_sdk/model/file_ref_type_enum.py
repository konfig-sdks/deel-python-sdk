# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from deel_python_sdk import schemas  # noqa: F401


class FileRefTypeEnum(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    type of files allowed when uploading attachments
    """


    class MetaOapg:
        min_length = 5
        enum_value_to_name = {
            "application/pdf": "APPLICATION_PDF",
            "text/csv": "TEXT_CSV",
            "text/plain": "TEXT_PLAIN",
            "image/jpeg": "IMAGE_JPEG",
            "image/png": "IMAGE_PNG",
        }
    
    @schemas.classproperty
    def APPLICATION_PDF(cls):
        return cls("application/pdf")
    
    @schemas.classproperty
    def TEXT_CSV(cls):
        return cls("text/csv")
    
    @schemas.classproperty
    def TEXT_PLAIN(cls):
        return cls("text/plain")
    
    @schemas.classproperty
    def IMAGE_JPEG(cls):
        return cls("image/jpeg")
    
    @schemas.classproperty
    def IMAGE_PNG(cls):
        return cls("image/png")
