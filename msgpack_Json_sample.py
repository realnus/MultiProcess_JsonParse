import msgpack

# Define data
data = {
    "a list": [1, 42, 3.141, 1337, "help"],
    "a string": "bla",
    "another dict": {"foo": "bar", "key": "value", "the answer": 42},
}

# Write msgpack file
with open("data.msgpack", "wb") as outfile:
    packed = msgpack.packb(data)
    outfile.write(packed)

# Read msgpack file
with open("data.msgpack", "rb") as data_file:
    byte_data = data_file.read()

data_loaded = msgpack.unpackb(byte_data)
print(data == data_loaded)
