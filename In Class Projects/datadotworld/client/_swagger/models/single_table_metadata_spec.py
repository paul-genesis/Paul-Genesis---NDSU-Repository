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


class SingleTableMetadataSpec(object):
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
        'database': 'str',
        'schema': 'str',
        'table': 'str',
        'table_type': 'str'
    }

    attribute_map = {
        'database': 'database',
        'schema': 'schema',
        'table': 'table',
        'table_type': 'tableType'
    }

    def __init__(self, database=None, schema=None, table=None, table_type=None):
        """
        SingleTableMetadataSpec - a model defined in Swagger
        """

        self._database = None
        self._schema = None
        self._table = None
        self._table_type = None

        if database is not None:
          self.database = database
        if schema is not None:
          self.schema = schema
        if table is not None:
          self.table = table
        if table_type is not None:
          self.table_type = table_type

    @property
    def database(self):
        """
        Gets the database of this SingleTableMetadataSpec.
        Database name

        :return: The database of this SingleTableMetadataSpec.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this SingleTableMetadataSpec.
        Database name

        :param database: The database of this SingleTableMetadataSpec.
        :type: str
        """
        if database is not None and len(database) > 128:
            raise ValueError("Invalid value for `database`, length must be less than or equal to `128`")
        if database is not None and len(database) < 1:
            raise ValueError("Invalid value for `database`, length must be greater than or equal to `1`")

        self._database = database

    @property
    def schema(self):
        """
        Gets the schema of this SingleTableMetadataSpec.
        Schema name

        :return: The schema of this SingleTableMetadataSpec.
        :rtype: str
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """
        Sets the schema of this SingleTableMetadataSpec.
        Schema name

        :param schema: The schema of this SingleTableMetadataSpec.
        :type: str
        """
        if schema is not None and len(schema) > 128:
            raise ValueError("Invalid value for `schema`, length must be less than or equal to `128`")
        if schema is not None and len(schema) < 1:
            raise ValueError("Invalid value for `schema`, length must be greater than or equal to `1`")

        self._schema = schema

    @property
    def table(self):
        """
        Gets the table of this SingleTableMetadataSpec.
        Table name

        :return: The table of this SingleTableMetadataSpec.
        :rtype: str
        """
        return self._table

    @table.setter
    def table(self, table):
        """
        Sets the table of this SingleTableMetadataSpec.
        Table name

        :param table: The table of this SingleTableMetadataSpec.
        :type: str
        """
        if table is not None and len(table) > 128:
            raise ValueError("Invalid value for `table`, length must be less than or equal to `128`")
        if table is not None and len(table) < 1:
            raise ValueError("Invalid value for `table`, length must be greater than or equal to `1`")

        self._table = table

    @property
    def table_type(self):
        """
        Gets the table_type of this SingleTableMetadataSpec.
        Table type

        :return: The table_type of this SingleTableMetadataSpec.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """
        Sets the table_type of this SingleTableMetadataSpec.
        Table type

        :param table_type: The table_type of this SingleTableMetadataSpec.
        :type: str
        """
        allowed_values = ["VIRTUAL"]
        if table_type not in allowed_values:
            raise ValueError(
                "Invalid value for `table_type` ({0}), must be one of {1}"
                .format(table_type, allowed_values)
            )

        self._table_type = table_type

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
        if not isinstance(other, SingleTableMetadataSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other