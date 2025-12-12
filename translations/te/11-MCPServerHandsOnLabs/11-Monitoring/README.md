<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "a603abf726c7d946f0b0f05a3a42d8ac",
  "translation_date": "2025-12-11T14:21:23+00:00",
  "source_file": "11-MCPServerHandsOnLabs/11-Monitoring/README.md",
  "language_code": "te"
}
-->
# మానిటరింగ్ మరియు ఆబ్జర్వబిలిటీ

## 🎯 ఈ ల్యాబ్ ఏమి కవర్ చేస్తుంది

ఈ ల్యాబ్ మీ MCP సర్వర్ కోసం ప్రొడక్షన్ వాతావరణాలలో మానిటరింగ్, ఆబ్జర్వబిలిటీ మరియు అలర్టింగ్ అమలు చేయడానికి సమగ్ర మార్గదర్శకాన్ని అందిస్తుంది. మీరు అప్లికేషన్ ఇన్సైట్స్ సెటప్ చేయడం, అర్థవంతమైన డాష్‌బోర్డ్లను సృష్టించడం, సమర్థవంతమైన అలర్టింగ్ అమలు చేయడం మరియు ఆపరేషనల్ ఎక్సలెన్స్ కోసం ట్రబుల్‌షూటింగ్ వర్క్‌ఫ్లోలను స్థాపించడం నేర్చుకుంటారు.

## అవలోకనం

ప్రభావవంతమైన మానిటరింగ్ మరియు ఆబ్జర్వబిలిటీ ప్రొడక్షన్‌లో నమ్మకమైన MCP సర్వర్లను నిర్వహించడానికి కీలకం. ఈ ల్యాబ్ ఆబ్జర్వబిలిటీ యొక్క మూడు స్తంభాలు—మెట్రిక్స్, లాగ్స్, మరియు ట్రేసెస్—ను కవర్ చేస్తుంది మరియు మీరు ప్రో యాక్టివ్ సమస్య గుర్తింపు మరియు వేగవంతమైన సమస్య పరిష్కారానికి సమగ్ర మానిటరింగ్‌ను ఎలా అమలు చేయాలో చూపిస్తుంది.

మీరు రా టెలిమెట్రీ డేటాను చర్యలకు అనువైన అవగాహనలుగా మార్చడం నేర్చుకుంటారు, ఇది సిస్టమ్ ప్రవర్తనను అర్థం చేసుకోవడంలో, పనితీరును ఆప్టిమైజ్ చేయడంలో మరియు ఉన్నత లభ్యతను నిర్ధారించడంలో సహాయపడుతుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ ల్యాబ్ ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- **అమలు చేయండి** MCP సర్వర్ల కోసం సమగ్ర అప్లికేషన్ ఇన్సైట్స్ ఇంటిగ్రేషన్  
- **డిజైన్ చేయండి** సమర్థవంతమైన ట్రబుల్‌షూటింగ్ కోసం నిర్మిత లాగింగ్ నమూనాలు  
- **సృష్టించండి** పనితీరు మెట్రిక్స్ సేకరణ మరియు విశ్లేషణ వ్యవస్థలు  
- **కాన్ఫిగర్ చేయండి** చర్యాత్మక నోటిఫికేషన్లతో తెలివైన అలర్టింగ్  
- **నిర్మించండి** రియల్-టైమ్ మానిటరింగ్ కోసం ఆపరేషనల్ డాష్‌బోర్డ్లు  
- **స్థాపించండి** సమర్థవంతమైన ట్రబుల్‌షూటింగ్ వర్క్‌ఫ్లోలు మరియు రన్‌బుక్స్  

## 📊 అప్లికేషన్ ఇన్సైట్స్ ఇంటిగ్రేషన్

### అప్లికేషన్ ఇన్సైట్స్ సెటప్ చేయడం

```python
# mcp_server/monitoring.py
"""
Comprehensive monitoring and telemetry for MCP server.
"""
import logging
import time
import psutil
from typing import Dict, Any, Optional
from contextlib import contextmanager
from azure.monitor.opentelemetry import configure_azure_monitor
from opentelemetry import trace, metrics
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.asyncpg import AsyncPGInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor

class MCPTelemetryManager:
    """Comprehensive telemetry management for MCP server."""
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.tracer = None
        self.meter = None
        self.custom_metrics = {}
        
    def initialize_telemetry(self, app):
        """Initialize Application Insights and OpenTelemetry."""
        
        # Azure మానిటర్‌ను కాన్ఫిగర్ చేయండి
        configure_azure_monitor(
            connection_string=self.connection_string,
            logger_name="mcp_server",
            disable_offline_storage=False
        )
        
        # ట్రేసర్ మరియు మీటర్ పొందండి
        self.tracer = trace.get_tracer(__name__)
        self.meter = metrics.get_meter(__name__)
        
        # కస్టమ్ మెట్రిక్స్‌ను ప్రారంభించండి
        self._setup_custom_metrics()
        
        # FastAPI ని ఇన్స్ట్రుమెంట్ చేయండి
        FastAPIInstrumentor.instrument_app(app)
        
        # డేటాబేస్‌ను ఇన్స్ట్రుమెంట్ చేయండి
        AsyncPGInstrumentor().instrument()
        
        # HTTP అభ్యర్థనలను ఇన్స్ట్రుమెంట్ చేయండి
        RequestsInstrumentor().instrument()
        
        logging.info("Telemetry initialization complete")
    
    def _setup_custom_metrics(self):
        """Set up custom metrics for MCP server operations."""
        
        self.custom_metrics = {
            # అభ్యర్థన మెట్రిక్స్
            "mcp_requests_total": self.meter.create_counter(
                name="mcp_requests_total",
                description="Total number of MCP requests",
                unit="1"
            ),
            
            "mcp_request_duration": self.meter.create_histogram(
                name="mcp_request_duration_seconds",
                description="MCP request duration in seconds",
                unit="s"
            ),
            
            # డేటాబేస్ మెట్రిక్స్
            "database_queries_total": self.meter.create_counter(
                name="database_queries_total",
                description="Total database queries executed",
                unit="1"
            ),
            
            "database_query_duration": self.meter.create_histogram(
                name="database_query_duration_seconds",
                description="Database query duration in seconds",
                unit="s"
            ),
            
            "database_connections_active": self.meter.create_up_down_counter(
                name="database_connections_active",
                description="Number of active database connections",
                unit="1"
            ),
            
            # టూల్ మెట్రిక్స్
            "tool_executions_total": self.meter.create_counter(
                name="tool_executions_total",
                description="Total tool executions",
                unit="1"
            ),
            
            "tool_execution_duration": self.meter.create_histogram(
                name="tool_execution_duration_seconds",
                description="Tool execution duration in seconds",
                unit="s"
            ),
            
            # సిస్టమ్ మెట్రిక్స్
            "system_cpu_usage": self.meter.create_gauge(
                name="system_cpu_usage_percent",
                description="System CPU usage percentage",
                unit="%"
            ),
            
            "system_memory_usage": self.meter.create_gauge(
                name="system_memory_usage_bytes",
                description="System memory usage in bytes",
                unit="byte"
            ),
            
            # లోపం మెట్రిక్స్
            "errors_total": self.meter.create_counter(
                name="errors_total",
                description="Total number of errors",
                unit="1"
            )
        }
    
    @contextmanager
    def trace_operation(self, operation_name: str, attributes: Dict[str, Any] = None):
        """Create a traced operation with automatic metrics collection."""
        
        with self.tracer.start_as_current_span(operation_name) as span:
            start_time = time.time()
            
            # స్పాన్‌కు లక్షణాలు జోడించండి
            if attributes:
                for key, value in attributes.items():
                    span.set_attribute(key, value)
            
            try:
                yield span
                
                # విజయమెట్రిక్స్‌ను రికార్డ్ చేయండి
                duration = time.time() - start_time
                
                if "request" in operation_name.lower():
                    self.custom_metrics["mcp_requests_total"].add(1, {"status": "success"})
                    self.custom_metrics["mcp_request_duration"].record(duration)
                
                elif "query" in operation_name.lower():
                    self.custom_metrics["database_queries_total"].add(1, {"status": "success"})
                    self.custom_metrics["database_query_duration"].record(duration)
                
                elif "tool" in operation_name.lower():
                    self.custom_metrics["tool_executions_total"].add(1, {"status": "success"})
                    self.custom_metrics["tool_execution_duration"].record(duration)
                
            except Exception as e:
                # లోపాన్ని రికార్డ్ చేయండి
                span.record_exception(e)
                span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
                
                # లోపం మెట్రిక్స్‌ను రికార్డ్ చేయండి
                self.custom_metrics["errors_total"].add(1, {
                    "operation": operation_name,
                    "error_type": type(e).__name__
                })
                
                raise
    
    def record_system_metrics(self):
        """Record system-level metrics."""
        
        # CPU వినియోగం
        cpu_percent = psutil.cpu_percent(interval=1)
        self.custom_metrics["system_cpu_usage"].set(cpu_percent)
        
        # మెమరీ వినియోగం
        memory = psutil.virtual_memory()
        self.custom_metrics["system_memory_usage"].set(memory.used)
        
        # డేటాబేస్ కనెక్షన్లు (ఉపలబ్ధి ఉంటే)
        if hasattr(db_provider, 'connection_pool') and db_provider.connection_pool:
            active_connections = db_provider.connection_pool.get_size()
            self.custom_metrics["database_connections_active"].add(active_connections)

# గ్లోబల్ టెలిమెట్రీ మేనేజర్
telemetry_manager = MCPTelemetryManager(
    connection_string=config.server.applicationinsights_connection_string
)
```

