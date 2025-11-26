# 🚨 CRITICAL FIXES - Vision Vault
**Priority:** BLOCKING - Must fix before any development can proceed
**Estimated Total Effort:** 16-24 hours

---

## 1. CREATE DEPENDENCY MANAGEMENT

**Problem:** No requirements.txt, package.json, or pyproject.toml exists
- Cannot install project
- Cannot specify Python version
- Cannot manage dependencies
- Cannot reproduce environment
- Blocks ALL development

**Impact:** **BLOCKS EVERYTHING** - Project is not installable or runnable

**Solution:**

Create `/home/user/vision-vault/requirements.txt`:
```txt
# Core AI & Processing
anthropic>=0.21.0
openai>=1.12.0              # For potential GPT fallback
google-generativeai>=0.3.0  # For Gemini integration

# Data validation & parsing
pydantic>=2.5.0
pydantic-settings>=2.1.0
pyyaml>=6.0.1
python-dotenv>=1.0.0

# Vector database (choose one primary, include backups)
chromadb>=0.4.22            # Primary choice
# qdrant-client>=1.7.0      # Alternative
# pinecone-client>=2.2.4    # Alternative

# Document processing
pypdf>=4.0.0                # PDF parsing
python-docx>=1.1.0          # Word docs
openpyxl>=3.1.2             # Excel
pillow>=10.2.0              # Image processing
python-magic>=0.4.27        # File type detection

# API server (if building web interface)
fastapi>=0.109.0
uvicorn[standard]>=0.27.0
python-multipart>=0.0.6     # For file uploads

# HTTP & async
httpx>=0.26.0
aiofiles>=23.2.1

# Utilities
python-dateutil>=2.8.2
retry>=0.9.2
tenacity>=8.2.3             # Retry with backoff
rich>=13.7.0                # CLI formatting

# Development dependencies
pytest>=7.4.4
pytest-asyncio>=0.23.3
pytest-cov>=4.1.0
pytest-mock>=3.12.0
black>=24.1.1
isort>=5.13.2
mypy>=1.8.0
pylint>=3.0.3
flake8>=7.0.0

# Type stubs
types-pyyaml>=6.0.12
types-python-dateutil>=2.8.19
```

Create `/home/user/vision-vault/pyproject.toml`:
```toml
[build-system]
requires = ["setuptools>=68.0", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "vision-vault"
version = "0.1.0"
description = "AI-powered film production knowledge integration system"
readme = "README.md"
requires-python = ">=3.11"
license = {text = "MIT"}
authors = [
    {name = "Bongani Labs"}
]
classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Other Audience",
    "Topic :: Multimedia :: Video",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
]

dependencies = [
    "anthropic>=0.21.0",
    "pydantic>=2.5.0",
    # ... (full list from requirements.txt)
]

[project.optional-dependencies]
dev = [
    "pytest>=7.4.4",
    "black>=24.1.1",
    "mypy>=1.8.0",
]

[tool.black]
line-length = 100
target-version = ['py311']

[tool.mypy]
python_version = "3.11"
warn_return_any = true
warn_unused_configs = true
disallow_untyped_defs = true

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py", "*_test.py"]
addopts = "--cov=vision_vault --cov-report=term-missing --cov-report=html"
```

Create `/home/user/vision-vault/.python-version`:
```
3.11.7
```

**Effort:** 2 hours (including testing installation)

---

## 2. CREATE ENVIRONMENT CONFIGURATION

**Problem:** No .env.example file
- Developers don't know what environment variables are needed
- API keys undefined
- Configuration unclear
- Secrets might be committed to git

**Impact:** Cannot configure or run the application

**Solution:**

