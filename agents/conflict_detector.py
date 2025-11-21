"""
Vision Vault Conflict Detection Agent

Analyzes production documents to identify potential conflicts between departments,
schedules, budgets, creative vision, and technical requirements.
"""

from typing import Dict, Any, List, Optional, Tuple
from datetime import datetime
import json
from enum import Enum

from .base_agent import AnalysisAgent


class ConflictType(Enum):
    """Types of conflicts that can be detected."""
    SCHEDULE = "schedule"
    BUDGET = "budget"
    CREATIVE_VISION = "creative_vision"
    TECHNICAL_FEASIBILITY = "technical_feasibility"
    RESOURCE_ALLOCATION = "resource_allocation"
    SAFETY = "safety"
    LEGAL_COMPLIANCE = "legal_compliance"
    DEPARTMENTAL = "departmental"
    CONTINUITY = "continuity"


class ConflictSeverity(Enum):
    """Severity levels for detected conflicts."""
    CRITICAL = "critical"  # Production-stopping
    HIGH = "high"          # Requires immediate attention
    MEDIUM = "medium"      # Should be addressed soon
    LOW = "low"            # Monitor and address when convenient


class ConflictDetector(AnalysisAgent):
    """
    Agent that detects conflicts between production documents and decisions.

    This agent analyzes:
    - Schedule overlaps and dependencies
    - Budget allocation conflicts
    - Creative vision discrepancies
    - Technical feasibility issues
    - Resource allocation problems
    - Safety concerns
    - Legal and compliance conflicts
    """

    def __init__(self, agent_id: Optional[str] = None, config: Optional[Dict[str, Any]] = None):
        super().__init__(agent_id, config)
        self.conflict_rules = self._load_conflict_rules()
        self.detected_conflicts = []

    def _load_conflict_rules(self) -> Dict[str, Any]:
        """
        Load conflict detection rules.

        Returns:
            Dictionary of conflict detection rules
        """
        return {
            "schedule": {
                "check_location_overlap": True,
                "check_crew_double_booking": True,
                "check_equipment_overlap": True,
                "check_cast_availability": True
            },
            "budget": {
                "check_department_overrun": True,
                "check_total_budget_exceeded": True,
                "check_unallocated_costs": True
            },
            "creative": {
                "check_vision_consistency": True,
                "check_character_continuity": True,
                "check_visual_style_conflicts": True
            },
            "technical": {
                "check_equipment_compatibility": True,
                "check_format_consistency": True,
                "check_workflow_conflicts": True
            },
            "safety": {
                "check_hazard_mitigation": True,
                "check_compliance_requirements": True
            }
        }

    def get_capabilities(self) -> List[str]:
        """Return capabilities of this agent."""
        return [
            "schedule_conflict_detection",
            "budget_conflict_detection",
            "creative_vision_analysis",
            "technical_feasibility_check",
            "resource_allocation_analysis",
            "safety_concern_identification",
            "departmental_conflict_detection",
            "continuity_checking"
        ]

    def process(self, input_data: Any, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Process a document or decision to detect conflicts.

        Args:
            input_data: Document or decision data to analyze
            context: Knowledge base and related documents

        Returns:
            Dictionary with detected conflicts
        """
        start_time = datetime.now()

        if not self.validate_input(input_data):
            return self.create_response(
                success=False,
                data=None,
                message="Invalid input data for conflict detection"
            )

        # Extract document metadata
        document = input_data
        metadata = document.get("metadata", {})
        department = metadata.get("department")
        doc_type = metadata.get("document_type")

        # Get knowledge base from context
        knowledge_base = context.get("knowledge_base", {}) if context else {}

        # Run conflict detection checks
        conflicts = []

        # Schedule conflicts
        if self.conflict_rules["schedule"]["check_location_overlap"]:
            conflicts.extend(self._check_schedule_conflicts(document, knowledge_base))

        # Budget conflicts
        if self.conflict_rules["budget"]["check_department_overrun"]:
            conflicts.extend(self._check_budget_conflicts(document, knowledge_base))

        # Creative vision conflicts
        if self.conflict_rules["creative"]["check_vision_consistency"]:
            conflicts.extend(self._check_creative_conflicts(document, knowledge_base))

        # Technical feasibility conflicts
        if self.conflict_rules["technical"]["check_equipment_compatibility"]:
            conflicts.extend(self._check_technical_conflicts(document, knowledge_base))

        # Resource allocation conflicts
        conflicts.extend(self._check_resource_conflicts(document, knowledge_base))

        # Safety conflicts
        if self.conflict_rules["safety"]["check_hazard_mitigation"]:
            conflicts.extend(self._check_safety_conflicts(document, knowledge_base))

        # Departmental dependency conflicts
        conflicts.extend(self._check_departmental_conflicts(document, knowledge_base))

        # Store detected conflicts
        self.detected_conflicts.extend(conflicts)

        # Generate summary
        summary = self._generate_conflict_summary(conflicts)

        # Log processing
        duration = (datetime.now() - start_time).total_seconds()
        self.log_processing(input_data, {"conflicts_found": len(conflicts)}, duration)

        return self.create_response(
            success=True,
            data={
                "conflicts": conflicts,
                "summary": summary,
                "total_conflicts": len(conflicts),
                "by_severity": self._count_by_severity(conflicts),
                "by_type": self._count_by_type(conflicts)
            },
            message=f"Detected {len(conflicts)} potential conflict(s)"
        )

    def _check_schedule_conflicts(self, document: Dict[str, Any], knowledge_base: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check for scheduling conflicts."""
        conflicts = []
        metadata = document.get("metadata", {})

        # Check if this is a schedule-related document
        doc_type = metadata.get("document_type")
        if doc_type not in ["Call Sheet", "Production Schedule", "Day Out of Days"]:
            return conflicts

        # Extract schedule information
        content = document.get("content", {})
        shoot_date = content.get("shoot_date") or metadata.get("related_date")
        location = content.get("location")
        cast_required = content.get("cast", [])
        crew_required = content.get("crew", [])
        equipment_required = content.get("equipment", [])

        # Check against other schedule documents
        for doc_id, kb_doc in knowledge_base.items():
            kb_metadata = kb_doc.get("metadata", {})
            kb_content = kb_doc.get("content", {})

            # Skip if not a schedule document
            if kb_metadata.get("document_type") not in ["Call Sheet", "Production Schedule"]:
                continue

            # Skip if same document
            if kb_metadata.get("document_id") == metadata.get("document_id"):
                continue

            kb_shoot_date = kb_content.get("shoot_date") or kb_metadata.get("related_date")

            # Check for same date conflicts
            if shoot_date and kb_shoot_date == shoot_date:
                # Location overlap
                if location and kb_content.get("location") == location:
                    conflicts.append(self._create_conflict(
                        conflict_type=ConflictType.SCHEDULE,
                        severity=ConflictSeverity.HIGH,
                        description=f"Location '{location}' is scheduled for multiple shoots on {shoot_date}",
                        source_document=metadata.get("document_id"),
                        conflicting_document=kb_metadata.get("document_id"),
                        affected_departments=["Locations", "Production"],
                        details={
                            "date": shoot_date,
                            "location": location
                        }
                    ))

                # Cast double-booking
                overlapping_cast = set(cast_required) & set(kb_content.get("cast", []))
                if overlapping_cast:
                    conflicts.append(self._create_conflict(
                        conflict_type=ConflictType.SCHEDULE,
                        severity=ConflictSeverity.CRITICAL,
                        description=f"Cast member(s) {', '.join(overlapping_cast)} double-booked on {shoot_date}",
                        source_document=metadata.get("document_id"),
                        conflicting_document=kb_metadata.get("document_id"),
                        affected_departments=["Production", "Casting"],
                        details={
                            "date": shoot_date,
                            "cast": list(overlapping_cast)
                        }
                    ))

                # Equipment overlap
                overlapping_equipment = set(equipment_required) & set(kb_content.get("equipment", []))
                if overlapping_equipment:
                    conflicts.append(self._create_conflict(
                        conflict_type=ConflictType.RESOURCE_ALLOCATION,
                        severity=ConflictSeverity.HIGH,
                        description=f"Equipment {', '.join(overlapping_equipment)} scheduled for multiple shoots on {shoot_date}",
                        source_document=metadata.get("document_id"),
                        conflicting_document=kb_metadata.get("document_id"),
                        affected_departments=["Camera", "Grip", "Lighting"],
                        details={
                            "date": shoot_date,
                            "equipment": list(overlapping_equipment)
                        }
                    ))

        return conflicts

    def _check_budget_conflicts(self, document: Dict[str, Any], knowledge_base: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check for budget-related conflicts."""
        conflicts = []
        metadata = document.get("metadata", {})
        content = document.get("content", {})

        # Only check budget documents
        if metadata.get("document_type") not in ["Budget", "Cost Report", "Purchase Order"]:
            return conflicts

        department = metadata.get("department")
        allocated_amount = content.get("allocated_amount", 0)
        spent_amount = content.get("spent_amount", 0)
        projected_amount = content.get("projected_amount", 0)

        # Check for department budget overrun
        if projected_amount > allocated_amount:
            overrun_percentage = ((projected_amount - allocated_amount) / allocated_amount) * 100

            severity = ConflictSeverity.CRITICAL if overrun_percentage > 20 else ConflictSeverity.HIGH

            conflicts.append(self._create_conflict(
                conflict_type=ConflictType.BUDGET,
                severity=severity,
                description=f"{department} projected to exceed budget by {overrun_percentage:.1f}%",
                source_document=metadata.get("document_id"),
                conflicting_document=None,
                affected_departments=[department, "Production", "Accounting"],
                details={
                    "allocated": allocated_amount,
                    "projected": projected_amount,
                    "overrun": projected_amount - allocated_amount,
                    "overrun_percentage": overrun_percentage
                }
            ))

        # Check against master budget
        for doc_id, kb_doc in knowledge_base.items():
            kb_metadata = kb_doc.get("metadata", {})

            if kb_metadata.get("document_type") == "Budget" and kb_metadata.get("department") == "Production":
                master_budget = kb_doc.get("content", {})
                total_budget = master_budget.get("total_budget", 0)

                # Calculate total projected spend across all departments
                total_projected = self._calculate_total_projected_spend(knowledge_base)

                if total_projected > total_budget:
                    conflicts.append(self._create_conflict(
                        conflict_type=ConflictType.BUDGET,
                        severity=ConflictSeverity.CRITICAL,
                        description=f"Total production budget exceeded by ${total_projected - total_budget:,.2f}",
                        source_document=metadata.get("document_id"),
                        conflicting_document=kb_metadata.get("document_id"),
                        affected_departments=["All Departments"],
                        details={
                            "total_budget": total_budget,
                            "total_projected": total_projected,
                            "overage": total_projected - total_budget
                        }
                    ))

        return conflicts

    def _check_creative_conflicts(self, document: Dict[str, Any], knowledge_base: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check for creative vision conflicts."""
        conflicts = []
        metadata = document.get("metadata", {})
        content = document.get("content", {})

        # Only check creative documents
        doc_type = metadata.get("document_type")
        if doc_type not in ["Lookbook", "Concept Art", "Storyboard", "Creative Brief", "Director's Notes"]:
            return conflicts

        department = metadata.get("department")

        # Check for conflicting creative direction
        # This would use AI analysis in production to compare creative visions

        # For now, check for explicit conflicting notes
        creative_notes = content.get("creative_notes", "")
        visual_style = content.get("visual_style", "")

        for doc_id, kb_doc in knowledge_base.items():
            kb_metadata = kb_doc.get("metadata", {})
            kb_content = kb_doc.get("content", {})

            # Compare with other creative documents for same scenes
            if kb_metadata.get("document_type") in ["Lookbook", "Creative Brief", "Director's Notes"]:
                # Check if they reference the same scenes
                related_scenes = set(metadata.get("related_scenes", "").split(","))
                kb_related_scenes = set(kb_metadata.get("related_scenes", "").split(","))

                if related_scenes & kb_related_scenes:
                    # Found documents about same scenes from different departments
                    if metadata.get("department") != kb_metadata.get("department"):
                        # This would trigger AI analysis to compare creative intent
                        # For demonstration, flag potential conflict
                        conflicts.append(self._create_conflict(
                            conflict_type=ConflictType.CREATIVE_VISION,
                            severity=ConflictSeverity.MEDIUM,
                            description=f"Multiple creative directions defined for scenes {', '.join(related_scenes & kb_related_scenes)}",
                            source_document=metadata.get("document_id"),
                            conflicting_document=kb_metadata.get("document_id"),
                            affected_departments=[department, kb_metadata.get("department")],
                            details={
                                "scenes": list(related_scenes & kb_related_scenes),
                                "departments": [department, kb_metadata.get("department")]
                            },
                            recommendation="Review creative direction with Director and affected department heads"
                        ))

        return conflicts

    def _check_technical_conflicts(self, document: Dict[str, Any], knowledge_base: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check for technical feasibility conflicts."""
        conflicts = []
        metadata = document.get("metadata", {})
        content = document.get("content", {})

        # Check technical documents
        if metadata.get("document_type") not in ["Equipment List", "Tech Scout Report", "Technical Specifications"]:
            return conflicts

        # Check for format/workflow incompatibilities
        if "technical_specs" in content:
            specs = content["technical_specs"]

            # Check camera format compatibility
            if "camera_format" in specs:
                camera_format = specs["camera_format"]

                # Check against post-production workflow
                for doc_id, kb_doc in knowledge_base.items():
                    kb_metadata = kb_doc.get("metadata", {})
                    if kb_metadata.get("department") == "Post-Production":
                        kb_content = kb_doc.get("content", {})
                        post_workflow = kb_content.get("workflow", {})

                        if "supported_formats" in post_workflow:
                            if camera_format not in post_workflow["supported_formats"]:
                                conflicts.append(self._create_conflict(
                                    conflict_type=ConflictType.TECHNICAL_FEASIBILITY,
                                    severity=ConflictSeverity.HIGH,
                                    description=f"Camera format '{camera_format}' not supported by post-production workflow",
                                    source_document=metadata.get("document_id"),
                                    conflicting_document=kb_metadata.get("document_id"),
                                    affected_departments=["Cinematography", "Post-Production"],
                                    details={
                                        "camera_format": camera_format,
                                        "supported_formats": post_workflow["supported_formats"]
                                    },
                                    recommendation="Update camera selection or post-production workflow"
                                ))

        return conflicts

    def _check_resource_conflicts(self, document: Dict[str, Any], knowledge_base: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check for resource allocation conflicts."""
        conflicts = []
        # Implementation similar to schedule conflicts but focused on resource sharing
        return conflicts

    def _check_safety_conflicts(self, document: Dict[str, Any], knowledge_base: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check for safety-related conflicts."""
        conflicts = []
        metadata = document.get("metadata", {})
        content = document.get("content", {})

        # Check for safety concerns
        if "safety_requirements" in content:
            safety_reqs = content["safety_requirements"]

            # Check if special effects have safety plan
            if metadata.get("department") == "Special Effects":
                has_safety_plan = content.get("safety_plan_approved", False)

                if not has_safety_plan:
                    conflicts.append(self._create_conflict(
                        conflict_type=ConflictType.SAFETY,
                        severity=ConflictSeverity.CRITICAL,
                        description="Special effects planned without approved safety plan",
                        source_document=metadata.get("document_id"),
                        conflicting_document=None,
                        affected_departments=["Special Effects", "Safety", "Production"],
                        details={"safety_requirements": safety_reqs},
                        recommendation="Obtain safety coordinator approval before proceeding"
                    ))

        return conflicts

    def _check_departmental_conflicts(self, document: Dict[str, Any], knowledge_base: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Check for inter-departmental conflicts."""
        conflicts = []
        metadata = document.get("metadata", {})

        # Check if document lists dependencies
        dependencies = metadata.get("dependencies", "")
        if dependencies:
            dep_list = [d.strip() for d in dependencies.split(",")]

            # Check if dependent departments have provided necessary information
            for dep_dept in dep_list:
                has_info = False
                for doc_id, kb_doc in knowledge_base.items():
                    if kb_doc.get("metadata", {}).get("department") == dep_dept:
                        has_info = True
                        break

                if not has_info:
                    conflicts.append(self._create_conflict(
                        conflict_type=ConflictType.DEPARTMENTAL,
                        severity=ConflictSeverity.MEDIUM,
                        description=f"Document depends on {dep_dept} but no information found",
                        source_document=metadata.get("document_id"),
                        conflicting_document=None,
                        affected_departments=[metadata.get("department"), dep_dept],
                        details={"missing_department": dep_dept},
                        recommendation=f"Coordinate with {dep_dept} to provide necessary information"
                    ))

        return conflicts

    def _create_conflict(self,
                        conflict_type: ConflictType,
                        severity: ConflictSeverity,
                        description: str,
                        source_document: str,
                        conflicting_document: Optional[str],
                        affected_departments: List[str],
                        details: Dict[str, Any],
                        recommendation: Optional[str] = None) -> Dict[str, Any]:
        """Create a standardized conflict report."""
        return {
            "conflict_id": f"CONF-{datetime.now().strftime('%Y%m%d')}-{len(self.detected_conflicts) + 1:04d}",
            "type": conflict_type.value,
            "severity": severity.value,
            "description": description,
            "source_document": source_document,
            "conflicting_document": conflicting_document,
            "affected_departments": affected_departments,
            "details": details,
            "recommendation": recommendation or self._generate_recommendation(conflict_type, severity),
            "detected_at": datetime.now().isoformat(),
            "status": "unresolved"
        }

    def _generate_recommendation(self, conflict_type: ConflictType, severity: ConflictSeverity) -> str:
        """Generate a recommendation based on conflict type and severity."""
        recommendations = {
            ConflictType.SCHEDULE: {
                ConflictSeverity.CRITICAL: "Immediate schedule revision required - contact all affected parties",
                ConflictSeverity.HIGH: "Reschedule or reallocate resources within 24 hours",
                ConflictSeverity.MEDIUM: "Adjust schedule at next production meeting",
                ConflictSeverity.LOW: "Monitor and adjust if necessary"
            },
            ConflictType.BUDGET: {
                ConflictSeverity.CRITICAL: "Emergency budget meeting required - may need to cut scenes or find additional funding",
                ConflictSeverity.HIGH: "Review and reallocate budget with producers",
                ConflictSeverity.MEDIUM: "Monitor spending and plan cost reductions",
                ConflictSeverity.LOW: "Note for future budget reviews"
            },
            # Add more recommendations for other conflict types
        }

        return recommendations.get(conflict_type, {}).get(
            severity,
            "Review with relevant department heads and production team"
        )

    def _generate_conflict_summary(self, conflicts: List[Dict[str, Any]]) -> str:
        """Generate a human-readable summary of detected conflicts."""
        if not conflicts:
            return "No conflicts detected."

        by_severity = self._count_by_severity(conflicts)
        by_type = self._count_by_type(conflicts)

        summary_parts = [f"Detected {len(conflicts)} conflict(s):"]

        if by_severity.get("critical", 0) > 0:
            summary_parts.append(f"  - {by_severity['critical']} CRITICAL (requires immediate attention)")

        if by_severity.get("high", 0) > 0:
            summary_parts.append(f"  - {by_severity['high']} HIGH priority")

        if by_severity.get("medium", 0) > 0:
            summary_parts.append(f"  - {by_severity['medium']} MEDIUM priority")

        if by_severity.get("low", 0) > 0:
            summary_parts.append(f"  - {by_severity['low']} LOW priority")

        summary_parts.append("\nBy type:")
        for conflict_type, count in by_type.items():
            summary_parts.append(f"  - {conflict_type}: {count}")

        return "\n".join(summary_parts)

    def _count_by_severity(self, conflicts: List[Dict[str, Any]]) -> Dict[str, int]:
        """Count conflicts by severity level."""
        counts = {"critical": 0, "high": 0, "medium": 0, "low": 0}
        for conflict in conflicts:
            severity = conflict.get("severity", "low")
            counts[severity] = counts.get(severity, 0) + 1
        return counts

    def _count_by_type(self, conflicts: List[Dict[str, Any]]) -> Dict[str, int]:
        """Count conflicts by type."""
        counts = {}
        for conflict in conflicts:
            conflict_type = conflict.get("type", "unknown")
            counts[conflict_type] = counts.get(conflict_type, 0) + 1
        return counts

    def _calculate_total_projected_spend(self, knowledge_base: Dict[str, Any]) -> float:
        """Calculate total projected spending across all departments."""
        total = 0.0
        for doc_id, doc in knowledge_base.items():
            if doc.get("metadata", {}).get("document_type") == "Budget":
                content = doc.get("content", {})
                total += content.get("projected_amount", 0)
        return total

    def get_conflict_report(self, include_resolved: bool = False) -> Dict[str, Any]:
        """
        Generate a comprehensive conflict report.

        Args:
            include_resolved: Whether to include resolved conflicts

        Returns:
            Conflict report dictionary
        """
        conflicts = self.detected_conflicts
        if not include_resolved:
            conflicts = [c for c in conflicts if c.get("status") != "resolved"]

        return {
            "total_conflicts": len(conflicts),
            "by_severity": self._count_by_severity(conflicts),
            "by_type": self._count_by_type(conflicts),
            "conflicts": conflicts,
            "generated_at": datetime.now().isoformat()
        }
