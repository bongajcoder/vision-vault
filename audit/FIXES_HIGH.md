# ⚠️ HIGH PRIORITY FIXES - Vision Vault
**Priority:** Important for functionality - Should complete within 1-2 weeks
**Estimated Total Effort:** 32-40 hours

---

## 1. IMPLEMENT REMAINING AI AGENTS

**Problem:** Only 2 of 6+ planned agents exist (base_agent, conflict_detector)
- Multi-modal agents missing (text, visual, audio, video)
- Decision support agent missing
- Resource optimizer missing
- Risk identifier missing
- Completeness checker missing

**Impact:** Core intelligence features don't work

**Solution:** Implement remaining agents based on documented architecture

**Files to create:**
```
agents/
├── text_agent.py              # Text document analysis
├── visual_agent.py            # Image/concept art analysis
├── audio_agent.py             # Sound design analysis
├── video_agent.py             # Footage analysis
├── decision_support.py        # Decision analysis across dimensions
├── resource_optimizer.py      # Resource allocation optimization
├── risk_identifier.py         # Risk identification and assessment
└── completeness_checker.py    # Production readiness verification
```

**Example implementation** (text_agent.py):
```python
"""Text document analysis agent."""

from typing import Dict, Any, List
from ..core.ai.claude_client import ClaudeClient
from .base_agent import DocumentProcessingAgent


class TextAgent(DocumentProcessingAgent):
    """
    Analyzes text documents (scripts, notes, briefs).

    Capabilities:
    - Script analysis (structure, characters, themes)
    - Document summarization
    - Entity extraction (characters, locations, props)
    - Sentiment analysis
    - Consistency checking
    """

    def __init__(self, agent_id=None, config=None):
        super().__init__(agent_id, config)
        self.ai_client = ClaudeClient()

    def get_capabilities(self) -> List[str]:
        return [
            "script_analysis",
            "document_summarization",
            "entity_extraction",
            "sentiment_analysis",
            "consistency_checking",
        ]

    async def process(
        self, input_data: Any, context: Dict[str, Any] = None
    ) -> Dict[str, Any]:
        """Process text document."""
        document_text = input_data
        department = context.get("department") if context else None

        # Analyze with AI
        analysis = await self._analyze_text(document_text, department)

        return {
            "analysis": analysis,
            "agent_type": "text",
            "capabilities_used": self.get_capabilities(),
        }

    async def _analyze_text(
        self, text: str, department: str = None
    ) -> Dict[str, Any]:
        """Use AI to analyze text."""
        prompt = self._build_analysis_prompt(text, department)
        result = await self.ai_client.query(prompt, max_tokens=2000)

        return {
            "summary": result["response"],
            "usage": result["usage"],
        }

    def _build_analysis_prompt(self, text: str, department: str) -> str:
        """Build AI prompt for text analysis."""
        dept_context = f"This is a {department} department document." if department else ""

        return f"""Analyze this production document:

{dept_context}

Document:
{text[:3000]}... (truncated if longer)

Provide:
1. Brief summary (2-3 sentences)
2. Key topics and themes
3. Main decisions or requirements
4. Departments involved or affected
5. Any potential issues or conflicts
6. Missing information or questions

Format as structured JSON.
"""
```

**Effort:** 20-24 hours (2-3 hours per agent)

---

## 2. CREATE COMPREHENSIVE TEST SUITE

**Problem:** Zero tests exist
- No unit tests
- No integration tests
- No end-to-end tests
- 0% code coverage

**Impact:** Cannot verify code works, high risk of regressions

**Solution:** Create test suite with >80% coverage

**Structure:**
```
tests/
├── __init__.py
├── conftest.py                # Pytest fixtures
├── unit/
│   ├── test_base_agent.py
│   ├── test_conflict_detector.py
│   ├── test_claude_client.py
│   ├── test_cost_tracker.py
│   ├── test_cache_manager.py
│   ├── test_knowledge_storage.py
│   └── test_document_parser.py
├── integration/
│   ├── test_document_ingestion.py
│   ├── test_ai_integration.py
│   └── test_agent_pipeline.py
└── e2e/
    └── test_full_workflow.py
```

**Example test** (test_base_agent.py):
```python
"""Tests for base agent."""

import pytest
from agents.base_agent import BaseAgent


class MockAgent(BaseAgent):
    """Mock agent for testing."""

    def process(self, input_data, context=None):
        return {"result": "mock", "input": input_data}

    def get_capabilities(self):
        return ["mock_capability"]


def test_agent_initialization():
    """Test agent can be initialized."""
    agent = MockAgent()
    assert agent.agent_id is not None
    assert isinstance(agent.processing_history, list)
    assert len(agent.processing_history) == 0


def test_agent_process_safe():
    """Test safe processing wrapper."""
    agent = MockAgent()
    result = agent.process_safe({"test": "data"})

    assert result["success"] is True
    assert "data" in result
    assert result["data"]["result"] == "mock"


def test_agent_validation_failure():
    """Test validation error handling."""
    agent = MockAgent()
    result = agent.process_safe(None)  # Invalid input

    assert result["success"] is False
    assert "error" in result
    assert result["error_type"] == "ValidationError"


def test_agent_logging():
    """Test processing history logging."""
    agent = MockAgent()
    agent.process_safe({"test": "data"})

    assert len(agent.processing_history) == 1
    assert "timestamp" in agent.processing_history[0]
    assert "duration_seconds" in agent.processing_history[0]


@pytest.mark.asyncio
async def test_agent_with_ai(mock_claude_client):
    """Test agent with mocked AI client."""
    # Test AI integration without hitting real API
    pass
```

**conftest.py:**
```python
"""Pytest configuration and fixtures."""

import pytest
from unittest.mock import Mock, AsyncMock


@pytest.fixture
def mock_claude_client():
    """Mock Claude API client."""
    client = Mock()
    client.query = AsyncMock(return_value={
        "response": "Mock AI response",
        "usage": {"input_tokens": 100, "output_tokens": 50},
        "model": "claude-sonnet-4",
        "cached": False,
    })
    return client


@pytest.fixture
def mock_knowledge_storage():
    """Mock knowledge storage."""
    storage = Mock()
    storage.add_document = Mock()
    storage.search = Mock(return_value={
        "documents": ["Test document"],
        "ids": ["DOC-001"],
        "distances": [0.1],
        "metadatas": [{"department": "Cinematography"}],
    })
    return storage


@pytest.fixture
def sample_metadata():
    """Sample document metadata."""
    return {
        "production": "Test Film",
        "department": "Cinematography",
        "creator": "Test DP",
        "version": 1,
        "status": "Draft",
    }
```

**Run tests:**
```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-cov pytest-mock

# Run all tests with coverage
pytest --cov=vision_vault --cov-report=html --cov-report=term

# Run only unit tests
pytest tests/unit/

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/unit/test_base_agent.py
```

**Effort:** 12-16 hours

---

## 3. CREATE CRITICAL DOCUMENTATION

**Problem:** Missing CLAUDE.md and CLAUDE_CODE_INSTRUCTIONS.md
- New developers can't understand project
- Can't set up development environment
- No context for Claude Code assistant

**Impact:** High friction for development and onboarding

**Solution:** Create comprehensive setup documentation

**CLAUDE.md:**
```markdown
# Vision Vault

## Overview
Vision Vault is an AI-powered knowledge integration system for film and television production. It serves as "connective tissue" for all production knowledge across departments - from pre-production planning through post-production delivery.

## Core Problem
Film productions generate massive amounts of information across 30+ departments:
- Scripts, storyboards, shot lists
- Budgets, schedules, call sheets
- Location scouts, equipment lists
- Costume designs, set plans
- Daily reports, notes, decisions

This information is scattered across:
- Google Docs, Sheets, Drive
- Email threads
- Department-specific software
- People's heads

**Result:** Critical information is lost, conflicts arise, and teams work in silos.

## Solution
Vision Vault provides:
1. **Centralized Knowledge Base** - One source of truth for all production info
2. **AI-Powered Intelligence** - Understand context, detect conflicts, support decisions
3. **Department-Specific Modules** - Specialized knowledge for each department
4. **Natural Language Queries** - Ask questions in plain English
5. **Conflict Detection** - Automatically identify schedule, budget, creative conflicts
6. **Decision Support** - Analyze decisions across creative, technical, financial dimensions

## Tech Stack

**Core:**
- Python 3.11+
- Claude Sonnet 4 (primary AI)
- ChromaDB (vector storage for knowledge)
- FastAPI (API server)
- Pydantic (data validation)

**AI & ML:**
- Anthropic Claude API (reasoning and analysis)
- Vector embeddings (semantic search)
- Cost tracking (<$50/month target)
- Intelligent caching (80%+ cache hit rate)

**Storage:**
- ChromaDB for vector storage (local/simple)
- JSON files for configuration
- File system for documents

**Integrations:**
- Google Workspace (Drive, Docs, Sheets)
- PDF, Word, Excel parsing
- Future: Frame.io, ShotGrid

## Architecture

6-layer architecture:

1. **User Interface Layer** - CLI, Web dashboard
2. **AI Intelligence Layer** - Specialized agents (6+ types)
3. **Core Engine Layer** - Knowledge base, query processing
4. **Department Module Layer** - Pluggable department configs (30+)
5. **Integration Layer** - Google Workspace, external systems
6. **Data Storage Layer** - Vector DB, file storage

## Key Concepts

**Department Modules:**
- YAML-based configuration files
- Define knowledge foundations, workflows, collaboration patterns
- Examples: Cinematography, Directing, Production Design
- 30+ departments planned (indie to studio scale)

**AI Agents:**
- Specialized processors for different tasks
- Multi-modal: text, visual, audio, video
- Conflict detection, decision support, resource optimization
- Communicate via standardized message protocol

**Knowledge Base:**
- Vector database for semantic search
- Document metadata (JSON Schema with 30+ fields)
- Department-specific organization
- Cross-departmental relationship mapping

## Project Structure
```
vision-vault/
├── agents/              # AI agent implementations
├── config/              # JSON/YAML configuration files
├── core/                # Core engine (knowledge base, AI, processing)
├── departments/         # Department module YAML configs
├── docs/                # User and developer documentation
├── integrations/        # External system integrations
├── templates/           # Document and query templates
├── utils/               # Utility functions
└── tests/               # Test suite
```

## Development Status

**Current Phase:** Foundation Building (20% complete)
- ✅ Architecture designed
- ✅ Base agent framework
- ✅ Metadata schema
- ✅ Department research (15+ departments)
- ⚠️ Claude integration (in progress)
- ⚠️ Knowledge storage (in progress)
- ⏳ Remaining agents (pending)
- ⏳ Query system (pending)
- ⏳ Web UI (pending)

## Cost Model

Target: <$50/month for AI at production scale

**Strategy:**
1. **Aggressive caching** (80-90% cache hit rate)
2. **Smart model selection** (Haiku for simple, Sonnet for complex)
3. **Query optimization** (compress prompts, structured outputs)
4. **Pre-computed knowledge** (store in vector DB, not AI)

**Estimated:**
- 100 queries/day = 3,000/month
- 85% cache hit rate = 450 AI calls
- Average 1,500 tokens per call = 675K tokens/month
- At $3/1M tokens (Sonnet) = **~$2/month** ✅

## Bongani Labs Ecosystem

Vision Vault is part of the Bongani Labs suite:
- **Universal Writers Room** - AI writing assistant
- **Knowledge Keeper** - General knowledge management
- **Session Manager** - Context preservation across sessions
- **Social Distributor** - Content distribution
- **Domain Generator** - Web project scaffolding

**Synergies:**
- Shared AI agent framework
- Common cost tracking
- Unified authentication
- Vision Vault is film-focused Knowledge Keeper

## Next Steps

**Immediate (Week 1-2):**
1. Complete Claude SDK integration
2. Implement knowledge storage
3. Build document ingestion
4. Create simple query system
5. Add remaining agents

**Near-term (Week 3-6):**
1. Complete all 6 agent types
2. Build department module loader
3. Create CLI interface
4. Add comprehensive error handling
5. Write test suite

**Medium-term (Week 7-10):**
1. Web dashboard
2. Google Workspace integration
3. Production deployment
4. Beta testing
5. User documentation

## Success Metrics

**MVP:**
- Upload production documents ✅
- Query knowledge base ✅
- Accurate, relevant answers ✅
- Detect basic conflicts ✅
- Costs <$50/month ✅

**Production:**
- Used by 1+ real production ✅
- Saves teams >10 hours/week ✅
- <5 critical bugs/month ✅
- 95%+ uptime ✅
- User satisfaction >8/10 ✅
```

**CLAUDE_CODE_INSTRUCTIONS.md:**
```markdown
# Vision Vault - Setup & Development Guide

## Quick Start (< 30 minutes)

### Prerequisites
- Python 3.11 or higher
- Anthropic API key (get from https://console.anthropic.com/)
- 8GB RAM minimum
- 2GB disk space

### Setup Steps

1. **Clone repository**
```bash
git clone https://github.com/bongani-labs/vision-vault.git
cd vision-vault
```

2. **Create virtual environment**
```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Configure environment**
```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your API key:
# ANTHROPIC_API_KEY=sk-ant-api03-...
```

5. **Initialize knowledge base**
```bash
python -m vision_vault.scripts.init_kb
```

6. **Run tests** (verify installation)
```bash
pytest
```

7. **Start application**
```bash
# CLI mode:
python -m vision_vault.cli

# API server mode:
uvicorn vision_vault.main:app --reload
```

### Verify Setup

```bash
# Test Claude API connection
python -c "from core.ai.claude_client import ClaudeClient; print(ClaudeClient().get_usage_stats())"

# Test knowledge storage
python -c "from core.knowledge_base.storage import KnowledgeStorage; print(KnowledgeStorage().get_stats())"
```

## Project Structure

```
vision-vault/
├── agents/              # AI agent implementations
│   ├── base_agent.py         # Abstract base class for all agents
│   ├── conflict_detector.py  # Detects conflicts between departments
│   ├── text_agent.py         # Text document analysis
│   ├── visual_agent.py       # Image/concept art analysis
│   └── ...                   # Other specialized agents
│
├── config/              # Configuration files
│   ├── metadata-schema.json      # JSON Schema for document metadata
│   └── document-classification.yaml  # Document types and categories
│
├── core/                # Core engine
│   ├── ai/
│   │   ├── claude_client.py  # Claude API client with caching
│   │   ├── cost_tracker.py   # Track AI costs
│   │   └── cache_manager.py  # Response caching
│   ├── knowledge_base/
│   │   ├── storage.py        # Vector database storage
│   │   ├── indexer.py        # Document indexing
│   │   └── retriever.py      # Knowledge retrieval
│   ├── document_processor/
│   │   ├── ingester.py       # Document ingestion pipeline
│   │   └── parser.py         # Multi-format parsing
│   └── query_engine/
│       ├── parser.py         # Query understanding
│       └── executor.py       # Query execution
│
├── departments/         # Department modules (YAML configs)
│   ├── cinematography.yaml   # Cinematography knowledge
│   ├── directing.yaml        # Directing knowledge
│   └── ...                   # 30+ department modules
│
├── integrations/        # External system integrations
│   └── google_workspace/     # Google Drive, Docs, Sheets
│
├── tests/               # Test suite
│   ├── unit/                 # Unit tests
│   ├── integration/          # Integration tests
│   └── e2e/                  # End-to-end tests
│
└── docs/                # Documentation
    ├── USER_GUIDE.md         # User documentation
    ├── API.md                # API reference
    └── DEPLOYMENT.md         # Deployment guide
```

## Development Workflow

### Adding a New Agent

1. Create agent file in `agents/`:
```python
from .base_agent import BaseAgent

class MyNewAgent(BaseAgent):
    def get_capabilities(self):
        return ["my_capability"]

    async def process(self, input_data, context=None):
        # Implementation
        return {"result": "..."}
```

2. Add tests in `tests/unit/`:
```python
def test_my_new_agent():
    agent = MyNewAgent()
    result = agent.process_safe({"test": "data"})
    assert result["success"] is True
```

3. Register in `agents/__init__.py`:
```python
from .my_new_agent import MyNewAgent
__all__ = [..., "MyNewAgent"]
```

### Adding a Department Module

1. Create YAML file in `departments/`:
```yaml
department:
  code: "XXX"
  name: "Department Name"
  description: "..."

knowledge_foundation:
  core_concepts:
    - concept: "..."
      key_elements: [...]

workflow:
  pre_production: [...]
  production: [...]
  post_production: [...]
```

2. Validate with schema (TODO: create validation script)

### Running Tests

```bash
# All tests
pytest

# With coverage
pytest --cov=vision_vault --cov-report=html

# Specific test file
pytest tests/unit/test_base_agent.py

# With verbose output
pytest -v

# Watch mode (re-run on file changes)
pytest-watch
```

### Code Quality

```bash
# Format code
black .

# Sort imports
isort .

# Type checking
mypy agents/ core/

# Linting
pylint vision_vault/
flake8 .
```

### Debugging

```bash
# Enable debug logging
export LOG_LEVEL=DEBUG

# Run with debugger
python -m pdb -m vision_vault.cli

# Interactive Python shell with app context
python -i -m vision_vault.shell
```

## Common Tasks

