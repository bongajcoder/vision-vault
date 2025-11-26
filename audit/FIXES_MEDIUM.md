# 💡 MEDIUM PRIORITY FIXES - Vision Vault
**Priority:** Nice-to-have enhancements - Can wait until MVP is functional
**Estimated Total Effort:** 24-32 hours

---

## 1. BUILD WEB DASHBOARD

**Problem:** Only CLI interface exists (or will exist)
- Not user-friendly for non-technical users
- No visual exploration of knowledge base
- Limited collaboration features

**Impact:** Reduced usability for production teams

**Solution:** Create FastAPI web dashboard

**Structure:**
```
web/
├── __init__.py
├── main.py                    # FastAPI app
├── routes/
│   ├── api.py                 # API endpoints
│   ├── documents.py           # Document management
│   ├── query.py               # Query interface
│   └── admin.py               # Admin functions
├── templates/                 # HTML templates (if using Jinja2)
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── models/
    └── schemas.py             # Pydantic models for API
```

**Example API endpoints:**
```python
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

app = FastAPI(title="Vision Vault API")


class QueryRequest(BaseModel):
    query: str
    department: Optional[str] = None
    limit: int = 10


@app.post("/api/documents/upload")
async def upload_document(
    file: UploadFile = File(...),
    department: str = None,
    metadata: str = None,
):
    """Upload production document."""
    # Implementation
    pass


@app.post("/api/query")
async def query_knowledge(request: QueryRequest):
    """Query knowledge base."""
    # Implementation
    pass


@app.get("/api/conflicts")
async def get_conflicts(department: str = None):
    """Get active conflicts."""
    # Implementation
    pass


@app.get("/api/stats")
async def get_stats():
    """Get system statistics."""
    # Implementation
    pass
```

**Frontend options:**
1. **Simple:** Jinja2 templates + HTMX (lightweight, fast)
2. **Modern:** React/Vue frontend (more features, slower dev)
3. **Hybrid:** FastAPI serves both API + simple templates

**Effort:** 12-16 hours

---

## 2. GOOGLE WORKSPACE INTEGRATION

**Problem:** No Google Drive, Docs, Sheets integration
- Cannot sync documents from Google Drive
- Manual document upload only
- No automatic updates

**Impact:** More friction for teams already using Google Workspace

**Solution:** Build Google Workspace connector

