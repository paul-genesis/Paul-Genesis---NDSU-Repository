# coding: utf-8

"""
    data.world API

    # data.world in a nutshell  data.world is a productive, secure platform for modern data teamwork.  We bring together your data practitioners, subject matter experts, and other stakeholders by removing costly barriers to data discovery, comprehension, integration, and sharing.   Everything your team needs to quickly understand and use data stays with it.   Social features and integrations encourage collaborators to ask and answer questions, share discoveries, and coordinate closely while still using their preferred tools.  Our focus on interoperability helps you enhance your own data with data from any source, including our vast and growing library of free public datasets.   Sophisticated permissions, auditing features, and more make it easy to manage who views your data and what they do with it.  # Conventions  ## Authentication  All data.world API calls require an API token.   OAuth2 is the preferred and most secure method for authenticating users of your data.world applications. Visit our [oauth documentation](https://apidocs.data.world/toolkit/oauth) for additional information. Alternatively, you can obtain a token for _personal use or testing_ by navigating to your profile settings, under the Advanced tab ([https://data.world/settings/advanced](https://data.world/settings/advanced)).  Authentication must be provided in API requests via the `Authorization` header. For example, for a user whose API token is `my_api_token`, the request header should be `Authorization: Bearer my_api_token` (note the `Bearer` prefix).  ## Content type   By default, `application/json` is the content type used in request and response bodies. Exceptions are noted in respective endpoint documentation.  ## HTTPS only   Our APIs can only be accessed via HTTPS.  # Interested in building data.world apps?  Check out our [developer portal](https://apidocs.data.world) for tips on how to get started, tutorials, and to interact with the API endpoints right within your browser.

    OpenAPI spec version: 0.21.0
    Contact: help@data.world
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class DOIsApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def add_doi(self, owner, id, doi, **kwargs):
        """
        Create dataset DOI
        Associate a DOI ([Digital Object Identifier](https://www.doi.org/)) with a dataset.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_doi(owner, id, doi, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str id: Dataset unique identifier. For example, in the URL:[https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), an-intro-to-dataworld-dataset is the unique identifier of the dataset. (required)
        :param str doi: DOI ([Digital Object Identifier](https://www.doi.org/)) (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_doi_with_http_info(owner, id, doi, **kwargs)
        else:
            (data) = self.add_doi_with_http_info(owner, id, doi, **kwargs)
            return data

    def add_doi_with_http_info(self, owner, id, doi, **kwargs):
        """
        Create dataset DOI
        Associate a DOI ([Digital Object Identifier](https://www.doi.org/)) with a dataset.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_doi_with_http_info(owner, id, doi, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str id: Dataset unique identifier. For example, in the URL:[https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), an-intro-to-dataworld-dataset is the unique identifier of the dataset. (required)
        :param str doi: DOI ([Digital Object Identifier](https://www.doi.org/)) (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'id', 'doi']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_doi" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `add_doi`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_doi`")
        # verify the required parameter 'doi' is set
        if ('doi' not in params) or (params['doi'] is None):
            raise ValueError("Missing the required parameter `doi` when calling `add_doi`")

        if 'owner' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['owner']):
            raise ValueError("Invalid value for parameter `owner` when calling `add_doi`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")
        if 'id' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['id']):
            raise ValueError("Invalid value for parameter `id` when calling `add_doi`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")
        if 'doi' in params and not re.search('10.\\\\d{4,9}\/[-._;()\/:a-zA-Z0-9]+', params['doi']):
            raise ValueError("Invalid value for parameter `doi` when calling `add_doi`, must conform to the pattern `/10.\\\\d{4,9}\/[-._;()\/:a-zA-Z0-9]+/`")

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']
        if 'id' in params:
            path_params['id'] = params['id']
        if 'doi' in params:
            path_params['doi'] = params['doi']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth']

        return self.api_client.call_api('/datasets/{owner}/{id}/dois/{doi}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SuccessMessage',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def add_version_doi(self, owner, id, version_id, doi, **kwargs):
        """
        Create dataset version DOI
        Associate a DOI ([Digital Object Identifier](https://www.doi.org/)) with a version of a dataset.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_version_doi(owner, id, version_id, doi, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str id: Dataset unique identifier. For example, in the URL:[https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), an-intro-to-dataworld-dataset is the unique identifier of the dataset. (required)
        :param str version_id: Version unique identifier. (required)
        :param str doi: DOI ([Digital Object Identifier](https://www.doi.org/)) (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.add_version_doi_with_http_info(owner, id, version_id, doi, **kwargs)
        else:
            (data) = self.add_version_doi_with_http_info(owner, id, version_id, doi, **kwargs)
            return data

    def add_version_doi_with_http_info(self, owner, id, version_id, doi, **kwargs):
        """
        Create dataset version DOI
        Associate a DOI ([Digital Object Identifier](https://www.doi.org/)) with a version of a dataset.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.add_version_doi_with_http_info(owner, id, version_id, doi, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str id: Dataset unique identifier. For example, in the URL:[https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), an-intro-to-dataworld-dataset is the unique identifier of the dataset. (required)
        :param str version_id: Version unique identifier. (required)
        :param str doi: DOI ([Digital Object Identifier](https://www.doi.org/)) (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'id', 'version_id', 'doi']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_version_doi" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `add_version_doi`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `add_version_doi`")
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params) or (params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `add_version_doi`")
        # verify the required parameter 'doi' is set
        if ('doi' not in params) or (params['doi'] is None):
            raise ValueError("Missing the required parameter `doi` when calling `add_version_doi`")

        if 'owner' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['owner']):
            raise ValueError("Invalid value for parameter `owner` when calling `add_version_doi`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")
        if 'id' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['id']):
            raise ValueError("Invalid value for parameter `id` when calling `add_version_doi`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")
        if 'doi' in params and not re.search('10.\\\\d{4,9}\/[-._;()\/:a-zA-Z0-9]+', params['doi']):
            raise ValueError("Invalid value for parameter `doi` when calling `add_version_doi`, must conform to the pattern `/10.\\\\d{4,9}\/[-._;()\/:a-zA-Z0-9]+/`")

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']
        if 'id' in params:
            path_params['id'] = params['id']
        if 'version_id' in params:
            path_params['versionId'] = params['version_id']
        if 'doi' in params:
            path_params['doi'] = params['doi']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth']

        return self.api_client.call_api('/datasets/{owner}/{id}/v/{versionId}/dois/{doi}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SuccessMessage',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_doi(self, owner, id, doi, **kwargs):
        """
        Delete dataset DOI
        Delete a DOI ([Digital Object Identifier](https://www.doi.org/)) associated with a dataset.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_doi(owner, id, doi, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str id: Dataset unique identifier. For example, in the URL:[https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), an-intro-to-dataworld-dataset is the unique identifier of the dataset. (required)
        :param str doi: DOI ([Digital Object Identifier](https://www.doi.org/)) (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_doi_with_http_info(owner, id, doi, **kwargs)
        else:
            (data) = self.delete_doi_with_http_info(owner, id, doi, **kwargs)
            return data

    def delete_doi_with_http_info(self, owner, id, doi, **kwargs):
        """
        Delete dataset DOI
        Delete a DOI ([Digital Object Identifier](https://www.doi.org/)) associated with a dataset.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_doi_with_http_info(owner, id, doi, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str id: Dataset unique identifier. For example, in the URL:[https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), an-intro-to-dataworld-dataset is the unique identifier of the dataset. (required)
        :param str doi: DOI ([Digital Object Identifier](https://www.doi.org/)) (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'id', 'doi']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_doi" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `delete_doi`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_doi`")
        # verify the required parameter 'doi' is set
        if ('doi' not in params) or (params['doi'] is None):
            raise ValueError("Missing the required parameter `doi` when calling `delete_doi`")

        if 'owner' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['owner']):
            raise ValueError("Invalid value for parameter `owner` when calling `delete_doi`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")
        if 'id' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['id']):
            raise ValueError("Invalid value for parameter `id` when calling `delete_doi`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")
        if 'doi' in params and not re.search('10.\\\\d{4,9}\/[-._;()\/:a-zA-Z0-9]+', params['doi']):
            raise ValueError("Invalid value for parameter `doi` when calling `delete_doi`, must conform to the pattern `/10.\\\\d{4,9}\/[-._;()\/:a-zA-Z0-9]+/`")

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']
        if 'id' in params:
            path_params['id'] = params['id']
        if 'doi' in params:
            path_params['doi'] = params['doi']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth']

        return self.api_client.call_api('/datasets/{owner}/{id}/dois/{doi}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SuccessMessage',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_version_doi(self, owner, id, version_id, doi, **kwargs):
        """
        Delete dataset version DOI
        Delete a DOI ([Digital Object Identifier](https://www.doi.org/)) associated with a version of a dataset.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_version_doi(owner, id, version_id, doi, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str id: Dataset unique identifier. For example, in the URL:[https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), an-intro-to-dataworld-dataset is the unique identifier of the dataset. (required)
        :param str version_id: Version unique identifier. (required)
        :param str doi: DOI ([Digital Object Identifier](https://www.doi.org/)) (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_version_doi_with_http_info(owner, id, version_id, doi, **kwargs)
        else:
            (data) = self.delete_version_doi_with_http_info(owner, id, version_id, doi, **kwargs)
            return data

    def delete_version_doi_with_http_info(self, owner, id, version_id, doi, **kwargs):
        """
        Delete dataset version DOI
        Delete a DOI ([Digital Object Identifier](https://www.doi.org/)) associated with a version of a dataset.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_version_doi_with_http_info(owner, id, version_id, doi, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str owner: User name and unique identifier of the user or organization a resource belongs to. For example, in the URL: [https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), jonloyens is the unique identifier of the owner. (required)
        :param str id: Dataset unique identifier. For example, in the URL:[https://data.world/jonloyens/an-intro-to-dataworld-dataset](https://data.world/jonloyens/an-intro-to-dataworld-dataset), an-intro-to-dataworld-dataset is the unique identifier of the dataset. (required)
        :param str version_id: Version unique identifier. (required)
        :param str doi: DOI ([Digital Object Identifier](https://www.doi.org/)) (required)
        :return: SuccessMessage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['owner', 'id', 'version_id', 'doi']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_version_doi" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'owner' is set
        if ('owner' not in params) or (params['owner'] is None):
            raise ValueError("Missing the required parameter `owner` when calling `delete_version_doi`")
        # verify the required parameter 'id' is set
        if ('id' not in params) or (params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_version_doi`")
        # verify the required parameter 'version_id' is set
        if ('version_id' not in params) or (params['version_id'] is None):
            raise ValueError("Missing the required parameter `version_id` when calling `delete_version_doi`")
        # verify the required parameter 'doi' is set
        if ('doi' not in params) or (params['doi'] is None):
            raise ValueError("Missing the required parameter `doi` when calling `delete_version_doi`")

        if 'owner' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['owner']):
            raise ValueError("Invalid value for parameter `owner` when calling `delete_version_doi`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")
        if 'id' in params and not re.search('[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]', params['id']):
            raise ValueError("Invalid value for parameter `id` when calling `delete_version_doi`, must conform to the pattern `/[a-z0-9](?:-(?!-)|[a-z0-9])+[a-z0-9]/`")
        if 'doi' in params and not re.search('10.\\\\d{4,9}\/[-._;()\/:a-zA-Z0-9]+', params['doi']):
            raise ValueError("Invalid value for parameter `doi` when calling `delete_version_doi`, must conform to the pattern `/10.\\\\d{4,9}\/[-._;()\/:a-zA-Z0-9]+/`")

        collection_formats = {}

        path_params = {}
        if 'owner' in params:
            path_params['owner'] = params['owner']
        if 'id' in params:
            path_params['id'] = params['id']
        if 'version_id' in params:
            path_params['versionId'] = params['version_id']
        if 'doi' in params:
            path_params['doi'] = params['doi']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # Authentication setting
        auth_settings = ['oauth']

        return self.api_client.call_api('/datasets/{owner}/{id}/v/{versionId}/dois/{doi}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SuccessMessage',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)