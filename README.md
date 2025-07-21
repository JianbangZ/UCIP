# UCIP
User Context Interchange Protocol for Agentic AI Applications
# User Context Interchange Protocol (UCIP)

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/ucip/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/yourusername/ucip.svg)](https://github.com/yourusername/ucip/issues)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/ucip.svg)](https://github.com/yourusername/ucip/stargazers)

## Overview

UCIP is an open protocol for compactly representing user context (e.g., habits, mood, location) in multi-device AI experiences. It's optimized for LLMs and agents, with compatibility for MCP and A2A.
# User Context Interchange Protocol (UCIP)

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/yourusername/ucip/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/yourusername/ucip.svg)](https://github.com/yourusername/ucip/issues)
[![GitHub Stars](https://img.shields.io/github/stars/yourusername/ucip.svg)](https://github.com/yourusername/ucip/stargazers)

## Overview

The User Context Interchange Protocol (UCIP) is an open-source, lightweight protocol designed to enable seamless, multi-device continuous AI experiences by compactly storing and sharing user context information. In an era where users interact with AI across smartphones, laptops, smart home devices, and more, UCIP acts as a "digital twin" for the user—capturing essential details like demographics, habits, historical interactions, current mood, location, and inferred intentions.

UCIP addresses key challenges in AI ecosystems:
- **Fragmentation**: Traditional AI assistants often lose context when switching devices, leading to repetitive queries and poor personalization.
- **Efficiency for AI**: Large Language Models (LLMs) and agents require concise, relevant input to avoid high token costs and latency. UCIP provides structured, injectable data (e.g., for prompts like "User is stressed in San Francisco—suggest activities").
- **Interoperability**: Built with compatibility for emerging standards like Model Context Protocol (MCP) for data access and Agent-to-Agent Protocol (A2A) for secure sharing between agents.
- **Privacy and Security**: Emphasizes user consent, encryption, and data minimization to comply with regulations like GDPR and build trust.

Originally conceptualized as a JSON schema, UCIP v1.1 evolves to use Protocol Buffers (Protobuf) as the core format for extreme lightness (3-10x smaller payloads than JSON), faster serialization, and better performance in resource-constrained environments. JSON exports are supported for LLM compatibility. This makes UCIP ideal for edge computing, real-time agentic workflows, and proactive AI applications.

UCIP is not a full-fledged product but a protocol/schema with reference implementations (e.g., API, validation scripts). It's extensible, allowing custom fields for domain-specific needs (e.g., health biometrics or e-commerce preferences).

### Why UCIP?
- **Novelty**: No exact equivalent exists for AI-specific user context schemas. It draws from standards like schema.org/Person and ontology-based modeling but is optimized for multi-device AI continuity.
- **Benefits**: Reduces AI hallucinations, enables proactive suggestions (e.g., based on mood), and supports distributed systems with low overhead.

## Key Use Cases

UCIP shines in scenarios requiring persistent, shared user state for personalized AI:

- **Multi-Device Continuity**: A user starts a conversation on their phone ("Plan my vacation") and switches to a laptop—UCIP syncs history and intentions seamlessly, avoiding restarts.
- **LLM Prompt Engineering**: Inject UCIP data into prompts for context-aware responses, e.g., "Given user habits [UCIP.habits] and current mood [UCIP.currentState.mood], recommend a routine."
- **AI Agent Workflows**: Agents query UCIP via MCP (e.g., "getUserLocation") or share updates via A2A, enabling collaborative tasks like a travel agent coordinating with a calendar agent.
- **Personalized Recommendations**: In apps like fitness trackers, use inferred insights (e.g., personality traits) to tailor suggestions, with real-time updates from biometrics.
- **Health and Wellness Assistants**: Track mood/emotion scores over time, inferring long-term goals while ensuring sensitive data (e.g., location) is encrypted and consent-scoped.
- **Enterprise AI**: For customer service bots, maintain conversation summaries across sessions, improving efficiency in multi-agent systems.
- **IoT Integrations**: Smart homes use UCIP's currentState to automate actions, like dimming lights if mood is "stressed," with lightweight binary transfers for low-bandwidth devices.

These use cases leverage UCIP's compactness to minimize latency and costs in high-volume AI interactions.

## Features

- **Lightweight Design**: Protobuf-based for binary efficiency—compact payloads (e.g., <500 bytes typical), fast encoding/decoding, and low memory usage. Supports delta updates for minimal transmissions.
- **Structured User Representation**: Hierarchical fields covering basic info, preferences, habits, history, current state, inferred insights, and custom extensions.
- **LLM/Agent-Friendly**: Easy serialization to JSON for prompts; queryable subsets for agents (e.g., via MCP endpoints).
- **Privacy-First**: Built-in consent metadata (scopes, expiration), data source tracking (user vs. inferred), and minimization guidelines. Supports anonymization and bias flags.
- **Security Enhancements**: End-to-end encryption (AES-256), JWT authentication, input validation, and audit logging to protect against breaches and unauthorized access.
- **Extensibility**: CustomData map for app-specific fields; backward-compatible schema evolution.
- **Real-Time Capabilities**: Timestamps and ephemeral state fields for frequent updates; integrable with WebSockets for sync.
- **Cross-Language Support**: Protobuf generates code for Python, JS, Java, etc.; examples provided.
- **Compactness Tools**: Enums for efficiency (e.g., habit frequency), array caps, and LLM summarization hooks for history.

## Protobuf Schema

Defined in [ucip.proto](./ucip.proto). Key messages include UCIP (root), Consent, BasicInfo, etc. Use enums for categorical data to save space.

### Example UCIP Message

See Python/Node.js snippets below for creation. Serialized binary is compact; export to JSON for readability.

## Setup and Installation

### Prerequisites
- Protobuf compiler (`protoc`—install via package manager).
- Python/Node.js for examples.
- Dependencies: See [requirements.txt](./requirements.txt) for Python.

### Quick Start
1. **Clone the Repo**:
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
