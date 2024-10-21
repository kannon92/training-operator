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
from kubeflow.training.models.v1_api_resource import V1APIResource  # noqa: E501
from kubeflow.training.rest import ApiException

class TestV1APIResource(unittest.TestCase):
    """V1APIResource unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1APIResource
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.v1_api_resource.V1APIResource()  # noqa: E501
        if include_optional :
            return V1APIResource(
                categories = [
                    '0'
                    ], 
                group = '0', 
                kind = '0', 
                name = '0', 
                namespaced = True, 
                short_names = [
                    '0'
                    ], 
                singular_name = '0', 
                storage_version_hash = '0', 
                verbs = [
                    '0'
                    ], 
                version = '0'
            )
        else :
            return V1APIResource(
                kind = '0',
                name = '0',
                namespaced = True,
                singular_name = '0',
                verbs = [
                    '0'
                    ],
        )

    def testV1APIResource(self):
        """Test V1APIResource"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()