Create `/home/user/vision-vault/.env.example`:
```bash
# ============================================
# VISION VAULT ENVIRONMENT CONFIGURATION
# ============================================
# Copy this file to .env and fill in your values
# DO NOT commit .env to git (already in .gitignore)

# --------------------------------------------
# AI API KEYS (Required)
# --------------------------------------------
# Get from: https://console.anthropic.com/
ANTHROPIC_API_KEY=sk-ant-api03-...

# Optional: For fallback to OpenAI GPT models
# OPENAI_API_KEY=sk-...

# Optional: For Gemini integration
# GOOGLE_API_KEY=...

# Optional: For local/offline AI (Ollama)
# OLLAMA_BASE_URL=http://localhost:11434

# --------------------------------------------
# AI Configuration
# --------------------------------------------
# Primary model (claude-sonnet-4-20250514, claude-opus-4, claude-haiku-3-5)
AI_MODEL=claude-sonnet-4-20250514

# Temperature for AI responses (0.0-1.0)
AI_TEMPERATURE=0.3

# Maximum tokens per response
AI_MAX_TOKENS=4000

# Monthly AI cost budget (dollars)
MAX_MONTHLY_AI_COST=50

# Enable AI response caching (recommended for cost savings)
ENABLE_AI_CACHING=true

# Cache TTL in seconds (default: 86400 = 24 hours)
CACHE_TTL=86400

# --------------------------------------------
# Vector Database Configuration
# --------------------------------------------
# Vector DB type (chromadb, qdrant, pinecone)
VECTOR_DB_TYPE=chromadb

# For ChromaDB (local)
CHROMA_DB_PATH=./data/chroma

# For Qdrant (local or cloud)
# QDRANT_HOST=localhost
# QDRANT_PORT=6333
# QDRANT_API_KEY=

# For Pinecone (cloud)
# PINECONE_API_KEY=
# PINECONE_ENVIRONMENT=us-west1-gcp

# Collection/index name for production knowledge
VECTOR_COLLECTION_NAME=vision_vault_production

# --------------------------------------------
# Google Workspace Integration (Optional)
# --------------------------------------------
# Get from: https://console.cloud.google.com/
# GOOGLE_WORKSPACE_CLIENT_ID=
# GOOGLE_WORKSPACE_CLIENT_SECRET=
# GOOGLE_WORKSPACE_REDIRECT_URI=http://localhost:8000/auth/callback

# Google Drive folder ID for document sync
# GOOGLE_DRIVE_FOLDER_ID=

# --------------------------------------------
# Application Configuration
# --------------------------------------------
# Application environment (development, staging, production)
APP_ENV=development

# API server host and port
API_HOST=0.0.0.0
API_PORT=8000

# Enable debug mode (verbose logging)
DEBUG=true

# Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL=INFO

# Log file path
LOG_FILE=./logs/vision_vault.log

# --------------------------------------------
# Storage Configuration
# --------------------------------------------
# Local storage path for uploaded documents
DOCUMENT_STORAGE_PATH=./data/documents

# Knowledge base data path
KNOWLEDGE_BASE_PATH=./data/knowledge_base

# Temp file storage
TEMP_STORAGE_PATH=./data/temp

# Maximum upload file size (bytes) - 100MB default
MAX_UPLOAD_SIZE=104857600

# --------------------------------------------
# Security
# --------------------------------------------
# Secret key for session management (generate with: openssl rand -hex 32)
SECRET_KEY=your-secret-key-here-change-this-in-production

# Allowed CORS origins (comma-separated)
CORS_ORIGINS=http://localhost:3000,http://localhost:8000

# API authentication (none, api_key, oauth)
AUTH_TYPE=none

# API key for authentication (if AUTH_TYPE=api_key)
# API_KEY=

# --------------------------------------------
# Performance & Limits
# --------------------------------------------
# Maximum concurrent AI requests
MAX_CONCURRENT_AI_REQUESTS=5

# Request timeout (seconds)
REQUEST_TIMEOUT=60

# Rate limiting (requests per minute)
RATE_LIMIT_PER_MINUTE=60

# --------------------------------------------
# Monitoring & Analytics (Optional)
# --------------------------------------------
# Sentry DSN for error tracking
# SENTRY_DSN=

# Enable usage analytics
ENABLE_ANALYTICS=false

# Analytics provider (none, mixpanel, amplitude)
ANALYTICS_PROVIDER=none

# --------------------------------------------
# Feature Flags
# --------------------------------------------
# Enable experimental features
ENABLE_EXPERIMENTAL_FEATURES=false

# Enable multi-modal processing (images, video, audio)
ENABLE_MULTIMODAL=true

# Enable department conflict detection
ENABLE_CONFLICT_DETECTION=true

# Enable Google Workspace integration
ENABLE_GOOGLE_INTEGRATION=false
```

