import unittest

from nested_dict import get_nested_val


class TestNestedVal(unittest.TestCase):

    def setUp(self):
        self.input_object = {"x": {"y": {"z": "a"}}}

    def test_valid_key(self):
        output = "a"
        keys = "x/y/z"

        result = get_nested_val(self.input_object, keys)

        # check if the result is equal to expected result
        self.assertEqual(result, output)

    def test_invalid_key(self):
        output = None
        keys = "x/y/x"

        result = get_nested_val(self.input_object, keys)

        # check if the result is equal to expected result
        self.assertEqual(result, output)


if __name__ == '__main__':
    unittest.main()
