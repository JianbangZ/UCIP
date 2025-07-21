import ucip_pb2  # Assumes compiled from ucip.proto
from google.protobuf import text_format

def validate_ucip(binary_data):
    ucip = ucip_pb2.UCIP()
    try:
        ucip.ParseFromString(binary_data)
        print("Validation successful!")
        print(text_format.MessageToString(ucip))
    except Exception as e:
        print(f"Validation failed: {e}")

# Example usage: Load from file
with open('example.pb', 'rb') as f:  # Assume you have an example.pb
    binary_data = f.read()
validate_ucip(binary_data)
