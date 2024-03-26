import typing_extensions

from deel_python_sdk.apis.tags import TagValues
from deel_python_sdk.apis.tags.partner_managed_api import PartnerManagedApi
from deel_python_sdk.apis.tags.global_payroll_api import GlobalPayrollApi
from deel_python_sdk.apis.tags.people_api import PeopleApi
from deel_python_sdk.apis.tags.contracts_api import ContractsApi
from deel_python_sdk.apis.tags.contractors_api import ContractorsApi
from deel_python_sdk.apis.tags.invoices_api import InvoicesApi
from deel_python_sdk.apis.tags.timesheets_api import TimesheetsApi
from deel_python_sdk.apis.tags.time_off_api import TimeOffApi
from deel_python_sdk.apis.tags.user_api import UserApi
from deel_python_sdk.apis.tags.eor_api import EORApi
from deel_python_sdk.apis.tags.milestones_api import MilestonesApi
from deel_python_sdk.apis.tags.organizations_api import OrganizationsApi
from deel_python_sdk.apis.tags.adjustments_api import AdjustmentsApi
from deel_python_sdk.apis.tags.webhooks_api import WebhooksApi
from deel_python_sdk.apis.tags.accounting_api import AccountingApi
from deel_python_sdk.apis.tags.lookups_api import LookupsApi
from deel_python_sdk.apis.tags.tasks_api import TasksApi
from deel_python_sdk.apis.tags.off_cycle_payments_api import OffCyclePaymentsApi
from deel_python_sdk.apis.tags.candidates_api import CandidatesApi
from deel_python_sdk.apis.tags.managers_api import ManagersApi
from deel_python_sdk.apis.tags.token_api import TokenApi
from deel_python_sdk.apis.tags.attachments_api import AttachmentsApi
from deel_python_sdk.apis.tags.service_provider_config_api import ServiceProviderConfigApi
from deel_python_sdk.apis.tags.hris_api import HrisApi
from deel_python_sdk.apis.tags.legal_entities_api import LegalEntitiesApi
from deel_python_sdk.apis.tags.teams_api import TeamsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PARTNER_MANAGED: PartnerManagedApi,
        TagValues.GLOBAL_PAYROLL: GlobalPayrollApi,
        TagValues.PEOPLE: PeopleApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.CONTRACTORS: ContractorsApi,
        TagValues.INVOICES: InvoicesApi,
        TagValues.TIMESHEETS: TimesheetsApi,
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.USER: UserApi,
        TagValues.EOR: EORApi,
        TagValues.MILESTONES: MilestonesApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.ADJUSTMENTS: AdjustmentsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.ACCOUNTING: AccountingApi,
        TagValues.LOOKUPS: LookupsApi,
        TagValues.TASKS: TasksApi,
        TagValues.OFFCYCLE_PAYMENTS: OffCyclePaymentsApi,
        TagValues.CANDIDATES: CandidatesApi,
        TagValues.MANAGERS: ManagersApi,
        TagValues.TOKEN: TokenApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.SERVICE_PROVIDER_CONFIG: ServiceProviderConfigApi,
        TagValues.HRIS: HrisApi,
        TagValues.LEGAL_ENTITIES: LegalEntitiesApi,
        TagValues.TEAMS: TeamsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PARTNER_MANAGED: PartnerManagedApi,
        TagValues.GLOBAL_PAYROLL: GlobalPayrollApi,
        TagValues.PEOPLE: PeopleApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.CONTRACTORS: ContractorsApi,
        TagValues.INVOICES: InvoicesApi,
        TagValues.TIMESHEETS: TimesheetsApi,
        TagValues.TIME_OFF: TimeOffApi,
        TagValues.USER: UserApi,
        TagValues.EOR: EORApi,
        TagValues.MILESTONES: MilestonesApi,
        TagValues.ORGANIZATIONS: OrganizationsApi,
        TagValues.ADJUSTMENTS: AdjustmentsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.ACCOUNTING: AccountingApi,
        TagValues.LOOKUPS: LookupsApi,
        TagValues.TASKS: TasksApi,
        TagValues.OFFCYCLE_PAYMENTS: OffCyclePaymentsApi,
        TagValues.CANDIDATES: CandidatesApi,
        TagValues.MANAGERS: ManagersApi,
        TagValues.TOKEN: TokenApi,
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.SERVICE_PROVIDER_CONFIG: ServiceProviderConfigApi,
        TagValues.HRIS: HrisApi,
        TagValues.LEGAL_ENTITIES: LegalEntitiesApi,
        TagValues.TEAMS: TeamsApi,
    }
)