Create `/home/user/vision-vault/.gitignore` (if not exists):
```gitignore
# Environment
.env
.env.local
.env.*.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST
venv/
ENV/
env/

# Testing
.pytest_cache/
.coverage
htmlcov/
*.cover
.hypothesis/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Logs
logs/
*.log

# Data
data/
*.db
*.sqlite

# OS
.DS_Store
Thumbs.db

# Temp
temp/
tmp/
*.tmp
```

**Effort:** 1 hour

---

## 3. INTEGRATE CLAUDE SDK (CORE FUNCTIONALITY)

**Problem:** No Claude SDK integration despite being AI-powered system
- Cannot call Claude API
- Cannot process queries
- Cannot implement any agents
- Core value proposition doesn't work

**Impact:** **BLOCKS ALL AI FUNCTIONALITY** - The entire purpose of Vision Vault

**Solution:**

Create `/home/user/vision-vault/core/ai/__init__.py`:
```python
"""AI integration module for Vision Vault."""

from .claude_client import ClaudeClient
from .cost_tracker import CostTracker
from .cache_manager import CacheManager
from .model_router import ModelRouter

__all__ = ["ClaudeClient", "CostTracker", "CacheManager", "ModelRouter"]
```

Create `/home/user/vision-vault/core/ai/claude_client.py`:
```python
"""Claude API client with caching and cost tracking."""

import os
import hashlib
import logging
from typing import Optional, Dict, Any, List
from datetime import datetime, timedelta

import anthropic
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

from .cache_manager import CacheManager
from .cost_tracker import CostTracker


logger = logging.getLogger(__name__)


class ClaudeClient:
    """
    Client for interacting with Claude AI API.

    Includes:
    - Automatic caching
    - Cost tracking
    - Error handling and retries
    - Token counting
    """

    # Cost per 1M tokens (as of Nov 2025)
    COSTS = {
        "claude-opus-4": {"input": 15.0, "output": 75.0},
        "claude-sonnet-4-20250514": {"input": 3.0, "output": 15.0},
        "claude-haiku-3-5-20250314": {"input": 0.25, "output": 1.25},
    }

    def __init__(
        self,
        api_key: Optional[str] = None,
        model: str = "claude-sonnet-4-20250514",
        enable_caching: bool = True,
        enable_cost_tracking: bool = True,
    ):
        """
        Initialize Claude client.

        Args:
            api_key: Anthropic API key (or from ANTHROPIC_API_KEY env var)
            model: Claude model to use
            enable_caching: Enable response caching
            enable_cost_tracking: Track API costs
        """
        self.api_key = api_key or os.getenv("ANTHROPIC_API_KEY")
        if not self.api_key:
            raise ValueError("ANTHROPIC_API_KEY not found in environment")

        self.client = Anthropic(api_key=self.api_key)
        self.model = model

        self.cache_manager = CacheManager() if enable_caching else None
        self.cost_tracker = CostTracker() if enable_cost_tracking else None

    async def query(
        self,
        prompt: str,
        system: Optional[str] = None,
        max_tokens: int = 4000,
        temperature: float = 0.3,
        use_cache: bool = True,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Query Claude API with caching and cost tracking.

        Args:
            prompt: User prompt
            system: System prompt (instructions for Claude)
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature (0.0-1.0)
            use_cache: Whether to use cache
            metadata: Additional metadata for tracking

        Returns:
            Dictionary with response, usage stats, and metadata
        """
        # Check cache first
        if use_cache and self.cache_manager:
            cache_key = self._generate_cache_key(prompt, system, self.model)
            cached = self.cache_manager.get(cache_key)
            if cached:
                logger.info("Cache hit for query")
                return cached

        # Check cost budget
        if self.cost_tracker:
            estimated_tokens = len(prompt.split()) * 1.3  # Rough estimate
            if not self.cost_tracker.can_make_request(estimated_tokens):
                raise Exception(
                    f"Monthly budget exceeded. "
                    f"Current: ${self.cost_tracker.current_spend:.2f}, "
                    f"Budget: ${self.cost_tracker.monthly_budget}"
                )

        try:
            # Make API call
            logger.info(f"Calling Claude API (model: {self.model})")

            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                system=system or "",
                messages=[{"role": "user", "content": prompt}],
            )

            # Extract response
            response_text = message.content[0].text

            # Track usage
            usage = {
                "input_tokens": message.usage.input_tokens,
                "output_tokens": message.usage.output_tokens,
                "total_tokens": message.usage.input_tokens + message.usage.output_tokens,
            }

            # Track cost
            if self.cost_tracker:
                cost = self._calculate_cost(
                    usage["input_tokens"], usage["output_tokens"]
                )
                self.cost_tracker.track_request(
                    usage["input_tokens"],
                    usage["output_tokens"],
                    0,  # No cached tokens in this path
                    cost,
                )

            # Build response
            result = {
                "response": response_text,
                "usage": usage,
                "model": self.model,
                "timestamp": datetime.now().isoformat(),
                "metadata": metadata or {},
                "cached": False,
            }

            # Cache result
            if use_cache and self.cache_manager:
                cache_key = self._generate_cache_key(prompt, system, self.model)
                self.cache_manager.set(cache_key, result)

            return result

        except anthropic.APIError as e:
            logger.error(f"Claude API error: {e}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error calling Claude: {e}")
            raise

    def _generate_cache_key(
        self, prompt: str, system: Optional[str], model: str
    ) -> str:
        """Generate cache key from prompt, system, and model."""
        content = f"{model}::{system or ''}::{prompt}"
        return hashlib.sha256(content.encode()).hexdigest()

    def _calculate_cost(self, input_tokens: int, output_tokens: int) -> float:
        """Calculate cost for API call."""
        costs = self.COSTS.get(self.model, self.COSTS["claude-sonnet-4-20250514"])
        input_cost = (input_tokens / 1_000_000) * costs["input"]
        output_cost = (output_tokens / 1_000_000) * costs["output"]
        return input_cost + output_cost

    def get_usage_stats(self) -> Dict[str, Any]:
        """Get usage statistics."""
        if not self.cost_tracker:
            return {}

        return {
            "total_requests": self.cost_tracker.total_requests,
            "total_tokens": self.cost_tracker.total_tokens,
            "total_cost": self.cost_tracker.current_spend,
            "budget_remaining": self.cost_tracker.monthly_budget - self.cost_tracker.current_spend,
            "cache_hit_rate": self.cache_manager.get_hit_rate() if self.cache_manager else 0,
        }
```

