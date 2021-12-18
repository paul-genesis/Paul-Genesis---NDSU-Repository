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


class InsightSummaryResponse(object):
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
        'author': 'str',
        'body': 'InsightBody',
        'created': 'str',
        'data_source_links': 'list[str]',
        'description': 'str',
        'id': 'str',
        'source_link': 'str',
        'thumbnail': 'str',
        'title': 'str',
        'updated': 'str',
        'version': 'str'
    }

    attribute_map = {
        'author': 'author',
        'body': 'body',
        'created': 'created',
        'data_source_links': 'dataSourceLinks',
        'description': 'description',
        'id': 'id',
        'source_link': 'sourceLink',
        'thumbnail': 'thumbnail',
        'title': 'title',
        'updated': 'updated',
        'version': 'version'
    }

    def __init__(self, author=None, body=None, created=None, data_source_links=None, description=None, id=None, source_link=None, thumbnail=None, title=None, updated=None, version=None):
        """
        InsightSummaryResponse - a model defined in Swagger
        """

        self._author = None
        self._body = None
        self._created = None
        self._data_source_links = None
        self._description = None
        self._id = None
        self._source_link = None
        self._thumbnail = None
        self._title = None
        self._updated = None
        self._version = None

        self.author = author
        self.body = body
        self.created = created
        if data_source_links is not None:
          self.data_source_links = data_source_links
        if description is not None:
          self.description = description
        self.id = id
        if source_link is not None:
          self.source_link = source_link
        if thumbnail is not None:
          self.thumbnail = thumbnail
        self.title = title
        self.updated = updated
        self.version = version

    @property
    def author(self):
        """
        Gets the author of this InsightSummaryResponse.
        User name of the author of the insight.

        :return: The author of this InsightSummaryResponse.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """
        Sets the author of this InsightSummaryResponse.
        User name of the author of the insight.

        :param author: The author of this InsightSummaryResponse.
        :type: str
        """
        if author is None:
            raise ValueError("Invalid value for `author`, must not be `None`")

        self._author = author

    @property
    def body(self):
        """
        Gets the body of this InsightSummaryResponse.

        :return: The body of this InsightSummaryResponse.
        :rtype: InsightBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this InsightSummaryResponse.

        :param body: The body of this InsightSummaryResponse.
        :type: InsightBody
        """
        if body is None:
            raise ValueError("Invalid value for `body`, must not be `None`")

        self._body = body

    @property
    def created(self):
        """
        Gets the created of this InsightSummaryResponse.
        Date and time when insight was created.

        :return: The created of this InsightSummaryResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this InsightSummaryResponse.
        Date and time when insight was created.

        :param created: The created of this InsightSummaryResponse.
        :type: str
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")

        self._created = created

    @property
    def data_source_links(self):
        """
        Gets the data_source_links of this InsightSummaryResponse.
        One or more permalinks to the data sources used to generate this insight. Allows others to access the data originally used to produce the insight.

        :return: The data_source_links of this InsightSummaryResponse.
        :rtype: list[str]
        """
        return self._data_source_links

    @data_source_links.setter
    def data_source_links(self, data_source_links):
        """
        Sets the data_source_links of this InsightSummaryResponse.
        One or more permalinks to the data sources used to generate this insight. Allows others to access the data originally used to produce the insight.

        :param data_source_links: The data_source_links of this InsightSummaryResponse.
        :type: list[str]
        """

        self._data_source_links = data_source_links

    @property
    def description(self):
        """
        Gets the description of this InsightSummaryResponse.
        Insight description.

        :return: The description of this InsightSummaryResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this InsightSummaryResponse.
        Insight description.

        :param description: The description of this InsightSummaryResponse.
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """
        Gets the id of this InsightSummaryResponse.
        Unique Insight id.

        :return: The id of this InsightSummaryResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this InsightSummaryResponse.
        Unique Insight id.

        :param id: The id of this InsightSummaryResponse.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def source_link(self):
        """
        Gets the source_link of this InsightSummaryResponse.
        Permalink to source code or platform this insight was generated with. Allows others to replicate the steps originally used to produce the insight.

        :return: The source_link of this InsightSummaryResponse.
        :rtype: str
        """
        return self._source_link

    @source_link.setter
    def source_link(self, source_link):
        """
        Sets the source_link of this InsightSummaryResponse.
        Permalink to source code or platform this insight was generated with. Allows others to replicate the steps originally used to produce the insight.

        :param source_link: The source_link of this InsightSummaryResponse.
        :type: str
        """

        self._source_link = source_link

    @property
    def thumbnail(self):
        """
        Gets the thumbnail of this InsightSummaryResponse.
        URL of insight thumbnai

        :return: The thumbnail of this InsightSummaryResponse.
        :rtype: str
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """
        Sets the thumbnail of this InsightSummaryResponse.
        URL of insight thumbnai

        :param thumbnail: The thumbnail of this InsightSummaryResponse.
        :type: str
        """

        self._thumbnail = thumbnail

    @property
    def title(self):
        """
        Gets the title of this InsightSummaryResponse.
        Insight title.

        :return: The title of this InsightSummaryResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this InsightSummaryResponse.
        Insight title.

        :param title: The title of this InsightSummaryResponse.
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")

        self._title = title

    @property
    def updated(self):
        """
        Gets the updated of this InsightSummaryResponse.
        Date and time when insight was last updated.

        :return: The updated of this InsightSummaryResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this InsightSummaryResponse.
        Date and time when insight was last updated.

        :param updated: The updated of this InsightSummaryResponse.
        :type: str
        """
        if updated is None:
            raise ValueError("Invalid value for `updated`, must not be `None`")

        self._updated = updated

    @property
    def version(self):
        """
        Gets the version of this InsightSummaryResponse.
        Insight version

        :return: The version of this InsightSummaryResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this InsightSummaryResponse.
        Insight version

        :param version: The version of this InsightSummaryResponse.
        :type: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version

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
        if not isinstance(other, InsightSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other