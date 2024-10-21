# coding: utf-8

"""
    Kubeflow Training SDK

    Python SDK for Kubeflow Training  # noqa: E501

    The version of the OpenAPI document: v1.7.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubeflow.training.configuration import Configuration


class KubeflowOrgV2alpha1TrainJobStatus(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'conditions': 'list[V1Condition]',
        'jobs_status': 'list[KubeflowOrgV2alpha1JobStatus]'
    }

    attribute_map = {
        'conditions': 'conditions',
        'jobs_status': 'jobsStatus'
    }

    def __init__(self, conditions=None, jobs_status=None, local_vars_configuration=None):  # noqa: E501
        """KubeflowOrgV2alpha1TrainJobStatus - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._conditions = None
        self._jobs_status = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if jobs_status is not None:
            self.jobs_status = jobs_status

    @property
    def conditions(self):
        """Gets the conditions of this KubeflowOrgV2alpha1TrainJobStatus.  # noqa: E501

        Conditions for the TrainJob.  # noqa: E501

        :return: The conditions of this KubeflowOrgV2alpha1TrainJobStatus.  # noqa: E501
        :rtype: list[V1Condition]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this KubeflowOrgV2alpha1TrainJobStatus.

        Conditions for the TrainJob.  # noqa: E501

        :param conditions: The conditions of this KubeflowOrgV2alpha1TrainJobStatus.  # noqa: E501
        :type: list[V1Condition]
        """

        self._conditions = conditions

    @property
    def jobs_status(self):
        """Gets the jobs_status of this KubeflowOrgV2alpha1TrainJobStatus.  # noqa: E501

        JobsStatus tracks the child Jobs in TrainJob.  # noqa: E501

        :return: The jobs_status of this KubeflowOrgV2alpha1TrainJobStatus.  # noqa: E501
        :rtype: list[KubeflowOrgV2alpha1JobStatus]
        """
        return self._jobs_status

    @jobs_status.setter
    def jobs_status(self, jobs_status):
        """Sets the jobs_status of this KubeflowOrgV2alpha1TrainJobStatus.

        JobsStatus tracks the child Jobs in TrainJob.  # noqa: E501

        :param jobs_status: The jobs_status of this KubeflowOrgV2alpha1TrainJobStatus.  # noqa: E501
        :type: list[KubeflowOrgV2alpha1JobStatus]
        """

        self._jobs_status = jobs_status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KubeflowOrgV2alpha1TrainJobStatus):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubeflowOrgV2alpha1TrainJobStatus):
            return True

        return self.to_dict() != other.to_dict()