# coding: utf-8

"""
    data.world API

    # data.world in a nutshell  data.world is a productive, secure platform for modern data teamwork.  We bring together your data practitioners, subject matter experts, and other stakeholders by removing costly barriers to data discovery, comprehension, integration, and sharing.   Everything your team needs to quickly understand and use data stays with it.   Social features and integrations encourage collaborators to ask and answer questions, share discoveries, and coordinate closely while still using their preferred tools.  Our focus on interoperability helps you enhance your own data with data from any source, including our vast and growing library of free public datasets.   Sophisticated permissions, auditing features, and more make it easy to manage who views your data and what they do with it.  # Conventions  ## Authentication  All data.world API calls require an API token.   OAuth2 is the preferred and most secure method for authenticating users of your data.world applications. Visit our [oauth documentation](https://apidocs.data.world/toolkit/oauth) for additional information. Alternatively, you can obtain a token for _personal use or testing_ by navigating to your profile settings, under the Advanced tab ([https://data.world/settings/advanced](https://data.world/settings/advanced)).  Authentication must be provided in API requests via the `Authorization` header. For example, for a user whose API token is `my_api_token`, the request header should be `Authorization: Bearer my_api_token` (note the `Bearer` prefix).  ## Content type   By default, `application/json` is the content type used in request and response bodies. Exceptions are noted in respective endpoint documentation.  ## HTTPS only   Our APIs can only be accessed via HTTPS.  # Interested in building data.world apps?  Check out our [developer portal](https://apidocs.data.world) for tips on how to get started, tutorials, and to interact with the API endpoints right within your browser.

    OpenAPI spec version: 0.21.0
    Contact: help@data.world
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class FileSourceCreateOrUpdateRequest(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'authorization': 'WebAuthorization',
        'credentials': 'WebCredentials',
        'expand_archive': 'bool',
        'method': 'str',
        'oauth_token': 'OauthTokenReference',
        'request_entity': 'str',
        'request_headers': 'dict(str, str)',
        'url': 'str'
    }

    attribute_map = {
        'authorization': 'authorization',
        'credentials': 'credentials',
        'expand_archive': 'expandArchive',
        'method': 'method',
        'oauth_token': 'oauthToken',
        'request_entity': 'requestEntity',
        'request_headers': 'requestHeaders',
        'url': 'url'
    }

    def __init__(self, authorization=None, credentials=None, expand_archive=False, method='GET', oauth_token=None, request_entity=None, request_headers=None, url=None):
        """
        FileSourceCreateOrUpdateRequest - a model defined in Swagger
        """

        self._authorization = None
        self._credentials = None
        self._expand_archive = None
        self._method = None
        self._oauth_token = None
        self._request_entity = None
        self._request_headers = None
        self._url = None

        if authorization is not None:
          self.authorization = authorization
        if credentials is not None:
          self.credentials = credentials
        if expand_archive is not None:
          self.expand_archive = expand_archive
        if method is not None:
          self.method = method
        if oauth_token is not None:
          self.oauth_token = oauth_token
        if request_entity is not None:
          self.request_entity = request_entity
        if request_headers is not None:
          self.request_headers = request_headers
        if url is not None:
          self.url = url

    @property
    def authorization(self):
        """
        Gets the authorization of this FileSourceCreateOrUpdateRequest.

        :return: The authorization of this FileSourceCreateOrUpdateRequest.
        :rtype: WebAuthorization
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        """
        Sets the authorization of this FileSourceCreateOrUpdateRequest.

        :param authorization: The authorization of this FileSourceCreateOrUpdateRequest.
        :type: WebAuthorization
        """

        self._authorization = authorization

    @property
    def credentials(self):
        """
        Gets the credentials of this FileSourceCreateOrUpdateRequest.

        :return: The credentials of this FileSourceCreateOrUpdateRequest.
        :rtype: WebCredentials
        """
        return self._credentials

    @credentials.setter
    def credentials(self, credentials):
        """
        Sets the credentials of this FileSourceCreateOrUpdateRequest.

        :param credentials: The credentials of this FileSourceCreateOrUpdateRequest.
        :type: WebCredentials
        """

        self._credentials = credentials

    @property
    def expand_archive(self):
        """
        Gets the expand_archive of this FileSourceCreateOrUpdateRequest.
        Indicates whether compressed files should be expanded upon upload.

        :return: The expand_archive of this FileSourceCreateOrUpdateRequest.
        :rtype: bool
        """
        return self._expand_archive

    @expand_archive.setter
    def expand_archive(self, expand_archive):
        """
        Sets the expand_archive of this FileSourceCreateOrUpdateRequest.
        Indicates whether compressed files should be expanded upon upload.

        :param expand_archive: The expand_archive of this FileSourceCreateOrUpdateRequest.
        :type: bool
        """

        self._expand_archive = expand_archive

    @property
    def method(self):
        """
        Gets the method of this FileSourceCreateOrUpdateRequest.

        :return: The method of this FileSourceCreateOrUpdateRequest.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """
        Sets the method of this FileSourceCreateOrUpdateRequest.

        :param method: The method of this FileSourceCreateOrUpdateRequest.
        :type: str
        """
        allowed_values = ["GET", "POST"]
        if method not in allowed_values:
            raise ValueError(
                "Invalid value for `method` ({0}), must be one of {1}"
                .format(method, allowed_values)
            )

        self._method = method

    @property
    def oauth_token(self):
        """
        Gets the oauth_token of this FileSourceCreateOrUpdateRequest.

        :return: The oauth_token of this FileSourceCreateOrUpdateRequest.
        :rtype: OauthTokenReference
        """
        return self._oauth_token

    @oauth_token.setter
    def oauth_token(self, oauth_token):
        """
        Sets the oauth_token of this FileSourceCreateOrUpdateRequest.

        :param oauth_token: The oauth_token of this FileSourceCreateOrUpdateRequest.
        :type: OauthTokenReference
        """

        self._oauth_token = oauth_token

    @property
    def request_entity(self):
        """
        Gets the request_entity of this FileSourceCreateOrUpdateRequest.

        :return: The request_entity of this FileSourceCreateOrUpdateRequest.
        :rtype: str
        """
        return self._request_entity

    @request_entity.setter
    def request_entity(self, request_entity):
        """
        Sets the request_entity of this FileSourceCreateOrUpdateRequest.

        :param request_entity: The request_entity of this FileSourceCreateOrUpdateRequest.
        :type: str
        """
        if request_entity is not None and len(request_entity) > 10000:
            raise ValueError("Invalid value for `request_entity`, length must be less than or equal to `10000`")

        self._request_entity = request_entity

    @property
    def request_headers(self):
        """
        Gets the request_headers of this FileSourceCreateOrUpdateRequest.
        A map of custom HTTP header name/value pairs to pass with the request.  If a `requestEntity` string is specified, this must contain a `Content-Type` header.  An `Authorization` header value will be converted to a `WebAuthorization` object and the credentials will be encrypted.  The total size of the url and custom headers must not exceed 4096 bytes in the HTTP request, including whitespace, colons and CRLF characters.

        :return: The request_headers of this FileSourceCreateOrUpdateRequest.
        :rtype: dict(str, str)
        """
        return self._request_headers

    @request_headers.setter
    def request_headers(self, request_headers):
        """
        Sets the request_headers of this FileSourceCreateOrUpdateRequest.
        A map of custom HTTP header name/value pairs to pass with the request.  If a `requestEntity` string is specified, this must contain a `Content-Type` header.  An `Authorization` header value will be converted to a `WebAuthorization` object and the credentials will be encrypted.  The total size of the url and custom headers must not exceed 4096 bytes in the HTTP request, including whitespace, colons and CRLF characters.

        :param request_headers: The request_headers of this FileSourceCreateOrUpdateRequest.
        :type: dict(str, str)
        """

        self._request_headers = request_headers

    @property
    def url(self):
        """
        Gets the url of this FileSourceCreateOrUpdateRequest.
        Source URL of file. Must be an http, https, ftp, ftps or stream URL.

        :return: The url of this FileSourceCreateOrUpdateRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this FileSourceCreateOrUpdateRequest.
        Source URL of file. Must be an http, https, ftp, ftps or stream URL.

        :param url: The url of this FileSourceCreateOrUpdateRequest.
        :type: str
        """
        if url is not None and len(url) > 4096:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `4096`")
        if url is not None and len(url) < 1:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `1`")
        if url is not None and not re.search('^(https?|ftps?|stream):.*', url):
            raise ValueError("Invalid value for `url`, must be a follow pattern or equal to `/^(https?|ftps?|stream):.*/`")

        self._url = url

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, FileSourceCreateOrUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
