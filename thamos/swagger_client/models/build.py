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


class Build(object):
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
        'base_image': 'str',
        'output_image': 'str',
        'build_log': 'BuildBuildLog'
    }

    attribute_map = {
        'base_image': 'base_image',
        'output_image': 'output_image',
        'build_log': 'build_log'
    }

    def __init__(self, base_image=None, output_image=None, build_log=None):  # noqa: E501
        """Build - a model defined in Swagger"""  # noqa: E501
        self._base_image = None
        self._output_image = None
        self._build_log = None
        self.discriminator = None
        if base_image is not None:
            self.base_image = base_image
        if output_image is not None:
            self.output_image = output_image
        if build_log is not None:
            self.build_log = build_log

    @property
    def base_image(self):
        """Gets the base_image of this Build.  # noqa: E501

        Name of base image used by the s2i build.   # noqa: E501

        :return: The base_image of this Build.  # noqa: E501
        :rtype: str
        """
        return self._base_image

    @base_image.setter
    def base_image(self, base_image):
        """Sets the base_image of this Build.

        Name of base image used by the s2i build.   # noqa: E501

        :param base_image: The base_image of this Build.  # noqa: E501
        :type: str
        """

        self._base_image = base_image

    @property
    def output_image(self):
        """Gets the output_image of this Build.  # noqa: E501

        Name of output image - can also specify remote registry to pull image from.   # noqa: E501

        :return: The output_image of this Build.  # noqa: E501
        :rtype: str
        """
        return self._output_image

    @output_image.setter
    def output_image(self, output_image):
        """Sets the output_image of this Build.

        Name of output image - can also specify remote registry to pull image from.   # noqa: E501

        :param output_image: The output_image of this Build.  # noqa: E501
        :type: str
        """

        self._output_image = output_image

    @property
    def build_log(self):
        """Gets the build_log of this Build.  # noqa: E501


        :return: The build_log of this Build.  # noqa: E501
        :rtype: BuildBuildLog
        """
        return self._build_log

    @build_log.setter
    def build_log(self, build_log):
        """Sets the build_log of this Build.


        :param build_log: The build_log of this Build.  # noqa: E501
        :type: BuildBuildLog
        """

        self._build_log = build_log

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
        if issubclass(Build, dict):
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
        if not isinstance(other, Build):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
