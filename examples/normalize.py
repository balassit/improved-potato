import json

arr = []


def normalize(input):
    if type(input) == dict:
        if input.get("value"):
            arr.append(input.get("value"))
        if input.get("children"):
            normalize(input.get("children"))
    elif type(input) == list:
        for element in input:
            normalize(element)


input = [
    {"value": "value1", "children": [{"value": "value2"}, {"value": "value3"}]},
    {"value": "value4"},
]

normalize(input)
print(arr)
