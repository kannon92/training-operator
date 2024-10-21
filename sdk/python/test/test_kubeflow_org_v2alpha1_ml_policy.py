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
from kubeflow.training.models.kubeflow_org_v2alpha1_ml_policy import KubeflowOrgV2alpha1MLPolicy  # noqa: E501
from kubeflow.training.rest import ApiException

class TestKubeflowOrgV2alpha1MLPolicy(unittest.TestCase):
    """KubeflowOrgV2alpha1MLPolicy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubeflowOrgV2alpha1MLPolicy
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.kubeflow_org_v2alpha1_ml_policy.KubeflowOrgV2alpha1MLPolicy()  # noqa: E501
        if include_optional :
            return KubeflowOrgV2alpha1MLPolicy(
                mpi = kubeflow.training.models.kubeflow/org/v2alpha1/mpiml_policy_source.kubeflow.org.v2alpha1.MPIMLPolicySource(
                    ssh_auth_mount_path = '0', 
                    mpi_implementation = '0', 
                    num_proc_per_node = 56, 
                    run_launcher_as_node = True, ), 
                num_nodes = 56, 
                torch = kubeflow.training.models.kubeflow/org/v2alpha1/torch_ml_policy_source.kubeflow.org.v2alpha1.TorchMLPolicySource(
                    elastic_policy = kubeflow.training.models.kubeflow/org/v2alpha1/torch_elastic_policy.kubeflow.org.v2alpha1.TorchElasticPolicy(
                        max_nodes = 56, 
                        max_restarts = 56, 
                        metrics = [
                            None
                            ], 
                        min_nodes = 56, ), 
                    num_proc_per_node = '0', )
            )
        else :
            return KubeflowOrgV2alpha1MLPolicy(
        )

    def testKubeflowOrgV2alpha1MLPolicy(self):
        """Test KubeflowOrgV2alpha1MLPolicy"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()