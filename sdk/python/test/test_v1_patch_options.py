# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.7.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

from kubeflow.training.models import *
from kubeflow.training.models.v1_patch_options import V1PatchOptions  # noqa: E501
from kubeflow.training.rest import ApiException

class TestV1PatchOptions(unittest.TestCase):
    """V1PatchOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1PatchOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.v1_patch_options.V1PatchOptions()  # noqa: E501
        if include_optional :
            return V1PatchOptions(
                api_version = '0', 
                dry_run = [
                    '0'
                    ], 
                field_manager = '0', 
                field_validation = '0', 
                force = True, 
                kind = '0'
            )
        else :
            return V1PatchOptions(
        )

    def testV1PatchOptions(self):
        """Test V1PatchOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()