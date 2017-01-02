# coding: utf-8

"""
    Phaxio API

    API Definition for Phaxio

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class PhoneNumber(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, phone_number=None, city=None, state=None, country=None, cost=None, last_billed_at=None, provisioned_at=None, callback_url=None):
        """
        PhoneNumber - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'phone_number': 'str',
            'city': 'str',
            'state': 'str',
            'country': 'str',
            'cost': 'int',
            'last_billed_at': 'datetime',
            'provisioned_at': 'datetime',
            'callback_url': 'str'
        }

        self.attribute_map = {
            'phone_number': 'phone_number',
            'city': 'city',
            'state': 'state',
            'country': 'country',
            'cost': 'cost',
            'last_billed_at': 'last_billed_at',
            'provisioned_at': 'provisioned_at',
            'callback_url': 'callback_url'
        }

        self._phone_number = phone_number
        self._city = city
        self._state = state
        self._country = country
        self._cost = cost
        self._last_billed_at = last_billed_at
        self._provisioned_at = provisioned_at
        self._callback_url = callback_url

    @property
    def phone_number(self):
        """
        Gets the phone_number of this PhoneNumber.

        :return: The phone_number of this PhoneNumber.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """
        Sets the phone_number of this PhoneNumber.

        :param phone_number: The phone_number of this PhoneNumber.
        :type: str
        """

        self._phone_number = phone_number

    @property
    def city(self):
        """
        Gets the city of this PhoneNumber.

        :return: The city of this PhoneNumber.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this PhoneNumber.

        :param city: The city of this PhoneNumber.
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """
        Gets the state of this PhoneNumber.

        :return: The state of this PhoneNumber.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this PhoneNumber.

        :param state: The state of this PhoneNumber.
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """
        Gets the country of this PhoneNumber.

        :return: The country of this PhoneNumber.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this PhoneNumber.

        :param country: The country of this PhoneNumber.
        :type: str
        """

        self._country = country

    @property
    def cost(self):
        """
        Gets the cost of this PhoneNumber.

        :return: The cost of this PhoneNumber.
        :rtype: int
        """
        return self._cost

    @cost.setter
    def cost(self, cost):
        """
        Sets the cost of this PhoneNumber.

        :param cost: The cost of this PhoneNumber.
        :type: int
        """

        self._cost = cost

    @property
    def last_billed_at(self):
        """
        Gets the last_billed_at of this PhoneNumber.

        :return: The last_billed_at of this PhoneNumber.
        :rtype: datetime
        """
        return self._last_billed_at

    @last_billed_at.setter
    def last_billed_at(self, last_billed_at):
        """
        Sets the last_billed_at of this PhoneNumber.

        :param last_billed_at: The last_billed_at of this PhoneNumber.
        :type: datetime
        """

        self._last_billed_at = last_billed_at

    @property
    def provisioned_at(self):
        """
        Gets the provisioned_at of this PhoneNumber.

        :return: The provisioned_at of this PhoneNumber.
        :rtype: datetime
        """
        return self._provisioned_at

    @provisioned_at.setter
    def provisioned_at(self, provisioned_at):
        """
        Sets the provisioned_at of this PhoneNumber.

        :param provisioned_at: The provisioned_at of this PhoneNumber.
        :type: datetime
        """

        self._provisioned_at = provisioned_at

    @property
    def callback_url(self):
        """
        Gets the callback_url of this PhoneNumber.

        :return: The callback_url of this PhoneNumber.
        :rtype: str
        """
        return self._callback_url

    @callback_url.setter
    def callback_url(self, callback_url):
        """
        Sets the callback_url of this PhoneNumber.

        :param callback_url: The callback_url of this PhoneNumber.
        :type: str
        """

        self._callback_url = callback_url

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
