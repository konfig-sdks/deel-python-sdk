operation_parameter_map = {
    '/invoices/deel-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/invoices/{invoice_id}/download-GET': {
        'parameters': [
            {
                'name': 'invoice_id'
            },
        ]
    },
    '/invoices-GET': {
        'parameters': [
            {
                'name': 'issued_from_date'
            },
            {
                'name': 'issued_to_date'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/payments/{payment_id}/breakdown-GET': {
        'parameters': [
            {
                'name': 'payment_id'
            },
        ]
    },
    '/payments-GET': {
        'parameters': [
            {
                'name': 'date_from'
            },
            {
                'name': 'date_to'
            },
            {
                'name': 'currencies'
            },
            {
                'name': 'entities'
            },
        ]
    },
    '/adjustments-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/contracts/{contract_id}/adjustments-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'from'
            },
            {
                'name': 'to'
            },
        ]
    },
    '/adjustments/{adjustment_id}-GET': {
        'parameters': [
            {
                'name': 'adjustment_id'
            },
        ]
    },
    '/adjustments/categories-GET': {
        'parameters': [
        ]
    },
    '/adjustments/{adjustment_id}-DELETE': {
        'parameters': [
            {
                'name': 'adjustment_id'
            },
        ]
    },
    '/adjustments/{adjustment_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'adjustment_id'
            },
        ]
    },
    '/attachments-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/candidates-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/candidates/{candidate_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'candidate_id'
            },
        ]
    },
    '/contracts/{contract_id}/amendments-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/contracts/fixed-rate-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/contracts/milestone-based-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/contracts/task-based-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/contracts/time-based-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/contracts/{contract_id}/preview-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'templateId'
            },
        ]
    },
    '/contracts/{contract_id}/premium-DELETE': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/contracts/{contract_id}/terminations-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/premium-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/archive-PATCH': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/documents-POST': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/contracts/{contract_id}/final-payments-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'calculation_type'
            },
            {
                'name': 'workweek_start'
            },
            {
                'name': 'workweek_end'
            },
        ]
    },
    '/contracts/estimate-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/contracts/{contract_id}/signatures-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/documents-PUT': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/contracts/{contract_id}/alternate_emails-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts-GET': {
        'parameters': [
            {
                'name': 'after_cursor'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'order_direction'
            },
            {
                'name': 'types'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'countries'
            },
            {
                'name': 'currencies'
            },
            {
                'name': 'search'
            },
            {
                'name': 'sort_by'
            },
        ]
    },
    '/contract-templates-GET': {
        'parameters': [
        ]
    },
    '/contracts/{contract_id}-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/invitations-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/invitations-DELETE': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/eor/employment_cost-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/eor-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/eor/{contract_id}/benefits-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/eor/validations/{country_code}-GET': {
        'parameters': [
            {
                'name': 'country_code'
            },
        ]
    },
    '/eor/workers/{worker_id}/payslips-GET': {
        'parameters': [
            {
                'name': 'worker_id'
            },
        ]
    },
    '/eor/workers/{worker_id}/payslips/{payslip_id}/download-GET': {
        'parameters': [
            {
                'name': 'worker_id'
            },
            {
                'name': 'payslip_id'
            },
        ]
    },
    '/gp/workers/{worker_id}/banks-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'worker_id'
            },
        ]
    },
    '/contracts/gp-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/gp/reports/{gp_report_id}/gross_to_net/csv-GET': {
        'parameters': [
            {
                'name': 'gp_report_id'
            },
        ]
    },
    '/gp/workers/{worker_id}/banks-GET': {
        'parameters': [
            {
                'name': 'worker_id'
            },
        ]
    },
    '/gp/workers/{worker_id}/banks/guide-GET': {
        'parameters': [
            {
                'name': 'worker_id'
            },
        ]
    },
    '/gp/reports/{gp_report_id}/gross_to_net-GET': {
        'parameters': [
            {
                'name': 'gp_report_id'
            },
        ]
    },
    '/gp/workers/{worker_id}/payslips/{payslip_id}/download-GET': {
        'parameters': [
            {
                'name': 'worker_id'
            },
            {
                'name': 'payslip_id'
            },
        ]
    },
    '/gp/workers/{worker_id}/payslips-GET': {
        'parameters': [
            {
                'name': 'worker_id'
            },
        ]
    },
    '/gp/legal-entities/{legal_entity_id}/reports-GET': {
        'parameters': [
            {
                'name': 'legal_entity_id'
            },
            {
                'name': 'start_date'
            },
        ]
    },
    '/gp/workers/{worker_id}/banks/{bank_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'worker_id'
            },
            {
                'name': 'bank_id'
            },
        ]
    },
    '/gp/workers/{worker_id}/terminations-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'worker_id'
            },
        ]
    },
    '/gp/workers/{worker_id}/compensation-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'worker_id'
            },
        ]
    },
    '/gp/workers/{worker_id}/employee-information-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'worker_id'
            },
        ]
    },
    '/gp/workers/{worker_id}/pto-policy-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'worker_id'
            },
        ]
    },
    '/gp/workers/{worker_id}/address-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'worker_id'
            },
        ]
    },
    '/invoice-adjustments-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'recurring'
            },
        ]
    },
    '/invoice-adjustments/{invoice_adjustment_id}-DELETE': {
        'parameters': [
            {
                'name': 'invoice_adjustment_id'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/invoice-adjustments/{invoice_adjustment_id}/attachment-GET': {
        'parameters': [
            {
                'name': 'invoice_adjustment_id'
            },
        ]
    },
    '/contracts/{contract_id}/invoice-adjustments-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'contract_types'
            },
            {
                'name': 'types'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'invoice_id'
            },
            {
                'name': 'reporter_id'
            },
            {
                'name': 'date_from'
            },
            {
                'name': 'date_to'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/invoice-adjustments-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'contract_types'
            },
            {
                'name': 'types'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'invoice_id'
            },
            {
                'name': 'reporter_id'
            },
            {
                'name': 'date_from'
            },
            {
                'name': 'date_to'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/invoice-adjustments/many/reviews-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/invoice-adjustments/{invoice_adjustment_id}/reviews-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'invoice_adjustment_id'
            },
        ]
    },
    '/invoice-adjustments/{invoice_adjustment_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'invoice_adjustment_id'
            },
        ]
    },
    '/lookups/countries-GET': {
        'parameters': [
        ]
    },
    '/lookups/currencies-GET': {
        'parameters': [
        ]
    },
    '/lookups/job-titles-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'after_cursor'
            },
        ]
    },
    '/lookups/seniorities-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
        ]
    },
    '/lookups/time-off-types-GET': {
        'parameters': [
        ]
    },
    '/managers-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/managers-GET': {
        'parameters': [
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/contracts/{contract_id}/milestones-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/milestones/{milestone_id}/reviews-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
            {
                'name': 'milestone_id'
            },
        ]
    },
    '/contracts/{contract_id}/milestones/{milestone_id}-DELETE': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'milestone_id'
            },
        ]
    },
    '/contracts/{contract_id}/milestones/{milestone_id}-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'milestone_id'
            },
        ]
    },
    '/contracts/{contract_id}/milestones-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/milestones/many/reviews-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/off-cycle-payments-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/off-cycle-payments-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/off-cycle-payments/{offcycle_payment_id}-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'offcycle_payment_id'
            },
        ]
    },
    '/departments-GET': {
        'parameters': [
        ]
    },
    '/organizations-GET': {
        'parameters': [
        ]
    },
    '/legal-entities-GET': {
        'parameters': [
            {
                'name': 'type'
            },
        ]
    },
    '/teams-GET': {
        'parameters': [
        ]
    },
    '/working-locations-GET': {
        'parameters': [
        ]
    },
    '/agreements-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/contracts/{contract_id}/additional-information-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/banks-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'employee_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/compliance-documents/{document_id}/templates/download-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'document_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/contracts/{contract_id}/employee-agreement/download-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/contracts/{contract_id}/hr-documents/{document_id}/download-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'contract_id'
            },
            {
                'name': 'document_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/banks/guide-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/contracts/{contract_id}/employee-agreement-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/compliance-documents-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/contracts/{contract_id}/hr-documents-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/payslips-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/tax-documents-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/banks/{bank_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'bank_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/contracts/{contract_id}/offer-letter-GET': {
        'parameters': [
            {
                'name': 'employee_id'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/contracts/{contract_id}/custom-verification-letter-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/contracts/{contract_id}/signatures-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/partner-managed/employees/{employee_id}/compliance-documents/{document_id}-POST': {
        'parameters': [
            {
                'name': 'file'
            },
            {
                'name': 'employee_id'
            },
            {
                'name': 'document_id'
            },
        ]
    },
    '/people/{worker_id}/time-offs-POST': {
        'parameters': [
            {
                'name': 'type'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'worker_id'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/hris/direct-employees-POST': {
        'parameters': [
            {
                'name': 'employee_details'
            },
            {
                'name': 'team_information'
            },
            {
                'name': 'job_information'
            },
            {
                'name': 'compensation'
            },
            {
                'name': 'contract'
            },
            {
                'name': 'vacation_info'
            },
        ]
    },
    '/people/{worker_id}/time-offs/{timeoff_id}-DELETE': {
        'parameters': [
            {
                'name': 'timeoff_id'
            },
            {
                'name': 'worker_id'
            },
        ]
    },
    '/people/{worker_id}/time-offs/{timeoff_id}-PATCH': {
        'parameters': [
            {
                'name': 'timeoff_id'
            },
            {
                'name': 'worker_id'
            },
            {
                'name': 'type'
            },
            {
                'name': 'start_date'
            },
            {
                'name': 'end_date'
            },
            {
                'name': 'reason'
            },
            {
                'name': 'attachments'
            },
        ]
    },
    '/people/me-GET': {
        'parameters': [
        ]
    },
    '/internal/people-GET': {
        'parameters': [
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/people-GET': {
        'parameters': [
            {
                'name': 'offset'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'search'
            },
            {
                'name': 'sort_by'
            },
            {
                'name': 'sort_order'
            },
            {
                'name': 'hiring_statuses[]'
            },
        ]
    },
    '/people/{worker_id}-GET': {
        'parameters': [
            {
                'name': 'worker_id'
            },
        ]
    },
    '/people/{worker_id}/time-offs/entitlements-GET': {
        'parameters': [
            {
                'name': 'worker_id'
            },
        ]
    },
    '/people/{worker_id}/time-offs/policies-GET': {
        'parameters': [
            {
                'name': 'worker_id'
            },
        ]
    },
    '/people/{worker_id}/time-offs-GET': {
        'parameters': [
            {
                'name': 'worker_id'
            },
        ]
    },
    '/people/{worker_id}/time-offs/{timeoff_id}/review-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'timeoff_id'
            },
            {
                'name': 'worker_id'
            },
        ]
    },
    '/people/{worker_id}/department-PUT': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'worker_id'
            },
        ]
    },
    '/people/{worker_id}/working-location-PUT': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'worker_id'
            },
        ]
    },
    '/ServiceProviderConfig-GET': {
        'parameters': [
        ]
    },
    '/contracts/{contract_id}/tasks-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/tasks/{task_id}-DELETE': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'task_id'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/contracts/{contract_id}/tasks-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/tasks/many/reviews-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/tasks/{task_id}/reviews-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
            {
                'name': 'task_id'
            },
        ]
    },
    '/contracts/{contract_id}/time-offs-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/time-offs/{timeoff_id}-DELETE': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'timeoff_id'
            },
        ]
    },
    '/contracts/{contract_id}/time-offs/{timeoff_id}-PUT': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'contract_id'
            },
            {
                'name': 'timeoff_id'
            },
        ]
    },
    '/time-offs-GET': {
        'parameters': [
        ]
    },
    '/lookups/time-off-types-GET': {
        'parameters': [
        ]
    },
    '/contracts/{contract_id}/time-offs-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/contracts/{contract_id}/entitlements-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
        ]
    },
    '/time-offs/{timeoff_id}/review-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'timeoff_id'
            },
        ]
    },
    '/timesheets/{timesheet_id}-DELETE': {
        'parameters': [
            {
                'name': 'timesheet_id'
            },
            {
                'name': 'reason'
            },
        ]
    },
    '/timesheets-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'contract_types'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'reporter_id'
            },
            {
                'name': 'date_from'
            },
            {
                'name': 'date_to'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/timesheets/{timesheet_id}-GET': {
        'parameters': [
            {
                'name': 'timesheet_id'
            },
        ]
    },
    '/contracts/{contract_id}/timesheets-GET': {
        'parameters': [
            {
                'name': 'contract_id'
            },
            {
                'name': 'contract_types'
            },
            {
                'name': 'statuses'
            },
            {
                'name': 'reporter_id'
            },
            {
                'name': 'date_from'
            },
            {
                'name': 'date_to'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/timesheets/many/reviews-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/timesheets/{timesheet_id}/reviews-POST': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'timesheet_id'
            },
        ]
    },
    '/timesheets-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/timesheets/{timesheet_id}-PATCH': {
        'parameters': [
            {
                'name': 'data'
            },
            {
                'name': 'timesheet_id'
            },
        ]
    },
    '/public-tokens-POST': {
        'parameters': [
            {
                'name': 'data'
            },
        ]
    },
    '/Users-POST': {
        'parameters': [
            {
                'name': 'schemas'
            },
            {
                'name': 'userName'
            },
            {
                'name': 'name'
            },
            {
                'name': 'userType'
            },
        ]
    },
    '/Users/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/Users/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/Users-GET': {
        'parameters': [
            {
                'name': 'filter'
            },
            {
                'name': 'startIndex'
            },
            {
                'name': 'count'
            },
        ]
    },
    '/Users/{id}-PATCH': {
        'parameters': [
            {
                'name': 'Operations'
            },
            {
                'name': 'schemas'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/Users/.search-POST': {
        'parameters': [
            {
                'name': 'count'
            },
            {
                'name': 'filter'
            },
            {
                'name': 'schemas'
            },
            {
                'name': 'startIndex'
            },
        ]
    },
    '/Users/{id}-PUT': {
        'parameters': [
            {
                'name': 'emails'
            },
            {
                'name': 'name'
            },
            {
                'name': 'schemas'
            },
            {
                'name': 'userName'
            },
            {
                'name': 'meta'
            },
            {
                'name': 'id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'active'
            },
            {
                'name': 'userType'
            },
            {
                'name': 'id'
            },
            {
                'name': 'urn:ietf:params:scim:schemas:extension:enterprise:2.0:User'
            },
            {
                'name': 'urn:ietf:params:scim:schemas:extension:2.0:User'
            },
        ]
    },
    '/webhooks-POST': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'url'
            },
            {
                'name': 'signing_key'
            },
            {
                'name': 'api_version'
            },
            {
                'name': 'events'
            },
        ]
    },
    '/webhooks/{id}-DELETE': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/webhooks/{id}-PATCH': {
        'parameters': [
            {
                'name': 'description'
            },
            {
                'name': 'name'
            },
            {
                'name': 'status'
            },
            {
                'name': 'url'
            },
            {
                'name': 'signing_key'
            },
            {
                'name': 'events'
            },
            {
                'name': 'id'
            },
            {
                'name': 'api_version'
            },
        ]
    },
    '/webhooks/{id}-GET': {
        'parameters': [
            {
                'name': 'id'
            },
        ]
    },
    '/webhooks/events/types-GET': {
        'parameters': [
        ]
    },
    '/webhooks-GET': {
        'parameters': [
        ]
    },
};