from deel_python_sdk.paths.webhooks_id.get import ApiForget
from deel_python_sdk.paths.webhooks_id.delete import ApiFordelete
from deel_python_sdk.paths.webhooks_id.patch import ApiForpatch


class WebhooksId(
    ApiForget,
    ApiFordelete,
    ApiForpatch,
):
    pass
