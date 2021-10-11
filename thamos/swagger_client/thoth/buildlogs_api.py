# coding: utf-8

"""
    Thoth User API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 0.6.0-dev
   
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from thamos.swagger_client.api_client import ApiClient


class BuildlogsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_buildlog(self, document_id, **kwargs):  # noqa: E501
        """Retrieve the given build log.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_buildlog(document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_id: Build log to be retrieved. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_buildlog_with_http_info(document_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_buildlog_with_http_info(document_id, **kwargs)  # noqa: E501
            return data

    def get_buildlog_with_http_info(self, document_id, **kwargs):  # noqa: E501
        """Retrieve the given build log.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_buildlog_with_http_info(document_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str document_id: Build log to be retrieved. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['document_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_buildlog" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'document_id' is set
        if ('document_id' not in params or
                params['document_id'] is None):
            raise ValueError("Missing the required parameter `document_id` when calling `get_buildlog`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'document_id' in params:
            path_params['document_id'] = params['document_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/buildlog/{document_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
