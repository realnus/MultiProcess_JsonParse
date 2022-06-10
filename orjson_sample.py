from random import sample
import orjson

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

print(sample_data)

# Loop Json Object
# Load JSON string into a dictionary
json_dicti = json.loads(jsonstring1)

# Loop along dictionary keys
for key in json_dicti:
    print(key, ":", json_dicti[key])