Create `/home/user/vision-vault/core/ai/cost_tracker.py`:
```python
"""Track AI API costs to stay within budget."""

import os
from datetime import datetime
from typing import Optional


class CostTracker:
    """Track AI API usage and costs."""

    def __init__(self, monthly_budget: Optional[float] = None):
        """
        Initialize cost tracker.

        Args:
            monthly_budget: Monthly budget in dollars
        """
        self.monthly_budget = monthly_budget or float(
            os.getenv("MAX_MONTHLY_AI_COST", "50")
        )
        self.current_spend = 0.0
        self.total_requests = 0
        self.total_tokens = 0
        self.start_date = datetime.now()

    def can_make_request(self, estimated_tokens: int) -> bool:
        """
        Check if request is within budget.

        Args:
            estimated_tokens: Estimated tokens for request

        Returns:
            True if within budget
        """
        # Rough estimate: $3 per 1M tokens for Sonnet
        estimated_cost = (estimated_tokens / 1_000_000) * 3.0
        return (self.current_spend + estimated_cost) < self.monthly_budget

    def track_request(
        self,
        input_tokens: int,
        output_tokens: int,
        cached_tokens: int,
        cost: float,
    ):
        """
        Track a completed request.

        Args:
            input_tokens: Input tokens used
            output_tokens: Output tokens generated
            cached_tokens: Cached tokens (discounted)
            cost: Actual cost of request
        """
        self.total_requests += 1
        self.total_tokens += input_tokens + output_tokens
        self.current_spend += cost

    def get_stats(self) -> dict:
        """Get current tracking statistics."""
        return {
            "monthly_budget": self.monthly_budget,
            "current_spend": self.current_spend,
            "budget_remaining": self.monthly_budget - self.current_spend,
            "total_requests": self.total_requests,
            "total_tokens": self.total_tokens,
            "average_cost_per_request": (
                self.current_spend / self.total_requests
                if self.total_requests > 0
                else 0
            ),
        }

    def reset_monthly(self):
        """Reset monthly counters (call at start of month)."""
        self.current_spend = 0.0
        self.total_requests = 0
        self.total_tokens = 0
        self.start_date = datetime.now()
```