### నిర్మిత డేటాతో మెరుగైన లాగింగ్

```python
# mcp_server/logging_config.py
"""
Structured logging configuration for MCP server.
"""
import logging
import json
import sys
from datetime import datetime
from typing import Dict, Any
import traceback

class StructuredFormatter(logging.Formatter):
    """Custom formatter for structured JSON logging."""
    
    def format(self, record: logging.LogRecord) -> str:
        """Format log record as structured JSON."""
        
        # ప్రాథమిక లాగ్ నిర్మాణం
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno
        }
        
        # ఉన్నట్లయితే తప్పిద సమాచారం జోడించండి
        if record.exc_info:
            log_entry["exception"] = {
                "type": record.exc_info[0].__name__,
                "message": str(record.exc_info[1]),
                "traceback": traceback.format_exception(*record.exc_info)
            }
        
        # అదనపు నుండి కస్టమ్ లక్షణాలను జోడించండి
        if hasattr(record, 'extra_data'):
            log_entry.update(record.extra_data)
        
        # అందుబాటులో ఉంటే సంబంధిత IDని జోడించండి
        if hasattr(record, 'correlation_id'):
            log_entry["correlation_id"] = record.correlation_id
        
        # అందుబాటులో ఉంటే వినియోగదారు సందర్భాన్ని జోడించండి
        if hasattr(record, 'user_id'):
            log_entry["user_id"] = record.user_id
        
        if hasattr(record, 'rls_user_id'):
            log_entry["rls_user_id"] = record.rls_user_id
        
        return json.dumps(log_entry, ensure_ascii=False)

class MCPLogger:
    """Enhanced logging utilities for MCP server."""
    
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self._setup_structured_logging()
    
    def _setup_structured_logging(self):
        """Configure structured logging."""
        
        # ఉన్న హ్యాండ్లర్లను తొలగించండి
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)
        
        # నిర్మిత హ్యాండ్లర్ సృష్టించండి
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(StructuredFormatter())
        
        self.logger.addHandler(handler)
        self.logger.setLevel(logging.INFO)
    
    def log_mcp_request(
        self, 
        method: str, 
        user_id: str, 
        rls_user_id: str,
        duration: float = None,
        status: str = "success",
        **kwargs
    ):
        """Log MCP request with structured data."""
        
        extra_data = {
            "event_type": "mcp_request",
            "method": method,
            "user_id": user_id,
            "rls_user_id": rls_user_id,
            "status": status
        }
        
        if duration is not None:
            extra_data["duration_ms"] = duration * 1000
        
        extra_data.update(kwargs)
        
        self.logger.info(
            f"MCP request: {method} - {status}",
            extra={"extra_data": extra_data}
        )
    
    def log_database_query(
        self,
        query: str,
        duration: float,
        row_count: int = None,
        user_id: str = None,
        **kwargs
    ):
        """Log database query with performance data."""
        
        extra_data = {
            "event_type": "database_query",
            "query_hash": hash(query.strip()),
            "duration_ms": duration * 1000,
            "query_preview": query[:100] + "..." if len(query) > 100 else query
        }
        
        if row_count is not None:
            extra_data["row_count"] = row_count
        
        if user_id:
            extra_data["user_id"] = user_id
        
        extra_data.update(kwargs)
        
        level = logging.WARNING if duration > 1.0 else logging.INFO
        
        self.logger.log(
            level,
            f"Database query executed ({duration*1000:.2f}ms)",
            extra={"extra_data": extra_data}
        )
    
    def log_security_event(
        self,
        event_type: str,
        user_id: str = None,
        ip_address: str = None,
        success: bool = True,
        details: Dict[str, Any] = None
    ):
        """Log security-related events."""
        
        extra_data = {
            "event_type": "security_event",
            "security_event_type": event_type,
            "success": success
        }
        
        if user_id:
            extra_data["user_id"] = user_id
        
        if ip_address:
            extra_data["ip_address"] = ip_address
        
        if details:
            extra_data["details"] = details
        
        level = logging.INFO if success else logging.WARNING
        
        self.logger.log(
            level,
            f"Security event: {event_type} - {'success' if success else 'failure'}",
            extra={"extra_data": extra_data}
        )
    
    def log_performance_metric(
        self,
        metric_name: str,
        value: float,
        unit: str = "count",
        dimensions: Dict[str, str] = None
    ):
        """Log custom performance metrics."""
        
        extra_data = {
            "event_type": "performance_metric",
            "metric_name": metric_name,
            "value": value,
            "unit": unit
        }
        
        if dimensions:
            extra_data["dimensions"] = dimensions
        
        self.logger.info(
            f"Performance metric: {metric_name} = {value} {unit}",
            extra={"extra_data": extra_data}
        )

# గ్లోబల్ లాగర్ ఉదాహరణ
mcp_logger = MCPLogger("mcp_server")
```

