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


class UserDataResponse(object):
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
        'avatar_url': 'str',
        'created': 'str',
        'display_name': 'str',
        'id': 'str',
        'updated': 'str'
    }

    attribute_map = {
        'avatar_url': 'avatarUrl',
        'created': 'created',
        'display_name': 'displayName',
        'id': 'id',
        'updated': 'updated'
    }

    def __init__(self, avatar_url=None, created=None, display_name=None, id=None, updated=None):
        """
        UserDataResponse - a model defined in Swagger
        """

        self._avatar_url = None
        self._created = None
        self._display_name = None
        self._id = None
        self._updated = None

        if avatar_url is not None:
          self.avatar_url = avatar_url
        self.created = created
        if display_name is not None:
          self.display_name = display_name
        self.id = id
        self.updated = updated

    @property
    def avatar_url(self):
        """
        Gets the avatar_url of this UserDataResponse.
        URL of profile image.

        :return: The avatar_url of this UserDataResponse.
        :rtype: str
        """
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, avatar_url):
        """
        Sets the avatar_url of this UserDataResponse.
        URL of profile image.

        :param avatar_url: The avatar_url of this UserDataResponse.
        :type: str
        """

        self._avatar_url = avatar_url

    @property
    def created(self):
        """
        Gets the created of this UserDataResponse.
        Date and time when account was created.

        :return: The created of this UserDataResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this UserDataResponse.
        Date and time when account was created.

        :param created: The created of this UserDataResponse.
        :type: str
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")

        self._created = created

    @property
    def display_name(self):
        """
        Gets the display_name of this UserDataResponse.
        User's name.

        :return: The display_name of this UserDataResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UserDataResponse.
        User's name.

        :param display_name: The display_name of this UserDataResponse.
        :type: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this UserDataResponse.
        User name and unique identifier.

        :return: The id of this UserDataResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this UserDataResponse.
        User name and unique identifier.

        :param id: The id of this UserDataResponse.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def updated(self):
        """
        Gets the updated of this UserDataResponse.
        Date and time when account was last updated.

        :return: The updated of this UserDataResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this UserDataResponse.
        Date and time when account was last updated.

        :param updated: The updated of this UserDataResponse.
        :type: str
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")

        self._updated = updated

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
        if not isinstance(other, UserDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