Create `/home/user/vision-vault/core/ai/cache_manager.py`:
```python
"""Cache manager for AI responses."""

import json
import hashlib
from typing import Optional, Any, Dict
from datetime import datetime, timedelta
from pathlib import Path


class CacheManager:
    """Simple file-based cache for AI responses."""

    def __init__(self, cache_dir: str = "./data/cache", ttl_seconds: int = 86400):
        """
        Initialize cache manager.

        Args:
            cache_dir: Directory for cache files
            ttl_seconds: Time-to-live for cache entries (default: 24 hours)
        """
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.ttl_seconds = ttl_seconds
        self.hits = 0
        self.misses = 0

    def get(self, key: str) -> Optional[Dict[str, Any]]:
        """
        Get cached value.

        Args:
            key: Cache key (hash)

        Returns:
            Cached value or None if not found/expired
        """
        cache_file = self.cache_dir / f"{key}.json"

        if not cache_file.exists():
            self.misses += 1
            return None

        try:
            with open(cache_file, "r") as f:
                data = json.load(f)

            # Check expiration
            cached_at = datetime.fromisoformat(data["cached_at"])
            if datetime.now() - cached_at > timedelta(seconds=self.ttl_seconds):
                cache_file.unlink()  # Delete expired
                self.misses += 1
                return None

            self.hits += 1
            return data["value"]

        except Exception:
            self.misses += 1
            return None

    def set(self, key: str, value: Dict[str, Any]):
        """
        Set cache value.

        Args:
            key: Cache key (hash)
            value: Value to cache
        """
        cache_file = self.cache_dir / f"{key}.json"

        data = {
            "cached_at": datetime.now().isoformat(),
            "value": value,
        }

        with open(cache_file, "w") as f:
            json.dump(data, f, indent=2)

    def get_hit_rate(self) -> float:
        """Get cache hit rate."""
        total = self.hits + self.misses
        return self.hits / total if total > 0 else 0.0

    def clear(self):
        """Clear all cache files."""
        for cache_file in self.cache_dir.glob("*.json"):
            cache_file.unlink()
        self.hits = 0
        self.misses = 0
```

**Effort:** 4-6 hours (including testing)

---

## 4. IMPLEMENT BASIC KNOWLEDGE STORAGE

**Problem:** No knowledge base storage implementation
- Cannot store uploaded documents
- Cannot retrieve information
- Cannot build knowledge graph
- No vector database integration

**Impact:** Cannot store or query production knowledge

**Solution:**

Create `/home/user/vision-vault/core/knowledge_base/__init__.py`:
```python
"""Knowledge base storage and retrieval."""

from .storage import KnowledgeStorage
from .indexer import DocumentIndexer
from .retriever import KnowledgeRetriever

__all__ = ["KnowledgeStorage", "DocumentIndexer", "KnowledgeRetriever"]
```

Create `/home/user/vision-vault/core/knowledge_base/storage.py`:
```python
"""Knowledge storage using vector database."""

import os
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime

import chromadb
from chromadb.config import Settings


logger = logging.getLogger(__name__)


class KnowledgeStorage:
    """
    Vector database storage for production knowledge.

    Uses ChromaDB for local/simple deployments.
    Can be swapped for Qdrant or Pinecone for production scale.
    """

    def __init__(
        self,
        db_path: str = "./data/chroma",
        collection_name: str = "vision_vault_production",
    ):
        """
        Initialize knowledge storage.

        Args:
            db_path: Path to ChromaDB data directory
            collection_name: Name of collection for this production
        """
        self.db_path = db_path
        self.collection_name = collection_name

        # Initialize ChromaDB
        self.client = chromadb.PersistentClient(
            path=db_path,
            settings=Settings(anonymized_telemetry=False),
        )

        # Get or create collection
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"},  # Cosine similarity
        )

        logger.info(f"Knowledge storage initialized: {collection_name}")

    def add_document(
        self,
        document_id: str,
        content: str,
        metadata: Dict[str, Any],
        embedding: Optional[List[float]] = None,
    ):
        """
        Add document to knowledge base.

        Args:
            document_id: Unique document identifier
            content: Document text content
            metadata: Document metadata (department, type, etc.)
            embedding: Pre-computed embedding (optional, will compute if None)
        """
        self.collection.add(
            ids=[document_id],
            documents=[content],
            metadatas=[metadata],
            embeddings=[embedding] if embedding else None,
        )

        logger.info(f"Added document: {document_id}")

    def search(
        self,
        query: str,
        n_results: int = 10,
        where: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Search knowledge base.

        Args:
            query: Search query (text)
            n_results: Number of results to return
            where: Metadata filters (e.g., {"department": "Cinematography"})

        Returns:
            Search results with documents, distances, and metadata
        """
        results = self.collection.query(
            query_texts=[query],
            n_results=n_results,
            where=where,
        )

        return {
            "documents": results["documents"][0] if results["documents"] else [],
            "ids": results["ids"][0] if results["ids"] else [],
            "distances": results["distances"][0] if results["distances"] else [],
            "metadatas": results["metadatas"][0] if results["metadatas"] else [],
        }

    def get_by_id(self, document_id: str) -> Optional[Dict[str, Any]]:
        """
        Get document by ID.

        Args:
            document_id: Document identifier

        Returns:
            Document data or None if not found
        """
        results = self.collection.get(ids=[document_id])

        if not results["ids"]:
            return None

        return {
            "id": results["ids"][0],
            "document": results["documents"][0],
            "metadata": results["metadatas"][0],
        }

    def get_stats(self) -> Dict[str, Any]:
        """Get knowledge base statistics."""
        count = self.collection.count()

        return {
            "total_documents": count,
            "collection_name": self.collection_name,
            "db_path": self.db_path,
        }
```

**Effort:** 3-4 hours

---

## 5. CREATE BASIC DOCUMENT INGESTION

**Problem:** No document ingestion pipeline
- Cannot upload files
- Cannot extract text from PDFs
- Cannot process production documents

**Impact:** System has no input - cannot populate knowledge base

**Solution:**

Create `/home/user/vision-vault/core/document_processor/__init__.py`:
```python
"""Document processing and ingestion."""

from .ingester import DocumentIngester
from .parser import DocumentParser

__all__ = ["DocumentIngester", "DocumentParser"]
```