### కస్టమ్ మెట్రిక్స్ సేకరణ

```python
# mcp_server/metrics_collector.py
"""
Custom metrics collection for business and operational insights.
"""
import asyncio
import time
from typing import Dict, Any, List
from dataclasses import dataclass
from collections import defaultdict, deque
import statistics

@dataclass
class MetricPoint:
    """Individual metric data point."""
    timestamp: float
    value: float
    dimensions: Dict[str, str]

class MetricsCollector:
    """Advanced metrics collection and analysis."""
    
    def __init__(self, retention_minutes: int = 60):
        self.retention_seconds = retention_minutes * 60
        self.metrics_buffer = defaultdict(lambda: deque(maxlen=1000))
        self.aggregated_metrics = {}
        
    def record_metric(
        self,
        name: str,
        value: float,
        dimensions: Dict[str, str] = None
    ):
        """Record a metric point."""
        
        metric_point = MetricPoint(
            timestamp=time.time(),
            value=value,
            dimensions=dimensions or {}
        )
        
        self.metrics_buffer[name].append(metric_point)
        self._cleanup_old_metrics(name)
    
    def _cleanup_old_metrics(self, metric_name: str):
        """Remove metrics older than retention period."""
        
        cutoff_time = time.time() - self.retention_seconds
        buffer = self.metrics_buffer[metric_name]
        
        while buffer and buffer[0].timestamp < cutoff_time:
            buffer.popleft()
    
    def get_metric_summary(
        self,
        name: str,
        time_window_minutes: int = 5
    ) -> Dict[str, Any]:
        """Get statistical summary of a metric."""
        
        time_window_seconds = time_window_minutes * 60
        cutoff_time = time.time() - time_window_seconds
        
        relevant_points = [
            point for point in self.metrics_buffer[name]
            if point.timestamp >= cutoff_time
        ]
        
        if not relevant_points:
            return {"error": "No data available"}
        
        values = [point.value for point in relevant_points]
        
        return {
            "count": len(values),
            "min": min(values),
            "max": max(values),
            "mean": statistics.mean(values),
            "median": statistics.median(values),
            "p95": self._percentile(values, 95),
            "p99": self._percentile(values, 99),
            "time_window_minutes": time_window_minutes
        }
    
    def _percentile(self, values: List[float], percentile: float) -> float:
        """Calculate percentile value."""
        if not values:
            return 0
        
        sorted_values = sorted(values)
        index = int((percentile / 100) * len(sorted_values))
        index = min(index, len(sorted_values) - 1)
        
        return sorted_values[index]
    
    async def collect_business_metrics(self):
        """Collect business-specific metrics."""
        
        try:
            # ప్రశ్న అమలు నమూనాలు
            query_types = await self._analyze_query_patterns()
            for query_type, count in query_types.items():
                self.record_metric(
                    "business_queries_by_type",
                    count,
                    {"query_type": query_type}
                )
            
            # వినియోగదారు కార్యకలాప నమూనాలు
            user_activity = await self._analyze_user_activity()
            for store_id, activity_count in user_activity.items():
                self.record_metric(
                    "user_activity_by_store",
                    activity_count,
                    {"store_id": store_id}
                )
            
            # సాధనం ఉపయోగ నమూనాలు
            tool_usage = await self._analyze_tool_usage()
            for tool_name, usage_count in tool_usage.items():
                self.record_metric(
                    "tool_usage",
                    usage_count,
                    {"tool_name": tool_name}
                )
                
        except Exception as e:
            mcp_logger.logger.error(f"Business metrics collection failed: {e}")
    
    async def _analyze_query_patterns(self) -> Dict[str, int]:
        """Analyze database query patterns."""
        
        # ఇది వాస్తవ ప్రశ్న లాగ్‌లను విశ్లేషిస్తుంది
        # డెమో ప్రయోజనాల కోసం, నమూనా డేటాను తిరిగి ఇస్తోంది
        return {
            "sales_analysis": 45,
            "inventory_check": 23,
            "customer_lookup": 18,
            "product_search": 31
        }
    
    async def _analyze_user_activity(self) -> Dict[str, int]:
        """Analyze user activity by store."""
        
        # ఇది వాస్తవ వినియోగదారు కార్యకలాప లాగ్‌లను విశ్లేషిస్తుంది
        return {
            "seattle": 67,
            "redmond": 34,
            "bellevue": 23,
            "online": 89
        }
    
    async def _analyze_tool_usage(self) -> Dict[str, int]:
        """Analyze MCP tool usage patterns."""
        
        return {
            "execute_sales_query": 156,
            "get_multiple_table_schemas": 45,
            "semantic_search_products": 78,
            "get_current_utc_date": 23
        }

# గ్లోబల్ మెట్రిక్స్ కలెక్టర్
metrics_collector = MetricsCollector()
```

## 🔔 అలర్ట్ కాన్ఫిగరేషన్

### తెలివైన అలర్టింగ్ సిస్టమ్

