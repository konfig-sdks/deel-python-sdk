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


class Contract(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "compensation_details",
            "created_at",
            "title",
            "type",
            "signatures",
            "special_clause",
            "is_archived",
            "invitations",
            "termination_date",
            "client",
            "id",
            "employment_details",
            "worker",
            "job_title",
            "seniority",
            "start_date",
            "status",
        }
        
        class properties:
            
            
            class title(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class id(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
        
            @staticmethod
            def type() -> typing.Type['ContractTypeEnum']:
                return ContractTypeEnum
        
            @staticmethod
            def status() -> typing.Type['ContractStatusEnum']:
                return ContractStatusEnum
        
            @staticmethod
            def created_at() -> typing.Type['DateTimeString']:
                return DateTimeString
            job_title = schemas.StrSchema
        
            @staticmethod
            def seniority() -> typing.Type['Seniority']:
                return Seniority
        
            @staticmethod
            def start_date() -> typing.Type['DateTimeString']:
                return DateTimeString
        
            @staticmethod
            def termination_date() -> typing.Type['DateTimeString']:
                return DateTimeString
            special_clause = schemas.StrSchema
            is_archived = schemas.BoolSchema
        
            @staticmethod
            def client() -> typing.Type['ClientOfContract']:
                return ClientOfContract
        
            @staticmethod
            def worker() -> typing.Type['WorkerOfContract']:
                return WorkerOfContract
        
            @staticmethod
            def invitations() -> typing.Type['InvitationsOfBasicContract']:
                return InvitationsOfBasicContract
        
            @staticmethod
            def signatures() -> typing.Type['SignaturesOfContract']:
                return SignaturesOfContract
        
            @staticmethod
            def compensation_details() -> typing.Type['CompensationDetailsOfContract']:
                return CompensationDetailsOfContract
        
            @staticmethod
            def employment_details() -> typing.Type['EmploymentDetailsOfContract']:
                return EmploymentDetailsOfContract
        
            @staticmethod
            def who_reports() -> typing.Type['ContractWhoReportsEnum']:
                return ContractWhoReportsEnum
            
            
            class scope_of_work(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'scope_of_work':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def notice_period() -> typing.Type['NoticePeriod']:
                return NoticePeriod
        
            @staticmethod
            def contract_template() -> typing.Type['ContractTemplate']:
                return ContractTemplate
            
            
            class custom_fields(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ContractCustomField']:
                        return ContractCustomField
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ContractCustomField'], typing.List['ContractCustomField']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'custom_fields':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ContractCustomField':
                    return super().__getitem__(i)
        
            @staticmethod
            def quote() -> typing.Type['EorQuoteBase']:
                return EorQuoteBase
            
            
            class external_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'external_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "title": title,
                "id": id,
                "type": type,
                "status": status,
                "created_at": created_at,
                "job_title": job_title,
                "seniority": seniority,
                "start_date": start_date,
                "termination_date": termination_date,
                "special_clause": special_clause,
                "is_archived": is_archived,
                "client": client,
                "worker": worker,
                "invitations": invitations,
                "signatures": signatures,
                "compensation_details": compensation_details,
                "employment_details": employment_details,
                "who_reports": who_reports,
                "scope_of_work": scope_of_work,
                "notice_period": notice_period,
                "contract_template": contract_template,
                "custom_fields": custom_fields,
                "quote": quote,
                "external_id": external_id,
            }
    
    compensation_details: 'CompensationDetailsOfContract'
    created_at: 'DateTimeString'
    title: MetaOapg.properties.title
    type: 'ContractTypeEnum'
    signatures: 'SignaturesOfContract'
    special_clause: MetaOapg.properties.special_clause
    is_archived: MetaOapg.properties.is_archived
    invitations: 'InvitationsOfBasicContract'
    termination_date: 'DateTimeString'
    client: 'ClientOfContract'
    id: MetaOapg.properties.id
    employment_details: 'EmploymentDetailsOfContract'
    worker: 'WorkerOfContract'
    job_title: MetaOapg.properties.job_title
    seniority: 'Seniority'
    start_date: 'DateTimeString'
    status: 'ContractStatusEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'ContractTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'ContractStatusEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> 'DateTimeString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["job_title"]) -> MetaOapg.properties.job_title: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["seniority"]) -> 'Seniority': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> 'DateTimeString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["termination_date"]) -> 'DateTimeString': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["special_clause"]) -> MetaOapg.properties.special_clause: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_archived"]) -> MetaOapg.properties.is_archived: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["client"]) -> 'ClientOfContract': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["worker"]) -> 'WorkerOfContract': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["invitations"]) -> 'InvitationsOfBasicContract': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["signatures"]) -> 'SignaturesOfContract': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["compensation_details"]) -> 'CompensationDetailsOfContract': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["employment_details"]) -> 'EmploymentDetailsOfContract': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["who_reports"]) -> 'ContractWhoReportsEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["scope_of_work"]) -> MetaOapg.properties.scope_of_work: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notice_period"]) -> 'NoticePeriod': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract_template"]) -> 'ContractTemplate': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_fields"]) -> MetaOapg.properties.custom_fields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quote"]) -> 'EorQuoteBase': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["title", "id", "type", "status", "created_at", "job_title", "seniority", "start_date", "termination_date", "special_clause", "is_archived", "client", "worker", "invitations", "signatures", "compensation_details", "employment_details", "who_reports", "scope_of_work", "notice_period", "contract_template", "custom_fields", "quote", "external_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["title"]) -> MetaOapg.properties.title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'ContractTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'ContractStatusEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> 'DateTimeString': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["job_title"]) -> MetaOapg.properties.job_title: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["seniority"]) -> 'Seniority': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> 'DateTimeString': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["termination_date"]) -> 'DateTimeString': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["special_clause"]) -> MetaOapg.properties.special_clause: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_archived"]) -> MetaOapg.properties.is_archived: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["client"]) -> 'ClientOfContract': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["worker"]) -> 'WorkerOfContract': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["invitations"]) -> 'InvitationsOfBasicContract': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["signatures"]) -> 'SignaturesOfContract': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["compensation_details"]) -> 'CompensationDetailsOfContract': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["employment_details"]) -> 'EmploymentDetailsOfContract': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["who_reports"]) -> typing.Union['ContractWhoReportsEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["scope_of_work"]) -> typing.Union[MetaOapg.properties.scope_of_work, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notice_period"]) -> typing.Union['NoticePeriod', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract_template"]) -> typing.Union['ContractTemplate', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_fields"]) -> typing.Union[MetaOapg.properties.custom_fields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quote"]) -> typing.Union['EorQuoteBase', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["title", "id", "type", "status", "created_at", "job_title", "seniority", "start_date", "termination_date", "special_clause", "is_archived", "client", "worker", "invitations", "signatures", "compensation_details", "employment_details", "who_reports", "scope_of_work", "notice_period", "contract_template", "custom_fields", "quote", "external_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        compensation_details: 'CompensationDetailsOfContract',
        created_at: 'DateTimeString',
        title: typing.Union[MetaOapg.properties.title, str, ],
        type: 'ContractTypeEnum',
        signatures: 'SignaturesOfContract',
        special_clause: typing.Union[MetaOapg.properties.special_clause, str, ],
        is_archived: typing.Union[MetaOapg.properties.is_archived, bool, ],
        invitations: 'InvitationsOfBasicContract',
        termination_date: 'DateTimeString',
        client: 'ClientOfContract',
        id: typing.Union[MetaOapg.properties.id, str, ],
        employment_details: 'EmploymentDetailsOfContract',
        worker: 'WorkerOfContract',
        job_title: typing.Union[MetaOapg.properties.job_title, str, ],
        seniority: 'Seniority',
        start_date: 'DateTimeString',
        status: 'ContractStatusEnum',
        who_reports: typing.Union['ContractWhoReportsEnum', schemas.Unset] = schemas.unset,
        scope_of_work: typing.Union[MetaOapg.properties.scope_of_work, None, str, schemas.Unset] = schemas.unset,
        notice_period: typing.Union['NoticePeriod', schemas.Unset] = schemas.unset,
        contract_template: typing.Union['ContractTemplate', schemas.Unset] = schemas.unset,
        custom_fields: typing.Union[MetaOapg.properties.custom_fields, list, tuple, schemas.Unset] = schemas.unset,
        quote: typing.Union['EorQuoteBase', schemas.Unset] = schemas.unset,
        external_id: typing.Union[MetaOapg.properties.external_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Contract':
        return super().__new__(
            cls,
            *args,
            compensation_details=compensation_details,
            created_at=created_at,
            title=title,
            type=type,
            signatures=signatures,
            special_clause=special_clause,
            is_archived=is_archived,
            invitations=invitations,
            termination_date=termination_date,
            client=client,
            id=id,
            employment_details=employment_details,
            worker=worker,
            job_title=job_title,
            seniority=seniority,
            start_date=start_date,
            status=status,
            who_reports=who_reports,
            scope_of_work=scope_of_work,
            notice_period=notice_period,
            contract_template=contract_template,
            custom_fields=custom_fields,
            quote=quote,
            external_id=external_id,
            _configuration=_configuration,
            **kwargs,
        )

from deel_python_sdk.model.client_of_contract import ClientOfContract
from deel_python_sdk.model.compensation_details_of_contract import CompensationDetailsOfContract
from deel_python_sdk.model.contract_custom_field import ContractCustomField
from deel_python_sdk.model.contract_status_enum import ContractStatusEnum
from deel_python_sdk.model.contract_template import ContractTemplate
from deel_python_sdk.model.contract_type_enum import ContractTypeEnum
from deel_python_sdk.model.contract_who_reports_enum import ContractWhoReportsEnum
from deel_python_sdk.model.date_time_string import DateTimeString
from deel_python_sdk.model.employment_details_of_contract import EmploymentDetailsOfContract
from deel_python_sdk.model.eor_quote_base import EorQuoteBase
from deel_python_sdk.model.invitations_of_basic_contract import InvitationsOfBasicContract
from deel_python_sdk.model.notice_period import NoticePeriod
from deel_python_sdk.model.seniority import Seniority
from deel_python_sdk.model.signatures_of_contract import SignaturesOfContract
from deel_python_sdk.model.worker_of_contract import WorkerOfContract
