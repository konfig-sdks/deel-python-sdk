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


class GetEmployeeComplianceDocumentsContainerDataDocumentsItem(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            description = schemas.StrSchema
            id = schemas.StrSchema
            name = schemas.StrSchema
            has_template = schemas.BoolSchema
            fillable = schemas.BoolSchema
            is_optional = schemas.BoolSchema
            country = schemas.StrSchema
            uploaded_at = schemas.StrSchema
        
            @staticmethod
            def filenames() -> typing.Type['GetEmployeeComplianceDocumentsContainerDataDocumentsItemFilenames']:
                return GetEmployeeComplianceDocumentsContainerDataDocumentsItemFilenames
            __annotations__ = {
                "description": description,
                "id": id,
                "name": name,
                "has_template": has_template,
                "fillable": fillable,
                "is_optional": is_optional,
                "country": country,
                "uploaded_at": uploaded_at,
                "filenames": filenames,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_template"]) -> MetaOapg.properties.has_template: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fillable"]) -> MetaOapg.properties.fillable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_optional"]) -> MetaOapg.properties.is_optional: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uploaded_at"]) -> MetaOapg.properties.uploaded_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["filenames"]) -> 'GetEmployeeComplianceDocumentsContainerDataDocumentsItemFilenames': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "has_template", "fillable", "is_optional", "country", "uploaded_at", "filenames", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_template"]) -> typing.Union[MetaOapg.properties.has_template, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fillable"]) -> typing.Union[MetaOapg.properties.fillable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_optional"]) -> typing.Union[MetaOapg.properties.is_optional, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uploaded_at"]) -> typing.Union[MetaOapg.properties.uploaded_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["filenames"]) -> typing.Union['GetEmployeeComplianceDocumentsContainerDataDocumentsItemFilenames', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "id", "name", "has_template", "fillable", "is_optional", "country", "uploaded_at", "filenames", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, str, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        has_template: typing.Union[MetaOapg.properties.has_template, bool, schemas.Unset] = schemas.unset,
        fillable: typing.Union[MetaOapg.properties.fillable, bool, schemas.Unset] = schemas.unset,
        is_optional: typing.Union[MetaOapg.properties.is_optional, bool, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, str, schemas.Unset] = schemas.unset,
        uploaded_at: typing.Union[MetaOapg.properties.uploaded_at, str, schemas.Unset] = schemas.unset,
        filenames: typing.Union['GetEmployeeComplianceDocumentsContainerDataDocumentsItemFilenames', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GetEmployeeComplianceDocumentsContainerDataDocumentsItem':
        return super().__new__(
            cls,
            *args,
            description=description,
            id=id,
            name=name,
            has_template=has_template,
            fillable=fillable,
            is_optional=is_optional,
            country=country,
            uploaded_at=uploaded_at,
            filenames=filenames,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.get_employee_compliance_documents_container_data_documents_item_filenames import GetEmployeeComplianceDocumentsContainerDataDocumentsItemFilenames