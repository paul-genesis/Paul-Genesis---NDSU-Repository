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


class MetadataResourceDto(object):
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
        'id': 'str',
        'title': 'str',
        'table': 'TableId',
        'category': 'str',
        'type_label': 'str',
        'type_iri': 'str',
        'root_parent_type_label': 'str',
        'root_parent_type_iri': 'str',
        'owner': 'str',
        'description': 'str',
        'visibility': 'str',
        'url': 'str',
        'created': 'datetime',
        'updated': 'datetime',
        'collections': 'list[CatalogId]',
        'relationship_types': 'list[str]',
        'tags': 'list[str]',
        'external_urls': 'list[str]',
        'asset_status': 'AssetStatus',
        'properties': 'dict(str, object)'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'table': 'table',
        'category': 'category',
        'type_label': 'typeLabel',
        'type_iri': 'typeIri',
        'root_parent_type_label': 'rootParentTypeLabel',
        'root_parent_type_iri': 'rootParentTypeIri',
        'owner': 'owner',
        'description': 'description',
        'visibility': 'visibility',
        'url': 'url',
        'created': 'created',
        'updated': 'updated',
        'collections': 'collections',
        'relationship_types': 'relationshipTypes',
        'tags': 'tags',
        'external_urls': 'externalUrls',
        'asset_status': 'assetStatus',
        'properties': 'properties'
    }

    def __init__(self, id=None, title=None, table=None, category=None, type_label=None, type_iri=None, root_parent_type_label=None, root_parent_type_iri=None, owner=None, description=None, visibility=None, url=None, created=None, updated=None, collections=None, relationship_types=None, tags=None, external_urls=None, asset_status=None, properties=None):
        """
        MetadataResourceDto - a model defined in Swagger
        """

        self._id = None
        self._title = None
        self._table = None
        self._category = None
        self._type_label = None
        self._type_iri = None
        self._root_parent_type_label = None
        self._root_parent_type_iri = None
        self._owner = None
        self._description = None
        self._visibility = None
        self._url = None
        self._created = None
        self._updated = None
        self._collections = None
        self._relationship_types = None
        self._tags = None
        self._external_urls = None
        self._asset_status = None
        self._properties = None

        self.id = id
        if title is not None:
          self.title = title
        if table is not None:
          self.table = table
        if category is not None:
          self.category = category
        if type_label is not None:
          self.type_label = type_label
        if type_iri is not None:
          self.type_iri = type_iri
        if root_parent_type_label is not None:
          self.root_parent_type_label = root_parent_type_label
        if root_parent_type_iri is not None:
          self.root_parent_type_iri = root_parent_type_iri
        self.owner = owner
        if description is not None:
          self.description = description
        self.visibility = visibility
        if url is not None:
          self.url = url
        self.created = created
        if updated is not None:
          self.updated = updated
        if collections is not None:
          self.collections = collections
        if relationship_types is not None:
          self.relationship_types = relationship_types
        if tags is not None:
          self.tags = tags
        if external_urls is not None:
          self.external_urls = external_urls
        if asset_status is not None:
          self.asset_status = asset_status
        if properties is not None:
          self.properties = properties

    @property
    def id(self):
        """
        Gets the id of this MetadataResourceDto.

        :return: The id of this MetadataResourceDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MetadataResourceDto.

        :param id: The id of this MetadataResourceDto.
        :type: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def title(self):
        """
        Gets the title of this MetadataResourceDto.

        :return: The title of this MetadataResourceDto.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this MetadataResourceDto.

        :param title: The title of this MetadataResourceDto.
        :type: str
        """

        self._title = title

    @property
    def table(self):
        """
        Gets the table of this MetadataResourceDto.

        :return: The table of this MetadataResourceDto.
        :rtype: TableId
        """
        return self._table

    @table.setter
    def table(self, table):
        """
        Sets the table of this MetadataResourceDto.

        :param table: The table of this MetadataResourceDto.
        :type: TableId
        """

        self._table = table

    @property
    def category(self):
        """
        Gets the category of this MetadataResourceDto.

        :return: The category of this MetadataResourceDto.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this MetadataResourceDto.

        :param category: The category of this MetadataResourceDto.
        :type: str
        """

        self._category = category

    @property
    def type_label(self):
        """
        Gets the type_label of this MetadataResourceDto.

        :return: The type_label of this MetadataResourceDto.
        :rtype: str
        """
        return self._type_label

    @type_label.setter
    def type_label(self, type_label):
        """
        Sets the type_label of this MetadataResourceDto.

        :param type_label: The type_label of this MetadataResourceDto.
        :type: str
        """

        self._type_label = type_label

    @property
    def type_iri(self):
        """
        Gets the type_iri of this MetadataResourceDto.

        :return: The type_iri of this MetadataResourceDto.
        :rtype: str
        """
        return self._type_iri

    @type_iri.setter
    def type_iri(self, type_iri):
        """
        Sets the type_iri of this MetadataResourceDto.

        :param type_iri: The type_iri of this MetadataResourceDto.
        :type: str
        """

        self._type_iri = type_iri

    @property
    def root_parent_type_label(self):
        """
        Gets the root_parent_type_label of this MetadataResourceDto.

        :return: The root_parent_type_label of this MetadataResourceDto.
        :rtype: str
        """
        return self._root_parent_type_label

    @root_parent_type_label.setter
    def root_parent_type_label(self, root_parent_type_label):
        """
        Sets the root_parent_type_label of this MetadataResourceDto.

        :param root_parent_type_label: The root_parent_type_label of this MetadataResourceDto.
        :type: str
        """

        self._root_parent_type_label = root_parent_type_label

    @property
    def root_parent_type_iri(self):
        """
        Gets the root_parent_type_iri of this MetadataResourceDto.

        :return: The root_parent_type_iri of this MetadataResourceDto.
        :rtype: str
        """
        return self._root_parent_type_iri

    @root_parent_type_iri.setter
    def root_parent_type_iri(self, root_parent_type_iri):
        """
        Sets the root_parent_type_iri of this MetadataResourceDto.

        :param root_parent_type_iri: The root_parent_type_iri of this MetadataResourceDto.
        :type: str
        """

        self._root_parent_type_iri = root_parent_type_iri

    @property
    def owner(self):
        """
        Gets the owner of this MetadataResourceDto.

        :return: The owner of this MetadataResourceDto.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this MetadataResourceDto.

        :param owner: The owner of this MetadataResourceDto.
        :type: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")

        self._owner = owner

    @property
    def description(self):
        """
        Gets the description of this MetadataResourceDto.

        :return: The description of this MetadataResourceDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this MetadataResourceDto.

        :param description: The description of this MetadataResourceDto.
        :type: str
        """

        self._description = description

    @property
    def visibility(self):
        """
        Gets the visibility of this MetadataResourceDto.

        :return: The visibility of this MetadataResourceDto.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """
        Sets the visibility of this MetadataResourceDto.

        :param visibility: The visibility of this MetadataResourceDto.
        :type: str
        """
        if visibility is None:
            raise ValueError("Invalid value for `visibility`, must not be `None`")
        allowed_values = ["DISCOVERABLE", "OPEN", "PRIVATE"]
        if visibility not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def url(self):
        """
        Gets the url of this MetadataResourceDto.

        :return: The url of this MetadataResourceDto.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """
        Sets the url of this MetadataResourceDto.

        :param url: The url of this MetadataResourceDto.
        :type: str
        """

        self._url = url

    @property
    def created(self):
        """
        Gets the created of this MetadataResourceDto.

        :return: The created of this MetadataResourceDto.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """
        Sets the created of this MetadataResourceDto.

        :param created: The created of this MetadataResourceDto.
        :type: datetime
        """
        if created is None:
            raise ValueError("Invalid value for `created`, must not be `None`")

        self._created = created

    @property
    def updated(self):
        """
        Gets the updated of this MetadataResourceDto.

        :return: The updated of this MetadataResourceDto.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this MetadataResourceDto.

        :param updated: The updated of this MetadataResourceDto.
        :type: datetime
        """

        self._updated = updated

    @property
    def collections(self):
        """
        Gets the collections of this MetadataResourceDto.

        :return: The collections of this MetadataResourceDto.
        :rtype: list[CatalogId]
        """
        return self._collections

    @collections.setter
    def collections(self, collections):
        """
        Sets the collections of this MetadataResourceDto.

        :param collections: The collections of this MetadataResourceDto.
        :type: list[CatalogId]
        """

        self._collections = collections

    @property
    def relationship_types(self):
        """
        Gets the relationship_types of this MetadataResourceDto.

        :return: The relationship_types of this MetadataResourceDto.
        :rtype: list[str]
        """
        return self._relationship_types

    @relationship_types.setter
    def relationship_types(self, relationship_types):
        """
        Sets the relationship_types of this MetadataResourceDto.

        :param relationship_types: The relationship_types of this MetadataResourceDto.
        :type: list[str]
        """

        self._relationship_types = relationship_types

    @property
    def tags(self):
        """
        Gets the tags of this MetadataResourceDto.

        :return: The tags of this MetadataResourceDto.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this MetadataResourceDto.

        :param tags: The tags of this MetadataResourceDto.
        :type: list[str]
        """

        self._tags = tags

    @property
    def external_urls(self):
        """
        Gets the external_urls of this MetadataResourceDto.

        :return: The external_urls of this MetadataResourceDto.
        :rtype: list[str]
        """
        return self._external_urls

    @external_urls.setter
    def external_urls(self, external_urls):
        """
        Sets the external_urls of this MetadataResourceDto.

        :param external_urls: The external_urls of this MetadataResourceDto.
        :type: list[str]
        """

        self._external_urls = external_urls

    @property
    def asset_status(self):
        """
        Gets the asset_status of this MetadataResourceDto.

        :return: The asset_status of this MetadataResourceDto.
        :rtype: AssetStatus
        """
        return self._asset_status

    @asset_status.setter
    def asset_status(self, asset_status):
        """
        Sets the asset_status of this MetadataResourceDto.

        :param asset_status: The asset_status of this MetadataResourceDto.
        :type: AssetStatus
        """

        self._asset_status = asset_status

    @property
    def properties(self):
        """
        Gets the properties of this MetadataResourceDto.

        :return: The properties of this MetadataResourceDto.
        :rtype: dict(str, object)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this MetadataResourceDto.

        :param properties: The properties of this MetadataResourceDto.
        :type: dict(str, object)
        """

        self._properties = properties

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
        if not isinstance(other, MetadataResourceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
