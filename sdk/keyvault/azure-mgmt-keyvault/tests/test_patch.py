# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from azure.mgmt.keyvault import KeyVaultManagementClient
from devtools_testutils import AzureMgmtRecordedTestCase, recorded_by_proxy
from utils import all_api_versions
import pytest


@pytest.mark.live_test_only
class TestKeyVaultManagementPatch(AzureMgmtRecordedTestCase):
    def setup_method(self, method):
        self.client = self.create_mgmt_client(KeyVaultManagementClient)

    @recorded_by_proxy
    def test_list(self):
        api_versions = all_api_versions()
        assert api_versions
        for api_version in api_versions:
            # make sure the client uses api_version we set
            self.client._get_api_version = lambda x: api_version
            response = self.client.vaults.list(
                filter="resourceType eq 'Microsoft.KeyVault/vaults'",
            )
            result = [r for r in response]
            assert result
