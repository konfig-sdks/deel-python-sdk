# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from deel_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PARTNER_MANAGED = "Partner Managed"
    GLOBAL_PAYROLL = "Global Payroll"
    PEOPLE = "People"
    CONTRACTS = "Contracts"
    CONTRACTORS = "Contractors"
    INVOICES = "Invoices"
    TIMESHEETS = "Timesheets"
    TIME_OFF = "Time Off"
    USER = "User"
    EOR = "EOR"
    MILESTONES = "Milestones"
    ORGANIZATIONS = "Organizations"
    ADJUSTMENTS = "Adjustments"
    WEBHOOKS = "Webhooks"
    ACCOUNTING = "Accounting"
    LOOKUPS = "Lookups"
    TASKS = "Tasks"
    OFFCYCLE_PAYMENTS = "Off-cycle Payments"
    CANDIDATES = "Candidates"
    MANAGERS = "Managers"
    TOKEN = "Token"
    ATTACHMENTS = "Attachments"
    SERVICE_PROVIDER_CONFIG = "ServiceProviderConfig"
    HRIS = "Hris"
    LEGAL_ENTITIES = "Legal Entities"
    TEAMS = "Teams"
