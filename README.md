# 🤖 Multi-Agent AI Framework

**Production-ready orchestration system for collaborative AI agents** using LangGraph, with advanced memory management, tool integration, and state synchronization for complex workflows.

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/langgraph-latest-green)](https://github.com/langchain-ai/langgraph)
[![FastAPI](https://img.shields.io/badge/fastapi-0.100%2B-green)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 🎯 Key Features

- **🤝 Multi-Agent Orchestration**: Coordinate multiple specialized agents with clear communication
- **🧠 Persistent Memory**: Long-term and short-term memory with semantic search
- **🔧 Tool Integration**: Extensible tool system with automatic registration & discovery
- **📊 State Management**: TypedDict-based state synchronization across agents
- **⚡ Async-Ready**: Fully async agent execution with proper concurrency handling
- **🔀 Workflow Patterns**: Sequential, parallel, conditional, and hierarchical execution
- **📈 Observability**: Complete tracing, logging, and monitoring for agent behaviors
- **🎯 Type Safety**: Full type hints for better IDE support and error catching
- **⚙️ Easy Configuration**: YAML-based agent and workflow configuration
- **🚀 Production-Ready**: Error handling, retries, and graceful degradation

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────┐
│              Multi-Agent Framework                   │
├─────────────────────────────────────────────────────┤
│  • Agent Orchestrator (LangGraph)                    │
│  • State Management (TypedDict + Reducers)           │
│  • Memory System (Short-term + Long-term)            │
│  • Tool Registry & Dispatcher                        │
│  • Error Handling & Retry Logic                      │
│  • Observability Layer (Logging, Tracing)            │
├─────────────────────────────────────────────────────┤
│ Specialized Agents:                                  │
│  • Research Agent - Gather & analyze information     │
│  • Planning Agent - Create execution strategies      │
│  • Execution Agent - Perform actions                 │
│  • Validation Agent - Verify & quality check         │
│  • Reporting Agent - Summarize & present findings    │
└─────────────────────────────────────────────────────┘
         ↓
    ┌─────────────────────┐
    │  Tool Ecosystem     │
    ├─────────────────────┤
    │ • Web Search        │
    │ • Database Query    │
    │ • API Calls         │
    │ • File Operations   │
    │ • Code Execution    │
    └─────────────────────┘
```

---

## 📦 Project Structure

```
multi-agent-ai-framework/
├── agents/
│   ├── __init__.py
│   ├── base_agent.py           # Base agent class with common logic
│   ├── research_agent.py        # Research & information gathering
│   ├── planning_agent.py        # Strategy & plan creation
│   ├── execution_agent.py       # Action execution
│   ├── validation_agent.py      # Quality assurance
│   └── reporting_agent.py       # Results compilation
├── tools/
│   ├── __init__.py
│   ├── base_tool.py             # Tool interface
│   ├── web_search.py            # Web search integration
│   ├── database.py              # Database operations
│   ├── api_client.py            # API integration
│   ├── file_ops.py              # File operations
│   └── code_executor.py         # Safe code execution
├── memory/
│   ├── __init__.py
│   ├── short_term.py            # Conversation memory
│   ├── long_term.py             # Persistent knowledge base
│   ├── semantic_search.py       # Vector-based retrieval
│   └── memory_manager.py        # Unified memory interface
├── orchestrator/
│   ├── __init__.py
│   ├── state.py                 # Shared state definitions
│   ├── reducer.py               # State reduction logic
│   ├── graph_builder.py         # LangGraph construction
│   ├── execution_engine.py      # Workflow execution
│   └── error_handler.py         # Error & retry handling
├── config/
│   ├── agent_config.yaml        # Agent configurations
│   └── tool_config.yaml         # Tool definitions
├── examples/
│   ├── research_workflow.py      # Example: Market research
│   ├── planning_workflow.py      # Example: Project planning
│   └── complex_workflow.py       # Example: Multi-stage workflow
├── tests/
│   ├── test_agents.py
│   ├── test_tools.py
│   ├── test_memory.py
│   └── test_orchestrator.py
├── requirements.txt
├── .env.example
├── docker-compose.yml
└── README.md
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- pip or Poetry
- Optional: Docker

### Installation

```bash
# Clone repository
git clone https://github.com/Neuro-kiran/multi-agent-ai-framework.git
cd multi-agent-ai-framework

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

```bash
cp .env.example .env
# Edit .env with your API keys and settings
```

### Run Example Workflow

```python
from orchestrator.execution_engine import ExecutionEngine
from config import load_config

# Load configuration
config = load_config('agent_config.yaml')

# Create execution engine
engine = ExecutionEngine(config)

# Execute workflow
result = await engine.execute(
    workflow='research_and_planning',
    input={'topic': 'AI trends 2025'}
)

print(result)
```

---

## 🧠 Agent Types

### 1. **Research Agent**
Gathers and analyzes information from multiple sources
- Tools: Web search, database queries, API calls
- Output: Structured findings and insights

### 2. **Planning Agent**
Creates strategies and execution plans
- Tools: Template rendering, outcome modeling
- Output: Actionable plan with milestones

### 3. **Execution Agent**
Performs actual tasks and operations
- Tools: API calls, code execution, file operations
- Output: Execution results with status

### 4. **Validation Agent**
Verifies quality and correctness
- Tools: Testing, validation rules, assertions
- Output: Quality report and compliance check

### 5. **Reporting Agent**
Compiles results into deliverable format
- Tools: Document generation, visualization
- Output: Report, presentation, summary

---

## 💾 Memory System

```python
# Short-term memory (Current conversation)
memory.short_term.add('user_preference', {'topic': 'AI', 'detail_level': 'advanced'})

# Long-term memory (Knowledge base)
memory.long_term.store('ai_trends', vector_embedding, metadata)

# Semantic search
results = memory.semantic_search('latest AI developments', top_k=5)
```

---

## 🔧 Tool Integration

```python
from tools.base_tool import BaseTool

class CustomTool(BaseTool):
    name = 'custom_tool'
    description = 'Does something specific'
    
    async def execute(self, **kwargs):
        # Implementation
        return result

# Automatically registered and available to agents
```

---

## 📊 Workflow Patterns

### Sequential
```
Agent A → Agent B → Agent C
```

### Parallel
```
  ↙ Agent A ↘
Start         Merge
  ↘ Agent B ↙
```

### Conditional
```
  ↙ Path 1 (if condition)
Agent A
  ↘ Path 2 (else)
```

### Hierarchical
```
Manager Agent
  ├─ Worker 1
  ├─ Worker 2
  └─ Worker 3
```

---

## 📈 Observability

```python
# Enable detailed logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Access execution trace
trace = result.execution_trace
for step in trace:
    print(f"{step.agent}: {step.action} → {step.result}")
```

---

## 🐳 Docker Support

```bash
# Build image
docker build -t multi-agent-framework:latest .

# Run container
docker run -p 8000:8000 --env-file .env multi-agent-framework:latest
```

---

## 🧪 Testing

```bash
pytest tests/ -v
pytest tests/ --cov=agents --cov=orchestrator
```

---

## 📚 Examples

### Market Research Workflow
- Research Agent gathers market data
- Analysis Agent processes insights
- Reporting Agent creates presentation

### Project Planning Workflow
- Planning Agent creates detailed plan
- Execution Agent schedules tasks
- Monitoring Agent tracks progress

### Customer Support Workflow
- Classifier Agent categorizes issue
- Resolver Agent finds solution
- Escalation Agent handles complex cases

---

## 🔐 Security Considerations

- ✅ Sandboxed code execution
- ✅ API key management via environment variables
- ✅ Rate limiting on external API calls
- ✅ Input validation and sanitization
- ✅ Audit logging for all actions

---

## 🚀 Deployment

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for:
- Kubernetes manifests
- CI/CD pipeline setup
- Scaling strategies
- Monitoring & alerting

---

## 📝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create feature branch: `git checkout -b feature/your-feature`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature/your-feature`
5. Open Pull Request

---

## 📄 License

MIT License - see [LICENSE](LICENSE)

---

## 👨‍💻 Author

**Kiran Marne** - AI/ML Engineer  
🔗 [GitHub](https://github.com/Neuro-kiran) | 📧 [Email](mailto:marne.kiran44@gmail.com)

---

## 📞 Support

Have questions? Open an [issue](https://github.com/Neuro-kiran/multi-agent-ai-framework/issues) or reach out!

---

## 🎯 Roadmap

- [ ] Web UI for workflow visualization
- [ ] Advanced scheduling system
- [ ] Multi-modal agent support (vision, audio)
- [ ] Reinforcement learning feedback loop
- [ ] Agent marketplace & plugins
- [ ] Real-time collaboration features
- [ ] GraphQL API endpoint
- [ ] Benchmark suite
