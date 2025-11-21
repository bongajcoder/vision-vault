"""
Vision Vault Base Agent
Base class for all AI agents in the Vision Vault system.
"""

from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
from datetime import datetime
import logging
import json
import uuid

class BaseAgent(ABC):
    """
    Abstract base class for all Vision Vault agents.

    All agents must inherit from this class and implement the required methods.
    """

    def __init__(self, agent_id: Optional[str] = None, config: Optional[Dict[str, Any]] = None):
        """
        Initialize the base agent.

        Args:
            agent_id: Unique identifier for this agent instance
            config: Configuration dictionary for the agent
        """
        self.agent_id = agent_id or f"{self.__class__.__name__}_{uuid.uuid4().hex[:8]}"
        self.config = config or {}
        self.logger = self._setup_logger()
        self.processing_history = []

    def _setup_logger(self) -> logging.Logger:
        """Set up logging for the agent."""
        logger = logging.Logger(self.agent_id)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            f'[%(asctime)s] [{self.agent_id}] %(levelname)s: %(message)s'
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    @abstractmethod
    def process(self, input_data: Any, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Main processing method for the agent.

        Args:
            input_data: The data to process
            context: Optional context information

        Returns:
            Dictionary containing processing results
        """
        pass

    @abstractmethod
    def get_capabilities(self) -> List[str]:
        """
        Return a list of capabilities this agent provides.

        Returns:
            List of capability strings
        """
        pass

    def validate_input(self, input_data: Any) -> bool:
        """
        Validate input data before processing.

        Args:
            input_data: The data to validate

        Returns:
            True if valid, False otherwise
        """
        # Override in subclasses for specific validation
        return input_data is not None

    def log_processing(self, input_data: Any, output_data: Any, duration: float):
        """
        Log processing activity for monitoring and debugging.

        Args:
            input_data: The input that was processed
            output_data: The output generated
            duration: Processing duration in seconds
        """
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "agent_id": self.agent_id,
            "duration_seconds": duration,
            "input_type": type(input_data).__name__,
            "output_keys": list(output_data.keys()) if isinstance(output_data, dict) else None,
            "success": output_data.get("success", True) if isinstance(output_data, dict) else True
        }
        self.processing_history.append(log_entry)
        self.logger.info(f"Processing completed in {duration:.2f}s")

    def create_response(self,
                       success: bool,
                       data: Any,
                       message: str = "",
                       metadata: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Create a standardized response dictionary.

        Args:
            success: Whether the operation was successful
            data: The result data
            message: Optional message describing the result
            metadata: Optional additional metadata

        Returns:
            Standardized response dictionary
        """
        response = {
            "agent_id": self.agent_id,
            "timestamp": datetime.now().isoformat(),
            "success": success,
            "data": data,
            "message": message
        }
        if metadata:
            response["metadata"] = metadata
        return response

    def get_processing_stats(self) -> Dict[str, Any]:
        """
        Get statistics about agent processing history.

        Returns:
            Dictionary with processing statistics
        """
        if not self.processing_history:
            return {
                "total_processed": 0,
                "success_rate": 0.0,
                "avg_duration": 0.0
            }

        total = len(self.processing_history)
        successes = sum(1 for entry in self.processing_history if entry["success"])
        avg_duration = sum(entry["duration_seconds"] for entry in self.processing_history) / total

        return {
            "agent_id": self.agent_id,
            "total_processed": total,
            "success_rate": successes / total,
            "avg_duration_seconds": avg_duration,
            "first_processed": self.processing_history[0]["timestamp"],
            "last_processed": self.processing_history[-1]["timestamp"]
        }


class DocumentProcessingAgent(BaseAgent):
    """
    Base class for agents that process documents.
    """

    def __init__(self, agent_id: Optional[str] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(agent_id, config)
        self.supported_formats = self.config.get("supported_formats", [])

    def validate_document(self, document: Dict[str, Any]) -> bool:
        """
        Validate that a document has required fields and format.

        Args:
            document: Document dictionary to validate

        Returns:
            True if valid, False otherwise
        """
        required_fields = ["document_id", "document_type", "file_path"]

        for field in required_fields:
            if field not in document:
                self.logger.error(f"Missing required field: {field}")
                return False

        # Check file format if supported_formats is specified
        if self.supported_formats:
            file_ext = document.get("file_format", "").lower()
            if file_ext not in self.supported_formats:
                self.logger.error(f"Unsupported file format: {file_ext}")
                return False

        return True

    def extract_metadata(self, document: Dict[str, Any]) -> Dict[str, Any]:
        """
        Extract metadata from a document.

        Args:
            document: Document dictionary

        Returns:
            Extracted metadata dictionary
        """
        metadata_fields = [
            "department", "creator", "creation_date", "version",
            "status", "certainty_level", "production_phase"
        ]

        return {
            field: document.get(field)
            for field in metadata_fields
            if field in document
        }


class AnalysisAgent(BaseAgent):
    """
    Base class for agents that analyze production data.
    """

    def __init__(self, agent_id: Optional[str] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(agent_id, config)
        self.analysis_threshold = self.config.get("analysis_threshold", 0.7)

    def generate_recommendations(self, analysis_results: Dict[str, Any]) -> List[Dict[str, str]]:
        """
        Generate actionable recommendations based on analysis results.

        Args:
            analysis_results: Results from analysis

        Returns:
            List of recommendation dictionaries
        """
        # Override in subclasses with specific recommendation logic
        return []

    def assess_severity(self, issue: Dict[str, Any]) -> str:
        """
        Assess the severity of an identified issue.

        Args:
            issue: Issue dictionary

        Returns:
            Severity level: "critical", "high", "medium", "low"
        """
        # Override in subclasses with specific severity logic
        impact_score = issue.get("impact_score", 0.5)

        if impact_score >= 0.9:
            return "critical"
        elif impact_score >= 0.7:
            return "high"
        elif impact_score >= 0.4:
            return "medium"
        else:
            return "low"


class MultiModalAgent(DocumentProcessingAgent):
    """
    Base class for agents that process multiple types of media.
    """

    def __init__(self, agent_id: Optional[str] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(agent_id, config)
        self.modality_handlers = {}

    def register_modality(self, modality: str, handler_func):
        """
        Register a handler function for a specific modality.

        Args:
            modality: Modality type (e.g., "text", "image", "video")
            handler_func: Function to handle that modality
        """
        self.modality_handlers[modality] = handler_func
        self.logger.info(f"Registered handler for modality: {modality}")

    def detect_modality(self, document: Dict[str, Any]) -> str:
        """
        Detect the modality of a document.

        Args:
            document: Document dictionary

        Returns:
            Detected modality string
        """
        file_format = document.get("file_format", "").lower()

        # Text formats
        if file_format in [".pdf", ".docx", ".txt", ".md", ".gdoc"]:
            return "text"

        # Image formats
        elif file_format in [".jpg", ".png", ".tiff", ".psd", ".ai"]:
            return "image"

        # Video formats
        elif file_format in [".mov", ".mp4", ".mxf"]:
            return "video"

        # Audio formats
        elif file_format in [".wav", ".mp3", ".aac"]:
            return "audio"

        # Spreadsheet formats
        elif file_format in [".xlsx", ".csv", ".gsheet"]:
            return "spreadsheet"

        else:
            return "unknown"

    def process(self, input_data: Any, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process multi-modal input by routing to appropriate handler.

        Args:
            input_data: Document or data to process
            context: Optional context information

        Returns:
            Processing results dictionary
        """
        modality = self.detect_modality(input_data)

        if modality in self.modality_handlers:
            handler = self.modality_handlers[modality]
            return handler(input_data, context)
        else:
            self.logger.warning(f"No handler for modality: {modality}")
            return self.create_response(
                success=False,
                data=None,
                message=f"Unsupported modality: {modality}"
            )


class AgentOrchestrator:
    """
    Orchestrates multiple agents working together.
    """

    def __init__(self):
        self.agents = {}
        self.pipelines = {}
        self.logger = logging.Logger("AgentOrchestrator")

    def register_agent(self, agent: BaseAgent):
        """
        Register an agent with the orchestrator.

        Args:
            agent: Agent instance to register
        """
        self.agents[agent.agent_id] = agent
        self.logger.info(f"Registered agent: {agent.agent_id}")

    def create_pipeline(self, pipeline_name: str, agent_ids: List[str]):
        """
        Create a processing pipeline from multiple agents.

        Args:
            pipeline_name: Name for the pipeline
            agent_ids: List of agent IDs in processing order
        """
        pipeline = []
        for agent_id in agent_ids:
            if agent_id in self.agents:
                pipeline.append(self.agents[agent_id])
            else:
                raise ValueError(f"Agent not found: {agent_id}")

        self.pipelines[pipeline_name] = pipeline
        self.logger.info(f"Created pipeline '{pipeline_name}' with {len(pipeline)} agents")

    def execute_pipeline(self, pipeline_name: str, input_data: Any, context: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Execute a processing pipeline.

        Args:
            pipeline_name: Name of the pipeline to execute
            input_data: Input data for the pipeline
            context: Optional context information

        Returns:
            List of results from each agent in the pipeline
        """
        if pipeline_name not in self.pipelines:
            raise ValueError(f"Pipeline not found: {pipeline_name}")

        pipeline = self.pipelines[pipeline_name]
        results = []
        current_data = input_data

        for agent in pipeline:
            self.logger.info(f"Executing agent: {agent.agent_id}")
            result = agent.process(current_data, context)
            results.append(result)

            # Pass result data to next agent if successful
            if result.get("success"):
                current_data = result.get("data", current_data)
            else:
                self.logger.error(f"Agent {agent.agent_id} failed, stopping pipeline")
                break

        return results

    def get_agent_capabilities(self) -> Dict[str, List[str]]:
        """
        Get capabilities of all registered agents.

        Returns:
            Dictionary mapping agent IDs to their capabilities
        """
        return {
            agent_id: agent.get_capabilities()
            for agent_id, agent in self.agents.items()
        }
