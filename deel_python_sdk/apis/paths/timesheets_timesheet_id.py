from deel_python_sdk.paths.timesheets_timesheet_id.get import ApiForget
from deel_python_sdk.paths.timesheets_timesheet_id.delete import ApiFordelete
from deel_python_sdk.paths.timesheets_timesheet_id.patch import ApiForpatch


class TimesheetsTimesheetId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
