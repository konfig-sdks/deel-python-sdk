import typing_extensions

from deel_python_sdk.paths import PathValues
from deel_python_sdk.apis.paths.invoices import Invoices
from deel_python_sdk.apis.paths.invoices_deel import InvoicesDeel
from deel_python_sdk.apis.paths.invoices_invoice_id_download import InvoicesInvoiceIdDownload
from deel_python_sdk.apis.paths.managers import Managers
from deel_python_sdk.apis.paths.hris_direct_employees import HrisDirectEmployees
from deel_python_sdk.apis.paths.eor_validations_country_code import EorValidationsCountryCode
from deel_python_sdk.apis.paths.eor_workers_worker_id_payslips import EorWorkersWorkerIdPayslips
from deel_python_sdk.apis.paths.eor_workers_worker_id_payslips_payslip_id_download import EorWorkersWorkerIdPayslipsPayslipIdDownload
from deel_python_sdk.apis.paths.eor_employment_cost import EorEmploymentCost
from deel_python_sdk.apis.paths.eor_contract_id_benefits import EorContractIdBenefits
from deel_python_sdk.apis.paths.eor import Eor
from deel_python_sdk.apis.paths.contracts_gp import ContractsGp
from deel_python_sdk.apis.paths.contracts_time_based import ContractsTimeBased
from deel_python_sdk.apis.paths.gp_workers_worker_id_payslips import GpWorkersWorkerIdPayslips
from deel_python_sdk.apis.paths.gp_workers_worker_id_address import GpWorkersWorkerIdAddress
from deel_python_sdk.apis.paths.gp_workers_worker_id_banks import GpWorkersWorkerIdBanks
from deel_python_sdk.apis.paths.gp_workers_worker_id_banks_bank_id import GpWorkersWorkerIdBanksBankId
from deel_python_sdk.apis.paths.gp_workers_worker_id_banks_guide import GpWorkersWorkerIdBanksGuide
from deel_python_sdk.apis.paths.gp_workers_worker_id_compensation import GpWorkersWorkerIdCompensation
from deel_python_sdk.apis.paths.gp_workers_worker_id_pto_policy import GpWorkersWorkerIdPtoPolicy
from deel_python_sdk.apis.paths.gp_workers_worker_id_employee_information import GpWorkersWorkerIdEmployeeInformation
from deel_python_sdk.apis.paths.gp_workers_worker_id_payslips_payslip_id_download import GpWorkersWorkerIdPayslipsPayslipIdDownload
from deel_python_sdk.apis.paths.gp_legal_entities_legal_entity_id_reports import GpLegalEntitiesLegalEntityIdReports
from deel_python_sdk.apis.paths.gp_reports_gp_report_id_gross_to_net import GpReportsGpReportIdGrossToNet
from deel_python_sdk.apis.paths.gp_reports_gp_report_id_gross_to_net_csv import GpReportsGpReportIdGrossToNetCsv
from deel_python_sdk.apis.paths.gp_workers_worker_id_terminations import GpWorkersWorkerIdTerminations
from deel_python_sdk.apis.paths.adjustments import Adjustments
from deel_python_sdk.apis.paths.adjustments_adjustment_id import AdjustmentsAdjustmentId
from deel_python_sdk.apis.paths.adjustments_categories import AdjustmentsCategories
from deel_python_sdk.apis.paths.candidates import Candidates
from deel_python_sdk.apis.paths.candidates_candidate_id import CandidatesCandidateId
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_contracts_contract_id_additional_information import PartnerManagedEmployeesEmployeeIdContractsContractIdAdditionalInformation
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_contracts_contract_id_signatures import PartnerManagedEmployeesEmployeeIdContractsContractIdSignatures
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_contracts_contract_id_custom_verification_letter import PartnerManagedEmployeesEmployeeIdContractsContractIdCustomVerificationLetter
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_contracts_contract_id_hr_documents import PartnerManagedEmployeesEmployeeIdContractsContractIdHrDocuments
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_contracts_contract_id_hr_documents_document_id_download import PartnerManagedEmployeesEmployeeIdContractsContractIdHrDocumentsDocumentIdDownload
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_contracts_contract_id_offer_letter import PartnerManagedEmployeesEmployeeIdContractsContractIdOfferLetter
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_contracts_contract_id_employee_agreement import PartnerManagedEmployeesEmployeeIdContractsContractIdEmployeeAgreement
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_contracts_contract_id_employee_agreement_download import PartnerManagedEmployeesEmployeeIdContractsContractIdEmployeeAgreementDownload
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_banks_guide import PartnerManagedEmployeesEmployeeIdBanksGuide
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_banks import PartnerManagedEmployeesEmployeeIdBanks
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_banks_bank_id import PartnerManagedEmployeesEmployeeIdBanksBankId
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_payslips import PartnerManagedEmployeesEmployeeIdPayslips
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_compliance_documents import PartnerManagedEmployeesEmployeeIdComplianceDocuments
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_compliance_documents_document_id import PartnerManagedEmployeesEmployeeIdComplianceDocumentsDocumentId
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_compliance_documents_document_id_templates_download import PartnerManagedEmployeesEmployeeIdComplianceDocumentsDocumentIdTemplatesDownload
from deel_python_sdk.apis.paths.partner_managed_employees_employee_id_tax_documents import PartnerManagedEmployeesEmployeeIdTaxDocuments
from deel_python_sdk.apis.paths.contracts_task_based import ContractsTaskBased
from deel_python_sdk.apis.paths.contracts_milestone_based import ContractsMilestoneBased
from deel_python_sdk.apis.paths.contracts_fixed_rate import ContractsFixedRate
from deel_python_sdk.apis.paths.contracts import Contracts
from deel_python_sdk.apis.paths.contracts_contract_id import ContractsContractId
from deel_python_sdk.apis.paths.contracts_contract_id_documents import ContractsContractIdDocuments
from deel_python_sdk.apis.paths.contracts_contract_id_preview import ContractsContractIdPreview
from deel_python_sdk.apis.paths.contracts_contract_id_tasks import ContractsContractIdTasks
from deel_python_sdk.apis.paths.contracts_contract_id_alternate_emails import ContractsContractIdAlternateEmails
from deel_python_sdk.apis.paths.contracts_contract_id_tasks_many_reviews import ContractsContractIdTasksManyReviews
from deel_python_sdk.apis.paths.contracts_contract_id_tasks_task_id_reviews import ContractsContractIdTasksTaskIdReviews
from deel_python_sdk.apis.paths.contracts_contract_id_tasks_task_id import ContractsContractIdTasksTaskId
from deel_python_sdk.apis.paths.contracts_contract_id_amendments import ContractsContractIdAmendments
from deel_python_sdk.apis.paths.contracts_contract_id_terminations import ContractsContractIdTerminations
from deel_python_sdk.apis.paths.contracts_contract_id_signatures import ContractsContractIdSignatures
from deel_python_sdk.apis.paths.contracts_contract_id_archive import ContractsContractIdArchive
from deel_python_sdk.apis.paths.contracts_contract_id_invitations import ContractsContractIdInvitations
from deel_python_sdk.apis.paths.contracts_contract_id_timesheets import ContractsContractIdTimesheets
from deel_python_sdk.apis.paths.contracts_contract_id_milestones import ContractsContractIdMilestones
from deel_python_sdk.apis.paths.contracts_contract_id_milestones_milestone_id import ContractsContractIdMilestonesMilestoneId
from deel_python_sdk.apis.paths.contracts_contract_id_milestones_milestone_id_reviews import ContractsContractIdMilestonesMilestoneIdReviews
from deel_python_sdk.apis.paths.contracts_contract_id_milestones_many_reviews import ContractsContractIdMilestonesManyReviews
from deel_python_sdk.apis.paths.contracts_contract_id_off_cycle_payments import ContractsContractIdOffCyclePayments
from deel_python_sdk.apis.paths.contracts_contract_id_off_cycle_payments_offcycle_payment_id import ContractsContractIdOffCyclePaymentsOffcyclePaymentId
from deel_python_sdk.apis.paths.contracts_contract_id_premium import ContractsContractIdPremium
from deel_python_sdk.apis.paths.contracts_contract_id_final_payments import ContractsContractIdFinalPayments
from deel_python_sdk.apis.paths.contracts_estimate import ContractsEstimate
from deel_python_sdk.apis.paths.contracts_contract_id_time_offs import ContractsContractIdTimeOffs
from deel_python_sdk.apis.paths.contracts_contract_id_time_offs_timeoff_id import ContractsContractIdTimeOffsTimeoffId
from deel_python_sdk.apis.paths.timesheets import Timesheets
from deel_python_sdk.apis.paths.timesheets_timesheet_id import TimesheetsTimesheetId
from deel_python_sdk.apis.paths.timesheets_timesheet_id_reviews import TimesheetsTimesheetIdReviews
from deel_python_sdk.apis.paths.timesheets_many_reviews import TimesheetsManyReviews
from deel_python_sdk.apis.paths.contracts_contract_id_invoice_adjustments import ContractsContractIdInvoiceAdjustments
from deel_python_sdk.apis.paths.invoice_adjustments import InvoiceAdjustments
from deel_python_sdk.apis.paths.invoice_adjustments_invoice_adjustment_id import InvoiceAdjustmentsInvoiceAdjustmentId
from deel_python_sdk.apis.paths.invoice_adjustments_invoice_adjustment_id_reviews import InvoiceAdjustmentsInvoiceAdjustmentIdReviews
from deel_python_sdk.apis.paths.invoice_adjustments_many_reviews import InvoiceAdjustmentsManyReviews
from deel_python_sdk.apis.paths.invoice_adjustments_invoice_adjustment_id_attachment import InvoiceAdjustmentsInvoiceAdjustmentIdAttachment
from deel_python_sdk.apis.paths.legal_entities import LegalEntities
from deel_python_sdk.apis.paths.lookups_countries import LookupsCountries
from deel_python_sdk.apis.paths.lookups_currencies import LookupsCurrencies
from deel_python_sdk.apis.paths.lookups_job_titles import LookupsJobTitles
from deel_python_sdk.apis.paths.lookups_seniorities import LookupsSeniorities
from deel_python_sdk.apis.paths.lookups_time_off_types import LookupsTimeOffTypes
from deel_python_sdk.apis.paths.organizations import Organizations
from deel_python_sdk.apis.paths.teams import Teams
from deel_python_sdk.apis.paths.attachments import Attachments
from deel_python_sdk.apis.paths.agreements import Agreements
from deel_python_sdk.apis.paths.contract_templates import ContractTemplates
from deel_python_sdk.apis.paths.contracts_contract_id_entitlements import ContractsContractIdEntitlements
from deel_python_sdk.apis.paths.contracts_contract_id_adjustments import ContractsContractIdAdjustments
from deel_python_sdk.apis.paths.time_offs_timeoff_id_review import TimeOffsTimeoffIdReview
from deel_python_sdk.apis.paths.payments import Payments
from deel_python_sdk.apis.paths.internal_people import InternalPeople
from deel_python_sdk.apis.paths.people import People
from deel_python_sdk.apis.paths.people_worker_id import PeopleWorkerId
from deel_python_sdk.apis.paths.people_worker_id_department import PeopleWorkerIdDepartment
from deel_python_sdk.apis.paths.people_worker_id_working_location import PeopleWorkerIdWorkingLocation
from deel_python_sdk.apis.paths.people_me import PeopleMe
from deel_python_sdk.apis.paths.people_worker_id_time_offs import PeopleWorkerIdTimeOffs
from deel_python_sdk.apis.paths.people_worker_id_time_offs_entitlements import PeopleWorkerIdTimeOffsEntitlements
from deel_python_sdk.apis.paths.people_worker_id_time_offs_timeoff_id import PeopleWorkerIdTimeOffsTimeoffId
from deel_python_sdk.apis.paths.people_worker_id_time_offs_timeoff_id_review import PeopleWorkerIdTimeOffsTimeoffIdReview
from deel_python_sdk.apis.paths.people_worker_id_time_offs_policies import PeopleWorkerIdTimeOffsPolicies
from deel_python_sdk.apis.paths.webhooks import Webhooks
from deel_python_sdk.apis.paths.webhooks_id import WebhooksId
from deel_python_sdk.apis.paths.webhooks_events_types import WebhooksEventsTypes
from deel_python_sdk.apis.paths.payments_payment_id_breakdown import PaymentsPaymentIdBreakdown
from deel_python_sdk.apis.paths.departments import Departments
from deel_python_sdk.apis.paths.working_locations import WorkingLocations
from deel_python_sdk.apis.paths.public_tokens import PublicTokens
from deel_python_sdk.apis.paths.service_provider_config import ServiceProviderConfig
from deel_python_sdk.apis.paths.users import Users
from deel_python_sdk.apis.paths.users__search import UsersSearch
from deel_python_sdk.apis.paths.users_id import UsersId
from deel_python_sdk.apis.paths.time_offs import TimeOffs

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.INVOICES: Invoices,
        PathValues.INVOICES_DEEL: InvoicesDeel,
        PathValues.INVOICES_INVOICE_ID_DOWNLOAD: InvoicesInvoiceIdDownload,
        PathValues.MANAGERS: Managers,
        PathValues.HRIS_DIRECTEMPLOYEES: HrisDirectEmployees,
        PathValues.EOR_VALIDATIONS_COUNTRY_CODE: EorValidationsCountryCode,
        PathValues.EOR_WORKERS_WORKER_ID_PAYSLIPS: EorWorkersWorkerIdPayslips,
        PathValues.EOR_WORKERS_WORKER_ID_PAYSLIPS_PAYSLIP_ID_DOWNLOAD: EorWorkersWorkerIdPayslipsPayslipIdDownload,
        PathValues.EOR_EMPLOYMENT_COST: EorEmploymentCost,
        PathValues.EOR_CONTRACT_ID_BENEFITS: EorContractIdBenefits,
        PathValues.EOR: Eor,
        PathValues.CONTRACTS_GP: ContractsGp,
        PathValues.CONTRACTS_TIMEBASED: ContractsTimeBased,
        PathValues.GP_WORKERS_WORKER_ID_PAYSLIPS: GpWorkersWorkerIdPayslips,
        PathValues.GP_WORKERS_WORKER_ID_ADDRESS: GpWorkersWorkerIdAddress,
        PathValues.GP_WORKERS_WORKER_ID_BANKS: GpWorkersWorkerIdBanks,
        PathValues.GP_WORKERS_WORKER_ID_BANKS_BANK_ID: GpWorkersWorkerIdBanksBankId,
        PathValues.GP_WORKERS_WORKER_ID_BANKS_GUIDE: GpWorkersWorkerIdBanksGuide,
        PathValues.GP_WORKERS_WORKER_ID_COMPENSATION: GpWorkersWorkerIdCompensation,
        PathValues.GP_WORKERS_WORKER_ID_PTOPOLICY: GpWorkersWorkerIdPtoPolicy,
        PathValues.GP_WORKERS_WORKER_ID_EMPLOYEEINFORMATION: GpWorkersWorkerIdEmployeeInformation,
        PathValues.GP_WORKERS_WORKER_ID_PAYSLIPS_PAYSLIP_ID_DOWNLOAD: GpWorkersWorkerIdPayslipsPayslipIdDownload,
        PathValues.GP_LEGALENTITIES_LEGAL_ENTITY_ID_REPORTS: GpLegalEntitiesLegalEntityIdReports,
        PathValues.GP_REPORTS_GP_REPORT_ID_GROSS_TO_NET: GpReportsGpReportIdGrossToNet,
        PathValues.GP_REPORTS_GP_REPORT_ID_GROSS_TO_NET_CSV: GpReportsGpReportIdGrossToNetCsv,
        PathValues.GP_WORKERS_WORKER_ID_TERMINATIONS: GpWorkersWorkerIdTerminations,
        PathValues.ADJUSTMENTS: Adjustments,
        PathValues.ADJUSTMENTS_ADJUSTMENT_ID: AdjustmentsAdjustmentId,
        PathValues.ADJUSTMENTS_CATEGORIES: AdjustmentsCategories,
        PathValues.CANDIDATES: Candidates,
        PathValues.CANDIDATES_CANDIDATE_ID: CandidatesCandidateId,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_ADDITIONALINFORMATION: PartnerManagedEmployeesEmployeeIdContractsContractIdAdditionalInformation,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_SIGNATURES: PartnerManagedEmployeesEmployeeIdContractsContractIdSignatures,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_CUSTOMVERIFICATIONLETTER: PartnerManagedEmployeesEmployeeIdContractsContractIdCustomVerificationLetter,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_HRDOCUMENTS: PartnerManagedEmployeesEmployeeIdContractsContractIdHrDocuments,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_HRDOCUMENTS_DOCUMENT_ID_DOWNLOAD: PartnerManagedEmployeesEmployeeIdContractsContractIdHrDocumentsDocumentIdDownload,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_OFFERLETTER: PartnerManagedEmployeesEmployeeIdContractsContractIdOfferLetter,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_EMPLOYEEAGREEMENT: PartnerManagedEmployeesEmployeeIdContractsContractIdEmployeeAgreement,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_EMPLOYEEAGREEMENT_DOWNLOAD: PartnerManagedEmployeesEmployeeIdContractsContractIdEmployeeAgreementDownload,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_BANKS_GUIDE: PartnerManagedEmployeesEmployeeIdBanksGuide,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_BANKS: PartnerManagedEmployeesEmployeeIdBanks,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_BANKS_BANK_ID: PartnerManagedEmployeesEmployeeIdBanksBankId,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_PAYSLIPS: PartnerManagedEmployeesEmployeeIdPayslips,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_COMPLIANCEDOCUMENTS: PartnerManagedEmployeesEmployeeIdComplianceDocuments,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_COMPLIANCEDOCUMENTS_DOCUMENT_ID: PartnerManagedEmployeesEmployeeIdComplianceDocumentsDocumentId,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_COMPLIANCEDOCUMENTS_DOCUMENT_ID_TEMPLATES_DOWNLOAD: PartnerManagedEmployeesEmployeeIdComplianceDocumentsDocumentIdTemplatesDownload,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_TAXDOCUMENTS: PartnerManagedEmployeesEmployeeIdTaxDocuments,
        PathValues.CONTRACTS_TASKBASED: ContractsTaskBased,
        PathValues.CONTRACTS_MILESTONEBASED: ContractsMilestoneBased,
        PathValues.CONTRACTS_FIXEDRATE: ContractsFixedRate,
        PathValues.CONTRACTS: Contracts,
        PathValues.CONTRACTS_CONTRACT_ID: ContractsContractId,
        PathValues.CONTRACTS_CONTRACT_ID_DOCUMENTS: ContractsContractIdDocuments,
        PathValues.CONTRACTS_CONTRACT_ID_PREVIEW: ContractsContractIdPreview,
        PathValues.CONTRACTS_CONTRACT_ID_TASKS: ContractsContractIdTasks,
        PathValues.CONTRACTS_CONTRACT_ID_ALTERNATE_EMAILS: ContractsContractIdAlternateEmails,
        PathValues.CONTRACTS_CONTRACT_ID_TASKS_MANY_REVIEWS: ContractsContractIdTasksManyReviews,
        PathValues.CONTRACTS_CONTRACT_ID_TASKS_TASK_ID_REVIEWS: ContractsContractIdTasksTaskIdReviews,
        PathValues.CONTRACTS_CONTRACT_ID_TASKS_TASK_ID: ContractsContractIdTasksTaskId,
        PathValues.CONTRACTS_CONTRACT_ID_AMENDMENTS: ContractsContractIdAmendments,
        PathValues.CONTRACTS_CONTRACT_ID_TERMINATIONS: ContractsContractIdTerminations,
        PathValues.CONTRACTS_CONTRACT_ID_SIGNATURES: ContractsContractIdSignatures,
        PathValues.CONTRACTS_CONTRACT_ID_ARCHIVE: ContractsContractIdArchive,
        PathValues.CONTRACTS_CONTRACT_ID_INVITATIONS: ContractsContractIdInvitations,
        PathValues.CONTRACTS_CONTRACT_ID_TIMESHEETS: ContractsContractIdTimesheets,
        PathValues.CONTRACTS_CONTRACT_ID_MILESTONES: ContractsContractIdMilestones,
        PathValues.CONTRACTS_CONTRACT_ID_MILESTONES_MILESTONE_ID: ContractsContractIdMilestonesMilestoneId,
        PathValues.CONTRACTS_CONTRACT_ID_MILESTONES_MILESTONE_ID_REVIEWS: ContractsContractIdMilestonesMilestoneIdReviews,
        PathValues.CONTRACTS_CONTRACT_ID_MILESTONES_MANY_REVIEWS: ContractsContractIdMilestonesManyReviews,
        PathValues.CONTRACTS_CONTRACT_ID_OFFCYCLEPAYMENTS: ContractsContractIdOffCyclePayments,
        PathValues.CONTRACTS_CONTRACT_ID_OFFCYCLEPAYMENTS_OFFCYCLE_PAYMENT_ID: ContractsContractIdOffCyclePaymentsOffcyclePaymentId,
        PathValues.CONTRACTS_CONTRACT_ID_PREMIUM: ContractsContractIdPremium,
        PathValues.CONTRACTS_CONTRACT_ID_FINALPAYMENTS: ContractsContractIdFinalPayments,
        PathValues.CONTRACTS_ESTIMATE: ContractsEstimate,
        PathValues.CONTRACTS_CONTRACT_ID_TIMEOFFS: ContractsContractIdTimeOffs,
        PathValues.CONTRACTS_CONTRACT_ID_TIMEOFFS_TIMEOFF_ID: ContractsContractIdTimeOffsTimeoffId,
        PathValues.TIMESHEETS: Timesheets,
        PathValues.TIMESHEETS_TIMESHEET_ID: TimesheetsTimesheetId,
        PathValues.TIMESHEETS_TIMESHEET_ID_REVIEWS: TimesheetsTimesheetIdReviews,
        PathValues.TIMESHEETS_MANY_REVIEWS: TimesheetsManyReviews,
        PathValues.CONTRACTS_CONTRACT_ID_INVOICEADJUSTMENTS: ContractsContractIdInvoiceAdjustments,
        PathValues.INVOICEADJUSTMENTS: InvoiceAdjustments,
        PathValues.INVOICEADJUSTMENTS_INVOICE_ADJUSTMENT_ID: InvoiceAdjustmentsInvoiceAdjustmentId,
        PathValues.INVOICEADJUSTMENTS_INVOICE_ADJUSTMENT_ID_REVIEWS: InvoiceAdjustmentsInvoiceAdjustmentIdReviews,
        PathValues.INVOICEADJUSTMENTS_MANY_REVIEWS: InvoiceAdjustmentsManyReviews,
        PathValues.INVOICEADJUSTMENTS_INVOICE_ADJUSTMENT_ID_ATTACHMENT: InvoiceAdjustmentsInvoiceAdjustmentIdAttachment,
        PathValues.LEGALENTITIES: LegalEntities,
        PathValues.LOOKUPS_COUNTRIES: LookupsCountries,
        PathValues.LOOKUPS_CURRENCIES: LookupsCurrencies,
        PathValues.LOOKUPS_JOBTITLES: LookupsJobTitles,
        PathValues.LOOKUPS_SENIORITIES: LookupsSeniorities,
        PathValues.LOOKUPS_TIMEOFFTYPES: LookupsTimeOffTypes,
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.TEAMS: Teams,
        PathValues.ATTACHMENTS: Attachments,
        PathValues.AGREEMENTS: Agreements,
        PathValues.CONTRACTTEMPLATES: ContractTemplates,
        PathValues.CONTRACTS_CONTRACT_ID_ENTITLEMENTS: ContractsContractIdEntitlements,
        PathValues.CONTRACTS_CONTRACT_ID_ADJUSTMENTS: ContractsContractIdAdjustments,
        PathValues.TIMEOFFS_TIMEOFF_ID_REVIEW: TimeOffsTimeoffIdReview,
        PathValues.PAYMENTS: Payments,
        PathValues.INTERNAL_PEOPLE: InternalPeople,
        PathValues.PEOPLE: People,
        PathValues.PEOPLE_WORKER_ID: PeopleWorkerId,
        PathValues.PEOPLE_WORKER_ID_DEPARTMENT: PeopleWorkerIdDepartment,
        PathValues.PEOPLE_WORKER_ID_WORKINGLOCATION: PeopleWorkerIdWorkingLocation,
        PathValues.PEOPLE_ME: PeopleMe,
        PathValues.PEOPLE_WORKER_ID_TIMEOFFS: PeopleWorkerIdTimeOffs,
        PathValues.PEOPLE_WORKER_ID_TIMEOFFS_ENTITLEMENTS: PeopleWorkerIdTimeOffsEntitlements,
        PathValues.PEOPLE_WORKER_ID_TIMEOFFS_TIMEOFF_ID: PeopleWorkerIdTimeOffsTimeoffId,
        PathValues.PEOPLE_WORKER_ID_TIMEOFFS_TIMEOFF_ID_REVIEW: PeopleWorkerIdTimeOffsTimeoffIdReview,
        PathValues.PEOPLE_WORKER_ID_TIMEOFFS_POLICIES: PeopleWorkerIdTimeOffsPolicies,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_ID: WebhooksId,
        PathValues.WEBHOOKS_EVENTS_TYPES: WebhooksEventsTypes,
        PathValues.PAYMENTS_PAYMENT_ID_BREAKDOWN: PaymentsPaymentIdBreakdown,
        PathValues.DEPARTMENTS: Departments,
        PathValues.WORKINGLOCATIONS: WorkingLocations,
        PathValues.PUBLICTOKENS: PublicTokens,
        PathValues.SERVICE_PROVIDER_CONFIG: ServiceProviderConfig,
        PathValues.USERS: Users,
        PathValues.USERS__SEARCH: UsersSearch,
        PathValues.USERS_ID: UsersId,
        PathValues.TIMEOFFS: TimeOffs,
    }
)

path_to_api = PathToApi(
    {
        PathValues.INVOICES: Invoices,
        PathValues.INVOICES_DEEL: InvoicesDeel,
        PathValues.INVOICES_INVOICE_ID_DOWNLOAD: InvoicesInvoiceIdDownload,
        PathValues.MANAGERS: Managers,
        PathValues.HRIS_DIRECTEMPLOYEES: HrisDirectEmployees,
        PathValues.EOR_VALIDATIONS_COUNTRY_CODE: EorValidationsCountryCode,
        PathValues.EOR_WORKERS_WORKER_ID_PAYSLIPS: EorWorkersWorkerIdPayslips,
        PathValues.EOR_WORKERS_WORKER_ID_PAYSLIPS_PAYSLIP_ID_DOWNLOAD: EorWorkersWorkerIdPayslipsPayslipIdDownload,
        PathValues.EOR_EMPLOYMENT_COST: EorEmploymentCost,
        PathValues.EOR_CONTRACT_ID_BENEFITS: EorContractIdBenefits,
        PathValues.EOR: Eor,
        PathValues.CONTRACTS_GP: ContractsGp,
        PathValues.CONTRACTS_TIMEBASED: ContractsTimeBased,
        PathValues.GP_WORKERS_WORKER_ID_PAYSLIPS: GpWorkersWorkerIdPayslips,
        PathValues.GP_WORKERS_WORKER_ID_ADDRESS: GpWorkersWorkerIdAddress,
        PathValues.GP_WORKERS_WORKER_ID_BANKS: GpWorkersWorkerIdBanks,
        PathValues.GP_WORKERS_WORKER_ID_BANKS_BANK_ID: GpWorkersWorkerIdBanksBankId,
        PathValues.GP_WORKERS_WORKER_ID_BANKS_GUIDE: GpWorkersWorkerIdBanksGuide,
        PathValues.GP_WORKERS_WORKER_ID_COMPENSATION: GpWorkersWorkerIdCompensation,
        PathValues.GP_WORKERS_WORKER_ID_PTOPOLICY: GpWorkersWorkerIdPtoPolicy,
        PathValues.GP_WORKERS_WORKER_ID_EMPLOYEEINFORMATION: GpWorkersWorkerIdEmployeeInformation,
        PathValues.GP_WORKERS_WORKER_ID_PAYSLIPS_PAYSLIP_ID_DOWNLOAD: GpWorkersWorkerIdPayslipsPayslipIdDownload,
        PathValues.GP_LEGALENTITIES_LEGAL_ENTITY_ID_REPORTS: GpLegalEntitiesLegalEntityIdReports,
        PathValues.GP_REPORTS_GP_REPORT_ID_GROSS_TO_NET: GpReportsGpReportIdGrossToNet,
        PathValues.GP_REPORTS_GP_REPORT_ID_GROSS_TO_NET_CSV: GpReportsGpReportIdGrossToNetCsv,
        PathValues.GP_WORKERS_WORKER_ID_TERMINATIONS: GpWorkersWorkerIdTerminations,
        PathValues.ADJUSTMENTS: Adjustments,
        PathValues.ADJUSTMENTS_ADJUSTMENT_ID: AdjustmentsAdjustmentId,
        PathValues.ADJUSTMENTS_CATEGORIES: AdjustmentsCategories,
        PathValues.CANDIDATES: Candidates,
        PathValues.CANDIDATES_CANDIDATE_ID: CandidatesCandidateId,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_ADDITIONALINFORMATION: PartnerManagedEmployeesEmployeeIdContractsContractIdAdditionalInformation,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_SIGNATURES: PartnerManagedEmployeesEmployeeIdContractsContractIdSignatures,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_CUSTOMVERIFICATIONLETTER: PartnerManagedEmployeesEmployeeIdContractsContractIdCustomVerificationLetter,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_HRDOCUMENTS: PartnerManagedEmployeesEmployeeIdContractsContractIdHrDocuments,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_HRDOCUMENTS_DOCUMENT_ID_DOWNLOAD: PartnerManagedEmployeesEmployeeIdContractsContractIdHrDocumentsDocumentIdDownload,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_OFFERLETTER: PartnerManagedEmployeesEmployeeIdContractsContractIdOfferLetter,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_EMPLOYEEAGREEMENT: PartnerManagedEmployeesEmployeeIdContractsContractIdEmployeeAgreement,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_CONTRACTS_CONTRACT_ID_EMPLOYEEAGREEMENT_DOWNLOAD: PartnerManagedEmployeesEmployeeIdContractsContractIdEmployeeAgreementDownload,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_BANKS_GUIDE: PartnerManagedEmployeesEmployeeIdBanksGuide,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_BANKS: PartnerManagedEmployeesEmployeeIdBanks,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_BANKS_BANK_ID: PartnerManagedEmployeesEmployeeIdBanksBankId,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_PAYSLIPS: PartnerManagedEmployeesEmployeeIdPayslips,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_COMPLIANCEDOCUMENTS: PartnerManagedEmployeesEmployeeIdComplianceDocuments,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_COMPLIANCEDOCUMENTS_DOCUMENT_ID: PartnerManagedEmployeesEmployeeIdComplianceDocumentsDocumentId,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_COMPLIANCEDOCUMENTS_DOCUMENT_ID_TEMPLATES_DOWNLOAD: PartnerManagedEmployeesEmployeeIdComplianceDocumentsDocumentIdTemplatesDownload,
        PathValues.PARTNERMANAGED_EMPLOYEES_EMPLOYEE_ID_TAXDOCUMENTS: PartnerManagedEmployeesEmployeeIdTaxDocuments,
        PathValues.CONTRACTS_TASKBASED: ContractsTaskBased,
        PathValues.CONTRACTS_MILESTONEBASED: ContractsMilestoneBased,
        PathValues.CONTRACTS_FIXEDRATE: ContractsFixedRate,
        PathValues.CONTRACTS: Contracts,
        PathValues.CONTRACTS_CONTRACT_ID: ContractsContractId,
        PathValues.CONTRACTS_CONTRACT_ID_DOCUMENTS: ContractsContractIdDocuments,
        PathValues.CONTRACTS_CONTRACT_ID_PREVIEW: ContractsContractIdPreview,
        PathValues.CONTRACTS_CONTRACT_ID_TASKS: ContractsContractIdTasks,
        PathValues.CONTRACTS_CONTRACT_ID_ALTERNATE_EMAILS: ContractsContractIdAlternateEmails,
        PathValues.CONTRACTS_CONTRACT_ID_TASKS_MANY_REVIEWS: ContractsContractIdTasksManyReviews,
        PathValues.CONTRACTS_CONTRACT_ID_TASKS_TASK_ID_REVIEWS: ContractsContractIdTasksTaskIdReviews,
        PathValues.CONTRACTS_CONTRACT_ID_TASKS_TASK_ID: ContractsContractIdTasksTaskId,
        PathValues.CONTRACTS_CONTRACT_ID_AMENDMENTS: ContractsContractIdAmendments,
        PathValues.CONTRACTS_CONTRACT_ID_TERMINATIONS: ContractsContractIdTerminations,
        PathValues.CONTRACTS_CONTRACT_ID_SIGNATURES: ContractsContractIdSignatures,
        PathValues.CONTRACTS_CONTRACT_ID_ARCHIVE: ContractsContractIdArchive,
        PathValues.CONTRACTS_CONTRACT_ID_INVITATIONS: ContractsContractIdInvitations,
        PathValues.CONTRACTS_CONTRACT_ID_TIMESHEETS: ContractsContractIdTimesheets,
        PathValues.CONTRACTS_CONTRACT_ID_MILESTONES: ContractsContractIdMilestones,
        PathValues.CONTRACTS_CONTRACT_ID_MILESTONES_MILESTONE_ID: ContractsContractIdMilestonesMilestoneId,
        PathValues.CONTRACTS_CONTRACT_ID_MILESTONES_MILESTONE_ID_REVIEWS: ContractsContractIdMilestonesMilestoneIdReviews,
        PathValues.CONTRACTS_CONTRACT_ID_MILESTONES_MANY_REVIEWS: ContractsContractIdMilestonesManyReviews,
        PathValues.CONTRACTS_CONTRACT_ID_OFFCYCLEPAYMENTS: ContractsContractIdOffCyclePayments,
        PathValues.CONTRACTS_CONTRACT_ID_OFFCYCLEPAYMENTS_OFFCYCLE_PAYMENT_ID: ContractsContractIdOffCyclePaymentsOffcyclePaymentId,
        PathValues.CONTRACTS_CONTRACT_ID_PREMIUM: ContractsContractIdPremium,
        PathValues.CONTRACTS_CONTRACT_ID_FINALPAYMENTS: ContractsContractIdFinalPayments,
        PathValues.CONTRACTS_ESTIMATE: ContractsEstimate,
        PathValues.CONTRACTS_CONTRACT_ID_TIMEOFFS: ContractsContractIdTimeOffs,
        PathValues.CONTRACTS_CONTRACT_ID_TIMEOFFS_TIMEOFF_ID: ContractsContractIdTimeOffsTimeoffId,
        PathValues.TIMESHEETS: Timesheets,
        PathValues.TIMESHEETS_TIMESHEET_ID: TimesheetsTimesheetId,
        PathValues.TIMESHEETS_TIMESHEET_ID_REVIEWS: TimesheetsTimesheetIdReviews,
        PathValues.TIMESHEETS_MANY_REVIEWS: TimesheetsManyReviews,
        PathValues.CONTRACTS_CONTRACT_ID_INVOICEADJUSTMENTS: ContractsContractIdInvoiceAdjustments,
        PathValues.INVOICEADJUSTMENTS: InvoiceAdjustments,
        PathValues.INVOICEADJUSTMENTS_INVOICE_ADJUSTMENT_ID: InvoiceAdjustmentsInvoiceAdjustmentId,
        PathValues.INVOICEADJUSTMENTS_INVOICE_ADJUSTMENT_ID_REVIEWS: InvoiceAdjustmentsInvoiceAdjustmentIdReviews,
        PathValues.INVOICEADJUSTMENTS_MANY_REVIEWS: InvoiceAdjustmentsManyReviews,
        PathValues.INVOICEADJUSTMENTS_INVOICE_ADJUSTMENT_ID_ATTACHMENT: InvoiceAdjustmentsInvoiceAdjustmentIdAttachment,
        PathValues.LEGALENTITIES: LegalEntities,
        PathValues.LOOKUPS_COUNTRIES: LookupsCountries,
        PathValues.LOOKUPS_CURRENCIES: LookupsCurrencies,
        PathValues.LOOKUPS_JOBTITLES: LookupsJobTitles,
        PathValues.LOOKUPS_SENIORITIES: LookupsSeniorities,
        PathValues.LOOKUPS_TIMEOFFTYPES: LookupsTimeOffTypes,
        PathValues.ORGANIZATIONS: Organizations,
        PathValues.TEAMS: Teams,
        PathValues.ATTACHMENTS: Attachments,
        PathValues.AGREEMENTS: Agreements,
        PathValues.CONTRACTTEMPLATES: ContractTemplates,
        PathValues.CONTRACTS_CONTRACT_ID_ENTITLEMENTS: ContractsContractIdEntitlements,
        PathValues.CONTRACTS_CONTRACT_ID_ADJUSTMENTS: ContractsContractIdAdjustments,
        PathValues.TIMEOFFS_TIMEOFF_ID_REVIEW: TimeOffsTimeoffIdReview,
        PathValues.PAYMENTS: Payments,
        PathValues.INTERNAL_PEOPLE: InternalPeople,
        PathValues.PEOPLE: People,
        PathValues.PEOPLE_WORKER_ID: PeopleWorkerId,
        PathValues.PEOPLE_WORKER_ID_DEPARTMENT: PeopleWorkerIdDepartment,
        PathValues.PEOPLE_WORKER_ID_WORKINGLOCATION: PeopleWorkerIdWorkingLocation,
        PathValues.PEOPLE_ME: PeopleMe,
        PathValues.PEOPLE_WORKER_ID_TIMEOFFS: PeopleWorkerIdTimeOffs,
        PathValues.PEOPLE_WORKER_ID_TIMEOFFS_ENTITLEMENTS: PeopleWorkerIdTimeOffsEntitlements,
        PathValues.PEOPLE_WORKER_ID_TIMEOFFS_TIMEOFF_ID: PeopleWorkerIdTimeOffsTimeoffId,
        PathValues.PEOPLE_WORKER_ID_TIMEOFFS_TIMEOFF_ID_REVIEW: PeopleWorkerIdTimeOffsTimeoffIdReview,
        PathValues.PEOPLE_WORKER_ID_TIMEOFFS_POLICIES: PeopleWorkerIdTimeOffsPolicies,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_ID: WebhooksId,
        PathValues.WEBHOOKS_EVENTS_TYPES: WebhooksEventsTypes,
        PathValues.PAYMENTS_PAYMENT_ID_BREAKDOWN: PaymentsPaymentIdBreakdown,
        PathValues.DEPARTMENTS: Departments,
        PathValues.WORKINGLOCATIONS: WorkingLocations,
        PathValues.PUBLICTOKENS: PublicTokens,
        PathValues.SERVICE_PROVIDER_CONFIG: ServiceProviderConfig,
        PathValues.USERS: Users,
        PathValues.USERS__SEARCH: UsersSearch,
        PathValues.USERS_ID: UsersId,
        PathValues.TIMEOFFS: TimeOffs,
    }
)
