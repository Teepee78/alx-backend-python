#!/usr/bin/env python3
"""Test cases for utils module"""
from typing import Any, Mapping, Sequence
from unittest import TestCase
from unittest.mock import Mock, patch

from parameterized import parameterized, parameterized_class

from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(TestCase):
    """Tests utils.access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, output: Any):
        """Tests access_nested_map function return value"""
        self.assertEqual(access_nested_map(nested_map, path), output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
        self,
        nested_map: Mapping,
        path: Sequence,
        exception: Exception
    ) -> None:
        """Tests access_nested_map function raises exception"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """Tests utils.get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, input: str, output: Mapping) -> None:
        ret = {"json.return_value": output}
        with patch("requests.get", return_value=Mock(**ret)) as r:
            self.assertEqual(get_json(input), output)
            r.assert_called_once_with(input)


class TestMemoize(TestCase):
    """Tests utils.memoize function"""

    def test_memoize(self) -> None:
        """Tests memoized function is called only once"""
        class TestClass:
            """Test class"""

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
            TestClass,
            "a_method",
            return_value=lambda: 42
        ) as r:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            r.assert_called_once()
