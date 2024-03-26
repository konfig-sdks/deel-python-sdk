# coding: utf-8

"""
    Deel REST API

    API specification for Deel HR user provisioning API. This YAML file is a preview of the API Deel is building. We are looking forward to your feedback.

    The version of the OpenAPI document: 1.25.0
    Contact: apiteam@deel.com
    Generated by: https://konfigthis.com
"""

from deel_python_sdk.paths.invoices_deel.get import GetDeelInvoicesRaw
from deel_python_sdk.paths.invoices_invoice_id_download.get import GetInvoicePdfDownloadLinkRaw
from deel_python_sdk.paths.invoices.get import GetPaidInvoicesRaw
from deel_python_sdk.paths.payments_payment_id_breakdown.get import GetPaymentBreakdownRaw
from deel_python_sdk.paths.payments.get import GetPaymentReceiptsRaw


class AccountingApiRaw(
    GetDeelInvoicesRaw,
    GetInvoicePdfDownloadLinkRaw,
    GetPaidInvoicesRaw,
    GetPaymentBreakdownRaw,
    GetPaymentReceiptsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass