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

class PythonPackageVersionsResponseVersions(object):
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
        'package_name': 'str',
        'package_version': 'str',
        'index_url': 'str'
    }

    attribute_map = {
        'package_name': 'package_name',
        'package_version': 'package_version',
        'index_url': 'index_url'
    }

    def __init__(self, package_name=None, package_version=None, index_url=None):  # noqa: E501
        """PythonPackageVersionsResponseVersions - a model defined in Swagger"""  # noqa: E501
        self._package_name = None
        self._package_version = None
        self._index_url = None
        self.discriminator = None
        self.package_name = package_name
        self.package_version = package_version
        self.index_url = index_url

    @property
    def package_name(self):
        """Gets the package_name of this PythonPackageVersionsResponseVersions.  # noqa: E501

        Name of the package.  # noqa: E501

        :return: The package_name of this PythonPackageVersionsResponseVersions.  # noqa: E501
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        """Sets the package_name of this PythonPackageVersionsResponseVersions.

        Name of the package.  # noqa: E501

        :param package_name: The package_name of this PythonPackageVersionsResponseVersions.  # noqa: E501
        :type: str
        """
        if package_name is None:
            raise ValueError("Invalid value for `package_name`, must not be `None`")  # noqa: E501

        self._package_name = package_name

    @property
    def package_version(self):
        """Gets the package_version of this PythonPackageVersionsResponseVersions.  # noqa: E501

        Version of the package.  # noqa: E501

        :return: The package_version of this PythonPackageVersionsResponseVersions.  # noqa: E501
        :rtype: str
        """
        return self._package_version

    @package_version.setter
    def package_version(self, package_version):
        """Sets the package_version of this PythonPackageVersionsResponseVersions.

        Version of the package.  # noqa: E501

        :param package_version: The package_version of this PythonPackageVersionsResponseVersions.  # noqa: E501
        :type: str
        """
        if package_version is None:
            raise ValueError("Invalid value for `package_version`, must not be `None`")  # noqa: E501

        self._package_version = package_version

    @property
    def index_url(self):
        """Gets the index_url of this PythonPackageVersionsResponseVersions.  # noqa: E501

        Source index URL of the package.  # noqa: E501

        :return: The index_url of this PythonPackageVersionsResponseVersions.  # noqa: E501
        :rtype: str
        """
        return self._index_url

    @index_url.setter
    def index_url(self, index_url):
        """Sets the index_url of this PythonPackageVersionsResponseVersions.

        Source index URL of the package.  # noqa: E501

        :param index_url: The index_url of this PythonPackageVersionsResponseVersions.  # noqa: E501
        :type: str
        """
        if index_url is None:
            raise ValueError("Invalid value for `index_url`, must not be `None`")  # noqa: E501

        self._index_url = index_url

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
        if issubclass(PythonPackageVersionsResponseVersions, dict):
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
        if not isinstance(other, PythonPackageVersionsResponseVersions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
