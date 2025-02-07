#### How to slice dictionary

Example scenario: taking top x k/v pair of a dictionary.

```python
a = {
    1:1
    2:2
    3:3
}

# convert to a list tuple first
a_list = list(a.items())
slice_list = a[:2]

```
