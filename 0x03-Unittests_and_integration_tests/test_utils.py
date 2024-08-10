#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from typing import Mapping, Sequence, Any
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """
        Test that access_nested_map returns the expected result.

        Args:
            nested_map (Mapping): The nested map to access.
            path (Sequence): The path to the desired value.
            expected (Any): The expected result.

        Returns:
            None
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping,
                                         path: Sequence,
                                         expected_key: str) -> None:
        """
        Test access_nested_map raises a KeyError with the expected message.

        Args:
            nested_map (Mapping): The nested map to access.
            path (Sequence): The path that should raise a KeyError.
            expected_key (str): The expected key in the error message.

        Returns:
            None
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), f"'{expected_key}'")


if __name__ == '__main__':
    unittest.main()
