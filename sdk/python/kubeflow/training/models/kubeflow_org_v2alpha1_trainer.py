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


class KubeflowOrgV2alpha1Trainer(object):
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
        'args': 'list[str]',
        'command': 'list[str]',
        'env': 'list[V1EnvVar]',
        'image': 'str',
        'num_nodes': 'int',
        'num_proc_per_node': 'str',
        'resources_per_node': 'V1ResourceRequirements'
    }

    attribute_map = {
        'args': 'args',
        'command': 'command',
        'env': 'env',
        'image': 'image',
        'num_nodes': 'numNodes',
        'num_proc_per_node': 'numProcPerNode',
        'resources_per_node': 'resourcesPerNode'
    }

    def __init__(self, args=None, command=None, env=None, image=None, num_nodes=None, num_proc_per_node=None, resources_per_node=None, local_vars_configuration=None):  # noqa: E501
        """KubeflowOrgV2alpha1Trainer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._args = None
        self._command = None
        self._env = None
        self._image = None
        self._num_nodes = None
        self._num_proc_per_node = None
        self._resources_per_node = None
        self.discriminator = None

        if args is not None:
            self.args = args
        if command is not None:
            self.command = command
        if env is not None:
            self.env = env
        if image is not None:
            self.image = image
        if num_nodes is not None:
            self.num_nodes = num_nodes
        if num_proc_per_node is not None:
            self.num_proc_per_node = num_proc_per_node
        if resources_per_node is not None:
            self.resources_per_node = resources_per_node

    @property
    def args(self):
        """Gets the args of this KubeflowOrgV2alpha1Trainer.  # noqa: E501

        Arguments to the entrypoint for the training container.  # noqa: E501

        :return: The args of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :rtype: list[str]
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this KubeflowOrgV2alpha1Trainer.

        Arguments to the entrypoint for the training container.  # noqa: E501

        :param args: The args of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :type: list[str]
        """

        self._args = args

    @property
    def command(self):
        """Gets the command of this KubeflowOrgV2alpha1Trainer.  # noqa: E501

        Entrypoint commands for the training container.  # noqa: E501

        :return: The command of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :rtype: list[str]
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this KubeflowOrgV2alpha1Trainer.

        Entrypoint commands for the training container.  # noqa: E501

        :param command: The command of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :type: list[str]
        """

        self._command = command

    @property
    def env(self):
        """Gets the env of this KubeflowOrgV2alpha1Trainer.  # noqa: E501

        List of environment variables to set in the training container. These values will be merged with the TrainingRuntime's trainer environments.  # noqa: E501

        :return: The env of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :rtype: list[V1EnvVar]
        """
        return self._env

    @env.setter
    def env(self, env):
        """Sets the env of this KubeflowOrgV2alpha1Trainer.

        List of environment variables to set in the training container. These values will be merged with the TrainingRuntime's trainer environments.  # noqa: E501

        :param env: The env of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :type: list[V1EnvVar]
        """

        self._env = env

    @property
    def image(self):
        """Gets the image of this KubeflowOrgV2alpha1Trainer.  # noqa: E501

        Docker image for the training container.  # noqa: E501

        :return: The image of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this KubeflowOrgV2alpha1Trainer.

        Docker image for the training container.  # noqa: E501

        :param image: The image of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :type: str
        """

        self._image = image

    @property
    def num_nodes(self):
        """Gets the num_nodes of this KubeflowOrgV2alpha1Trainer.  # noqa: E501

        Number of training nodes.  # noqa: E501

        :return: The num_nodes of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :rtype: int
        """
        return self._num_nodes

    @num_nodes.setter
    def num_nodes(self, num_nodes):
        """Sets the num_nodes of this KubeflowOrgV2alpha1Trainer.

        Number of training nodes.  # noqa: E501

        :param num_nodes: The num_nodes of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :type: int
        """

        self._num_nodes = num_nodes

    @property
    def num_proc_per_node(self):
        """Gets the num_proc_per_node of this KubeflowOrgV2alpha1Trainer.  # noqa: E501

        Number of processes/workers/slots on every training node. For the Torch runtime: `auto`, `cpu`, `gpu`, or int value can be set. For the MPI runtime only int value can be set.  # noqa: E501

        :return: The num_proc_per_node of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :rtype: str
        """
        return self._num_proc_per_node

    @num_proc_per_node.setter
    def num_proc_per_node(self, num_proc_per_node):
        """Sets the num_proc_per_node of this KubeflowOrgV2alpha1Trainer.

        Number of processes/workers/slots on every training node. For the Torch runtime: `auto`, `cpu`, `gpu`, or int value can be set. For the MPI runtime only int value can be set.  # noqa: E501

        :param num_proc_per_node: The num_proc_per_node of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :type: str
        """

        self._num_proc_per_node = num_proc_per_node

    @property
    def resources_per_node(self):
        """Gets the resources_per_node of this KubeflowOrgV2alpha1Trainer.  # noqa: E501


        :return: The resources_per_node of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :rtype: V1ResourceRequirements
        """
        return self._resources_per_node

    @resources_per_node.setter
    def resources_per_node(self, resources_per_node):
        """Sets the resources_per_node of this KubeflowOrgV2alpha1Trainer.


        :param resources_per_node: The resources_per_node of this KubeflowOrgV2alpha1Trainer.  # noqa: E501
        :type: V1ResourceRequirements
        """

        self._resources_per_node = resources_per_node

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
        if not isinstance(other, KubeflowOrgV2alpha1Trainer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KubeflowOrgV2alpha1Trainer):
            return True

        return self.to_dict() != other.to_dict()