```python
# mcp_server/alerting.py
"""
Intelligent alerting system for MCP server operations.
"""
import asyncio
import json
from typing import Dict, List, Any, Callable
from enum import Enum
from dataclasses import dataclass
from azure.communication.email import EmailClient
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class AlertSeverity(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

@dataclass
class AlertRule:
    """Alert rule configuration."""
    name: str
    condition: Callable[[Dict[str, Any]], bool]
    severity: AlertSeverity
    cooldown_minutes: int
    message_template: str
    enabled: bool = True

@dataclass
class Alert:
    """Alert instance."""
    rule_name: str
    severity: AlertSeverity
    message: str
    timestamp: float
    details: Dict[str, Any]
    acknowledged: bool = False

class AlertManager:
    """Comprehensive alerting management."""
    
    def __init__(self):
        self.alert_rules = {}
        self.active_alerts = {}
        self.alert_history = deque(maxlen=1000)
        self.notification_channels = {}
        self._setup_default_rules()
        self._setup_notification_channels()
    
    def _setup_default_rules(self):
        """Set up default alert rules."""
        
        # డేటాబేస్ కనెక్షన్ సమస్యలు
        self.add_alert_rule(AlertRule(
            name="database_connection_failure",
            condition=lambda metrics: metrics.get("database_status") != "healthy",
            severity=AlertSeverity.CRITICAL,
            cooldown_minutes=5,
            message_template="Database connection failure detected. Service may be unavailable."
        ))
        
        # అధిక లోపాల రేటు
        self.add_alert_rule(AlertRule(
            name="high_error_rate",
            condition=lambda metrics: metrics.get("error_rate", 0) > 0.05,  # 5% లోపాల రేటు
            severity=AlertSeverity.HIGH,
            cooldown_minutes=10,
            message_template="High error rate detected: {error_rate:.2%}. Investigate immediately."
        ))
        
        # మెల్లగా క్వెరీ పనితీరు
        self.add_alert_rule(AlertRule(
            name="slow_query_performance",
            condition=lambda metrics: metrics.get("avg_query_duration", 0) > 2.0,  # 2 సెకన్లు
            severity=AlertSeverity.MEDIUM,
            cooldown_minutes=15,
            message_template="Slow query performance detected. Average duration: {avg_query_duration:.2f}s"
        ))
        
        # అధిక CPU వినియోగం
        self.add_alert_rule(AlertRule(
            name="high_cpu_usage",
            condition=lambda metrics: metrics.get("cpu_usage", 0) > 85,  # 85% CPU
            severity=AlertSeverity.MEDIUM,
            cooldown_minutes=10,
            message_template="High CPU usage detected: {cpu_usage:.1f}%"
        ))
        
        # మెమరీ వినియోగం
        self.add_alert_rule(AlertRule(
            name="high_memory_usage",
            condition=lambda metrics: metrics.get("memory_usage_percent", 0) > 90,  # 90% మెమరీ
            severity=AlertSeverity.HIGH,
            cooldown_minutes=5,
            message_template="High memory usage detected: {memory_usage_percent:.1f}%"
        ))
        
        # ధృవీకరణ విఫలమవడం
        self.add_alert_rule(AlertRule(
            name="authentication_failures",
            condition=lambda metrics: metrics.get("auth_failure_rate", 0) > 0.1,  # 10% విఫల రేటు
            severity=AlertSeverity.HIGH,
            cooldown_minutes=5,
            message_template="High authentication failure rate: {auth_failure_rate:.2%}. Possible security incident."
        ))
    
    def _setup_notification_channels(self):
        """Set up notification channels."""
        
        # ఇమెయిల్ నోటిఫికేషన్లు
        email_config = {
            "smtp_server": os.getenv("SMTP_SERVER", "smtp.office365.com"),
            "smtp_port": int(os.getenv("SMTP_PORT", "587")),
            "username": os.getenv("SMTP_USERNAME"),
            "password": os.getenv("SMTP_PASSWORD"),
            "from_address": os.getenv("ALERT_FROM_EMAIL"),
            "to_addresses": os.getenv("ALERT_TO_EMAILS", "").split(",")
        }
        
        if email_config["username"] and email_config["password"]:
            self.notification_channels["email"] = EmailNotifier(email_config)
        
        # మైక్రోసాఫ్ట్ టీమ్స్ వెబ్‌హుక్
        teams_webhook = os.getenv("TEAMS_WEBHOOK_URL")
        if teams_webhook:
            self.notification_channels["teams"] = TeamsNotifier(teams_webhook)
        
        # స్లాక్ వెబ్‌హుక్
        slack_webhook = os.getenv("SLACK_WEBHOOK_URL")
        if slack_webhook:
            self.notification_channels["slack"] = SlackNotifier(slack_webhook)
    
    def add_alert_rule(self, rule: AlertRule):
        """Add or update an alert rule."""
        self.alert_rules[rule.name] = rule
    
    async def evaluate_metrics(self, metrics: Dict[str, Any]):
        """Evaluate metrics against alert rules."""
        
        for rule_name, rule in self.alert_rules.items():
            if not rule.enabled:
                continue
            
            try:
                # నియమ పరిస్థితి తీరిందో లేదో తనిఖీ చేయండి
                if rule.condition(metrics):
                    await self._trigger_alert(rule, metrics)
                else:
                    # పరిస్థితి ఇక తీరనప్పుడు అలర్ట్ క్లియర్ చేయండి
                    await self._clear_alert(rule_name)
                    
            except Exception as e:
                mcp_logger.logger.error(f"Error evaluating alert rule {rule_name}: {e}")
    
    async def _trigger_alert(self, rule: AlertRule, metrics: Dict[str, Any]):
        """Trigger an alert."""
        
        current_time = time.time()
        
        # కూల్‌డౌన్ కాలం తనిఖీ చేయండి
        if rule.name in self.active_alerts:
            last_alert_time = self.active_alerts[rule.name].timestamp
            if current_time - last_alert_time < rule.cooldown_minutes * 60:
                return  # ఇంకా కూల్‌డౌన్‌లో ఉంది
        
        # అలర్ట్ సందేశాన్ని ఫార్మాట్ చేయండి
        message = rule.message_template.format(**metrics)
        
        # అలర్ట్ సృష్టించండి
        alert = Alert(
            rule_name=rule.name,
            severity=rule.severity,
            message=message,
            timestamp=current_time,
            details=metrics.copy()
        )
        
        # అలర్ట్ నిల్వ చేయండి
        self.active_alerts[rule.name] = alert
        self.alert_history.append(alert)
        
        # నోటిఫికేషన్లు పంపండి
        await self._send_notifications(alert)
        
        mcp_logger.log_security_event(
            "alert_triggered",
            details={
                "rule_name": rule.name,
                "severity": rule.severity.value,
                "message": message
            }
        )
    
    async def _clear_alert(self, rule_name: str):
        """Clear an active alert."""
        
        if rule_name in self.active_alerts:
            alert = self.active_alerts[rule_name]
            del self.active_alerts[rule_name]
            
            # అధిక/సంక్షిప్త అలర్ట్స్ కోసం పరిష్కార నోటిఫికేషన్ పంపండి
            if alert.severity in [AlertSeverity.HIGH, AlertSeverity.CRITICAL]:
                resolution_alert = Alert(
                    rule_name=rule_name,
                    severity=AlertSeverity.LOW,
                    message=f"RESOLVED: {alert.message}",
                    timestamp=time.time(),
                    details={"resolution": True}
                )
                
                await self._send_notifications(resolution_alert)
    
    async def _send_notifications(self, alert: Alert):
        """Send alert notifications through all configured channels."""
        
        tasks = []
        
        for channel_name, notifier in self.notification_channels.items():
            task = asyncio.create_task(
                notifier.send_notification(alert),
                name=f"notify_{channel_name}"
            )
            tasks.append(task)
        
        if tasks:
            # టైమ్‌అవుట్‌తో అన్ని నోటిఫికేషన్ల కోసం వేచి ఉండండి
            try:
                await asyncio.wait_for(
                    asyncio.gather(*tasks, return_exceptions=True),
                    timeout=30.0
                )
            except asyncio.TimeoutError:
                mcp_logger.logger.warning("Some alert notifications timed out")

# నోటిఫికేషన్ అమలు విధానాలు
class EmailNotifier:
    """Email notification handler."""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
    
    async def send_notification(self, alert: Alert):
        """Send email notification."""
        
        try:
            msg = MIMEMultipart()
            msg['From'] = self.config['from_address']
            msg['To'] = ', '.join(self.config['to_addresses'])
            msg['Subject'] = f"[{alert.severity.value.upper()}] MCP Server Alert: {alert.rule_name}"
            
            body = f"""
Alert Details:
- Rule: {alert.rule_name}
- Severity: {alert.severity.value.upper()}
- Time: {datetime.fromtimestamp(alert.timestamp).isoformat()}
- Message: {alert.message}

Additional Details:
{json.dumps(alert.details, indent=2)}

This is an automated alert from the MCP Server monitoring system.
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            # ఇమెయిల్ పంపండి
            with smtplib.SMTP(self.config['smtp_server'], self.config['smtp_port']) as server:
                server.starttls()
                server.login(self.config['username'], self.config['password'])
                server.send_message(msg)
                
        except Exception as e:
            mcp_logger.logger.error(f"Failed to send email notification: {e}")

class TeamsNotifier:
    """Microsoft Teams notification handler."""
    
    def __init__(self, webhook_url: str):
        self.webhook_url = webhook_url
    
    async def send_notification(self, alert: Alert):
        """Send Teams notification."""
        
        color_map = {
            AlertSeverity.LOW: "28a745",     # ఆకుపచ్చ
            AlertSeverity.MEDIUM: "ffc107",   # పసుపు
            AlertSeverity.HIGH: "fd7e14",     # కమల రంగు
            AlertSeverity.CRITICAL: "dc3545"  # ఎరుపు
        }
        
        payload = {
            "@type": "MessageCard",
            "@context": "http://schema.org/extensions",
            "themeColor": color_map.get(alert.severity, "0076D7"),
            "summary": f"MCP Server Alert: {alert.rule_name}",
            "sections": [{
                "activityTitle": f"🚨 {alert.severity.value.upper()} Alert",
                "activitySubtitle": alert.rule_name,
                "text": alert.message,
                "facts": [
                    {"name": "Timestamp", "value": datetime.fromtimestamp(alert.timestamp).isoformat()},
                    {"name": "Severity", "value": alert.severity.value.upper()}
                ]
            }]
        }
        
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(self.webhook_url, json=payload) as response:
                    if response.status != 200:
                        raise Exception(f"Teams webhook returned {response.status}")
                        
        except Exception as e:
            mcp_logger.logger.error(f"Failed to send Teams notification: {e}")

# గ్లోబల్ అలర్ట్ మేనేజర్
alert_manager = AlertManager()
```

