
import json

jsonstring1 = """
            [
                {"e":"24hrMiniTicker","E":1,"s":"ETHUSDT","c":"1783.33000000","o":"1824.12000000","h":"1833.00000000",
                "l":"1745.01000000","v":"549714.84290000","q":"985569658.04603000"},
                {"e":"24hrMiniTicker","E":2,"s":"ETHUSDT","c":"1783.33000000","o":"1824.12000000","h":"1833.00000000",
                "l":"1745.01000000","v":"549714.84290000","q":"985569658.04603000"},
                {"e":"24hrMiniTicker","E":3,"s":"ETHUSDT","c":"1783.33000000","o":"1824.12000000","h":"1833.00000000",
                "l":"1745.01000000","v":"549714.84290000","q":"985569658.04603000"}
            ]
"""

print(jsonstring1)

# Loop Json Object
# Load JSON string into a dictionary
json_dicti = json.loads(jsonstring1)

"""
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)
"""


# Loop along dictionary keys
for x in json_dicti:
    print(x)
    # x değeri dictionary, dictionary değerleri index ile okunamaz bu sebeple list'e çeviririz
    # Convert to list
    keys_list = list(x)
    value_list = list(x.values())

    # Liste icinden index ile deger okuma
    key = keys_list[1]
    value = value_list[1]
