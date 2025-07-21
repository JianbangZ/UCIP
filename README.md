# UCIP
User Context Interchange Protocol for Agentic AI Applications
# User Context Interchange Protocol (UCIP)

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/ucip/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/yourusername/ucip.svg)](https://github.com/yourusername/ucip/issues)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/ucip.svg)](https://github.com/yourusername/ucip/stargazers)

## Overview

UCIP is an open protocol for compactly representing user context (e.g., habits, mood, location) in multi-device AI experiences. It's optimized for LLMs and agents, with compatibility for MCP and A2A.

Key Enhancements (v1.1):
- **Lightweight**: Uses Protobuf for binary serialization (compact, fast).
- **Secure**: E2EE with AES-256, JWT auth, and consent enforcement.
- **Developer-Friendly**: Multi-language examples, easy API integration.

### Use Cases
- Multi-device AI continuity.
- LLM prompt injection: "User mood: [decode UCIP.currentState.mood]".
- Agent memory via MCP/A2A.

## Features
- Compact binary format.
- Privacy: Consent scopes, encryption.
- Extensible: Custom fields.

## Protobuf Schema (ucip.proto)

See [ucip.proto](./ucip.proto) for the full definition.

### Example UCIP Message (Protobuf)
Compile with `protoc --python_out=. ucip.proto`, then use in code.

## Setup and Installation

### Prerequisites
- Python 3.12+ (for examples).
- `protoc` compiler.
- Dependencies: `pip install -r requirements.txt`.

### Quick Start
1. Clone: `git clone https://github.com/yourusername/ucip.git && cd ucip`
2. Compile Protobuf: `protoc --python_out=. ucip.proto`
3. Run validation: `python validate.py`
4. Start API: `python api.py` (access at http://localhost:8000/docs)

### Python Example: Encode/Decode UCIP
```python
import ucip_pb2  # Generated from ucip.proto
from google.protobuf.json_format import MessageToJson, Parse

# Create message
ucip = ucip_pb2.UCIP()
ucip.version = "1.0"
ucip.userId = "user-123"
ucip.timestamp = "2025-07-21T12:00:00Z"
ucip.consent.granted = True
ucip.consent.scopes.append("basic")

# Serialize to binary
binary_data = ucip.SerializeToString()

# Deserialize
decoded = ucip_pb2.UCIP()
decoded.ParseFromString(binary_data)

# To JSON (for LLM prompts)
json_str = MessageToJson(decoded)
print(json_str)
