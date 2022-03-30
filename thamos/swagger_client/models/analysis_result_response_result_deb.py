# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.7.0-dev

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class AnalysisResultResponseResultDeb(object):
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
        'arch': 'str',
        'name': 'str',
        'version': 'str'
    }

    attribute_map = {
        'arch': 'arch',
        'name': 'name',
        'version': 'version'
    }

    def __init__(self, arch=None, name=None, version=None):  # noqa: E501
        """AnalysisResultResponseResultDeb - a model defined in Swagger"""  # noqa: E501
        self._arch = None
        self._name = None
        self._version = None
        self.discriminator = None
        self.arch = arch
        self.name = name
        self.version = version

    @property
    def arch(self):
        """Gets the arch of this AnalysisResultResponseResultDeb.  # noqa: E501

        Package architecture  # noqa: E501

        :return: The arch of this AnalysisResultResponseResultDeb.  # noqa: E501
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this AnalysisResultResponseResultDeb.

        Package architecture  # noqa: E501

        :param arch: The arch of this AnalysisResultResponseResultDeb.  # noqa: E501
        :type: str
        """
        if arch is None:
            raise ValueError("Invalid value for `arch`, must not be `None`")  # noqa: E501

        self._arch = arch

    @property
    def name(self):
        """Gets the name of this AnalysisResultResponseResultDeb.  # noqa: E501

        Name of the Debian package  # noqa: E501

        :return: The name of this AnalysisResultResponseResultDeb.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AnalysisResultResponseResultDeb.

        Name of the Debian package  # noqa: E501

        :param name: The name of this AnalysisResultResponseResultDeb.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this AnalysisResultResponseResultDeb.  # noqa: E501

        Version identifier of the Debian package  # noqa: E501

        :return: The version of this AnalysisResultResponseResultDeb.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this AnalysisResultResponseResultDeb.

        Version identifier of the Debian package  # noqa: E501

        :param version: The version of this AnalysisResultResponseResultDeb.  # noqa: E501
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

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
        if issubclass(AnalysisResultResponseResultDeb, dict):
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
        if not isinstance(other, AnalysisResultResponseResultDeb):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