## 📈 డాష్‌బోర్డ్ సృష్టి

### Azure Monitor వర్క్‌బుక్స్

```json
{
  "version": "Notebook/1.0",
  "items": [
    {
      "type": 1,
      "content": {
        "json": "# MCP Server Operations Dashboard\n\nComprehensive monitoring dashboard for Zava Retail MCP Server operations, performance, and health metrics."
      },
      "name": "title"
    },
    {
      "type": 10,
      "content": {
        "chartId": "workbook-interactive-chart",
        "version": "KqlItem/1.0",
        "query": "requests\n| where timestamp >= ago(1h)\n| where name contains \"mcp\"\n| summarize RequestCount = count(), AvgDuration = avg(duration) by bin(timestamp, 5m)\n| order by timestamp asc",
        "size": 0,
        "title": "MCP Request Volume and Performance",
        "timeContext": {
          "durationMs": 3600000
        },
        "queryType": 0,
        "resourceType": "microsoft.insights/components",
        "visualization": "timechart"
      },
      "name": "request-metrics"
    },
    {
      "type": 10,
      "content": {
        "chartId": "workbook-interactive-chart-2",
        "version": "KqlItem/1.0",
        "query": "customMetrics\n| where name == \"database_query_duration_seconds\"\n| where timestamp >= ago(1h)\n| summarize \n    AvgDuration = avg(value),\n    P95Duration = percentile(value, 95),\n    P99Duration = percentile(value, 99)\n    by bin(timestamp, 5m)\n| order by timestamp asc",
        "size": 0,
        "title": "Database Query Performance",
        "timeContext": {
          "durationMs": 3600000
        },
        "queryType": 0,
        "resourceType": "microsoft.insights/components",
        "visualization": "timechart"
      },
      "name": "database-performance"
    },
    {
      "type": 10,
      "content": {
        "chartId": "workbook-interactive-chart-3",
        "version": "KqlItem/1.0",
        "query": "exceptions\n| where timestamp >= ago(24h)\n| where method contains \"mcp\"\n| summarize ErrorCount = count() by bin(timestamp, 1h), type\n| order by timestamp asc",
        "size": 0,
        "title": "Error Rate Analysis",
        "timeContext": {
          "durationMs": 86400000
        },
        "queryType": 0,
        "resourceType": "microsoft.insights/components",
        "visualization": "barchart"
      },
      "name": "error-analysis"
    },
    {
      "type": 10,
      "content": {
        "chartId": "workbook-interactive-chart-4",
        "version": "KqlItem/1.0",
        "query": "customMetrics\n| where name in (\"system_cpu_usage_percent\", \"system_memory_usage_bytes\")\n| where timestamp >= ago(2h)\n| extend MetricType = case(\n    name == \"system_cpu_usage_percent\", \"CPU %\",\n    name == \"system_memory_usage_bytes\", \"Memory GB\",\n    \"Unknown\"\n)\n| extend NormalizedValue = case(\n    name == \"system_memory_usage_bytes\", value / (1024*1024*1024),\n    value\n)\n| summarize AvgValue = avg(NormalizedValue) by bin(timestamp, 5m), MetricType\n| order by timestamp asc",
        "size": 0,
        "title": "System Resource Usage",
        "timeContext": {
          "durationMs": 7200000
        },
        "queryType": 0,
        "resourceType": "microsoft.insights/components",
        "visualization": "linechart"
      },
      "name": "system-resources"
    }
  ],
  "isLocked": false,
  "fallbackResourceIds": [
    "/subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/microsoft.insights/components/{app-insights-name}"
  ]
}
```

