#!/usr/bin/env python3
"""Module for testing the get_json function from utils."""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from typing import Dict, Any
from utils import get_json


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('requests.get')
    def test_get_json(self, test_url: str, test_payload: Dict[str, Any],
                      mock_get: Mock) -> None:
        """
        Test that utils.get_json returns the expected result.

        Args:
            test_url (str): The URL to test.
            test_payload (Dict[str, Any]): The expected payload.
            mock_get (Mock): The mocked requests.get function.

        Returns:
            None
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