Create `/home/user/vision-vault/integrations/google_workspace/connector.py`:
```python
"""Google Workspace integration."""

import os
from typing import List, Dict, Any
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build


class GoogleWorkspaceConnector:
    """Connect to Google Drive, Docs, and Sheets."""

    SCOPES = [
        'https://www.googleapis.com/auth/drive.readonly',
        'https://www.googleapis.com/auth/documents.readonly',
        'https://www.googleapis.com/auth/spreadsheets.readonly',
    ]

    def __init__(self, credentials: Credentials = None):
        """Initialize connector."""
        self.credentials = credentials or self._get_credentials()
        self.drive_service = build('drive', 'v3', credentials=self.credentials)
        self.docs_service = build('docs', 'v1', credentials=self.credentials)
        self.sheets_service = build('sheets', 'v4', credentials=self.credentials)

    def list_files_in_folder(
        self, folder_id: str, file_types: List[str] = None
    ) -> List[Dict[str, Any]]:
        """
        List files in Google Drive folder.

        Args:
            folder_id: Google Drive folder ID
            file_types: Filter by MIME types

        Returns:
            List of file metadata
        """
        query = f"'{folder_id}' in parents and trashed=false"

        if file_types:
            mime_query = " or ".join([f"mimeType='{mt}'" for mt in file_types])
            query += f" and ({mime_query})"

        results = self.drive_service.files().list(
            q=query,
            fields="files(id, name, mimeType, modifiedTime, createdTime)"
        ).execute()

        return results.get('files', [])

    def download_document(self, file_id: str) -> str:
        """
        Download Google Doc as text.

        Args:
            file_id: Google Docs file ID

        Returns:
            Document text content
        """
        doc = self.docs_service.documents().get(documentId=file_id).execute()
        content = doc.get('body', {}).get('content', [])

        # Extract text from structured content
        text = self._extract_text_from_doc(content)
        return text

    def download_sheet(self, spreadsheet_id: str, range_name: str = None) -> List[List[Any]]:
        """
        Download Google Sheet data.

        Args:
            spreadsheet_id: Google Sheets file ID
            range_name: Range to download (e.g., 'Sheet1!A1:Z100')

        Returns:
            2D list of cell values
        """
        result = self.sheets_service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id,
            range=range_name or 'Sheet1'
        ).execute()

        return result.get('values', [])

    def watch_folder(self, folder_id: str, callback_url: str) -> str:
        """
        Set up webhook for folder changes.

        Args:
            folder_id: Google Drive folder ID
            callback_url: Webhook URL for notifications

        Returns:
            Channel ID for webhook
        """
        body = {
            'id': f'vision_vault_{folder_id}',
            'type': 'web_hook',
            'address': callback_url
        }

        response = self.drive_service.files().watch(
            fileId=folder_id,
            body=body
        ).execute()

        return response['id']

    def _get_credentials(self) -> Credentials:
        """Get Google API credentials from environment."""
        # Implement OAuth2 flow
        # For now, placeholder
        return None

    def _extract_text_from_doc(self, content: List[Dict]) -> str:
        """Extract text from Google Docs content structure."""
        text = []

        for element in content:
            if 'paragraph' in element:
                for elem in element['paragraph'].get('elements', []):
                    if 'textRun' in elem:
                        text.append(elem['textRun']['content'])

        return ''.join(text)
```

**Setup OAuth2:**
1. Create Google Cloud project
2. Enable Drive, Docs, Sheets APIs
3. Create OAuth2 credentials
4. Implement authorization flow
5. Store refresh tokens securely

**Effort:** 8-10 hours

---

## 3. CREATE REMAINING DEPARTMENT MODULES

**Problem:** Only 2 of 30+ department modules exist
- Cinematography ✅
- Directing ✅
- Missing: 28+ departments

**Impact:** System only useful for 2 departments

**Solution:** Create remaining department YAML configs

**Departments to create:**
1. Production Design (high priority)
2. Sound (production & post)
3. Editing
4. Costume Design
5. Hair & Makeup
6. Props
7. Set Decoration
8. Construction
9. Art Department
10. Lighting (Gaffer)
11. Grip
12. VFX
13. Stunts
14. Locations
15. Casting
16. Music
17. Post Sound
18. Color/DI
19. Writing
20. Producing (multiple types)
21. Unit Production Management
22. Assistant Directing
23. Transportation
24. Catering
25. Safety
26. Legal/Business Affairs
27. Marketing
28. Accounting

**Template (based on existing cinematography.yaml):**
```yaml
department:
  code: "XXX"
  name: "Department Name"
  full_name: "Full Department Name"
  description: "Brief description"

key_personnel:
  - role: "Primary Role"
    responsibilities:
      - "Responsibility 1"
      - "Responsibility 2"

knowledge_foundation:
  core_concepts:
    - concept: "Concept Name"
      description: "Description"
      key_elements:
        - "Element 1"
        - "Element 2"

workflow:
  pre_production:
    - "Step 1"
    - "Step 2"
  production:
    - "Step 1"
  post_production:
    - "Step 1"

collaboration_matrix:
  primary_collaborators:
    - department: "Other Department"
      interaction: "Frequency and nature"
      key_touchpoints:
        - "Touchpoint 1"

document_types:
  creates:
    - "Document Type 1"
  references:
    - "Document Type 1"

query_templates:
  common_questions:
    - "Sample question?"

decision_points:
  critical_decisions:
    - decision: "Decision Name"
      timing: "When"
      factors:
        - "Factor 1"
      affects: ["Department 1", "Department 2"]

resource_requirements:
  equipment:
    - "Item 1"
  personnel:
    minimum_crew:
      - "Role 1"
  budget_considerations:
    - "Consideration 1"

risk_factors:
  common_challenges:
    - challenge: "Challenge Name"
      mitigation:
        - "Mitigation 1"

foundational_texts:
  essential_reading:
    - "Book 1"
  online_resources:
    - "Resource 1"

production_scales:
  micro_budget:
    typical_setup: "Description"
    focus: "Focus areas"
  low_budget:
    typical_setup: "Description"
  mid_budget:
    typical_setup: "Description"
  studio:
    typical_setup: "Description"
```

