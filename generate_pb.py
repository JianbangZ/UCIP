import ucip_pb2
from google.protobuf.json_format import MessageToJson

ucip = ucip_pb2.UCIP()
ucip.version = "1.0"
ucip.userId = "user-123"
ucip.timestamp = "2025-07-21T12:00:00Z"
ucip.consent.granted = True
ucip.consent.scopes.append("basic")
binary = ucip.SerializeToString()

# Write to file
with open('example.pb', 'wb') as f:
    f.write(binary)
    
# Decode
decoded = ucip_pb2.UCIP()
decoded.ParseFromString(binary)
print(MessageToJson(decoded))