### కస్టమ్ డాష్‌బోర్డ్ అమలు

```python
# mcp_server/dashboard.py
"""
Custom dashboard data provider for MCP server metrics.
"""
from typing import Dict, List, Any
from fastapi import APIRouter, Depends
from datetime import datetime, timedelta

dashboard_router = APIRouter(prefix="/dashboard", tags=["dashboard"])

class DashboardDataProvider:
    """Provide dashboard data from various sources."""
    
    def __init__(self):
        self.metrics_collector = metrics_collector
        self.alert_manager = alert_manager
    
    async def get_overview_metrics(self) -> Dict[str, Any]:
        """Get high-level overview metrics."""
        
        current_time = time.time()
        one_hour_ago = current_time - 3600
        
        return {
            "timestamp": current_time,
            "active_alerts": len(self.alert_manager.active_alerts),
            "critical_alerts": len([
                alert for alert in self.alert_manager.active_alerts.values()
                if alert.severity == AlertSeverity.CRITICAL
            ]),
            "requests_last_hour": await self._get_request_count(one_hour_ago),
            "avg_response_time": await self._get_avg_response_time(one_hour_ago),
            "error_rate": await self._get_error_rate(one_hour_ago),
            "database_status": await self._get_database_status(),
            "system_health": await self._get_system_health()
        }
    
    async def get_performance_trends(self, hours: int = 24) -> Dict[str, List[Dict]]:
        """Get performance trends over time."""
        
        end_time = time.time()
        start_time = end_time - (hours * 3600)
        
        # గంటల వారీగా డేటా పాయింట్లను ఉత్పత్తి చేయండి
        data_points = []
        current = start_time
        
        while current < end_time:
            hour_start = current
            hour_end = current + 3600
            
            data_points.append({
                "timestamp": current,
                "requests": await self._get_request_count_range(hour_start, hour_end),
                "avg_duration": await self._get_avg_duration_range(hour_start, hour_end),
                "error_count": await self._get_error_count_range(hour_start, hour_end),
                "cpu_usage": await self._get_cpu_usage_range(hour_start, hour_end),
                "memory_usage": await self._get_memory_usage_range(hour_start, hour_end)
            })
            
            current = hour_end
        
        return {
            "time_series": data_points,
            "period_hours": hours,
            "data_points": len(data_points)
        }
    
    async def get_business_insights(self) -> Dict[str, Any]:
        """Get business-specific insights."""
        
        return {
            "top_queries": await self._get_top_queries(),
            "store_activity": await self._get_store_activity(),
            "tool_usage": await self._get_tool_usage_stats(),
            "user_patterns": await self._get_user_patterns(),
            "peak_hours": await self._get_peak_hours()
        }
    
    async def _get_request_count(self, since_time: float) -> int:
        """Get request count since specified time."""
        summary = self.metrics_collector.get_metric_summary(
            "mcp_requests_total",
            time_window_minutes=int((time.time() - since_time) / 60)
        )
        return summary.get("count", 0)
    
    async def _get_avg_response_time(self, since_time: float) -> float:
        """Get average response time since specified time."""
        summary = self.metrics_collector.get_metric_summary(
            "mcp_request_duration_seconds",
            time_window_minutes=int((time.time() - since_time) / 60)
        )
        return summary.get("mean", 0.0) * 1000  # మిల్లీసెకన్లకు మార్చండి
    
    async def _get_error_rate(self, since_time: float) -> float:
        """Calculate error rate since specified time."""
        
        total_requests = await self._get_request_count(since_time)
        error_summary = self.metrics_collector.get_metric_summary(
            "errors_total",
            time_window_minutes=int((time.time() - since_time) / 60)
        )
        error_count = error_summary.get("count", 0)
        
        if total_requests == 0:
            return 0.0
        
        return error_count / total_requests
    
    async def _get_database_status(self) -> str:
        """Get current database status."""
        try:
            health = await db_provider.health_check()
            return health.get("status", "unknown")
        except Exception:
            return "unhealthy"
    
    async def _get_system_health(self) -> Dict[str, Any]:
        """Get current system health metrics."""
        
        cpu_summary = self.metrics_collector.get_metric_summary("system_cpu_usage_percent", 5)
        memory_summary = self.metrics_collector.get_metric_summary("system_memory_usage_bytes", 5)
        
        return {
            "cpu_usage": cpu_summary.get("mean", 0),
            "memory_usage_gb": memory_summary.get("mean", 0) / (1024**3),
            "status": "healthy"  # వాస్తవ ఆరోగ్య లాజిక్‌ను అమలు చేస్తుంది
        }

# డాష్‌బోర్డ్ API ఎండ్‌పాయింట్లు
dashboard_provider = DashboardDataProvider()

@dashboard_router.get("/overview")
async def get_dashboard_overview():
    """Get dashboard overview data."""
    return await dashboard_provider.get_overview_metrics()

@dashboard_router.get("/performance")
async def get_performance_data(hours: int = 24):
    """Get performance trend data."""
    return await dashboard_provider.get_performance_trends(hours)

@dashboard_router.get("/business")
async def get_business_insights():
    """Get business insights data."""
    return await dashboard_provider.get_business_insights()

@dashboard_router.get("/alerts")
async def get_active_alerts():
    """Get active alerts."""
    return {
        "active_alerts": [
            {
                "rule_name": alert.rule_name,
                "severity": alert.severity.value,
                "message": alert.message,
                "timestamp": alert.timestamp,
                "acknowledged": alert.acknowledged
            }
            for alert in alert_manager.active_alerts.values()
        ],
        "alert_count": len(alert_manager.active_alerts)
    }
```

## 🔍 ట్రబుల్‌షూటింగ్ వర్క్‌ఫ్లోలు

### ఆటోమేటెడ్ డయాగ్నోస్టిక్స్