### Upload a Document
```python
from core.document_processor.ingester import DocumentIngester
from core.knowledge_base.storage import KnowledgeStorage

storage = KnowledgeStorage()
ingester = DocumentIngester(storage)

result = await ingester.ingest_file(
    Path("script.pdf"),
    metadata={"department": "Writing", "version": 1}
)
```

### Query Knowledge Base
```python
from core.knowledge_base.storage import KnowledgeStorage

storage = KnowledgeStorage()
results = storage.search(
    query="What is the lighting plan for Scene 12?",
    where={"department": "Cinematography"}
)
```

### Check AI Costs
```python
from core.ai.cost_tracker import CostTracker

tracker = CostTracker()
print(tracker.get_stats())
# Output: {'current_spend': 2.45, 'budget_remaining': 47.55, ...}
```

## Troubleshooting

### "ModuleNotFoundError: No module named 'anthropic'"
- Solution: `pip install -r requirements.txt`

### "ANTHROPIC_API_KEY not found"
- Solution: Add to `.env` file: `ANTHROPIC_API_KEY=sk-ant-...`

### "ChromaDB permission denied"
- Solution: Check `data/chroma` directory permissions
- Or: Delete and reinitialize: `rm -rf data/chroma && python -m vision_vault.scripts.init_kb`

### Tests failing with "AsyncIO error"
- Solution: Install `pytest-asyncio`: `pip install pytest-asyncio`
- Add to `pyproject.toml`: `asyncio_mode = "auto"`

### AI costs too high
- Check cache hit rate: Should be >80%
- Review `MAX_MONTHLY_AI_COST` in `.env`
- Use Haiku model for simple queries

## Deployment

See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for production deployment instructions.

Quick deploy to Railway:
```bash
railway login
railway up
```

## Contributing

1. Create feature branch: `git checkout -b feature/my-feature`
2. Write tests for new functionality
3. Ensure all tests pass: `pytest`
4. Format code: `black . && isort .`
5. Type check: `mypy agents/ core/`
6. Commit and push
7. Open pull request

## Resources

