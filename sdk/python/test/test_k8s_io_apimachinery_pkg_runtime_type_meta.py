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
from kubeflow.training.models.k8s_io_apimachinery_pkg_runtime_type_meta import K8sIoApimachineryPkgRuntimeTypeMeta  # noqa: E501
from kubeflow.training.rest import ApiException

class TestK8sIoApimachineryPkgRuntimeTypeMeta(unittest.TestCase):
    """K8sIoApimachineryPkgRuntimeTypeMeta unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test K8sIoApimachineryPkgRuntimeTypeMeta
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.k8s_io_apimachinery_pkg_runtime_type_meta.K8sIoApimachineryPkgRuntimeTypeMeta()  # noqa: E501
        if include_optional :
            return K8sIoApimachineryPkgRuntimeTypeMeta(
                api_version = '0', 
                kind = '0'
            )
        else :
            return K8sIoApimachineryPkgRuntimeTypeMeta(
        )

    def testK8sIoApimachineryPkgRuntimeTypeMeta(self):
        """Test K8sIoApimachineryPkgRuntimeTypeMeta"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()