```python
# mcp_server/diagnostics.py
"""
Automated diagnostics and troubleshooting for MCP server.
"""
import asyncio
import subprocess
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

@dataclass
class DiagnosticResult:
    """Result of a diagnostic check."""
    check_name: str
    status: str  # "పాస్", "ఫెయిల్", "హెచ్చరిక"
    message: str
    details: Dict[str, Any]
    remediation: Optional[str] = None

class DiagnosticsEngine:
    """Comprehensive diagnostics engine."""
    
    def __init__(self):
        self.diagnostic_checks = []
        self._register_default_checks()
    
    def _register_default_checks(self):
        """Register default diagnostic checks."""
        
        self.diagnostic_checks = [
            self._check_database_connectivity,
            self._check_azure_services,
            self._check_system_resources,
            self._check_configuration,
            self._check_network_connectivity,
            self._check_disk_space,
            self._check_log_files,
            self._check_security_status
        ]
    
    async def run_full_diagnostics(self) -> List[DiagnosticResult]:
        """Run all diagnostic checks."""
        
        results = []
        
        for check_func in self.diagnostic_checks:
            try:
                result = await check_func()
                results.append(result)
            except Exception as e:
                results.append(DiagnosticResult(
                    check_name=check_func.__name__,
                    status="fail",
                    message=f"Diagnostic check failed: {str(e)}",
                    details={"exception": str(e)}
                ))
        
        return results
    
    async def _check_database_connectivity(self) -> DiagnosticResult:
        """Check database connectivity and performance."""
        
        try:
            start_time = time.time()
            health = await db_provider.health_check()
            duration = time.time() - start_time
            
            if health["status"] == "healthy":
                if duration > 1.0:
                    return DiagnosticResult(
                        check_name="database_connectivity",
                        status="warning",
                        message=f"Database responsive but slow ({duration:.2f}s)",
                        details=health,
                        remediation="Check database server load and network latency"
                    )
                else:
                    return DiagnosticResult(
                        check_name="database_connectivity",
                        status="pass",
                        message=f"Database healthy ({duration:.2f}s response time)",
                        details=health
                    )
            else:
                return DiagnosticResult(
                    check_name="database_connectivity",
                    status="fail",
                    message="Database not healthy",
                    details=health,
                    remediation="Check database server status and connection parameters"
                )
                
        except Exception as e:
            return DiagnosticResult(
                check_name="database_connectivity",
                status="fail",
                message=f"Database connectivity failed: {str(e)}",
                details={"error": str(e)},
                remediation="Verify database server is running and connection parameters are correct"
            )
    
    async def _check_azure_services(self) -> DiagnosticResult:
        """Check Azure AI services connectivity."""
        
        try:
            # Azure OpenAI కనెక్టివిటీని పరీక్షించండి
            from azure.identity import DefaultAzureCredential
            from azure.ai.projects import AIProjectClient
            
            credential = DefaultAzureCredential()
            project_client = AIProjectClient(
                endpoint=config.azure.project_endpoint,
                credential=credential
            )
            
            # ఇది వాస్తవ కనెక్టివిటీ పరీక్షను నిర్వహిస్తుంది
            # ఇప్పటికీ, కేవలం కాన్ఫిగరేషన్‌ను తనిఖీ చేయండి
            
            if config.azure.is_configured():
                return DiagnosticResult(
                    check_name="azure_services",
                    status="pass",
                    message="Azure services configuration valid",
                    details={
                        "project_endpoint": config.azure.project_endpoint,
                        "openai_endpoint": config.azure.openai_endpoint
                    }
                )
            else:
                return DiagnosticResult(
                    check_name="azure_services",
                    status="fail",
                    message="Azure services not properly configured",
                    details={"missing_config": "Check environment variables"},
                    remediation="Ensure all Azure configuration environment variables are set"
                )
                
        except Exception as e:
            return DiagnosticResult(
                check_name="azure_services",
                status="fail",
                message=f"Azure services check failed: {str(e)}",
                details={"error": str(e)},
                remediation="Check Azure credentials and network connectivity"
            )
    
    async def _check_system_resources(self) -> DiagnosticResult:
        """Check system resource usage."""
        
        try:
            import psutil
            
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            disk = psutil.disk_usage('/')
            
            warnings = []
            
            if cpu_percent > 85:
                warnings.append(f"High CPU usage: {cpu_percent:.1f}%")
            
            if memory.percent > 85:
                warnings.append(f"High memory usage: {memory.percent:.1f}%")
            
            if disk.percent > 85:
                warnings.append(f"High disk usage: {disk.percent:.1f}%")
            
            details = {
                "cpu_percent": cpu_percent,
                "memory_percent": memory.percent,
                "memory_available_gb": memory.available / (1024**3),
                "disk_percent": disk.percent,
                "disk_free_gb": disk.free / (1024**3)
            }
            
            if warnings:
                return DiagnosticResult(
                    check_name="system_resources",
                    status="warning",
                    message=f"Resource warnings: {'; '.join(warnings)}",
                    details=details,
                    remediation="Monitor resource usage and consider scaling"
                )
            else:
                return DiagnosticResult(
                    check_name="system_resources",
                    status="pass",
                    message="System resources normal",
                    details=details
                )
                
        except Exception as e:
            return DiagnosticResult(
                check_name="system_resources",
                status="fail",
                message=f"Resource check failed: {str(e)}",
                details={"error": str(e)}
            )
    
    async def _check_configuration(self) -> DiagnosticResult:
        """Check configuration validity."""
        
        try:
            issues = []
            
            # అవసరమైన పర్యావరణ చరాలు తనిఖీ చేయండి
            required_vars = [
                "POSTGRES_HOST", "POSTGRES_PASSWORD",
                "PROJECT_ENDPOINT", "AZURE_CLIENT_ID"
            ]
            
            for var in required_vars:
                if not os.getenv(var):
                    issues.append(f"Missing environment variable: {var}")
            
            # కాన్ఫిగరేషన్ సారూప్యతను తనిఖీ చేయండి
            if config.server.enable_health_check and not config.server.applicationinsights_connection_string:
                issues.append("Health check enabled but Application Insights not configured")
            
            if issues:
                return DiagnosticResult(
                    check_name="configuration",
                    status="fail",
                    message=f"Configuration issues: {'; '.join(issues)}",
                    details={"issues": issues},
                    remediation="Fix configuration issues and restart service"
                )
            else:
                return DiagnosticResult(
                    check_name="configuration",
                    status="pass",
                    message="Configuration valid",
                    details={"status": "all_checks_passed"}
                )
                
        except Exception as e:
            return DiagnosticResult(
                check_name="configuration",
                status="fail",
                message=f"Configuration check failed: {str(e)}",
                details={"error": str(e)}
            )

# డయాగ్నోస్టిక్ API ఎండ్‌పాయింట్
@dashboard_router.get("/diagnostics")
async def run_diagnostics():
    """Run comprehensive diagnostics."""
    
    diagnostics_engine = DiagnosticsEngine()
    results = await diagnostics_engine.run_full_diagnostics()
    
    # ఫలితాలను సారాంశం చేయండి
    summary = {
        "total_checks": len(results),
        "passed": len([r for r in results if r.status == "pass"]),
        "warnings": len([r for r in results if r.status == "warning"]),
        "failed": len([r for r in results if r.status == "fail"]),
        "overall_status": "healthy" if all(r.status in ["pass", "warning"] for r in results) else "unhealthy"
    }
    
    return {
        "summary": summary,
        "results": [
            {
                "check_name": r.check_name,
                "status": r.status,
                "message": r.message,
                "details": r.details,
                "remediation": r.remediation
            }
            for r in results
        ],
        "timestamp": time.time()
    }
```

### ఆపరేషనల్ రన్‌బుక్స్

