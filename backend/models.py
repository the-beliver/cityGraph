from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, index=True, nullable=False)
    full_name = Column(String, nullable=True)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default="Incident Commander")
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class CitizenReportDB(Base):
    __tablename__ = "citizen_reports"

    id = Column(Integer, primary_key=True, index=True)
    report_id = Column(String, unique=True, index=True, nullable=False)
    category = Column(String, index=True, nullable=False)  # flooding, fire, waterlogging, road_blockage, emergency
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    address = Column(String, nullable=False)
    severity = Column(String, default="MEDIUM")  # LOW, MEDIUM, HIGH, CRITICAL
    verification_status = Column(String, default="UNVERIFIED")  # UNVERIFIED, VERIFIED, REJECTED, RESOLVED
    reporter_name = Column(String, nullable=True)
    reporter_contact = Column(String, nullable=True)
    source_type = Column(String, default="LIVE")  # LIVE, SIMULATED
    corroboration_count = Column(Integer, default=1)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class IncidentDB(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    incident_id = Column(String, unique=True, index=True, nullable=False)
    title = Column(String, nullable=False)
    category = Column(String, index=True, nullable=False)  # flood, fire, traffic_paralysis, structural, water_contamination, hazmat
    severity = Column(String, index=True, default="MEDIUM")  # LOW, MEDIUM, HIGH, CRITICAL
    status = Column(String, index=True, default="DETECTED")  # DETECTED, INVESTIGATING, ACTIVE, DISPATCHED, RESOLVED
    confidence = Column(Float, default=0.85)
    latitude = Column(Float, nullable=False)
    longitude = Column(Float, nullable=False)
    address = Column(String, nullable=False)
    zone_id = Column(String, nullable=True)
    detected_by = Column(String, default="City Sentinel Agent")
    correlated_event_ids = Column(Text, default="[]")  # JSON list of event_ids
    workflow_id = Column(String, nullable=True)
    workflow_status = Column(String, nullable=True)
    history_json = Column(Text, default="[]")  # JSON list of audit transitions
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))


class AgentEventDB(Base):
    __tablename__ = "agent_events"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(String, unique=True, index=True, nullable=False)
    source_agent = Column(String, index=True, nullable=False)  # Weather, Traffic, Citizen, Sensor, Sentinel
    source_type = Column(String, default="LIVE")  # LIVE, REPLAYED, SIMULATED
    category = Column(String, index=True, nullable=False)
    severity = Column(String, index=True, default="INFO")  # INFO, LOW, MEDIUM, HIGH, CRITICAL
    confidence = Column(Float, default=0.90)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    address = Column(String, nullable=True)
    zone_id = Column(String, nullable=True)
    raw_data_json = Column(Text, nullable=True)
    justification = Column(Text, nullable=True)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


class AgentLogDB(Base):
    __tablename__ = "agent_logs"

    id = Column(Integer, primary_key=True, index=True)
    log_id = Column(String, unique=True, index=True, nullable=False)
    agent_id = Column(String, index=True, nullable=False)
    level = Column(String, default="INFO")  # INFO, WARNING, ERROR, SUCCESS
    message = Column(Text, nullable=False)
    details_json = Column(Text, nullable=True)
    timestamp = Column(DateTime, default=lambda: datetime.now(timezone.utc))
