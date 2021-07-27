# This script helps to get value of key from a nested dictionary.

from functools import reduce


def get_nested_val(dictionary, keys, default=None):
    """This function returns value from nested dictionary"""
    return reduce(lambda d, key: d.get(key, default) if isinstance(d, dict) else default, keys.split("/"), dictionary)


if __name__ == '__main__':
    object = {"a": {"b": {"c": "d"}}}
    key = "a/b/c"
    val = get_nested_val(object, key)
    print(val)
