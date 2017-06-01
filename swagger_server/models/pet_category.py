# coding: utf-8

from __future__ import absolute_import
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class PetCategory(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, id: int=None, name: str=None):
        """
        PetCategory - a model defined in Swagger

        :param id: The id of this PetCategory.
        :type id: int
        :param name: The name of this PetCategory.
        :type name: str
        """
        self.swagger_types = {
            'id': int,
            'name': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name'
        }

        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt) -> 'PetCategory':
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The pet_category of this PetCategory.
        :rtype: PetCategory
        """
        return deserialize_model(dikt, cls)

    @property
    def id(self) -> int:
        """
        Gets the id of this PetCategory.

        :return: The id of this PetCategory.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id: int):
        """
        Sets the id of this PetCategory.

        :param id: The id of this PetCategory.
        :type id: int
        """

        self._id = id

    @property
    def name(self) -> str:
        """
        Gets the name of this PetCategory.

        :return: The name of this PetCategory.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """
        Sets the name of this PetCategory.

        :param name: The name of this PetCategory.
        :type name: str
        """

        self._name = name

