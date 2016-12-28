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


class AreaCode(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, country_code=None, area_code=None, city=None, state=None, country=None, toll_free=None):
        """
        AreaCode - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'country_code': 'int',
            'area_code': 'int',
            'city': 'str',
            'state': 'str',
            'country': 'str',
            'toll_free': 'bool'
        }

        self.attribute_map = {
            'country_code': 'country_code',
            'area_code': 'area_code',
            'city': 'city',
            'state': 'state',
            'country': 'country',
            'toll_free': 'toll_free'
        }

        self._country_code = country_code
        self._area_code = area_code
        self._city = city
        self._state = state
        self._country = country
        self._toll_free = toll_free

    @property
    def country_code(self):
        """
        Gets the country_code of this AreaCode.

        :return: The country_code of this AreaCode.
        :rtype: int
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """
        Sets the country_code of this AreaCode.

        :param country_code: The country_code of this AreaCode.
        :type: int
        """

        self._country_code = country_code

    @property
    def area_code(self):
        """
        Gets the area_code of this AreaCode.

        :return: The area_code of this AreaCode.
        :rtype: int
        """
        return self._area_code

    @area_code.setter
    def area_code(self, area_code):
        """
        Sets the area_code of this AreaCode.

        :param area_code: The area_code of this AreaCode.
        :type: int
        """

        self._area_code = area_code

    @property
    def city(self):
        """
        Gets the city of this AreaCode.

        :return: The city of this AreaCode.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """
        Sets the city of this AreaCode.

        :param city: The city of this AreaCode.
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """
        Gets the state of this AreaCode.

        :return: The state of this AreaCode.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """
        Sets the state of this AreaCode.

        :param state: The state of this AreaCode.
        :type: str
        """

        self._state = state

    @property
    def country(self):
        """
        Gets the country of this AreaCode.

        :return: The country of this AreaCode.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """
        Sets the country of this AreaCode.

        :param country: The country of this AreaCode.
        :type: str
        """

        self._country = country

    @property
    def toll_free(self):
        """
        Gets the toll_free of this AreaCode.

        :return: The toll_free of this AreaCode.
        :rtype: bool
        """
        return self._toll_free

    @toll_free.setter
    def toll_free(self, toll_free):
        """
        Sets the toll_free of this AreaCode.

        :param toll_free: The toll_free of this AreaCode.
        :type: bool
        """

        self._toll_free = toll_free

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