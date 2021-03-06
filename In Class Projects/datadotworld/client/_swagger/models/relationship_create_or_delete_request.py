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


class RelationshipCreateOrDeleteRequest(object):
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
        'relationship_type': 'str',
        'source_dataset_id': 'str',
        'source_id': 'str',
        'source_table_id': 'str',
        'source_type': 'str',
        'target_dataset_id': 'str',
        'target_id': 'str',
        'target_table_id': 'str',
        'target_type': 'str'
    }

    attribute_map = {
        'relationship_type': 'relationshipType',
        'source_dataset_id': 'sourceDatasetId',
        'source_id': 'sourceId',
        'source_table_id': 'sourceTableId',
        'source_type': 'sourceType',
        'target_dataset_id': 'targetDatasetId',
        'target_id': 'targetId',
        'target_table_id': 'targetTableId',
        'target_type': 'targetType'
    }

    def __init__(self, relationship_type=None, source_dataset_id=None, source_id=None, source_table_id=None, source_type=None, target_dataset_id=None, target_id=None, target_table_id=None, target_type=None):
        """
        RelationshipCreateOrDeleteRequest - a model defined in Swagger
        """

        self._relationship_type = None
        self._source_dataset_id = None
        self._source_id = None
        self._source_table_id = None
        self._source_type = None
        self._target_dataset_id = None
        self._target_id = None
        self._target_table_id = None
        self._target_type = None

        self.relationship_type = relationship_type
        if source_dataset_id is not None:
          self.source_dataset_id = source_dataset_id
        self.source_id = source_id
        if source_table_id is not None:
          self.source_table_id = source_table_id
        self.source_type = source_type
        if target_dataset_id is not None:
          self.target_dataset_id = target_dataset_id
        self.target_id = target_id
        if target_table_id is not None:
          self.target_table_id = target_table_id
        self.target_type = target_type

    @property
    def relationship_type(self):
        """
        Gets the relationship_type of this RelationshipCreateOrDeleteRequest.

        :return: The relationship_type of this RelationshipCreateOrDeleteRequest.
        :rtype: str
        """
        return self._relationship_type

    @relationship_type.setter
    def relationship_type(self, relationship_type):
        """
        Sets the relationship_type of this RelationshipCreateOrDeleteRequest.

        :param relationship_type: The relationship_type of this RelationshipCreateOrDeleteRequest.
        :type: str
        """
        if relationship_type is None:
            raise ValueError("Invalid value for `relationship_type`, must not be `None`")
        allowed_values = ["USES_DATASET", "REFERENCE_BUSINESS_TERM", "RELATED_TO_BUSINESS_TERM", "USES_DATA_FROM"]
        if relationship_type not in allowed_values:
            raise ValueError(
                "Invalid value for `relationship_type` ({0}), must be one of {1}"
                .format(relationship_type, allowed_values)
            )

        self._relationship_type = relationship_type

    @property
    def source_dataset_id(self):
        """
        Gets the source_dataset_id of this RelationshipCreateOrDeleteRequest.
        If source is a table or column, populate with dataset ID that contains table.

        :return: The source_dataset_id of this RelationshipCreateOrDeleteRequest.
        :rtype: str
        """
        return self._source_dataset_id

    @source_dataset_id.setter
    def source_dataset_id(self, source_dataset_id):
        """
        Sets the source_dataset_id of this RelationshipCreateOrDeleteRequest.
        If source is a table or column, populate with dataset ID that contains table.

        :param source_dataset_id: The source_dataset_id of this RelationshipCreateOrDeleteRequest.
        :type: str
        """

        self._source_dataset_id = source_dataset_id

    @property
    def source_id(self):
        """
        Gets the source_id of this RelationshipCreateOrDeleteRequest.

        :return: The source_id of this RelationshipCreateOrDeleteRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this RelationshipCreateOrDeleteRequest.

        :param source_id: The source_id of this RelationshipCreateOrDeleteRequest.
        :type: str
        """
        if source_id is None:
            raise ValueError("Invalid value for `source_id`, must not be `None`")

        self._source_id = source_id

    @property
    def source_table_id(self):
        """
        Gets the source_table_id of this RelationshipCreateOrDeleteRequest.
        If source is a column, populate with table ID that contains column.

        :return: The source_table_id of this RelationshipCreateOrDeleteRequest.
        :rtype: str
        """
        return self._source_table_id

    @source_table_id.setter
    def source_table_id(self, source_table_id):
        """
        Sets the source_table_id of this RelationshipCreateOrDeleteRequest.
        If source is a column, populate with table ID that contains column.

        :param source_table_id: The source_table_id of this RelationshipCreateOrDeleteRequest.
        :type: str
        """

        self._source_table_id = source_table_id

    @property
    def source_type(self):
        """
        Gets the source_type of this RelationshipCreateOrDeleteRequest.

        :return: The source_type of this RelationshipCreateOrDeleteRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """
        Sets the source_type of this RelationshipCreateOrDeleteRequest.

        :param source_type: The source_type of this RelationshipCreateOrDeleteRequest.
        :type: str
        """
        if source_type is None:
            raise ValueError("Invalid value for `source_type`, must not be `None`")
        allowed_values = ["CATALOG", "ANALYSIS", "BUSINESS_TERM", "COLUMN", "DATA_TYPE", "DATASET", "PROJECT", "TABLE"]
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def target_dataset_id(self):
        """
        Gets the target_dataset_id of this RelationshipCreateOrDeleteRequest.
        If target is a table or column, populate with dataset ID that contains table.

        :return: The target_dataset_id of this RelationshipCreateOrDeleteRequest.
        :rtype: str
        """
        return self._target_dataset_id

    @target_dataset_id.setter
    def target_dataset_id(self, target_dataset_id):
        """
        Sets the target_dataset_id of this RelationshipCreateOrDeleteRequest.
        If target is a table or column, populate with dataset ID that contains table.

        :param target_dataset_id: The target_dataset_id of this RelationshipCreateOrDeleteRequest.
        :type: str
        """

        self._target_dataset_id = target_dataset_id

    @property
    def target_id(self):
        """
        Gets the target_id of this RelationshipCreateOrDeleteRequest.

        :return: The target_id of this RelationshipCreateOrDeleteRequest.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this RelationshipCreateOrDeleteRequest.

        :param target_id: The target_id of this RelationshipCreateOrDeleteRequest.
        :type: str
        """
        if target_id is None:
            raise ValueError("Invalid value for `target_id`, must not be `None`")

        self._target_id = target_id

    @property
    def target_table_id(self):
        """
        Gets the target_table_id of this RelationshipCreateOrDeleteRequest.
        If target is a column, populate with table ID that contains column.

        :return: The target_table_id of this RelationshipCreateOrDeleteRequest.
        :rtype: str
        """
        return self._target_table_id

    @target_table_id.setter
    def target_table_id(self, target_table_id):
        """
        Sets the target_table_id of this RelationshipCreateOrDeleteRequest.
        If target is a column, populate with table ID that contains column.

        :param target_table_id: The target_table_id of this RelationshipCreateOrDeleteRequest.
        :type: str
        """

        self._target_table_id = target_table_id

    @property
    def target_type(self):
        """
        Gets the target_type of this RelationshipCreateOrDeleteRequest.

        :return: The target_type of this RelationshipCreateOrDeleteRequest.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        """
        Sets the target_type of this RelationshipCreateOrDeleteRequest.

        :param target_type: The target_type of this RelationshipCreateOrDeleteRequest.
        :type: str
        """
        if target_type is None:
            raise ValueError("Invalid value for `target_type`, must not be `None`")
        allowed_values = ["CATALOG", "ANALYSIS", "BUSINESS_TERM", "COLUMN", "DATA_TYPE", "DATASET", "PROJECT", "TABLE"]
        if target_type not in allowed_values:
            raise ValueError(
                "Invalid value for `target_type` ({0}), must be one of {1}"
                .format(target_type, allowed_values)
            )

        self._target_type = target_type

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
        if not isinstance(other, RelationshipCreateOrDeleteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
