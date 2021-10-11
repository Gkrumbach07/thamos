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


class S2IPythonResponseS2i(object):
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
        'thoth_s2i': 'str',
        'thoth_s2i_image_name': 'str',
        'thoth_s2i_image_version': 'str',
        'analysis_id': 'str'
    }

    attribute_map = {
        'thoth_s2i': 'thoth_s2i',
        'thoth_s2i_image_name': 'thoth_s2i_image_name',
        'thoth_s2i_image_version': 'thoth_s2i_image_version',
        'analysis_id': 'analysis_id'
    }

    def __init__(self, thoth_s2i=None, thoth_s2i_image_name=None, thoth_s2i_image_version=None, analysis_id=None):  # noqa: E501
        """S2IPythonResponseS2i - a model defined in Swagger"""  # noqa: E501
        self._thoth_s2i = None
        self._thoth_s2i_image_name = None
        self._thoth_s2i_image_version = None
        self._analysis_id = None
        self.discriminator = None
        self.thoth_s2i = thoth_s2i
        self.thoth_s2i_image_name = thoth_s2i_image_name
        self.thoth_s2i_image_version = thoth_s2i_image_version
        self.analysis_id = analysis_id

    @property
    def thoth_s2i(self):
        """Gets the thoth_s2i of this S2IPythonResponseS2i.  # noqa: E501

        Full qualifier of Thoth's s2i.  # noqa: E501

        :return: The thoth_s2i of this S2IPythonResponseS2i.  # noqa: E501
        :rtype: str
        """
        return self._thoth_s2i

    @thoth_s2i.setter
    def thoth_s2i(self, thoth_s2i):
        """Sets the thoth_s2i of this S2IPythonResponseS2i.

        Full qualifier of Thoth's s2i.  # noqa: E501

        :param thoth_s2i: The thoth_s2i of this S2IPythonResponseS2i.  # noqa: E501
        :type: str
        """
        if thoth_s2i is None:
            raise ValueError("Invalid value for `thoth_s2i`, must not be `None`")  # noqa: E501

        self._thoth_s2i = thoth_s2i

    @property
    def thoth_s2i_image_name(self):
        """Gets the thoth_s2i_image_name of this S2IPythonResponseS2i.  # noqa: E501

        Name of the Thoth s2i.  # noqa: E501

        :return: The thoth_s2i_image_name of this S2IPythonResponseS2i.  # noqa: E501
        :rtype: str
        """
        return self._thoth_s2i_image_name

    @thoth_s2i_image_name.setter
    def thoth_s2i_image_name(self, thoth_s2i_image_name):
        """Sets the thoth_s2i_image_name of this S2IPythonResponseS2i.

        Name of the Thoth s2i.  # noqa: E501

        :param thoth_s2i_image_name: The thoth_s2i_image_name of this S2IPythonResponseS2i.  # noqa: E501
        :type: str
        """
        if thoth_s2i_image_name is None:
            raise ValueError("Invalid value for `thoth_s2i_image_name`, must not be `None`")  # noqa: E501

        self._thoth_s2i_image_name = thoth_s2i_image_name

    @property
    def thoth_s2i_image_version(self):
        """Gets the thoth_s2i_image_version of this S2IPythonResponseS2i.  # noqa: E501

        Version of the Thoth s2i.  # noqa: E501

        :return: The thoth_s2i_image_version of this S2IPythonResponseS2i.  # noqa: E501
        :rtype: str
        """
        return self._thoth_s2i_image_version

    @thoth_s2i_image_version.setter
    def thoth_s2i_image_version(self, thoth_s2i_image_version):
        """Sets the thoth_s2i_image_version of this S2IPythonResponseS2i.

        Version of the Thoth s2i.  # noqa: E501

        :param thoth_s2i_image_version: The thoth_s2i_image_version of this S2IPythonResponseS2i.  # noqa: E501
        :type: str
        """
        if thoth_s2i_image_version is None:
            raise ValueError("Invalid value for `thoth_s2i_image_version`, must not be `None`")  # noqa: E501

        self._thoth_s2i_image_version = thoth_s2i_image_version

    @property
    def analysis_id(self):
        """Gets the analysis_id of this S2IPythonResponseS2i.  # noqa: E501

        Container image analysis id.  # noqa: E501

        :return: The analysis_id of this S2IPythonResponseS2i.  # noqa: E501
        :rtype: str
        """
        return self._analysis_id

    @analysis_id.setter
    def analysis_id(self, analysis_id):
        """Sets the analysis_id of this S2IPythonResponseS2i.

        Container image analysis id.  # noqa: E501

        :param analysis_id: The analysis_id of this S2IPythonResponseS2i.  # noqa: E501
        :type: str
        """
        if analysis_id is None:
            raise ValueError("Invalid value for `analysis_id`, must not be `None`")  # noqa: E501

        self._analysis_id = analysis_id

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
        if issubclass(S2IPythonResponseS2i, dict):
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
        if not isinstance(other, S2IPythonResponseS2i):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