**Effort:** 6-8 hours (can use research already done, ~15 min per department)

---

## 4. IMPLEMENT QUERY TEMPLATES SYSTEM

**Problem:** No pre-built query templates
- Users must compose queries from scratch
- Inconsistent query formats
- Missing department-specific optimizations

**Impact:** Harder to use, less efficient queries

**Solution:** Create template system with common queries

Create `/home/user/vision-vault/templates/queries/cinematography.yaml`:
```yaml
department: "Cinematography"

templates:
  - id: "cin_lighting_plan"
    name: "Get Lighting Plan"
    template: "What is the lighting approach for {scene}?"
    parameters:
      - name: "scene"
        type: "string"
        description: "Scene number or description"

  - id: "cin_camera_movement"
    name: "Get Camera Movement"
    template: "What camera movement is planned for {scene}?"
    parameters:
      - name: "scene"
        type: "string"

  - id: "cin_lens_selection"
    name: "Get Lens Choice"
    template: "What lenses are designated for {subject}?"
    parameters:
      - name: "subject"
        type: "string"
        description: "Scene, character, or sequence"

  - id: "cin_color_palette"
    name: "Get Color Palette"
    template: "What color palette is established for {context}?"
    parameters:
      - name: "context"
        type: "string"
        description: "Scene, location, or character"

  - id: "cin_visual_style"
    name: "Get Visual Style Notes"
    template: "What are the director's visual style notes for {context}?"
    parameters:
      - name: "context"
        type: "string"

  - id: "cin_special_equipment"
    name: "Get Special Equipment Needs"
    template: "What special equipment is needed for {scene}?"
    parameters:
      - name: "scene"
        type: "string"

  - id: "cin_conflicts"
    name: "Check for Cinematography Conflicts"
    template: "Are there any conflicts affecting Cinematography for {timeframe}?"
    parameters:
      - name: "timeframe"
        type: "string"
        description: "Date, day, or period"
```

**Template executor:**
```python
class QueryTemplateExecutor:
    """Execute query templates with parameter substitution."""

    def __init__(self, template_dir: str = "./templates/queries"):
        self.templates = self._load_templates(template_dir)

    def execute(
        self,
        template_id: str,
        parameters: Dict[str, str]
    ) -> str:
        """
        Execute template with parameters.

        Args:
            template_id: Template identifier (e.g., "cin_lighting_plan")
            parameters: Parameter values

        Returns:
            Formatted query string
        """
        template = self.templates.get(template_id)
        if not template:
            raise ValueError(f"Template not found: {template_id}")

        # Substitute parameters
        query = template["template"].format(**parameters)
        return query

    def list_templates(self, department: str = None) -> List[Dict]:
        """List available templates, optionally filtered by department."""
        if department:
            return [t for t in self.templates.values() if t.get("department") == department]
        return list(self.templates.values())
```

**Effort:** 4 hours

---

## 5. ADD PROGRESS INDICATORS (NEURODIVERGENT UX)

**Problem:** No visual feedback during long operations
- Users don't know if system is working
- No progress indication
- Poor ADHD-friendly UX

**Impact:** Confusion, anxiety during use

**Solution:** Add rich progress indicators

