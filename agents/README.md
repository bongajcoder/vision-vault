# Vision Vault AI Agents

This directory contains the AI intelligence layer for Vision Vault - specialized agents that process documents, detect conflicts, support decisions, and optimize resources.

## Agent Architecture

Vision Vault uses a multi-agent system where each agent specializes in a specific aspect of production intelligence:

```
┌─────────────────────────────────────────────────────────┐
│              ORCHESTRATION LAYER                         │
│  (Coordinates all agents, manages workflow)              │
└─────────────────────────────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │               │
┌───────▼──────┐ ┌────▼─────┐ ┌──────▼──────┐
│  Multi-Modal │ │ Conflict │ │   Decision  │
│  Processing  │ │ Detection│ │   Support   │
│    Agents    │ │  Agent   │ │    Agent    │
└──────────────┘ └──────────┘ └─────────────┘
        │              │               │
┌───────▼──────┐ ┌────▼─────┐ ┌──────▼──────┐
│  Resource    │ │   Risk   │ │ Completeness│
│Optimization  │ │Identifier│ │   Checker   │
│    Agent     │ │  Agent   │ │    Agent    │
└──────────────┘ └──────────┘ └─────────────┘
```

## Agent Types

### 1. Multi-Modal Processing Agents
Process different types of production documents:

- **Text Agent** (`text_agent.py`)
  - Script analysis
  - Document summarization
  - Entity extraction
  - Sentiment analysis
  - Consistency checking

- **Visual Agent** (`visual_agent.py`)
  - Image classification
  - Concept art analysis
  - Storyboard processing
  - Style consistency checking

- **Audio Agent** (`audio_agent.py`)
  - Sound design analysis
  - Music classification
  - Dialogue transcription

- **Video Agent** (`video_agent.py`)
  - Scene analysis
  - Shot classification
  - Continuity checking

### 2. Conflict Detection Agent (`conflict_detector.py`)
Identifies potential conflicts between departments:

- Schedule conflicts
- Budget allocation conflicts
- Creative vision discrepancies
- Technical feasibility issues
- Resource conflicts
- Safety concerns

### 3. Decision Support Agent (`decision_support.py`)
Analyzes decisions across multiple dimensions:

- Creative implications
- Technical feasibility
- Logistical impacts
- Financial consequences
- Timeline effects
- Risk assessment

### 4. Resource Optimization Agent (`resource_optimizer.py`)
Suggests improvements in resource allocation:

- Equipment sharing opportunities
- Crew scheduling optimization
- Location consolidation
- Budget reallocation
- Timeline efficiency

### 5. Risk Identification Agent (`risk_identifier.py`)
Identifies and assesses production risks:

- Schedule risks
- Budget overruns
- Technical challenges
- Safety hazards
- Legal/compliance risks

### 6. Completeness Checker Agent (`completeness_checker.py`)
Verifies production readiness:

- Required documents for phase
- Missing metadata
- Incomplete decisions
- Unaddressed conflicts
- Pending approvals

## Agent Communication Protocol

Agents communicate using a standardized message format:

```json
{
  "agent_id": "conflict_detector_001",
  "timestamp": "2025-03-01T10:30:00Z",
  "message_type": "conflict_detected",
  "priority": "high",
  "payload": {
    "conflict_id": "CONF-2025-001",
    "type": "schedule",
    "severity": "high",
    "affected_departments": ["Cinematography", "Locations"],
    "description": "...",
    "recommended_actions": [...]
  }
}
```

## Using Agents

### Basic Agent Invocation

```python
from agents import TextAgent, ConflictDetector

# Initialize agent
text_agent = TextAgent()

# Process document
result = text_agent.process_document(
    document_path="/path/to/script.pdf",
    document_metadata={...}
)

# Check for conflicts
conflict_detector = ConflictDetector()
conflicts = conflict_detector.analyze_new_document(
    document=result,
    knowledge_base=kb
)
```

### Agent Pipeline

```python
from agents import AgentPipeline

# Create processing pipeline
pipeline = AgentPipeline([
    TextAgent(),
    ConflictDetector(),
    RiskIdentifier(),
    CompletenessChecker()
])

# Process document through pipeline
results = pipeline.process(document, metadata)
```

## Agent Configuration

Each agent can be configured via YAML:

```yaml
# agents/config/text_agent.yaml
agent_name: "text_agent"
model: "claude-sonnet-4"
temperature: 0.3
max_tokens: 4000
specialized_prompts:
  script_analysis: "prompts/script_analysis.txt"
  entity_extraction: "prompts/entity_extraction.txt"
```

## Agent Performance Monitoring

Agents log all activities for performance monitoring:

- Processing time
- Success/failure rates
- Accuracy metrics
- Resource usage

## Agent Development Guidelines

When creating new agents:

1. **Single Responsibility**: Each agent should have one clear purpose
2. **Stateless Operation**: Agents should not maintain state between invocations
3. **Standard Interface**: Use the BaseAgent class
4. **Error Handling**: Graceful degradation on errors
5. **Logging**: Comprehensive logging for debugging
6. **Testing**: Unit tests for all agent functions

## Future Agent Types

Planned future agents:

- **Continuity Agent**: Track continuity across scenes
- **Budget Forecasting Agent**: Predict final costs
- **Schedule Optimization Agent**: Suggest schedule improvements
- **Casting Match Agent**: Match actors to roles
- **Location Scout Agent**: Suggest locations based on requirements
