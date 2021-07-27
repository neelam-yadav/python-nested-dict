# python-nested-dict

## Overview
This repo contains a script which will help in fetching nested key values from a nested dictionary.

## Run Tests
Run below command in cmd:

    python -m unittest

## Run Script
On cmd, run below command:

    python nested_dict.py


## Usage
To use the script in other modules, use below snippet :

```
from nested_dict import get_nested_val

object = {"a": {"b": {"c": "d"}}}
key = "a/b/c"
val = get_nested_val(object, key)
```
