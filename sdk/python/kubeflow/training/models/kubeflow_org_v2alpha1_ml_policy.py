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


class KubeflowOrgV2alpha1MLPolicy(object):
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
        'mpi': 'KubeflowOrgV2alpha1MPIMLPolicySource',
        'num_nodes': 'int',
        'torch': 'KubeflowOrgV2alpha1TorchMLPolicySource'
    }

    attribute_map = {
        'mpi': 'mpi',
        'num_nodes': 'numNodes',
        'torch': 'torch'
    }

    def __init__(self, mpi=None, num_nodes=None, torch=None, local_vars_configuration=None):  # noqa: E501
        """KubeflowOrgV2alpha1MLPolicy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mpi = None
        self._num_nodes = None
        self._torch = None
        self.discriminator = None

        if mpi is not None:
            self.mpi = mpi
        if num_nodes is not None:
            self.num_nodes = num_nodes
        if torch is not None:
            self.torch = torch

    @property
    def mpi(self):
        """Gets the mpi of this KubeflowOrgV2alpha1MLPolicy.  # noqa: E501


        :return: The mpi of this KubeflowOrgV2alpha1MLPolicy.  # noqa: E501
        :rtype: KubeflowOrgV2alpha1MPIMLPolicySource
        """
        return self._mpi

    @mpi.setter
    def mpi(self, mpi):
        """Sets the mpi of this KubeflowOrgV2alpha1MLPolicy.


        :param mpi: The mpi of this KubeflowOrgV2alpha1MLPolicy.  # noqa: E501
        :type: KubeflowOrgV2alpha1MPIMLPolicySource
        """

        self._mpi = mpi

    @property
    def num_nodes(self):
        """Gets the num_nodes of this KubeflowOrgV2alpha1MLPolicy.  # noqa: E501

        Number of training nodes. Defaults to 1.  # noqa: E501

        :return: The num_nodes of this KubeflowOrgV2alpha1MLPolicy.  # noqa: E501
        :rtype: int
        """
        return self._num_nodes

    @num_nodes.setter
    def num_nodes(self, num_nodes):
        """Sets the num_nodes of this KubeflowOrgV2alpha1MLPolicy.

        Number of training nodes. Defaults to 1.  # noqa: E501

        :param num_nodes: The num_nodes of this KubeflowOrgV2alpha1MLPolicy.  # noqa: E501
        :type: int
        """

        self._num_nodes = num_nodes

    @property
    def torch(self):
        """Gets the torch of this KubeflowOrgV2alpha1MLPolicy.  # noqa: E501


        :return: The torch of this KubeflowOrgV2alpha1MLPolicy.  # noqa: E501
        :rtype: KubeflowOrgV2alpha1TorchMLPolicySource
        """
        return self._torch

    @torch.setter
    def torch(self, torch):
        """Sets the torch of this KubeflowOrgV2alpha1MLPolicy.


        :param torch: The torch of this KubeflowOrgV2alpha1MLPolicy.  # noqa: E501
        :type: KubeflowOrgV2alpha1TorchMLPolicySource
        """

        self._torch = torch

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
        if not isinstance(other, KubeflowOrgV2alpha1MLPolicy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubeflowOrgV2alpha1MLPolicy):
            return True

        return self.to_dict() != other.to_dict()