```python
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn

console = Console()

# For CLI:
with Progress(
    SpinnerColumn(),
    TextColumn("[progress.description]{task.description}"),
    BarColumn(),
    TaskProgressColumn(),
) as progress:
    task = progress.add_task("Processing document...", total=100)

    # Update as processing progresses
    progress.update(task, advance=10, description="Extracting text...")
    # ...
    progress.update(task, advance=30, description="Analyzing with AI...")
    # ...
    progress.update(task, advance=40, description="Storing in knowledge base...")
    # ...
    progress.update(task, advance=20, description="Complete!")

# For API (return status endpoint):
@app.get("/api/status/{task_id}")
async def get_task_status(task_id: str):
    return {
        "task_id": task_id,
        "status": "processing",
        "progress": 65,
        "current_step": "Analyzing with AI",
        "estimated_remaining": "15 seconds"
    }
```

**Features to add:**
- Spinner for indeterminate tasks
- Progress bar for deterministic tasks
- Estimated time remaining
- Current step description
- Success/error states with clear icons

**Effort:** 3-4 hours

---

## 6. CREATE USER GUIDE & API DOCUMENTATION

**Problem:** No end-user documentation
- Users don't know how to use system
- No API reference
- No examples

**Impact:** Poor adoption, support burden

**Solution:** Create comprehensive docs

**docs/USER_GUIDE.md** - See HIGH priority #3

**docs/API.md:**
```markdown
# Vision Vault API Reference

## Authentication

All API requests require authentication (if enabled):
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://api.visionvault.com/v1/query
```

## Endpoints

### Upload Document
```http
POST /api/documents/upload
Content-Type: multipart/form-data

Parameters:
- file: File (required)
- department: string (optional)
- metadata: JSON string (optional)

Response:
{
  "success": true,
  "document_id": "DOC-20251126-Script-a1b2c3d4",
  "content_length": 12453,
  "metadata": {...}
}
```

### Query Knowledge Base
```http
POST /api/query
Content-Type: application/json

{
  "query": "What is the lighting plan for Scene 12?",
  "department": "Cinematography",
  "limit": 10
}

Response:
{
  "success": true,
  "results": [
    {
      "document_id": "DOC-...",
      "content": "...",
      "relevance": 0.95,
      "metadata": {...}
    }
  ],
  "ai_analysis": "..."
}
```

### Get Conflicts
```http
GET /api/conflicts?department=Cinematography

Response:
{
  "conflicts": [
    {
      "conflict_id": "CONF-2025-001",
      "type": "schedule",
      "severity": "high",
      "description": "...",
      "affected_departments": ["Cinematography", "Locations"],
      "recommended_actions": [...]
    }
  ]
}
```

## Python SDK

```python
from vision_vault import VisionVaultClient

# Initialize
client = VisionVaultClient(api_key="YOUR_API_KEY")

# Upload document
result = client.upload_document(
    file_path="script.pdf",
    department="Writing",
    metadata={"version": 3, "status": "Final"}
)

# Query
results = client.query(
    "What is the DP's visual approach?",
    department="Cinematography"
)

# Get conflicts
conflicts = client.get_conflicts(department="Cinematography")
```

## Rate Limits
- 60 requests per minute
- 1000 requests per day
- Contact for higher limits

## Error Codes
- 400: Bad Request (invalid parameters)
- 401: Unauthorized (missing/invalid API key)
- 429: Too Many Requests (rate limit exceeded)
- 500: Internal Server Error
```

**Effort:** 4-5 hours

---

## SUMMARY

**Total Medium Priority Fixes:** 6
**Total Estimated Effort:** 24-32 hours
**Timeline:** 1-2 weeks (after high priority complete)

### Benefits

After medium priority fixes:
- ✅ User-friendly web interface
- ✅ Google Workspace integration
- ✅ All 30+ departments configured
- ✅ Query template system
- ✅ ADHD-friendly UX with progress indicators
- ✅ Complete documentation

**Result:** Production-ready system that teams can actually use!

These fixes transform Vision Vault from a functional MVP into a polished, user-friendly production tool.
