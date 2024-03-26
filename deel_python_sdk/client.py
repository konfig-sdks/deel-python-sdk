# coding: utf-8
"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

import typing
import inspect
from datetime import date, datetime
from deel_python_sdk.client_custom import ClientCustom
from deel_python_sdk.configuration import Configuration
from deel_python_sdk.api_client import ApiClient
from deel_python_sdk.type_util import copy_signature
from deel_python_sdk.apis.tags.accounting_api import AccountingApi
from deel_python_sdk.apis.tags.adjustments_api import AdjustmentsApi
from deel_python_sdk.apis.tags.attachments_api import AttachmentsApi
from deel_python_sdk.apis.tags.candidates_api import CandidatesApi
from deel_python_sdk.apis.tags.contractors_api import ContractorsApi
from deel_python_sdk.apis.tags.contracts_api import ContractsApi
from deel_python_sdk.apis.tags.eor_api import EORApi
from deel_python_sdk.apis.tags.global_payroll_api import GlobalPayrollApi
from deel_python_sdk.apis.tags.invoices_api import InvoicesApi
from deel_python_sdk.apis.tags.lookups_api import LookupsApi
from deel_python_sdk.apis.tags.managers_api import ManagersApi
from deel_python_sdk.apis.tags.milestones_api import MilestonesApi
from deel_python_sdk.apis.tags.off_cycle_payments_api import OffCyclePaymentsApi
from deel_python_sdk.apis.tags.organizations_api import OrganizationsApi
from deel_python_sdk.apis.tags.partner_managed_api import PartnerManagedApi
from deel_python_sdk.apis.tags.people_api import PeopleApi
from deel_python_sdk.apis.tags.service_provider_config_api import ServiceProviderConfigApi
from deel_python_sdk.apis.tags.tasks_api import TasksApi
from deel_python_sdk.apis.tags.time_off_api import TimeOffApi
from deel_python_sdk.apis.tags.timesheets_api import TimesheetsApi
from deel_python_sdk.apis.tags.token_api import TokenApi
from deel_python_sdk.apis.tags.user_api import UserApi
from deel_python_sdk.apis.tags.webhooks_api import WebhooksApi



class Deel(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.accounting: AccountingApi = AccountingApi(api_client)
        self.adjustments: AdjustmentsApi = AdjustmentsApi(api_client)
        self.attachments: AttachmentsApi = AttachmentsApi(api_client)
        self.candidates: CandidatesApi = CandidatesApi(api_client)
        self.contractors: ContractorsApi = ContractorsApi(api_client)
        self.contracts: ContractsApi = ContractsApi(api_client)
        self.eor: EORApi = EORApi(api_client)
        self.global_payroll: GlobalPayrollApi = GlobalPayrollApi(api_client)
        self.invoices: InvoicesApi = InvoicesApi(api_client)
        self.lookups: LookupsApi = LookupsApi(api_client)
        self.managers: ManagersApi = ManagersApi(api_client)
        self.milestones: MilestonesApi = MilestonesApi(api_client)
        self.off_cycle_payments: OffCyclePaymentsApi = OffCyclePaymentsApi(api_client)
        self.organizations: OrganizationsApi = OrganizationsApi(api_client)
        self.partner_managed: PartnerManagedApi = PartnerManagedApi(api_client)
        self.people: PeopleApi = PeopleApi(api_client)
        self.service_provider_config: ServiceProviderConfigApi = ServiceProviderConfigApi(api_client)
        self.tasks: TasksApi = TasksApi(api_client)
        self.time_off: TimeOffApi = TimeOffApi(api_client)
        self.timesheets: TimesheetsApi = TimesheetsApi(api_client)
        self.token: TokenApi = TokenApi(api_client)
        self.user: UserApi = UserApi(api_client)
        self.webhooks: WebhooksApi = WebhooksApi(api_client)