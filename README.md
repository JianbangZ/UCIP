# User Context Interchange Protocol (UCIP)

[![GitHub License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/JianbangZ/ucip/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/JianbangZ/ucip.svg)](https://github.com/JianbangZ/ucip/issues)
[![GitHub Stars](https://img.shields.io/github/stars/JianbangZ/ucip.svg)](https://github.com/JianbangZ/ucip/stargazers)

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
   git clone https://github.com/JianbangZ/ucip.git cd ucip
2. **Compile Protobuf**:
   protoc –python_out=. ucip.proto  # Add –js_out=… for Node.js
3. **Install Dependencies**:
- Python: `pip install -r requirements.txt`
- Node.js: `npm install protobufjs`

4. **Validate and Test**:
Run `python validate.py` (assumes example.pb—generate via examples).

5. **Run API**:
   python api.py
   Access Swagger docs at http://localhost:8000/docs.

6. **Sync and Integrate**:
- Use WebSockets (e.g., Socket.io) for real-time device sync.
- Expose as MCP tool: Define endpoints like `/queryMood/{user_id}`.

### Python Example: Encode/Decode
```python
import ucip_pb2
from google.protobuf.json_format import MessageToJson

ucip = ucip_pb2.UCIP()
ucip.version = "1.0"
ucip.userId = "user-123"
ucip.timestamp = "2025-07-21T12:00:00Z"
ucip.consent.granted = True
ucip.consent.scopes.append("basic")
binary = ucip.SerializeToString()

# Decode
decoded = ucip_pb2.UCIP()
decoded.ParseFromString(binary)
print(MessageToJson(decoded))
```
### Node.js Example
```
const protobuf = require('protobufjs');
protobuf.load('ucip.proto', (err, root) => {
  const UCIP = root.lookupType('UCIP');
  const payload = { version: '1.0', userId: 'user-123', timestamp: '2025-07-21T12:00:00Z', consent: { granted: true, scopes: ['basic'] } };
  const message = UCIP.create(payload);
  const buffer = UCIP.encode(message).finish();
  const decoded = UCIP.decode(buffer);
  console.log(decoded);
});
```

### Contributing
1.  Fork and create a branch: git checkout -b feature/new.
2.  Commit: git commit -m 'Add feature'.
3.  Push and open a PR. Discuss major changes in issues first. Follow CODE_OF_CONDUCT.md.
### License
MIT - see LICENSE.
### Acknowledgments
Inspired by AI continuity needs and standards like MCP/A2A. Contributions welcome to evolve UCIP!