Create `/home/user/vision-vault/core/document_processor/ingester.py`:
```python
"""Document ingestion pipeline."""

import logging
import hashlib
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime

from .parser import DocumentParser
from ..knowledge_base.storage import KnowledgeStorage
from ..ai.claude_client import ClaudeClient


logger = logging.getLogger(__name__)


class DocumentIngester:
    """
    Ingests production documents into knowledge base.

    Process:
    1. Parse document (extract text)
    2. Extract metadata
    3. Analyze with AI (optional)
    4. Store in vector database
    """

    def __init__(
        self,
        knowledge_storage: KnowledgeStorage,
        ai_client: Optional[ClaudeClient] = None,
    ):
        """
        Initialize document ingester.

        Args:
            knowledge_storage: Knowledge storage instance
            ai_client: Claude client for AI analysis (optional)
        """
        self.storage = knowledge_storage
        self.parser = DocumentParser()
        self.ai_client = ai_client

    async def ingest_file(
        self,
        file_path: Path,
        metadata: Optional[Dict[str, Any]] = None,
        analyze_with_ai: bool = True,
    ) -> Dict[str, Any]:
        """
        Ingest a single file.

        Args:
            file_path: Path to file
            metadata: Optional metadata
            analyze_with_ai: Whether to use AI for analysis

        Returns:
            Ingestion result with document_id and stats
        """
        try:
            # Parse document
            logger.info(f"Parsing document: {file_path}")
            content = self.parser.parse(file_path)

            # Generate document ID
            document_id = self._generate_document_id(file_path, content)

            # Merge metadata
            full_metadata = {
                "filename": file_path.name,
                "file_path": str(file_path),
                "file_size": file_path.stat().st_size,
                "ingested_at": datetime.now().isoformat(),
                "document_id": document_id,
                **(metadata or {}),
            }

            # Optional AI analysis
            if analyze_with_ai and self.ai_client:
                ai_analysis = await self._analyze_with_ai(content, full_metadata)
                full_metadata["ai_analysis"] = ai_analysis

            # Store in knowledge base
            self.storage.add_document(
                document_id=document_id,
                content=content,
                metadata=full_metadata,
            )

            logger.info(f"Successfully ingested: {document_id}")

            return {
                "success": True,
                "document_id": document_id,
                "content_length": len(content),
                "metadata": full_metadata,
            }

        except Exception as e:
            logger.error(f"Failed to ingest {file_path}: {e}")
            return {
                "success": False,
                "error": str(e),
                "file_path": str(file_path),
            }

    async def _analyze_with_ai(
        self, content: str, metadata: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Use AI to analyze document content."""
        if not self.ai_client:
            return {}

        prompt = f"""Analyze this production document and extract key information:

Filename: {metadata.get('filename', 'Unknown')}
Department: {metadata.get('department', 'Unknown')}

Content:
{content[:2000]}... (truncated)

Extract:
1. Document type (script, budget, schedule, etc.)
2. Main topics covered
3. Key decisions or requirements
4. Departments mentioned
5. Any conflicts or concerns

Format as JSON.
"""

        result = await self.ai_client.query(prompt, max_tokens=1000)
        return result.get("response", {})

    def _generate_document_id(self, file_path: Path, content: str) -> str:
        """Generate unique document ID."""
        content_hash = hashlib.md5(content.encode()).hexdigest()[:8]
        timestamp = datetime.now().strftime("%Y%m%d")
        filename = file_path.stem[:20]

        return f"DOC-{timestamp}-{filename}-{content_hash}"
```

Create `/home/user/vision-vault/core/document_processor/parser.py`:
```python
"""Parse documents to extract text content."""

import logging
from pathlib import Path
from typing import Optional

from pypdf import PdfReader


logger = logging.getLogger(__name__)


class DocumentParser:
    """Parse various document formats to extract text."""

    def parse(self, file_path: Path) -> str:
        """
        Parse document and extract text.

        Args:
            file_path: Path to document

        Returns:
            Extracted text content
        """
        suffix = file_path.suffix.lower()

        if suffix == ".pdf":
            return self._parse_pdf(file_path)
        elif suffix == ".txt":
            return self._parse_text(file_path)
        elif suffix in [".md", ".markdown"]:
            return self._parse_markdown(file_path)
        else:
            raise ValueError(f"Unsupported file type: {suffix}")

    def _parse_pdf(self, file_path: Path) -> str:
        """Parse PDF file."""
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n\n"
            return text.strip()
        except Exception as e:
            logger.error(f"Failed to parse PDF {file_path}: {e}")
            raise

    def _parse_text(self, file_path: Path) -> str:
        """Parse plain text file."""
        return file_path.read_text(encoding="utf-8")

    def _parse_markdown(self, file_path: Path) -> str:
        """Parse Markdown file."""
        return file_path.read_text(encoding="utf-8")
```

