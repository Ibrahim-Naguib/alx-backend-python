#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    """Tests the access_nested_map function"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: int) -> None:
        """
        Test the access_nested_map method.

        Args:
            nested_map (Dict): A dictionary that may have nested dictionaries
            path (List, tuple, set): Keys to get to the required value in the
                                     nested dictionary
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence) -> None:
        """
        Test the access_nested_map method raises an error when expected to

        Args:
            nested_map (Dict): A dictionary that may have nested dictionaries
            path (List, tuple, set): Keys to get to the required value in the
                                     nested dictionary
        """
        with self.assertRaises(Exception):
            access_nested_map(nested_map, path)
