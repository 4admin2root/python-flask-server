# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class Person(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name: str=None, single: bool=None):
        """
        Person - a model defined in Swagger

        :param name: The name of this Person.
        :type name: str
        :param single: The single of this Person.
        :type single: bool
        """
        self.swagger_types = {
            'name': str,
            'single': bool
        }

        self.attribute_map = {
            'name': 'name',
            'single': 'single'
        }

        self._name = name
        self._single = single

    @classmethod
    def from_dict(cls, dikt) -> 'Person':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Person of this Person.
        :rtype: Person
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """
        Gets the name of this Person.

        :return: The name of this Person.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this Person.

        :param name: The name of this Person.
        :type name: str
        """

        self._name = name

    @property
    def single(self) -> bool:
        """
        Gets the single of this Person.

        :return: The single of this Person.
        :rtype: bool
        """
        return self._single

    @single.setter
    def single(self, single: bool):
        """
        Sets the single of this Person.

        :param single: The single of this Person.
        :type single: bool
        """

        self._single = single

