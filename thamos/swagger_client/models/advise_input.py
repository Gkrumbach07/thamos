# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.6.0-dev

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AdviseInput(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'application_stack': 'PythonStack',
        'constraints': 'str',
        'runtime_environment': 'RuntimeEnvironment',
        'labels': 'object',
        'library_usage': 'AdviseInputLibraryUsage',
        'kebechet_metadata': 'KebechetMetadata',
        'justification': 'Justification',
        'stack_info': 'StackInfo'
    }

    attribute_map = {
        'application_stack': 'application_stack',
        'constraints': 'constraints',
        'runtime_environment': 'runtime_environment',
        'labels': 'labels',
        'library_usage': 'library_usage',
        'kebechet_metadata': 'kebechet_metadata',
        'justification': 'justification',
        'stack_info': 'stack_info'
    }

    def __init__(self, application_stack=None, constraints=None, runtime_environment=None, labels=None, library_usage=None, kebechet_metadata=None, justification=None, stack_info=None):  # noqa: E501
        """AdviseInput - a model defined in Swagger"""  # noqa: E501
        self._application_stack = None
        self._constraints = None
        self._runtime_environment = None
        self._labels = None
        self._library_usage = None
        self._kebechet_metadata = None
        self._justification = None
        self._stack_info = None
        self.discriminator = None
        self.application_stack = application_stack
        if constraints is not None:
            self.constraints = constraints
        if runtime_environment is not None:
            self.runtime_environment = runtime_environment
        if labels is not None:
            self.labels = labels
        if library_usage is not None:
            self.library_usage = library_usage
        if kebechet_metadata is not None:
            self.kebechet_metadata = kebechet_metadata
        if justification is not None:
            self.justification = justification
        if stack_info is not None:
            self.stack_info = stack_info

    @property
    def application_stack(self):
        """Gets the application_stack of this AdviseInput.  # noqa: E501


        :return: The application_stack of this AdviseInput.  # noqa: E501
        :rtype: PythonStack
        """
        return self._application_stack

    @application_stack.setter
    def application_stack(self, application_stack):
        """Sets the application_stack of this AdviseInput.


        :param application_stack: The application_stack of this AdviseInput.  # noqa: E501
        :type: PythonStack
        """
        if application_stack is None:
            raise ValueError("Invalid value for `application_stack`, must not be `None`")  # noqa: E501

        self._application_stack = application_stack

    @property
    def constraints(self):
        """Gets the constraints of this AdviseInput.  # noqa: E501

        Constraints to apply during the resolution.  # noqa: E501

        :return: The constraints of this AdviseInput.  # noqa: E501
        :rtype: str
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this AdviseInput.

        Constraints to apply during the resolution.  # noqa: E501

        :param constraints: The constraints of this AdviseInput.  # noqa: E501
        :type: str
        """

        self._constraints = constraints

    @property
    def runtime_environment(self):
        """Gets the runtime_environment of this AdviseInput.  # noqa: E501


        :return: The runtime_environment of this AdviseInput.  # noqa: E501
        :rtype: RuntimeEnvironment
        """
        return self._runtime_environment

    @runtime_environment.setter
    def runtime_environment(self, runtime_environment):
        """Sets the runtime_environment of this AdviseInput.


        :param runtime_environment: The runtime_environment of this AdviseInput.  # noqa: E501
        :type: RuntimeEnvironment
        """

        self._runtime_environment = runtime_environment

    @property
    def labels(self):
        """Gets the labels of this AdviseInput.  # noqa: E501

        Labels used to label the request.  # noqa: E501

        :return: The labels of this AdviseInput.  # noqa: E501
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this AdviseInput.

        Labels used to label the request.  # noqa: E501

        :param labels: The labels of this AdviseInput.  # noqa: E501
        :type: object
        """

        self._labels = labels

    @property
    def library_usage(self):
        """Gets the library_usage of this AdviseInput.  # noqa: E501


        :return: The library_usage of this AdviseInput.  # noqa: E501
        :rtype: AdviseInputLibraryUsage
        """
        return self._library_usage

    @library_usage.setter
    def library_usage(self, library_usage):
        """Sets the library_usage of this AdviseInput.


        :param library_usage: The library_usage of this AdviseInput.  # noqa: E501
        :type: AdviseInputLibraryUsage
        """

        self._library_usage = library_usage

    @property
    def kebechet_metadata(self):
        """Gets the kebechet_metadata of this AdviseInput.  # noqa: E501


        :return: The kebechet_metadata of this AdviseInput.  # noqa: E501
        :rtype: KebechetMetadata
        """
        return self._kebechet_metadata

    @kebechet_metadata.setter
    def kebechet_metadata(self, kebechet_metadata):
        """Sets the kebechet_metadata of this AdviseInput.


        :param kebechet_metadata: The kebechet_metadata of this AdviseInput.  # noqa: E501
        :type: KebechetMetadata
        """

        self._kebechet_metadata = kebechet_metadata

    @property
    def justification(self):
        """Gets the justification of this AdviseInput.  # noqa: E501


        :return: The justification of this AdviseInput.  # noqa: E501
        :rtype: Justification
        """
        return self._justification

    @justification.setter
    def justification(self, justification):
        """Sets the justification of this AdviseInput.


        :param justification: The justification of this AdviseInput.  # noqa: E501
        :type: Justification
        """

        self._justification = justification

    @property
    def stack_info(self):
        """Gets the stack_info of this AdviseInput.  # noqa: E501


        :return: The stack_info of this AdviseInput.  # noqa: E501
        :rtype: StackInfo
        """
        return self._stack_info

    @stack_info.setter
    def stack_info(self, stack_info):
        """Sets the stack_info of this AdviseInput.


        :param stack_info: The stack_info of this AdviseInput.  # noqa: E501
        :type: StackInfo
        """

        self._stack_info = stack_info

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(AdviseInput, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AdviseInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
