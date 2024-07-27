#!/usr/bin/env python3
"""Parameterize a unit test"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence, Any
from unittest.mock import patch
import requests


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


class TestGetJson(unittest.TestCase):
    """Test the get_json function"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(self, url, payload, mock_get):
        """
        Test the get_json method to ensure it returns the expected output.

        Args:
            url: url to send http request to
            payload: expected json response
        """
        mock_get.return_value.json.return_value = payload
        result = get_json(url)
        self.assertEqual(result, payload)
        mock_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """Test the memoization decorator memoize"""
    def test_memoize(self):
        """Test that utils.memoize decorator works as intended"""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_object:
            test = TestClass()
            test.a_property()
            test.a_property()
            mock_object.assert_called_once()
