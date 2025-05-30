# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
from ._access_control_client import KeyVaultAccessControlClient
from ._backup_client import KeyVaultBackupClient
from ._enums import KeyVaultRoleScope, KeyVaultDataAction, KeyVaultSettingType
from ._internal.client_base import ApiVersion
from ._models import (
    KeyVaultBackupOperation,
    KeyVaultBackupResult,
    KeyVaultPermission,
    KeyVaultRestoreOperation,
    KeyVaultRoleAssignment,
    KeyVaultRoleAssignmentProperties,
    KeyVaultRoleDefinition,
    KeyVaultSetting,
)
from ._settings_client import KeyVaultSettingsClient


__all__ = [
    "ApiVersion",
    "KeyVaultBackupOperation",
    "KeyVaultBackupResult",
    "KeyVaultAccessControlClient",
    "KeyVaultBackupClient",
    "KeyVaultDataAction",
    "KeyVaultPermission",
    "KeyVaultRestoreOperation",
    "KeyVaultRoleAssignment",
    "KeyVaultRoleAssignmentProperties",
    "KeyVaultRoleDefinition",
    "KeyVaultRoleScope",
    "KeyVaultSetting",
    "KeyVaultSettingsClient",
    "KeyVaultSettingType",
]

from ._version import VERSION
__version__ = VERSION