```yaml
# operational-runbooks.yml
runbooks:
  
  database_connection_failure:
    title: "Database Connection Failure"
    description: "Steps to resolve database connectivity issues"
    severity: "critical"
    steps:
      - name: "Check database server status"
        action: "Verify PostgreSQL service is running"
        commands:
          - "docker-compose ps postgres"
          - "docker-compose logs postgres"
      
      - name: "Test network connectivity"
        action: "Verify network connection to database"
        commands:
          - "telnet postgres-host 5432"
          - "nslookup postgres-host"
      
      - name: "Check connection pool"
        action: "Verify connection pool status"
        commands:
          - "curl http://localhost:8000/health/detailed"
      
      - name: "Restart services"
        action: "Restart MCP server and database if needed"
        commands:
          - "docker-compose restart"
    
    escalation:
      - "If issue persists, contact database administrator"
      - "Check for infrastructure issues in Azure portal"

  high_error_rate:
    title: "High Error Rate Detected"
    description: "Steps to investigate and resolve high error rates"
    severity: "high"
    steps:
      - name: "Check recent logs"
        action: "Review error logs for patterns"
        commands:
          - "docker-compose logs mcp_server | grep ERROR | tail -50"
      
      - name: "Analyze error types"
        action: "Categorize errors by type and frequency"
        api_endpoint: "/dashboard/diagnostics"
      
      - name: "Check system resources"
        action: "Verify system is not under resource pressure"
        commands:
          - "curl http://localhost:8000/health/detailed"
      
      - name: "Review recent deployments"
        action: "Check if errors started after recent deployment"
        
      - name: "Enable debug logging"
        action: "Temporarily increase log level for detailed diagnostics"
        environment_variable: "LOG_LEVEL=DEBUG"

  slow_performance:
    title: "Slow Query Performance"
    description: "Steps to diagnose and improve query performance"
    severity: "medium"
    steps:
      - name: "Identify slow queries"
        action: "Find queries taking longer than normal"
        sql_query: "SELECT query, mean_exec_time FROM pg_stat_statements ORDER BY mean_exec_time DESC LIMIT 10"
      
      - name: "Check database indexes"
        action: "Verify proper indexes exist"
        sql_query: "SELECT schemaname, tablename, indexname FROM pg_indexes WHERE schemaname = 'retail'"
      
      - name: "Analyze query plans"
        action: "Review execution plans for slow queries"
        sql_command: "EXPLAIN ANALYZE"
      
      - name: "Check connection pool"
        action: "Verify connection pool is not exhausted"
        api_endpoint: "/health/detailed"
      
      - name: "Monitor resource usage"
        action: "Check CPU and memory during queries"
        commands:
          - "top -p $(pgrep postgres)"
```

## 🎯 ముఖ్యమైన పాఠాలు

ఈ ల్యాబ్ పూర్తి చేసిన తర్వాత, మీ వద్ద ఉండాలి:

✅ **అప్లికేషన్ ఇన్సైట్స్ ఇంటిగ్రేషన్**: పూర్తి టెలిమెట్రీ మరియు మానిటరింగ్ సెటప్  
✅ **నిర్మిత లాగింగ్**: సంబంధం మరియు సందర్భంతో ప్రొడక్షన్-రెడీ లాగింగ్  
✅ **కస్టమ్ మెట్రిక్స్**: వ్యాపార మరియు సాంకేతిక మెట్రిక్స్ సేకరణ మరియు విశ్లేషణ  
✅ **తెలివైన అలర్టింగ్**: బహుళ నోటిఫికేషన్ ఛానల్స్‌తో ప్రో యాక్టివ్ అలర్టింగ్  
✅ **ఆపరేషనల్ డాష్‌బోర్డ్లు**: రియల్-టైమ్ మానిటరింగ్ మరియు వ్యాపార అవగాహన  
✅ **ట్రబుల్‌షూటింగ్ వర్క్‌ఫ్లోలు**: ఆటోమేటెడ్ డయాగ్నోస్టిక్స్ మరియు ఆపరేషనల్ రన్‌బుక్స్  

## 🚀 తదుపరి ఏమిటి

**[ల్యాబ్ 12: ఉత్తమ పద్ధతులు మరియు ఆప్టిమైజేషన్](../12-Best-Practices/README.md)** తో కొనసాగండి:

- పనితీరు ఆప్టిమైజేషన్ సాంకేతికతలను వర్తింపజేయండి  
- సమగ్ర భద్రత హార్డెనింగ్ అమలు చేయండి  
- ప్రొడక్షన్ డిప్లాయ్‌మెంట్ ఉత్తమ పద్ధతులు నేర్చుకోండి  
- ఖర్చు ఆప్టిమైజేషన్ వ్యూహాలను స్థాపించండి  

## 📚 అదనపు వనరులు

### Azure Monitor
- [Application Insights Documentation](https://docs.microsoft.com/azure/azure-monitor/app/app-insights-overview) - పూర్తి మానిటరింగ్ గైడ్  
- [KQL Query Reference](https://docs.microsoft.com/azure/data-explorer/kql-quick-reference) - అప్లికేషన్ ఇన్సైట్స్ కోసం క్వెరీ భాష  
- [Azure Monitor Workbooks](https://docs.microsoft.com/azure/azure-monitor/visualize/workbooks-overview) - కస్టమ్ డాష్‌బోర్డ్ సృష్టి  

### OpenTelemetry
- [OpenTelemetry Python](https://opentelemetry.io/docs/instrumentation/python/) - ఇన్‌స్ట్రుమెంటేషన్ గైడ్  
- [Distributed Tracing](https://opentelemetry.io/docs/concepts/observability-primer/#distributed-traces) - ట్రేసింగ్ కాన్సెప్ట్‌లు  
- [Metrics Collection](https://opentelemetry.io/docs/concepts/observability-primer/#reliability--metrics) - మెట్రిక్స్ ఉత్తమ పద్ధతులు  

### ఆపరేషనల్ ఎక్సలెన్స్
- [SRE Handbook](https://sre.google/sre-book/table-of-contents/) - సైట్ రీలయబిలిటీ ఇంజనీరింగ్ సూత్రాలు  
- [Monitoring Best Practices](https://cloud.google.com/architecture/framework/reliability/monitoring-alerting-logging) - పరిశ్రమ ఉత్తమ పద్ధతులు  
- [Incident Response](https://response.pagerduty.com/) - సంఘటన నిర్వహణ గైడ్  

---

**మునుపటి**: [ల్యాబ్ 10: డిప్లాయ్‌మెంట్ వ్యూహాలు](../10-Deployment/README.md)  
**తదుపరి**: [ల్యాబ్ 12: ఉత్తమ పద్ధతులు మరియు ఆప్టిమైజేషన్](../12-Best-Practices/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలోనే అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారుల బాధ్యత మేము తీసుకోము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->