- [Claude API Documentation](https://docs.anthropic.com/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pytest Documentation](https://docs.pytest.org/)
```

**Effort:** 4-6 hours

---

## 4. IMPLEMENT MODEL ROUTER & COST OPTIMIZATION

**Problem:** No intelligent model routing
- Always uses same AI model regardless of query complexity
- No fallback to cheaper models
- No offline/local AI option
- Costs not optimized

**Impact:** Higher AI costs than necessary

**Solution:** Create model router to select optimal model per query

Create `/home/user/vision-vault/core/ai/model_router.py`:
```python
"""Intelligent model routing for cost optimization."""

import logging
from enum import Enum
from typing import Dict, Any, Optional

from .claude_client import ClaudeClient
from .cost_tracker import CostTracker


logger = logging.getLogger(__name__)


class TaskComplexity(Enum):
    """Task complexity levels."""
    SIMPLE = "simple"           # Lookup, extraction, simple Q&A
    MODERATE = "moderate"       # Analysis, summarization
    COMPLEX = "complex"         # Reasoning, creative, multi-step
    CRITICAL = "critical"       # Production-critical decisions


class ModelRouter:
    """
    Route AI requests to optimal model based on:
    - Task complexity
    - Budget remaining
    - Urgency
    - Availability
    """

    # Model selection matrix
    MODEL_SELECTION = {
        TaskComplexity.SIMPLE: {
            "primary": "claude-haiku-3-5-20250314",  # Cheapest
            "fallback": "ollama",  # Local/free
        },
        TaskComplexity.MODERATE: {
            "primary": "claude-sonnet-4-20250514",  # Balanced
            "fallback": "claude-haiku-3-5-20250314",
        },
        TaskComplexity.COMPLEX: {
            "primary": "claude-sonnet-4-20250514",  # Best reasoning
            "fallback": "claude-sonnet-4-20250514",  # No downgrade
        },
        TaskComplexity.CRITICAL: {
            "primary": "claude-opus-4",  # Most capable
            "fallback": "claude-sonnet-4-20250514",
        },
    }

    def __init__(self, cost_tracker: Optional[CostTracker] = None):
        """
        Initialize model router.

        Args:
            cost_tracker: Cost tracker for budget awareness
        """
        self.cost_tracker = cost_tracker or CostTracker()
        self.clients = {}  # Cache of model clients

    def route(
        self,
        task_complexity: TaskComplexity,
        urgency: str = "normal",
        budget_threshold: float = 0.9,  # Use fallback if >90% budget used
    ) -> str:
        """
        Route request to optimal model.

        Args:
            task_complexity: Complexity of the task
            urgency: Urgency level (low, normal, high, critical)
            budget_threshold: Threshold for switching to cheaper models

        Returns:
            Model identifier to use
        """
        # Check budget
        budget_usage = self.cost_tracker.current_spend / self.cost_tracker.monthly_budget

        # If budget critical, use fallback
        if budget_usage >= budget_threshold:
            logger.warning(
                f"Budget at {budget_usage*100:.1f}%, using fallback model"
            )
            return self.MODEL_SELECTION[task_complexity]["fallback"]

        # If critical urgency, always use primary
        if urgency == "critical":
            return self.MODEL_SELECTION[task_complexity]["primary"]

        # Normal routing
        return self.MODEL_SELECTION[task_complexity]["primary"]

    def get_client(self, model: str) -> ClaudeClient:
        """
        Get or create client for model.

        Args:
            model: Model identifier

        Returns:
            Configured client
        """
        if model not in self.clients:
            self.clients[model] = ClaudeClient(model=model)

        return self.clients[model]

    def classify_complexity(self, query: str, context: Dict[str, Any] = None) -> TaskComplexity:
        """
        Classify query complexity (simple heuristics).

        Args:
            query: User query
            context: Optional context

        Returns:
            Complexity classification
        """
        query_lower = query.lower()

        # Simple: Lookup, retrieval
        simple_keywords = ["what is", "when is", "who is", "where is", "list", "show"]
        if any(kw in query_lower for kw in simple_keywords):
            return TaskComplexity.SIMPLE

        # Critical: Decision-making
        critical_keywords = ["should we", "approve", "reject", "decide", "recommend"]
        if any(kw in query_lower for kw in critical_keywords):
            return TaskComplexity.CRITICAL

        # Complex: Analysis, reasoning
        complex_keywords = ["analyze", "compare", "evaluate", "why", "how", "explain"]
        if any(kw in query_lower for kw in complex_keywords):
            return TaskComplexity.COMPLEX

        # Default: Moderate
        return TaskComplexity.MODERATE

    async def query_optimal(
        self,
        prompt: str,
        context: Dict[str, Any] = None,
        force_complexity: Optional[TaskComplexity] = None,
    ) -> Dict[str, Any]:
        """
        Query using optimal model.

        Args:
            prompt: User prompt
            context: Optional context
            force_complexity: Override complexity classification

        Returns:
            AI response with routing metadata
        """
        # Determine complexity
        complexity = force_complexity or self.classify_complexity(prompt, context)

        # Route to model
        model = self.route(complexity)

        logger.info(f"Routing {complexity.value} task to {model}")

        # Get client and query
        client = self.get_client(model)
        result = await client.query(prompt)

        # Add routing metadata
        result["routing"] = {
            "complexity": complexity.value,
            "model_used": model,
            "budget_remaining": self.cost_tracker.monthly_budget - self.cost_tracker.current_spend,
        }

        return result
```

**Effort:** 4 hours

---

## 5. CREATE DOCKERFILE & DOCKER COMPOSE

**Problem:** No Docker configuration
- Cannot deploy consistently
- No containerization
- Environment differences between dev/prod

**Impact:** Difficult deployment and scaling

**Solution:** (Already documented in FIXES_CRITICAL, but needs implementation)

**Effort:** 3-4 hours

---

## 6. CREATE GITHUB ACTIONS CI/CD

**Problem:** No automated testing or deployment
- Manual testing only
- No continuous integration
- No automated deployment

**Impact:** High risk of breaking changes, slow deployment

**Solution:** (Already documented in FIXES_CRITICAL, needs implementation)

**Effort:** 4-5 hours

---

## SUMMARY

**Total High Priority Fixes:** 6
**Total Estimated Effort:** 32-40 hours
**Timeline:** 1-2 weeks

### Priority Order

1. **Week 1:** Fixes #1-3 (Agents, Tests, Documentation)
2. **Week 2:** Fixes #4-6 (Routing, Docker, CI/CD)

**After completing high priority fixes, the project will have:**
- ✅ All core AI agents implemented
- ✅ Comprehensive test coverage (>80%)
- ✅ Complete developer documentation
- ✅ Optimized AI costs
- ✅ Docker deployment
- ✅ Automated CI/CD

**Then can proceed to:** Medium priority fixes (web UI, integrations, polish)
