from deel_python_sdk.paths.users_id.get import ApiForget
from deel_python_sdk.paths.users_id.put import ApiForput
from deel_python_sdk.paths.users_id.delete import ApiFordelete
from deel_python_sdk.paths.users_id.patch import ApiForpatch


class UsersId(
    ApiForget,
    ApiForput,
    ApiFordelete,
    ApiForpatch,
):
    pass
