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


class DatasetHydrationDto(object):
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
        'agentid': 'str',
        'created_by': 'AgentHydrationDto',
        'datasetid': 'str',
        'headline': 'str',
        'name': 'str',
        'project': 'bool',
        'relationship': 'ResourceRelationshipDto',
        'type': 'str',
        'updated': 'datetime',
        'user_updated': 'datetime',
        'abstract': 'str'
    }

    attribute_map = {
        'agentid': 'agentid',
        'created_by': 'createdBy',
        'datasetid': 'datasetid',
        'headline': 'headline',
        'name': 'name',
        'project': 'project',
        'relationship': 'relationship',
        'type': 'type',
        'updated': 'updated',
        'user_updated': 'userUpdated',
        'abstract': 'abstract'
    }

    def __init__(self, agentid=None, created_by=None, datasetid=None, headline=None, name=None, project=False, relationship=None, type=None, updated=None, user_updated=None, abstract=None):
        """
        DatasetHydrationDto - a model defined in Swagger
        """

        self._agentid = None
        self._created_by = None
        self._datasetid = None
        self._headline = None
        self._name = None
        self._project = None
        self._relationship = None
        self._type = None
        self._updated = None
        self._user_updated = None
        self._abstract = None

        if agentid is not None:
          self.agentid = agentid
        if created_by is not None:
          self.created_by = created_by
        if datasetid is not None:
          self.datasetid = datasetid
        if headline is not None:
          self.headline = headline
        if name is not None:
          self.name = name
        if project is not None:
          self.project = project
        if relationship is not None:
          self.relationship = relationship
        if type is not None:
          self.type = type
        if updated is not None:
          self.updated = updated
        if user_updated is not None:
          self.user_updated = user_updated
        if abstract is not None:
          self.abstract = abstract

    @property
    def agentid(self):
        """
        Gets the agentid of this DatasetHydrationDto.

        :return: The agentid of this DatasetHydrationDto.
        :rtype: str
        """
        return self._agentid

    @agentid.setter
    def agentid(self, agentid):
        """
        Sets the agentid of this DatasetHydrationDto.

        :param agentid: The agentid of this DatasetHydrationDto.
        :type: str
        """

        self._agentid = agentid

    @property
    def created_by(self):
        """
        Gets the created_by of this DatasetHydrationDto.

        :return: The created_by of this DatasetHydrationDto.
        :rtype: AgentHydrationDto
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """
        Sets the created_by of this DatasetHydrationDto.

        :param created_by: The created_by of this DatasetHydrationDto.
        :type: AgentHydrationDto
        """

        self._created_by = created_by

    @property
    def datasetid(self):
        """
        Gets the datasetid of this DatasetHydrationDto.

        :return: The datasetid of this DatasetHydrationDto.
        :rtype: str
        """
        return self._datasetid

    @datasetid.setter
    def datasetid(self, datasetid):
        """
        Sets the datasetid of this DatasetHydrationDto.

        :param datasetid: The datasetid of this DatasetHydrationDto.
        :type: str
        """

        self._datasetid = datasetid

    @property
    def headline(self):
        """
        Gets the headline of this DatasetHydrationDto.

        :return: The headline of this DatasetHydrationDto.
        :rtype: str
        """
        return self._headline

    @headline.setter
    def headline(self, headline):
        """
        Sets the headline of this DatasetHydrationDto.

        :param headline: The headline of this DatasetHydrationDto.
        :type: str
        """

        self._headline = headline

    @property
    def name(self):
        """
        Gets the name of this DatasetHydrationDto.

        :return: The name of this DatasetHydrationDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DatasetHydrationDto.

        :param name: The name of this DatasetHydrationDto.
        :type: str
        """

        self._name = name

    @property
    def project(self):
        """
        Gets the project of this DatasetHydrationDto.

        :return: The project of this DatasetHydrationDto.
        :rtype: bool
        """
        return self._project

    @project.setter
    def project(self, project):
        """
        Sets the project of this DatasetHydrationDto.

        :param project: The project of this DatasetHydrationDto.
        :type: bool
        """

        self._project = project

    @property
    def relationship(self):
        """
        Gets the relationship of this DatasetHydrationDto.

        :return: The relationship of this DatasetHydrationDto.
        :rtype: ResourceRelationshipDto
        """
        return self._relationship

    @relationship.setter
    def relationship(self, relationship):
        """
        Sets the relationship of this DatasetHydrationDto.

        :param relationship: The relationship of this DatasetHydrationDto.
        :type: ResourceRelationshipDto
        """

        self._relationship = relationship

    @property
    def type(self):
        """
        Gets the type of this DatasetHydrationDto.

        :return: The type of this DatasetHydrationDto.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this DatasetHydrationDto.

        :param type: The type of this DatasetHydrationDto.
        :type: str
        """

        self._type = type

    @property
    def updated(self):
        """
        Gets the updated of this DatasetHydrationDto.

        :return: The updated of this DatasetHydrationDto.
        :rtype: datetime
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """
        Sets the updated of this DatasetHydrationDto.

        :param updated: The updated of this DatasetHydrationDto.
        :type: datetime
        """

        self._updated = updated

    @property
    def user_updated(self):
        """
        Gets the user_updated of this DatasetHydrationDto.

        :return: The user_updated of this DatasetHydrationDto.
        :rtype: datetime
        """
        return self._user_updated

    @user_updated.setter
    def user_updated(self, user_updated):
        """
        Sets the user_updated of this DatasetHydrationDto.

        :param user_updated: The user_updated of this DatasetHydrationDto.
        :type: datetime
        """

        self._user_updated = user_updated

    @property
    def abstract(self):
        """
        Gets the abstract of this DatasetHydrationDto.

        :return: The abstract of this DatasetHydrationDto.
        :rtype: str
        """
        return self._abstract

    @abstract.setter
    def abstract(self, abstract):
        """
        Sets the abstract of this DatasetHydrationDto.

        :param abstract: The abstract of this DatasetHydrationDto.
        :type: str
        """

        self._abstract = abstract

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
        if not isinstance(other, DatasetHydrationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