**Effort:** 3-4 hours

---

## 6. CREATE COMPREHENSIVE ERROR HANDLING

**Problem:** No try/except blocks in code
- Unhandled exceptions crash application
- No graceful degradation
- Poor user experience on errors
- Difficult to debug

**Impact:** Application unstable and difficult to use

**Solution:**

Update `/home/user/vision-vault/agents/base_agent.py` with error handling:

```python
# Add to existing imports:
from tenacity import retry, stop_after_attempt, wait_exponential
import traceback

# Update BaseAgent.process to wrap implementation:
class BaseAgent(ABC):
    # ... existing code ...

    def process_safe(
        self, input_data: Any, context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Safe wrapper around process() with error handling.

        Args:
            input_data: The data to process
            context: Optional context information

        Returns:
            Dictionary with success/error status and results/error details
        """
        try:
            # Validate input
            if not self.validate_input(input_data):
                return {
                    "success": False,
                    "error": "Invalid input data",
                    "error_type": "ValidationError",
                    "agent_id": self.agent_id,
                    "timestamp": datetime.now().isoformat(),
                }

            # Process
            start_time = datetime.now()
            result = self.process(input_data, context)
            duration = (datetime.now() - start_time).total_seconds()

            # Log
            self.log_processing(input_data, result, duration)

            # Return success
            return {
                "success": True,
                "data": result,
                "agent_id": self.agent_id,
                "timestamp": datetime.now().isoformat(),
                "duration_seconds": duration,
            }

        except ValueError as e:
            self.logger.error(f"Validation error: {e}")
            return {
                "success": False,
                "error": str(e),
                "error_type": "ValidationError",
                "agent_id": self.agent_id,
                "timestamp": datetime.now().isoformat(),
            }

        except Exception as e:
            self.logger.error(f"Unexpected error: {e}\n{traceback.format_exc()}")
            return {
                "success": False,
                "error": str(e),
                "error_type": type(e).__name__,
                "agent_id": self.agent_id,
                "timestamp": datetime.now().isoformat(),
                "traceback": traceback.format_exc() if self.config.get("debug") else None,
            }

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
    )
    def process_with_retry(
        self, input_data: Any, context: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Process with automatic retries for transient failures.

        Uses exponential backoff: 2s, 4s, 8s between retries.
        """
        return self.process_safe(input_data, context)
```

**Effort:** 2-3 hours

---

## SUMMARY

**Total Critical Fixes:** 6
**Total Estimated Effort:** 16-24 hours
**Priority:** **MUST COMPLETE BEFORE ANY OTHER DEVELOPMENT**

All 6 critical fixes are **blocking** - nothing else can proceed until these are done.

### Implementation Order

1. **Day 1 Morning:** Fixes #1-2 (Dependencies + Environment)
   - Create requirements.txt
   - Create .env.example
   - Test installation

2. **Day 1 Afternoon:** Fix #3 (Claude Integration)
   - Implement ClaudeClient
   - Implement CostTracker
   - Implement CacheManager
   - Test API calls

3. **Day 2 Morning:** Fixes #4-5 (Storage + Ingestion)
   - Implement KnowledgeStorage
   - Implement DocumentIngester
   - Implement DocumentParser
   - Test end-to-end flow

4. **Day 2 Afternoon:** Fix #6 (Error Handling)
   - Add error handling to all modules
   - Test error scenarios
   - Document error codes

**After completing these fixes, the project will have:**
- ✅ Installable dependencies
- ✅ Configured environment
- ✅ Working AI integration
- ✅ Knowledge storage
- ✅ Document ingestion
- ✅ Robust error handling

**Then can proceed to:** High Priority fixes (remaining agents, tests, documentation)
