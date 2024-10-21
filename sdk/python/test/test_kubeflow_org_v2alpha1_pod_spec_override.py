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
from kubeflow.training.models.kubeflow_org_v2alpha1_pod_spec_override import KubeflowOrgV2alpha1PodSpecOverride  # noqa: E501
from kubeflow.training.rest import ApiException

class TestKubeflowOrgV2alpha1PodSpecOverride(unittest.TestCase):
    """KubeflowOrgV2alpha1PodSpecOverride unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test KubeflowOrgV2alpha1PodSpecOverride
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = kubeflow.training.models.kubeflow_org_v2alpha1_pod_spec_override.KubeflowOrgV2alpha1PodSpecOverride()  # noqa: E501
        if include_optional :
            return KubeflowOrgV2alpha1PodSpecOverride(
                containers = [
                    kubeflow.training.models.kubeflow/org/v2alpha1/container_override.kubeflow.org.v2alpha1.ContainerOverride(
                        args = [
                            '0'
                            ], 
                        command = [
                            '0'
                            ], 
                        env = [
                            None
                            ], 
                        env_from = [
                            None
                            ], 
                        name = '0', 
                        volume_mounts = [
                            None
                            ], )
                    ], 
                init_containers = [
                    kubeflow.training.models.kubeflow/org/v2alpha1/container_override.kubeflow.org.v2alpha1.ContainerOverride(
                        args = [
                            '0'
                            ], 
                        command = [
                            '0'
                            ], 
                        env = [
                            None
                            ], 
                        env_from = [
                            None
                            ], 
                        name = '0', 
                        volume_mounts = [
                            None
                            ], )
                    ], 
                node_selector = {
                    'key' : '0'
                    }, 
                service_account_name = '0', 
                target_jobs = [
                    kubeflow.training.models.kubeflow/org/v2alpha1/pod_spec_override_target_job.kubeflow.org.v2alpha1.PodSpecOverrideTargetJob(
                        name = '0', )
                    ], 
                tolerations = [
                    None
                    ], 
                volumes = [
                    None
                    ]
            )
        else :
            return KubeflowOrgV2alpha1PodSpecOverride(
                target_jobs = [
                    kubeflow.training.models.kubeflow/org/v2alpha1/pod_spec_override_target_job.kubeflow.org.v2alpha1.PodSpecOverrideTargetJob(
                        name = '0', )
                    ],
        )

    def testKubeflowOrgV2alpha1PodSpecOverride(self):
        """Test KubeflowOrgV2alpha1PodSpecOverride"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()