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


class Subscription(object):
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
        'dataset': 'DatasetIdentifier',
        'events': 'list[str]',
        'project': 'DatasetIdentifier',
        'user': 'UserIdentifier'
    }

    attribute_map = {
        'dataset': 'dataset',
        'events': 'events',
        'project': 'project',
        'user': 'user'
    }

    def __init__(self, dataset=None, events=None, project=None, user=None):
        """
        Subscription - a model defined in Swagger
        """

        self._dataset = None
        self._events = None
        self._project = None
        self._user = None

        if dataset is not None:
          self.dataset = dataset
        self.events = events
        if project is not None:
          self.project = project
        if user is not None:
          self.user = user

    @property
    def dataset(self):
        """
        Gets the dataset of this Subscription.

        :return: The dataset of this Subscription.
        :rtype: DatasetIdentifier
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """
        Sets the dataset of this Subscription.

        :param dataset: The dataset of this Subscription.
        :type: DatasetIdentifier
        """

        self._dataset = dataset

    @property
    def events(self):
        """
        Gets the events of this Subscription.
        Specifies which events should trigger API calls. Currently, only `ALL` is supported. Clients are free to ignore irrelevant events. For all supported events, see: https://apidocs.data.world/toolkit/webhooks

        :return: The events of this Subscription.
        :rtype: list[str]
        """
        return self._events

    @events.setter
    def events(self, events):
        """
        Sets the events of this Subscription.
        Specifies which events should trigger API calls. Currently, only `ALL` is supported. Clients are free to ignore irrelevant events. For all supported events, see: https://apidocs.data.world/toolkit/webhooks

        :param events: The events of this Subscription.
        :type: list[str]
        """
        if events is None:
            raise ValueError("Invalid value for `events`, must not be `None`")
        allowed_values = ["ALL"]
        if not set(events).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `events` [{0}], must be a subset of [{1}]"
                .format(", ".join(map(str, set(events)-set(allowed_values))),
                        ", ".join(map(str, allowed_values)))
            )

        self._events = events

    @property
    def project(self):
        """
        Gets the project of this Subscription.

        :return: The project of this Subscription.
        :rtype: DatasetIdentifier
        """
        return self._project

    @project.setter
    def project(self, project):
        """
        Sets the project of this Subscription.

        :param project: The project of this Subscription.
        :type: DatasetIdentifier
        """

        self._project = project

    @property
    def user(self):
        """
        Gets the user of this Subscription.

        :return: The user of this Subscription.
        :rtype: UserIdentifier
        """
        return self._user

    @user.setter
    def user(self, user):
        """
        Sets the user of this Subscription.

        :param user: The user of this Subscription.
        :type: UserIdentifier
        """

        self._user = user

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
        if not isinstance(other, Subscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
