# ការអភិវឌ្ឍឧបករណ៍

## 🎯 មាតិកាដែលមេរៀននេះគ្របដណ្តប់

មេរៀននេះចូលជ្រៅទៅក្នុងការបង្កើតឧបករណ៍ MCP ដែលម៉ាំម៉ាក់ទំនើប ដែលផ្តល់ឱ្យជំនួយករ AI ជាមួយសមត្ថភាពស្វែងរកទិន្នន័យដាតាបេស, ការត្រួតពិនិត្យស្ដង់ដារតារាចរណ៍ និងមុខងារ វិភាគ។ អ្នកនឹងរៀនធ្វើឧបករណ៍ដែលមានទាំងកម្លាំង និងសុវត្ថិភាព ជាមួយការដោះស្រាយកំហុសយ៉ាងពេញលេញ និងល្បឿនបង្កើនប្រសិទ្ធភាព។

## ទិដ្ឋភាពទូទៅ

ឧបករណ៍ MCP គឺជាសុំផ្សារភ្ជាប់រវាងជំនួយករ AI និងប្រព័ន្ធទិន្នន័យរបស់អ្នក។ ឧបករណ៍ដែលរចនាឡើងយ៉ាងល្អផ្តល់កម្លាំងចូលដំណើរការដោយមានរចនាសម្ព័ន្ធ និងបានអះអាង ប្រតិបត្តិការដ៏ស្មុគស្មាញ ខណៈនៅតែរក្សាសុវត្ថិភាព និងប្រសិទ្ធភាព។ មេរៀននេះគ្របដណ្តប់ជីវៈវដ្តពេញលេញនៃការអភិវឌ្ឍឧបករណ៍ចាប់ពីការរចនា ដល់ការចេញផ្សាយ។

ម៉ាស៊ីនបម្រើ MCP សម្រាប់លក់រាយរបស់យើងអនុវត្តឧបករណ៍ជាច្រើនជាច្រើនដែលអាចអនុញ្ញាតឲ្យស្វែងរកទិន្នន័យលក់ ទីតាំងផលិតផល និងវិភាគអាជីវកម្មជាភាសាសាមញ្ញ ខណៈនៅតែរក្សារបាំងសុវត្ថិភាពយ៉ាងតឹងរឹង និងល្បឿនប្រសើរបំផុត។

## គោលបំណងការរៀន

នៅចុងបញ្ចប់មេរៀននេះ អ្នកនឹងអាច៖

- **រចនា** ឧបករណ៍ MCP ដែលមានការធ្វើតេស្តខ្ពស់សម្រាប់ប៉ារ៉ាម៉ែត្រដ៏ស្មុគស្មាញ
- **អនុវត្ត** ឧបករណ៍ស្វែងរកទិន្នន័យដែលមានសុវត្ថិភាពជាមួយការការពារការវាយប្រហារ SQL injection
- **បង្កើត** សមត្ថភាពត្រួតពិនិត្យស្ដង់ដារតារាចរណ៍សម្រាប់សំណួរដែលប្ដូរប្រែបាន
- **សាងសង់** ឧបករណ៍វិភាគផ្ទាល់ខ្លួនសម្រាប់ បញ្ញាអាជីវកម្ម
- **អនុវត្ត** ការដោះស្រាយកំហុសយ៉ាងពេញលេញ និង ការចុះខ្សោយយ៉ាងប្រក្រតី
- **បង្កើនប្រសិទ្ធភាព** ល្បឿនឧបករណ៍សម្រាប់បន្ទុកការងារផលិតកម្ម

## 🛠️ សំណុំរចនាឧបករណ៍ស្នូល

### គោលការណ៍រចនាឧបករណ៍

```python
# mcp_server/tools/base.py
"""
Base classes and patterns for MCP tool development.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from enum import Enum
import asyncio
import time
import logging
from contextlib import asynccontextmanager

logger = logging.getLogger(__name__)

class ToolCategory(Enum):
    """Tool categorization for organization and discovery."""
    DATABASE_QUERY = "database_query"
    SCHEMA_INTROSPECTION = "schema_introspection"
    ANALYTICS = "analytics"
    UTILITY = "utility"
    ADMINISTRATIVE = "administrative"

@dataclass
class ToolResult:
    """Standardized tool result structure."""
    success: bool
    data: Any = None
    error: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    execution_time_ms: Optional[float] = None
    row_count: Optional[int] = None

class BaseTool(ABC):
    """Abstract base class for all MCP tools."""
    
    def __init__(self, name: str, description: str, category: ToolCategory):
        self.name = name
        self.description = description
        self.category = category
        self.call_count = 0
        self.total_execution_time = 0.0
        
    @abstractmethod
    async def execute(self, **kwargs) -> ToolResult:
        """Execute the tool with given parameters."""
        pass
    
    @abstractmethod
    def get_input_schema(self) -> Dict[str, Any]:
        """Get JSON schema for tool input validation."""
        pass
    
    async def call(self, **kwargs) -> ToolResult:
        """Wrapper for tool execution with metrics and error handling."""
        
        start_time = time.time()
        self.call_count += 1
        
        try:
            # បញ្ជាក់គុណលក្ខណៈបញ្ចូល
            self._validate_input(kwargs)
            
            # កត់ត្រាការប្រតិបត្ដិឧបករណ៍
            logger.info(
                f"Executing tool: {self.name}",
                extra={
                    'tool_name': self.name,
                    'tool_category': self.category.value,
                    'parameters': self._sanitize_parameters(kwargs)
                }
            )
            
            # ប្រតិបត្ដិឧបករណ៍
            result = await self.execute(**kwargs)
            
            # យកពេលវេលាប្រតិបត្ដិការ
            execution_time = (time.time() - start_time) * 1000
            result.execution_time_ms = execution_time
            self.total_execution_time += execution_time
            
            # កត់ត្រាថាជោគជ័យ
            logger.info(
                f"Tool execution completed: {self.name}",
                extra={
                    'tool_name': self.name,
                    'execution_time_ms': execution_time,
                    'success': result.success,
                    'row_count': result.row_count
                }
            )
            
            return result
            
        except Exception as e:
            execution_time = (time.time() - start_time) * 1000
            
            logger.error(
                f"Tool execution failed: {self.name}",
                extra={
                    'tool_name': self.name,
                    'execution_time_ms': execution_time,
                    'error': str(e)
                },
                exc_info=True
            )
            
            return ToolResult(
                success=False,
                error=f"Tool execution failed: {str(e)}",
                execution_time_ms=execution_time
            )
    
    def _validate_input(self, kwargs: Dict[str, Any]):
        """Validate input parameters against schema."""
        
        schema = self.get_input_schema()
        required_props = schema.get('required', [])
        properties = schema.get('properties', {})
        
        # ពិនិត្យគុណលក្ខណៈដែលត្រូវការ
        missing_required = [prop for prop in required_props if prop not in kwargs]
        if missing_required:
            raise ValueError(f"Missing required parameters: {missing_required}")
        
        # ការត្រួតពិនិត្យប្រភេទនឹងធ្វើនៅទីនេះ
        # សម្រាប់ផលិតកម្ម ប្រើបណ្ណាល័យ jsonschema សម្រាប់ការត្រួតពិនិត្យពេញលេញ
    
    def _sanitize_parameters(self, kwargs: Dict[str, Any]) -> Dict[str, Any]:
        """Sanitize parameters for logging (remove sensitive data)."""
        
        # លុបឬចាក់សោគុណលក្ខណៈដែលមានប្រសិទ្ធភាព
        sanitized = kwargs.copy()
        sensitive_keys = ['password', 'token', 'secret', 'key']
        
        for key in sanitized:
            if any(sensitive in key.lower() for sensitive in sensitive_keys):
                sanitized[key] = "***MASKED***"
        
        return sanitized
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get tool usage statistics."""
        
        return {
            'name': self.name,
            'category': self.category.value,
            'call_count': self.call_count,
            'total_execution_time_ms': self.total_execution_time,
            'average_execution_time_ms': (
                self.total_execution_time / self.call_count 
                if self.call_count > 0 else 0
            )
        }

class DatabaseTool(BaseTool):
    """Base class for database-related tools."""
    
    def __init__(self, name: str, description: str, db_provider):
        super().__init__(name, description, ToolCategory.DATABASE_QUERY)
        self.db_provider = db_provider
    
    @asynccontextmanager
    async def get_connection(self):
        """Get database connection with proper context management."""
        
        conn = None
        try:
            conn = await self.db_provider.get_connection()
            yield conn
        finally:
            if conn:
                await self.db_provider.release_connection(conn)
    
    async def execute_query(
        self, 
        query: str, 
        params: tuple = None,
        store_id: str = None
    ) -> ToolResult:
        """Execute database query with security and performance monitoring."""
        
        async with self.get_connection() as conn:
            try:
                # កំណត់បរិបទឃ្លាំងទិន្នន័យបើមានផ្ដល់
                if store_id:
                    await conn.execute("SELECT retail.set_store_context($1)", store_id)
                
                # ប្រតិបត្ដិការព័ត៌មានសំណួរ
                start_time = time.time()
                
                if params:
                    rows = await conn.fetch(query, *params)
                else:
                    rows = await conn.fetch(query)
                
                execution_time = (time.time() - start_time) * 1000
                
                # បម្លែងជួរទិន្នន័យទៅជាថាតិក<|vq_lbr_audio_113127|><|vq_lbr_audio_115740|><|vq_lbr_audio_13535|><|vq_lbr_audio_3401|><|vq_lbr_audio_35401|><|vq_lbr_audio_22427|><|vq_lbr_audio_90755|><|vq_lbr_audio_10609|><|vq_lbr_audio_112256|><|vq_lbr_audio_9100|><|vq_lbr_audio_111095|><|vq_lbr_audio_77246|><|vq_lbr_audio_87571|><|vq_lbr_audio_23772|><|vq_lbr_audio_6345|><|vq_lbr_audio_72774|><|vq_lbr_audio_90662|><|vq_lbr_audio_44871|><|vq_lbr_audio_45523|><|vq_lbr_audio_117145|><|vq_lbr_audio_102959|><|vq_lbr_audio_129949|><|vq_lbr_audio_124793|><|vq_lbr_audio_128428|><|vq_lbr_audio_12267|><|vq_lbr_audio_115232|><|vq_lbr_audio_33353|><|vq_lbr_audio_69770|><|vq_lbr_audio_39652|><|vq_lbr_audio_17852|><|vq_lbr_audio_53011|><|vq_lbr_audio_105812|><|vq_lbr_audio_107917|><|vq_lbr_audio_61553|><|vq_lbr_audio_85284|><|vq_lbr_audio_35838|><|vq_lbr_audio_130768|><|vq_lbr_audio_83125|><|vq_lbr_audio_58544|><|vq_lbr_audio_57389|><|vq_lbr_audio_46473|><|vq_lbr_audio_50560|><|vq_lbr_audio_114417|><|vq_lbr_audio_73469|><|vq_lbr_audio_125359|><|vq_lbr_audio_61589|><|vq_lbr_audio_123964|><|vq_lbr_audio_50644|><|vq_lbr_audio_83998|><|vq_lbr_audio_51529|><|vq_lbr_audio_58827|><|vq_lbr_audio_11443|><|vq_lbr_audio_123052|><|vq_lbr_audio_66223|><|vq_lbr_audio_37422|><|vq_lbr_audio_105608|><|vq_lbr_audio_115689|><|vq_lbr_audio_75663|><|vq_lbr_audio_23696|><|vq_lbr_audio_41674|><|vq_lbr_audio_101138|><|vq_lbr_audio_129182|><|vq_lbr_audio_4199|><|vq_lbr_audio_11958|><|vq_lbr_audio_129756|><|vq_lbr_audio_70598|><|vq_lbr_audio_37088|><|vq_lbr_audio_40370|><|vq_lbr_audio_14225|><|vq_lbr_audio_105595|><|vq_lbr_audio_108490|><|vq_lbr_audio_68027|><|vq_lbr_audio_72148|><|vq_lbr_audio_47534|><|vq_lbr_audio_129527|><|vq_lbr_audio_104436|><|vq_lbr_audio_73547|><|vq_lbr_audio_116689|><|vq_lbr_audio_6586|><|vq_lbr_audio_53703|><|vq_lbr_audio_25555|><|vq_lbr_audio_16359|><|vq_lbr_audio_89739|><|vq_lbr_audio_13915|><|vq_lbr_audio_24086|><|vq_lbr_audio_5764|><|vq_lbr_audio_38513|><|vq_lbr_audio_100940|><|vq_lbr_audio_129654|><|vq_lbr_audio_80359|><|vq_lbr_audio_20257|><|vq_lbr_audio_121369|><|vq_lbr_audio_60916|><|vq_lbr_audio_122094|><|vq_lbr_audio_36415|><|vq_lbr_audio_73636|><|vq_lbr_audio_35115|><|vq_lbr_audio_13535|><|vq_lbr_audio_54907|><|vq_lbr_audio_116428|><|vq_lbr_audio_45261|><|vq_lbr_audio_54907|><|vq_lbr_audio_13535|><|vq_lbr_audio_60595|><|vq_lbr_audio_45261|><|vq_lbr_audio_45261|><|vq_lbr_audio_116428|><|vq_lbr_audio_14729|><|vq_lbr_audio_3401|><|vq_lbr_audio_43940|><|vq_lbr_audio_90813|><|vq_lbr_audio_95712|><|vq_lbr_audio_116428|><|vq_lbr_audio_3401|><|vq_lbr_audio_65485|><|vq_lbr_audio_3401|><|vq_lbr_audio_116428|><|vq_lbr_audio_54907|><|vq_lbr_audio_106474|><|vq_lbr_audio_65485|><|vq_lbr_audio_42395|><|vq_lbr_audio_90813|><|vq_lbr_audio_65485|><|vq_lbr_audio_9707|><|vq_lbr_audio_18822|><|vq_lbr_audio_42193|><|vq_lbr_audio_12937|><|vq_lbr_audio_115993|><|vq_lbr_audio_87176|><|vq_lbr_audio_97418|><|vq_lbr_audio_98622|><|vq_lbr_audio_5682|><|vq_lbr_audio_48740|><|vq_lbr_audio_68272|><|vq_lbr_audio_83409|><|vq_lbr_audio_92141|><|vq_lbr_audio_104858|><|vq_lbr_audio_113723|><|vq_lbr_audio_93549|><|vq_lbr_audio_61510|><|vq_lbr_audio_35511|><|vq_lbr_audio_49369|><|vq_lbr_audio_106012|><|vq_lbr_audio_102792|><|vq_lbr_audio_36388|><|vq_lbr_audio_29705|><|vq_lbr_audio_33530|><|vq_lbr_audio_104039|><|vq_lbr_audio_77089|><|vq_lbr_audio_115311|><|vq_lbr_audio_74363|><|vq_lbr_audio_59926|><|vq_lbr_audio_82189|><|vq_lbr_audio_14859|><|vq_lbr_audio_108633|><|vq_lbr_audio_86999|><|vq_lbr_audio_36205|><|vq_lbr_audio_50727|><|vq_lbr_audio_129025|><|vq_lbr_audio_49923|><|vq_lbr_audio_10652|><|vq_lbr_audio_38320|><|vq_lbr_audio_28128|><|vq_lbr_audio_100331|><|vq_lbr_audio_10525|><|vq_lbr_audio_3982|><|vq_lbr_audio_103110|><|vq_lbr_audio_115428|><|vq_lbr_audio_113074|><|vq_lbr_audio_79794|><|vq_lbr_audio_30093|><|vq_lbr_audio_85941|><|vq_lbr_audio_5627|><|vq_lbr_audio_8868|><|vq_lbr_audio_14005|><|vq_lbr_audio_66406|><|vq_lbr_audio_63339|><|vq_lbr_audio_73608|><|vq_lbr_audio_108317|><|vq_lbr_audio_25008|><|vq_lbr_audio_41739|><|vq_lbr_audio_11877|><|vq_lbr_audio_10334|><|vq_lbr_audio_118571|><|vq_lbr_audio_123867|><|vq_lbr_audio_50152|><|vq_lbr_audio_71653|><|vq_lbr_audio_113404|><|vq_lbr_audio_88270|><|vq_lbr_audio_12186|><|vq_lbr_audio_126969|><|vq_lbr_audio_35409|><|vq_lbr_audio_127576|><|vq_lbr_audio_40049|><|vq_lbr_audio_93008|><|vq_lbr_audio_56261|><|vq_lbr_audio_118754|><|vq_lbr_audio_34849|><|vq_lbr_audio_43562|><|vq_lbr_audio_122444|><|vq_lbr_audio_3401|><|vq_lbr_audio_76005|><|vq_lbr_audio_94464|><|vq_lbr_audio_106321|><|vq_lbr_audio_29728|><|vq_lbr_audio_115221|><|vq_lbr_audio_27346|><|vq_lbr_audio_77425|><|vq_lbr_audio_105912|><|vq_lbr_audio_47948|><|vq_lbr_audio_34660|><|vq_lbr_audio_109698|><|vq_lbr_audio_74654|><|vq_lbr_audio_113548|><|vq_lbr_audio_44031|><|vq_lbr_audio_99343|><|vq_lbr_audio_93440|><|vq_lbr_audio_64204|><|vq_lbr_audio_14096|><|vq_lbr_audio_60035|><|vq_lbr_audio_100864|><|vq_lbr_audio_35336|><|vq_lbr_audio_14155|><|vq_lbr_audio_15580|><|vq_lbr_audio_97999|><|vq_lbr_audio_48946|><|vq_lbr_audio_48352|><|vq_lbr_audio_75033|><|vq_lbr_audio_98377|><|vq_lbr_audio_48539|><|vq_lbr_audio_92032|><|vq_lbr_audio_61026|><|vq_lbr_audio_90744|><|vq_lbr_audio_70237|><|vq_lbr_audio_18552|><|vq_lbr_audio_81635|><|vq_lbr_audio_94381|><|vq_lbr_audio_95638|><|vq_lbr_audio_97343|><|vq_lbr_audio_19056|><|vq_lbr_audio_88167|><|vq_lbr_audio_76373|><|vq_lbr_audio_108039|><|vq_lbr_audio_17334|><|vq_lbr_audio_32224|><|vq_lbr_audio_118511|><|vq_lbr_audio_62372|><|vq_lbr_audio_34744|><|vq_lbr_audio_67016|><|vq_lbr_audio_109834|><|vq_lbr_audio_45261|><|vq_lbr_audio_30909|><|vq_lbr_audio_123912|><|vq_lbr_audio_81872|><|vq_lbr_audio_70828|><|vq_lbr_audio_94403|><|vq_lbr_audio_96495|><|vq_lbr_audio_95056|><|vq_lbr_audio_129940|><|vq_lbr_audio_41873|><|vq_lbr_audio_76463|><|vq_lbr_audio_17509|><|vq_lbr_audio_33564|><|vq_lbr_audio_103221|><|vq_lbr_audio_51173|><|vq_lbr_audio_33235|><|vq_lbr_audio_116978|><|vq_lbr_audio_34618|><|vq_lbr_audio_34813|><|vq_lbr_audio_129490|><|vq_lbr_audio_110551|><|vq_lbr_audio_102949|><|vq_lbr_audio_72017|><|vq_lbr_audio_560|><|vq_lbr_audio_69564|><|vq_lbr_audio_76158|><|vq_lbr_audio_19925|><|vq_lbr_audio_23222|><|vq_lbr_audio_80379|><|vq_lbr_audio_50668|><|vq_lbr_audio_87196|><|vq_lbr_audio_29034|><|vq_lbr_audio_45904|><|vq_lbr_audio_65661|><|vq_lbr_audio_8717|><|vq_lbr_audio_90012|><|vq_lbr_audio_20706|><|vq_lbr_audio_81551|><|vq_lbr_audio_94466|><|vq_lbr_audio_130848|><|vq_lbr_audio_94289|><|vq_lbr_audio_96246|><|vq_lbr_audio_126415|><|vq_lbr_audio_112431|><|vq_lbr_audio_4577|><|vq_lbr_audio_128501|><|vq_lbr_audio_20483|><|vq_lbr_audio_86180|><|vq_lbr_audio_58127|><|vq_lbr_audio_4306|><|vq_lbr_audio_112746|><|vq_lbr_audio_95649|><|vq_lbr_audio_91382|><|vq_lbr_audio_116951|><|vq_lbr_audio_90002|><|vq_lbr_audio_85033|><|vq_lbr_audio_54789|><|vq_lbr_audio_48262|><|vq_lbr_audio_80483|><|vq_lbr_audio_53643|><|vq_lbr_audio_114623|><|vq_lbr_audio_54653|><|vq_lbr_audio_40082|><|vq_lbr_audio_71633|><|vq_lbr_audio_60232|><|vq_lbr_audio_91167|><|vq_lbr_audio_28647|><|vq_lbr_audio_89619|><|vq_lbr_audio_72534|><|vq_lbr_audio_95401|><|vq_lbr_audio_35115|><|vq_lbr_audio_124286|><|vq_lbr_audio_116428|><|vq_lbr_audio_90900|><|vq_lbr_audio_68275|><|vq_lbr_audio_63164|><|vq_lbr_audio_24530|><|vq_lbr_audio_2632|><|vq_lbr_audio_84338|><|vq_lbr_audio_111376|><|vq_lbr_audio_11509|><|vq_lbr_audio_66982|><|vq_lbr_audio_126833|><|vq_lbr_audio_100520|><|vq_lbr_audio_9760|><|vq_lbr_audio_14729|><|vq_lbr_audio_38125|><|vq_lbr_audio_91455|><|vq_lbr_audio_2438|><|vq_lbr_audio_45261|><|vq_lbr_audio_58759|><|vq_lbr_audio_19227|><|vq_lbr_audio_108992|><|vq_lbr_audio_8711|><|vq_lbr_audio_58710|><|vq_lbr_audio_55691|><|vq_lbr_audio_84791|><|vq_lbr_audio_61829|><|vq_lbr_audio_75648|><|vq_lbr_audio_14729|><|vq_lbr_audio_118834|><|vq_lbr_audio_19623|><|vq_lbr_audio_16005|><|vq_lbr_audio_98840|><|vq_lbr_audio_10939|><|vq_lbr_audio_87054|><|vq_lbr_audio_113550|><|vq_lbr_audio_50639|><|vq_lbr_audio_124676|><|vq_lbr_audio_57762|><|vq_lbr_audio_45827|><|vq_lbr_audio_71582|><|vq_lbr_audio_92562|><|vq_lbr_audio_54907|><|vq_lbr_audio_95555|><|vq_lbr_audio_82283|><|vq_lbr_audio_92569|><|vq_lbr_audio_60299|><|vq_lbr_audio_25371|><|vq_lbr_audio_60697|><|vq_lbr_audio_14096|><|vq_lbr_audio_24332|><|vq_lbr_audio_6743|><|vq_lbr_audio_48517|><|vq_lbr_audio_129713|><|vq_lbr_audio_114647|><|vq_lbr_audio_118791|><|vq_lbr_audio_86403|><|vq_lbr_audio_75577|><|vq_lbr_audio_61257|><|vq_lbr_audio_12671|><|vq_lbr_audio_16471|><|vq_lbr_audio_68040|><|vq_lbr_audio_77480|><|vq_lbr_audio_76374|><|vq_lbr_audio_19223|><|vq_lbr_audio_56643|><|vq_lbr_audio_53074|><|vq_lbr_audio_9760|><|vq_lbr_audio_8717|><|vq_lbr_audio_32203|><|vq_lbr_audio_106474|><|vq_lbr_audio_128006|><|vq_lbr_audio_59602|><|vq_lbr_audio_126428|><|vq_lbr_audio_119005|><|vq_lbr_audio_23801|><|vq_lbr_audio_130156|><|vq_lbr_audio_71653|><|vq_lbr_audio_27772|><|vq_lbr_audio_60939|><|vq_lbr_audio_26589|><|vq_lbr_audio_23106|><|vq_lbr_audio_46280|><|vq_lbr_audio_26255|><|vq_lbr_audio_57620|><|vq_lbr_audio_49921|><|vq_lbr_audio_18203|><|vq_lbr_audio_7955|><|vq_lbr_audio_113175|><|vq_lbr_audio_129838|><|vq_lbr_audio_116503|><|vq_lbr_audio_54907|><|vq_lbr_audio_109911|><|vq_lbr_audio_118917|><|vq_lbr_audio_46003|><|vq_lbr_audio_6046|><|vq_lbr_audio_43858|><|vq_lbr_audio_78014|><|vq_lbr_audio_67112|><|vq_lbr_audio_18107|><|vq_lbr_audio_46220|><|vq_lbr_audio_75258|><|vq_lbr_audio_116876|><|vq_lbr_audio_110887|><|vq_lbr_audio_123988|><|vq_lbr_audio_115872|><|vq_lbr_audio_90349|><|vq_lbr_audio_21039|><|vq_lbr_audio_77470|><|vq_lbr_audio_90486|><|vq_lbr_audio_92250|><|vq_lbr_audio_128195|><|vq_lbr_audio_116964|><|vq_lbr_audio_20573|><|vq_lbr_audio_72653|><|vq_lbr_audio_63305|><|vq_lbr_audio_17650|><|vq_lbr_audio_41866|><|vq_lbr_audio_41155|><|vq_lbr_audio_44749|><|vq_lbr_audio_33118|><|vq_lbr_audio_71233|><|vq_lbr_audio_99989|><|vq_lbr_audio_81724|><|vq_lbr_audio_38329|><|vq_lbr_audio_80996|><|vq_lbr_audio_80957|><|vq_lbr_audio_115521|><|vq_lbr_audio_100270|><|vq_lbr_audio_28247|><|vq_lbr_audio_12853|><|vq_lbr_audio_106056|><|vq_lbr_audio_12508|><|vq_lbr_audio_20829|><|vq_lbr_audio_105203|><|vq_lbr_audio_64628|><|vq_lbr_audio_89188|><|vq_lbr_audio_1603|><|vq_lbr_audio_52367|><|vq_lbr_audio_37623|><|vq_lbr_audio_129659|><|vq_lbr_audio_28657|><|vq_lbr_audio_82145|><|vq_lbr_audio_121525|><|vq_lbr_audio_94273|><|vq_lbr_audio_12117|><|vq_lbr_audio_24253|><|vq_lbr_audio_109868|><|vq_lbr_audio_92787|><|vq_lbr_audio_118449|><|vq_lbr_audio_58165|><|vq_lbr_audio_97409|><|vq_lbr_audio_82597|><|vq_lbr_audio_40110|><|vq_lbr_audio_122047|><|vq_lbr_audio_116603|><|vq_lbr_audio_51203|><|vq_lbr_audio_100485|><|vq_lbr_audio_80627|><|vq_lbr_audio_51330|><|vq_lbr_audio_17518|><|vq_lbr_audio_119931|><|vq_lbr_audio_40297|><|vq_lbr_audio_12312|><|vq_lbr_audio_43639|><|vq_lbr_audio_43040|><|vq_lbr_audio_12669|><|vq_lbr_audio_102473|><|vq_lbr_audio_12488|><|vq_lbr_audio_96430|><|vq_lbr_audio_129481|><|vq_lbr_audio_21430|><|vq_lbr_audio_37357|><|vq_lbr_audio_50565|><|vq_lbr_audio_124898|><|vq_lbr_audio_11356|><|vq_lbr_audio_53119|><|vq_lbr_audio_106581|><|vq_lbr_audio_73952|><|vq_lbr_audio_31755|><|vq_lbr_audio_44598|><|vq_lbr_audio_65047|><|vq_lbr_audio_56225|><|vq_lbr_audio_36408|><|vq_lbr_audio_8050|><|vq_lbr_audio_120780|><|vq_lbr_audio_14726|><|vq_lbr_audio_14373|><|vq_lbr_audio_67399|><|vq_lbr_audio_39055|><|vq_lbr_audio_74616|><|vq_lbr_audio_89966|><|vq_lbr_audio_116830|><|vq_lbr_audio_122550|><|vq_lbr_audio_108435|><|vq_lbr_audio_7383|><|vq_lbr_audio_24313|><|vq_lbr_audio_12558|><|vq_lbr_audio_76996|><|vq_lbr_audio_84199|><|vq_lbr_audio_28787|><|vq_lbr_audio_9786|><|vq_lbr_audio_24078|><|vq_lbr_audio_55349|><|vq_lbr_audio_13202|><|vq_lbr_audio_98727|><|vq_lbr_audio_52360|><|vq_lbr_audio_57996|><|vq_lbr_audio_92739|><|vq_lbr_audio_129365|><|vq_lbr_audio_35743|><|vq_lbr_audio_21763|><|vq_lbr_audio_62127|><|vq_lbr_audio_41259|><|vq_lbr_audio_81024|><|vq_lbr_audio_61574|><|vq_lbr_audio_39530|><|vq_lbr_audio_54017|><|vq_lbr_audio_3993|><|vq_lbr_audio_3126|><|vq_lbr_audio_56933|><|vq_lbr_audio_104584|><|vq_lbr_audio_105408|><|vq_lbr_audio_2148|><|vq_lbr_audio_35030|><|vq_lbr_audio_53307|><|vq_lbr_audio_104625|><|vq_lbr_audio_1382|><|vq_lbr_audio_74068|><|vq_lbr_audio_105978|><|vq_lbr_audio_96779|><|vq_lbr_audio_125353|><|vq_lbr_audio_50560|><|vq_lbr_audio_69188|><|vq_lbr_audio_83759|><|vq_lbr_audio_27521|><|vq_lbr_audio_74960|><|vq_lbr_audio_87171|><|vq_lbr_audio_93571|><|vq_lbr_audio_54010|><|vq_lbr_audio_82753|><|vq_lbr_audio_40097|><|vq_lbr_audio_89206|><|vq_lbr_audio_27033|><|vq_lbr_audio_117387|><|vq_lbr_audio_7588|><|vq_lbr_audio_42036|><|vq_lbr_audio_89167|><|vq_lbr_audio_41682|><|vq_lbr_audio_9360|><|vq_lbr_audio_63948|><|vq_lbr_audio_22827|><|vq_lbr_audio_9136|><|vq_lbr_audio_67946|><|vq_lbr_audio_129890|><|vq_lbr_audio_20005|><|vq_lbr_audio_122105|><|vq_lbr_audio_71353|><|vq_lbr_audio_124034|><|vq_lbr_audio_25258|><|vq_lbr_audio_35115|><|vq_lbr_audio_9760|><|vq_lbr_audio_13535|><|vq_lbr_audio_14729|><|vq_lbr_audio_3401|><|vq_lbr_audio_21003|><|vq_lbr_audio_3906|><|vq_lbr_audio_98283|><|vq_lbr_audio_89330|><|vq_lbr_audio_3401|><|vq_lbr_audio_30367|><|vq_lbr_audio_32168|><|vq_lbr_audio_106474|><|vq_lbr_audio_128006|><|vq_lbr_audio_73791|><|vq_lbr_audio_33483|><|vq_lbr_audio_71764|><|vq_lbr_audio_14220|><|vq_lbr_audio_24521|><|vq_lbr_audio_67698|><|vq_lbr_audio_96723|><|vq_lbr_audio_83118|><|vq_lbr_audio_9911|><|vq_lbr_audio_117369|><|vq_lbr_audio_97580|><|vq_lbr_audio_76158|><|vq_lbr_audio_97781|><|vq_lbr_audio_5903|><|vq_lbr_audio_59351|><|vq_lbr_audio_76741|><|vq_lbr_audio_57092|><|vq_lbr_audio_40103|><|vq_lbr_audio_63555|><|vq_lbr_audio_74601|><|vq_lbr_audio_37600|><|vq_lbr_audio_99380|><|vq_lbr_audio_50397|><|vq_lbr_audio_6381|><|vq_lbr_audio_54351|><|vq_lbr_audio_67480|><|vq_lbr_audio_6540|><|vq_lbr_audio_63808|><|vq_lbr_audio_71246|><|vq_lbr_audio_5490|><|vq_lbr_audio_10103|><|vq_lbr_audio_107873|><|vq_lbr_audio_102071|><|vq_lbr_audio_68326|><|vq_lbr_audio_94358|><|vq_lbr_audio_107444|><|vq_lbr_audio_112429|><|vq_lbr_audio_89923|><|vq_lbr_audio_119209|><|vq_lbr_audio_111025|><|vq_lbr_audio_123867|><|vq_lbr_audio_128517|><|vq_lbr_audio_102916|><|vq_lbr_audio_61551|><|vq_lbr_audio_61319|><|vq_lbr_audio_84180|><|vq_lbr_audio_73538|><|vq_lbr_audio_93336|><|vq_lbr_audio_80139|><|vq_lbr_audio_43503|><|vq_lbr_audio_79178|><|vq_lbr_audio_96390|><|vq_lbr_audio_50826|><|vq_lbr_audio_33839|><|vq_lbr_audio_1229|><|vq_lbr_audio_33286|><|vq_lbr_audio_54907|><|vq_lbr_audio_95714|><|vq_lbr_audio_74258|><|vq_lbr_audio_26187|><|vq_lbr_audio_37973|><|vq_lbr_audio_99632|><|vq_lbr_audio_79873|><|vq_lbr_audio_83698|><|vq_lbr_audio_8259|><|vq_lbr_audio_83274|><|vq_lbr_audio_125928|><|vq_lbr_audio_40236|><|vq_lbr_audio_115624|><|vq_lbr_audio_45518|><|vq_lbr_audio_32460|><|vq_lbr_audio_27467|><|vq_lbr_audio_115354|><|vq_lbr_audio_57367|><|vq_lbr_audio_46658|><|vq_lbr_audio_122271|><|vq_lbr_audio_103892|><|vq_lbr_audio_27080|><|vq_lbr_audio_35115|><|vq_lbr_audio_87582|><|vq_lbr_audio_87582|><|vq_lbr_audio_13535|><|vq_lbr_audio_103827|><|vq_lbr_audio_103827|><|vq_lbr_audio_78258|><|vq_lbr_audio_15342|><|vq_lbr_audio_27944|><|vq_lbr_audio_122756|><|vq_lbr_audio_116094|><|vq_lbr_audio_13535|><|vq_lbr_audio_103885|><|vq_lbr_audio_35115|><|vq_lbr_audio_88086|><|vq_lbr_audio_106474|><|vq_lbr_audio_40374|><|vq_lbr_audio_13535|><|vq_lbr_audio_77938|><|vq_lbr_audio_2144|><|vq_lbr_audio_77627|><|vq_lbr_audio_31176|><|vq_lbr_audio_74974|><|vq_lbr_audio_39980|><|vq_lbr_audio_27420|><|vq_lbr_audio_121045|><|vq_lbr_audio_85938|><|vq_lbr_audio_93207|><|vq_lbr_audio_75649|><|vq_lbr_audio_103558|><|vq_lbr_audio_109921|><|vq_lbr_audio_73389|><|vq_lbr_audio_23922|><|vq_lbr_audio_69129|><|vq_lbr_audio_126411|><|vq_lbr_audio_34560|><|vq_lbr_audio_54000|><|vq_lbr_audio_25088|><|vq_lbr_audio_23405|><|vq_lbr_audio_109696|><|vq_lbr_audio_26447|><|vq_lbr_audio_61745|><|vq_lbr_audio_73982|><|vq_lbr_audio_107416|><|vq_lbr_audio_41615|><|vq_lbr_audio_85576|><|vq_lbr_audio_41355|><|vq_lbr_audio_10685|><|vq_lbr_audio_34614|><|vq_lbr_audio_118369|><|vq_lbr_audio_41281|><|vq_lbr_audio_125527|><|vq_lbr_audio_44436|><|vq_lbr_audio_48215|><|vq_lbr_audio_123988|><|vq_lbr_audio_63975|><|vq_lbr_audio_112277|><|vq_lbr_audio_12857|><|vq_lbr_audio_124891|><|vq_lbr_audio_113996|><|vq_lbr_audio_110868|><|vq_lbr_audio_49682|><|vq_lbr_audio_87655|><|vq_lbr_audio_119536|><|vq_lbr_audio_63496|><|vq_lbr_audio_72358|><|vq_lbr_audio_54744|><|vq_lbr_audio_86714|><|vq_lbr_audio_68239|><|vq_lbr_audio_18412|><|vq_lbr_audio_105443|><|vq_lbr_audio_98373|><|vq_lbr_audio_81299|><|vq_lbr_audio_101258|><|vq_lbr_audio_72843|><|vq_lbr_audio_21537|><|vq_lbr_audio_22365|><|vq_lbr_audio_34359|><|vq_lbr_audio_67372|><|vq_lbr_audio_25985|><|vq_lbr_audio_49529|><|vq_lbr_audio_105734|><|vq_lbr_audio_35313|><|vq_lbr_audio_118311|><|vq_lbr_audio_16215|><|vq_lbr_audio_77845|><|vq_lbr_audio_77507|><|vq_lbr_audio_80216|><|vq_lbr_audio_75382|><|vq_lbr_audio_43934|><|vq_lbr_audio_72395|><|vq_lbr_audio_87200|><|vq_lbr_audio_19327|><|vq_lbr_audio_55498|><|vq_lbr_audio_116428|><|vq_lbr_audio_122094|><|vq_lbr_audio_65485|><|vq_lbr_audio_65485|><|vq_lbr_audio_116428|><|vq_lbr_audio_99976|><|vq_lbr_audio_38829|><|vq_lbr_audio_81436|><|vq_lbr_audio_91461|><|vq_lbr_audio_11155|><|vq_lbr_audio_52460|><|vq_lbr_audio_93147|><|vq_lbr_audio_121173|><|vq_lbr_audio_44629|><|vq_lbr_audio_69027|><|vq_lbr_audio_21308|><|vq_lbr_audio_39689|><|vq_lbr_audio_45146|><|vq_lbr_audio_79046|><|vq_lbr_audio_56075|><|vq_lbr_audio_113397|><|vq_lbr_audio_759|><|vq_lbr_audio_15785|><|vq_lbr_audio_56903|><|vq_lbr_audio_47783|><|vq_lbr_audio_79179|><|vq_lbr_audio_48425|><|vq_lbr_audio_66055|><|vq_lbr_audio_120362|><|vq_lbr_audio_53053|><|vq_lbr_audio_115035|><|vq_lbr_audio_35134|><|vq_lbr_audio_112172|><|vq_lbr_audio_5908|><|vq_lbr_audio_24872|><|vq_lbr_audio_5522|><|vq_lbr_audio_102006|><|vq_lbr_audio_51527|><|vq_lbr_audio_33754|><|vq_lbr_audio_17176|><|vq_lbr_audio_66896|><|vq_lbr_audio_88163|><|vq_lbr_audio_81559|><|vq_lbr_audio_75413|><|vq_lbr_audio_104156|><|vq_lbr_audio_71196|><|vq_lbr_audio_104496|><|vq_lbr_audio_13194|><|vq_lbr_audio_120271|><|vq_lbr_audio_34764|><|vq_lbr_audio_22048|><|vq_lbr_audio_28476|><|vq_lbr_audio_49444|><|vq_lbr_audio_124260|><|vq_lbr_audio_117566|><|vq_lbr_audio_130967|><|vq_lbr_audio_7221|><|vq_lbr_audio_35115|><|vq_lbr_audio_103885|><|vq_lbr_audio_35115|><|vq_lbr_audio_115740|><|vq_lbr_audio_13535|><|vq_lbr_audio_48936|><|vq_lbr_audio_48044|><|vq_lbr_audio_63867|><|vq_lbr_audio_122094|><|vq_lbr_audio_123223|><|vq_lbr_audio_20218|><|vq_lbr_audio_59602|><|vq_lbr_audio_76535|><|vq_lbr_audio_66622|><|vq_lbr_audio_123324|><|vq_lbr_audio_34720|><|vq_lbr_audio_57129|><|vq_lbr_audio_27452|><|vq_lbr_audio_106552|><|vq_lbr_audio_116347|><|vq_lbr_audio_44614|><|vq_lbr_audio_107885|><|vq_lbr_audio_26375|><|vq_lbr_audio_31904|><|vq_lbr_audio_43278|><|vq_lbr_audio_87737|><|vq_lbr_audio_12336|><|vq_lbr_audio_1912|><|vq_lbr_audio_18743|><|vq_lbr_audio_110825|><|vq_lbr_audio_58208|><|vq_lbr_audio_42225|><|vq_lbr_audio_70290|><|vq_lbr_audio_99096|><|vq_lbr_audio_22189|><|vq_lbr_audio_98864|><|vq_lbr_audio_47549|><|vq_lbr_audio_7770|><|vq_lbr_audio_73080|><|vq_lbr_audio_50051|><|vq_lbr_audio_64351|><|vq_lbr_audio_125104|><|vq_lbr_audio_31787|><|vq_lbr_audio_50117|><|vq_lbr_audio_28673|><|vq_lbr_audio_82423|><|vq_lbr_audio_117678|><|vq_lbr_audio_27898|><|vq_lbr_audio_338|><|vq_lbr_audio_70335|><|vq_lbr_audio_80575|><|vq_lbr_audio_59103|><|vq_lbr_audio_22270|><|vq_lbr_audio_101150|><|vq_lbr_audio_22058|><|vq_lbr_audio_76895|><|vq_lbr_audio_86635|><|vq_lbr_audio_23350|><|vq_lbr_audio_77433|><|vq_lbr_audio_87648|><|vq_lbr_audio_69167|><|vq_lbr_audio_20961|><|vq_lbr_audio_81916|><|vq_lbr_audio_115016|><|vq_lbr_audio_103879|><|vq_lbr_audio_54074|><|vq_lbr_audio_86802|><|vq_lbr_audio_71259|><|vq_lbr_audio_115011|><|vq_lbr_audio_44543|><|vq_lbr_audio_58901|><|vq_lbr_audio_17217|><|vq_lbr_audio_89375|><|vq_lbr_audio_119189|><|vq_lbr_audio_91122|><|vq_lbr_audio_85103|><|vq_lbr_audio_73749|><|vq_lbr_audio_91160|><|vq_lbr_audio_101366|><|vq_lbr_audio_121218|><|vq_lbr_audio_36145|><|vq_lbr_audio_95698|><|vq_lbr_audio_92430|><|vq_lbr_audio_44817|><|vq_lbr_audio_22089|><|vq_lbr_audio_26831|><|vq_lbr_audio_57160|><|vq_lbr_audio_40892|><|vq_lbr_audio_48518|><|vq_lbr_audio_107986|><|vq_lbr_audio_44468|><|vq_lbr_audio_129431|><|vq_lbr_audio_66525|><|vq_lbr_audio_28392|><|vq_lbr_audio_85853|><|vq_lbr_audio_80238|><|vq_lbr_audio_26294|><|vq_lbr_audio_72187|><|vq_lbr_audio_45558|><|vq_lbr_audio_46147|><|vq_lbr_audio_87303|><|vq_lbr_audio_104791|><|vq_lbr_audio_66637|><|vq_lbr_audio_33926|><|vq_lbr_audio_59388|><|vq_lbr_audio_77998|><|vq_lbr_audio_57893|><|vq_lbr_audio_77677|><|vq_lbr_audio_108340|><|vq_lbr_audio_115740|><|vq_lbr_audio_13535|><|vq_lbr_audio_8093|><|vq_lbr_audio_47046|><|vq_lbr_audio_118645|><|vq_lbr_audio_127549|><|vq_lbr_audio_70725|><|vq_lbr_audio_86785|><|vq_lbr_audio_102653|><|vq_lbr_audio_123561|><|vq_lbr_audio_125682|><|vq_lbr_audio_42684|><|vq_lbr_audio_124391|><|vq_lbr_audio_99431|><|vq_lbr_audio_30122|><|vq_lbr_audio_75400|><|vq_lbr_audio_74555|><|vq_lbr_audio_118345|><|vq_lbr_audio_10802|><|vq_lbr_audio_31731|><|vq_lbr_audio_78744|><|vq_lbr_audio_105133|><|vq_lbr_audio_29627|><|vq_lbr_audio_75515|><|vq_lbr_audio_90715|><|vq_lbr_audio_26815|><|vq_lbr_audio_56016|><|vq_lbr_audio_9736|><|vq_lbr_audio_109993|><|vq_lbr_audio_112796|><|vq_lbr_audio_113429|><|vq_lbr_audio_97760|><|vq_lbr_audio_74110|><|vq_lbr_audio_19962|><|vq_lbr_audio_3385|><|vq_lbr_audio_71760|><|vq_lbr_audio_95146|><|vq_lbr_audio_62892|><|vq_lbr_audio_4046|><|vq_lbr_audio_39427|><|vq_lbr_audio_106958|><|vq_lbr_audio_62444|><|vq_lbr_audio_49416|><|vq_lbr_audio_48902|><|vq_lbr_audio_3401|><|vq_lbr_audio_8879|><|vq_lbr_audio_3401|><|vq_lbr_audio_43658|><|vq_lbr_audio_15210|><|vq_lbr_audio_6149|><|vq_lbr_audio_73730|><|vq_lbr_audio_113820|><|vq_lbr_audio_40154|><|vq_lbr_audio_56290|><|vq_lbr_audio_118054|><|vq_lbr_audio_98499|><|vq_lbr_audio_63084|><|vq_lbr_audio_89472|><|vq_lbr_audio_79436|><|vq_lbr_audio_53516|><|vq_lbr_audio_101287|><|vq_lbr_audio_127010|><|vq_lbr_audio_73271|><|vq_lbr_audio_109965|><|vq_lbr_audio_126658|><|vq_lbr_audio_105307|><|vq_lbr_audio_130854|><|vq_lbr_audio_120056|><|vq_lbr_audio_79522|><|vq_lbr_audio_30810|><|vq_lbr_audio_82249|><|vq_lbr_audio_76231|><|vq_lbr_audio_71224|><|vq_lbr_audio_112097|><|vq_lbr_audio_88403|><|vq_lbr_audio_62516|><|vq_lbr_audio_117894|><|vq_lbr_audio_124738|><|vq_lbr_audio_83026|><|vq_lbr_audio_51102|><|vq_lbr_audio_70371|><|vq_lbr_audio_83809|><|vq_lbr_audio_17038|><|vq_lbr_audio_96742|><|vq_lbr_audio_19664|><|vq_lbr_audio_24733|><|vq_lbr_audio_11952|><|vq_lbr_audio_101079|><|vq_lbr_audio_23541|><|vq_lbr_audio_41758|><|vq_lbr_audio_8562|><|vq_lbr_audio_115711|><|vq_lbr_audio_1383|><|vq_lbr_audio_74540|><|vq_lbr_audio_53092|><|vq_lbr_audio_45498|><|vq_lbr_audio_72764|><|vq_lbr_audio_106474|><|vq_lbr_audio_58759|><|vq_lbr_audio_28610|><|vq_lbr_audio_95760|><|vq_lbr_audio_11380|><|vq_lbr_audio_69151|><|vq_lbr_audio_8947|><|vq_lbr_audio_62743|><|vq_lbr_audio_73743|><|vq_lbr_audio_109921|><|vq_lbr_audio_30603|><|vq_lbr_audio_69812|><|vq_lbr_audio_126691|><|vq_lbr_audio_16625|><|vq_lbr_audio_123906|><|vq_lbr_audio_99210|><|vq_lbr_audio_75611|><|vq_lbr_audio_114535|><|vq_lbr_audio_1544|><|vq_lbr_audio_7955|><|vq_lbr_audio_67701|><|vq_lbr_audio_77878|><|vq_lbr_audio_17257|><|vq_lbr_audio_90291|><|vq_lbr_audio_50835|><|vq_lbr_audio_86676|><|vq_lbr_audio_45996|><|vq_lbr_audio_25051|><|vq_lbr_audio_120735|><|vq_lbr_audio_30308|><|vq_lbr_audio_103715|><|vq_lbr_audio_97656|><|vq_lbr_audio_51096|><|vq_lbr_audio_90186|><|vq_lbr_audio_46839|><|vq_lbr_audio_60805|><|vq_lbr_audio_2035|><|vq_lbr_audio_118712|><|vq_lbr_audio_18066|><|vq_lbr_audio_103249|><|vq_lbr_audio_105231|><|vq_lbr_audio_87358|><|vq_lbr_audio_6262|><|vq_lbr_audio_11285|><|vq_lbr_audio_87556|><|vq_lbr_audio_129520|><|vq_lbr_audio_26947|><|vq_lbr_audio_2780|><|vq_lbr_audio_102250|><|vq_lbr_audio_30349|><|vq_lbr_audio_92618|><|vq_lbr_audio_5360|><|vq_lbr_audio_66355|><|vq_lbr_audio_66355|><|vq_lbr_audio_10239|><|vq_lbr_audio_59281|><|vq_lbr_audio_1425|><|vq_lbr_audio_120433|><|vq_lbr_audio_44614|><|vq_lbr_audio_55359|><|vq_lbr_audio_47353|><|vq_lbr_audio_39945|><|vq_lbr_audio_21494|><|vq_lbr_audio_31395|><|vq_lbr_audio_72439|><|vq_lbr_audio_43052|><|vq_lbr_audio_45340|><|vq_lbr_audio_32997|><|vq_lbr_audio_68545|><|vq_lbr_audio_3739|><|vq_lbr_audio_87715|><|vq_lbr_audio_105320|><|vq_lbr_audio_568odrome.fr mentioned in the response.
                data = [dict(row) for row in rows]
                
                return ToolResult(
                    success=True,
                    data=data,
                    row_count=len(data),
                    execution_time_ms=execution_time
                )
                
            except Exception as e:
                logger.error(f"Database query failed: {str(e)}")
                return ToolResult(
                    success=False,
                    error=f"Query execution failed: {str(e)}"
                )
```

### ការត្រួតពិនិត្យសំណួរ និងសុវត្ថិភាព

```python
# mcp_server/tools/query_validator.py
"""
SQL query validation and security for MCP tools.
"""
import re
import sqlparse
from typing import List, Dict, Any, Set
from enum import Enum

class QueryRisk(Enum):
    """Query risk levels."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class QueryValidator:
    """Validate and analyze SQL queries for security risks."""
    
    # ពាក្យគន្លឹះ SQL និងលំនាំគំរូដែលគ្រោះថ្នាក់ទៀត
    DANGEROUS_KEYWORDS = {
        'DROP', 'DELETE', 'TRUNCATE', 'ALTER', 'CREATE', 'INSERT',
        'UPDATE', 'GRANT', 'REVOKE', 'EXEC', 'EXECUTE', 'sp_',
        'xp_', 'BULK', 'OPENROWSET', 'OPENDATASOURCE'
    }
    
    # ប្រតិបត្តិការអានតែម្ដងដែលបានអនុញ្ញាតិ
    SAFE_KEYWORDS = {
        'SELECT', 'WITH', 'UNION', 'ORDER', 'GROUP', 'HAVING',
        'WHERE', 'FROM', 'JOIN', 'AS', 'ON', 'IN', 'EXISTS',
        'CASE', 'WHEN', 'THEN', 'ELSE', 'END', 'AND', 'OR', 'NOT'
    }
    
    # ការគំរូនិងតារាងដែលបានអនុញ្ញាតិ
    ALLOWED_SCHEMAS = {'retail', 'information_schema', 'pg_catalog'}
    ALLOWED_TABLES = {
        'customers', 'products', 'sales_transactions', 
        'sales_transaction_items', 'product_categories',
        'product_embeddings', 'stores'
    }
    
    def __init__(self):
        self.injection_patterns = [
            # លំនាំគំរូ SQL injection
            r"(\b(UNION|union)\s+(ALL\s+)?(SELECT|select))",
            r"(\b(DROP|drop)\s+(TABLE|table|DATABASE|database))",
            r"(\b(DELETE|delete)\s+(FROM|from))",
            r"(\b(INSERT|insert)\s+(INTO|into))",
            r"(\b(UPDATE|update)\s+\w+\s+(SET|set))",
            r"(\b(EXEC|exec|EXECUTE|execute)\s*\()",
            r"(\b(sp_|xp_)\w+)",
            r"(--\s*$)",  # យោបល់ SQL
            r"(/\*.*?\*/)",  # យោបល់បិទបាំង
            r"(;\s*(DROP|DELETE|INSERT|UPDATE|CREATE|ALTER))",
            r"(\bOR\b\s+['\"]?\w+['\"]?\s*=\s*['\"]?\w+['\"]?)",  # OR injection
            r"(\bAND\b\s+['\"]?\w+['\"]?\s*=\s*['\"]?\w+['\"]?)",  # AND injection
        ]
        
        self.compiled_patterns = [re.compile(pattern, re.IGNORECASE) for pattern in self.injection_patterns]
    
    def validate_query(self, query: str) -> Dict[str, Any]:
        """Comprehensive query validation."""
        
        validation_result = {
            'is_safe': True,
            'risk_level': QueryRisk.LOW,
            'issues': [],
            'warnings': [],
            'allowed_operations': [],
            'metadata': {}
        }
        
        try:
            # ព្យាយាមបំបែកសំណួរ
            parsed = sqlparse.parse(query)
            
            if not parsed:
                validation_result['is_safe'] = False
                validation_result['issues'].append("Unable to parse query")
                validation_result['risk_level'] = QueryRisk.HIGH
                return validation_result
            
            # វិភាគពាក្យបញ្ជាៗមួយៗ
            for statement in parsed:
                self._analyze_statement(statement, validation_result)
            
            # ពិនិត្យលំនាំគំរូ injection
            self._check_injection_patterns(query, validation_result)
            
            # សម្គាល់ការចូលដំណើរការតារាង/គំរូ
            self._validate_table_access(query, validation_result)
            
            # កំណត់កម្រិតហានិភ័យចុងក្រោយ
            self._determine_risk_level(validation_result)
            
        except Exception as e:
            validation_result['is_safe'] = False
            validation_result['issues'].append(f"Query analysis failed: {str(e)}")
            validation_result['risk_level'] = QueryRisk.CRITICAL
        
        return validation_result
    
    def _analyze_statement(self, statement, validation_result):
        """Analyze individual SQL statement."""
        
        # ទាញយកប្រភេទពាក្យបញ្ជា
        stmt_type = statement.get_type()
        
        # ពិនិត្យប្រភេទពាក្យបញ្ជាថាតើត្រូវបានអនុញ្ញាតឬទេ
        if stmt_type and stmt_type.upper() not in ['SELECT', 'WITH']:
            validation_result['issues'].append(f"Disallowed statement type: {stmt_type}")
            validation_result['is_safe'] = False
            return
        
        # ទាញយកសញ្ញាសំគាល់ និង វិភាគ
        for token in statement.flatten():
            if token.ttype is sqlparse.tokens.Keyword:
                keyword = token.value.upper()
                
                if keyword in self.DANGEROUS_KEYWORDS:
                    validation_result['issues'].append(f"Dangerous keyword detected: {keyword}")
                    validation_result['is_safe'] = False
                elif keyword in self.SAFE_KEYWORDS:
                    if keyword not in validation_result['allowed_operations']:
                        validation_result['allowed_operations'].append(keyword)
    
    def _check_injection_patterns(self, query: str, validation_result):
        """Check for SQL injection patterns."""
        
        for pattern in self.compiled_patterns:
            matches = pattern.findall(query)
            if matches:
                validation_result['issues'].append(f"Potential injection pattern detected")
                validation_result['is_safe'] = False
    
    def _validate_table_access(self, query: str, validation_result):
        """Validate that only allowed tables/schemas are accessed."""
        
        # ទាញយកឈ្មោះតារាង (វិធីសាស្រ្តសាមញ្ញ)
        # ក្នុងការផលិតប្រើការវិភាគ SQL ដែលត្រឹមត្រូវ
        from_match = re.findall(r'FROM\s+(\w+\.?\w*)', query, re.IGNORECASE)
        join_match = re.findall(r'JOIN\s+(\w+\.?\w*)', query, re.IGNORECASE)
        
        all_tables = from_match + join_match
        
        for table_ref in all_tables:
            if '.' in table_ref:
                schema, table = table_ref.split('.', 1)
                if schema.lower() not in self.ALLOWED_SCHEMAS:
                    validation_result['issues'].append(f"Access to unauthorized schema: {schema}")
                    validation_result['is_safe'] = False
                if table.lower() not in self.ALLOWED_TABLES:
                    validation_result['warnings'].append(f"Access to table: {table}")
            else:
                # សន្មត់ថាជាគំរូលក់រាយ ប្រសិនបើមិនបានបញ្ជាក់
                if table_ref.lower() not in self.ALLOWED_TABLES:
                    validation_result['warnings'].append(f"Access to table: {table_ref}")
    
    def _determine_risk_level(self, validation_result):
        """Determine overall risk level."""
        
        if not validation_result['is_safe']:
            if any('injection' in issue.lower() for issue in validation_result['issues']):
                validation_result['risk_level'] = QueryRisk.CRITICAL
            elif any('DROP' in issue or 'DELETE' in issue for issue in validation_result['issues']):
                validation_result['risk_level'] = QueryRisk.HIGH
            else:
                validation_result['risk_level'] = QueryRisk.MEDIUM
        elif validation_result['warnings']:
            validation_result['risk_level'] = QueryRisk.LOW
        else:
            validation_result['risk_level'] = QueryRisk.LOW

# អនុស្សរណៈអ្នកផ្ទៀងផ្ទាត់សកល
query_validator = QueryValidator()
```

## 🗃️ ឧបករណ៍ស្វែងរកទិន្នន័យ

### ឧបករណ៍វិភាគការលក់

```python
# mcp_server/tools/sales_analysis.py
"""
Comprehensive sales analysis tool for retail data querying.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta
from .base import DatabaseTool, ToolResult
from .query_validator import query_validator

class SalesAnalysisTool(DatabaseTool):
    """Advanced sales analysis and reporting tool."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="execute_sales_query",
            description="Execute sophisticated sales analysis queries with natural language support",
            db_provider=db_provider
        )
        
        # តម្រងការសួរដែលបានបង្កើតមុនសម្រាប់ការវិភាគទូទៅ
        self.query_templates = {
            'daily_sales': """
                SELECT 
                    DATE(transaction_date) as sales_date,
                    COUNT(*) as transaction_count,
                    SUM(total_amount) as total_revenue,
                    AVG(total_amount) as avg_transaction_value,
                    COUNT(DISTINCT customer_id) as unique_customers
                FROM retail.sales_transactions 
                WHERE transaction_date >= $1 AND transaction_date <= $2
                  AND transaction_type = 'sale'
                GROUP BY DATE(transaction_date)
                ORDER BY sales_date DESC
            """,
            
            'top_products': """
                SELECT 
                    p.product_name,
                    p.brand,
                    SUM(sti.quantity) as total_quantity_sold,
                    SUM(sti.total_price) as total_revenue,
                    COUNT(DISTINCT st.transaction_id) as transaction_count,
                    AVG(sti.unit_price) as avg_price
                FROM retail.sales_transaction_items sti
                JOIN retail.sales_transactions st ON sti.transaction_id = st.transaction_id
                JOIN retail.products p ON sti.product_id = p.product_id
                WHERE st.transaction_date >= $1 AND st.transaction_date <= $2
                  AND st.transaction_type = 'sale'
                GROUP BY p.product_id, p.product_name, p.brand
                ORDER BY total_revenue DESC
                LIMIT $3
            """,
            
            'customer_analysis': """
                SELECT 
                    c.customer_id,
                    c.first_name || ' ' || c.last_name as customer_name,
                    c.loyalty_tier,
                    COUNT(st.transaction_id) as transaction_count,
                    SUM(st.total_amount) as total_spent,
                    AVG(st.total_amount) as avg_transaction_value,
                    MAX(st.transaction_date) as last_purchase_date,
                    DATE_PART('day', CURRENT_DATE - MAX(st.transaction_date)) as days_since_last_purchase
                FROM retail.customers c
                LEFT JOIN retail.sales_transactions st ON c.customer_id = st.customer_id
                WHERE st.transaction_date >= $1 AND st.transaction_date <= $2
                  AND st.transaction_type = 'sale'
                GROUP BY c.customer_id, c.first_name, c.last_name, c.loyalty_tier
                HAVING COUNT(st.transaction_id) > 0
                ORDER BY total_spent DESC
                LIMIT $3
            """,
            
            'category_performance': """
                SELECT 
                    pc.category_name,
                    COUNT(DISTINCT p.product_id) as unique_products,
                    SUM(sti.quantity) as total_quantity_sold,
                    SUM(sti.total_price) as total_revenue,
                    AVG(sti.unit_price) as avg_price,
                    COUNT(DISTINCT st.transaction_id) as transaction_count
                FROM retail.product_categories pc
                JOIN retail.products p ON pc.category_id = p.category_id
                JOIN retail.sales_transaction_items sti ON p.product_id = sti.product_id
                JOIN retail.sales_transactions st ON sti.transaction_id = st.transaction_id
                WHERE st.transaction_date >= $1 AND st.transaction_date <= $2
                  AND st.transaction_type = 'sale'
                GROUP BY pc.category_id, pc.category_name
                ORDER BY total_revenue DESC
            """,
            
            'sales_trends': """
                WITH daily_sales AS (
                    SELECT 
                        DATE(transaction_date) as sales_date,
                        SUM(total_amount) as daily_revenue,
                        COUNT(*) as daily_transactions
                    FROM retail.sales_transactions 
                    WHERE transaction_date >= $1 AND transaction_date <= $2
                      AND transaction_type = 'sale'
                    GROUP BY DATE(transaction_date)
                ),
                trend_analysis AS (
                    SELECT 
                        sales_date,
                        daily_revenue,
                        daily_transactions,
                        LAG(daily_revenue, 1) OVER (ORDER BY sales_date) as prev_day_revenue,
                        LAG(daily_revenue, 7) OVER (ORDER BY sales_date) as prev_week_revenue,
                        AVG(daily_revenue) OVER (
                            ORDER BY sales_date 
                            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
                        ) as rolling_7day_avg
                    FROM daily_sales
                )
                SELECT 
                    sales_date,
                    daily_revenue,
                    daily_transactions,
                    rolling_7day_avg,
                    CASE 
                        WHEN prev_day_revenue IS NOT NULL THEN
                            ROUND(((daily_revenue - prev_day_revenue) / prev_day_revenue * 100)::numeric, 2)
                        ELSE NULL
                    END as day_over_day_growth_pct,
                    CASE 
                        WHEN prev_week_revenue IS NOT NULL THEN
                            ROUND(((daily_revenue - prev_week_revenue) / prev_week_revenue * 100)::numeric, 2)
                        ELSE NULL
                    END as week_over_week_growth_pct
                FROM trend_analysis
                ORDER BY sales_date DESC
            """
        }
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute sales analysis query."""
        
        query_type = kwargs.get('query_type', 'custom')
        store_id = kwargs.get('store_id')
        
        if not store_id:
            return ToolResult(
                success=False,
                error="store_id is required for sales analysis"
            )
        
        try:
            if query_type in self.query_templates:
                return await self._execute_template_query(query_type, kwargs)
            elif query_type == 'custom':
                return await self._execute_custom_query(kwargs)
            else:
                return ToolResult(
                    success=False,
                    error=f"Unknown query type: {query_type}"
                )
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Sales analysis failed: {str(e)}"
            )
    
    async def _execute_template_query(self, query_type: str, kwargs: Dict[str, Any]) -> ToolResult:
        """Execute pre-built template query."""
        
        query = self.query_templates[query_type]
        store_id = kwargs['store_id']
        
        # ប៉ារ៉ាម៉ែត្រ​មូលដ្ឋាន​សម្រាប់​តម្រង​ការសួរ
        start_date = kwargs.get('start_date', (datetime.now() - timedelta(days=30)).date())
        end_date = kwargs.get('end_date', datetime.now().date())
        limit = kwargs.get('limit', 20)
        
        # បម្លែងថ្ងៃខែឆ្នាំជាអក្សរ ប្រសិនបើចាំបាច់
        if isinstance(start_date, str):
            start_date = datetime.fromisoformat(start_date).date()
        if isinstance(end_date, str):
            end_date = datetime.fromisoformat(end_date).date()
        
        # អនុវត្តតម្រងការសួរជាមួយប៉ារ៉ាម៉ែត្រ
        params = (start_date, end_date, limit) if '$3' in query else (start_date, end_date)
        
        result = await self.execute_query(query, params, store_id)
        
        if result.success:
            result.metadata = {
                'query_type': query_type,
                'date_range': f"{start_date} to {end_date}",
                'store_id': store_id,
                'analysis_type': 'template'
            }
        
        return result
    
    async def _execute_custom_query(self, kwargs: Dict[str, Any]) -> ToolResult:
        """Execute custom SQL query with validation."""
        
        custom_query = kwargs.get('query')
        store_id = kwargs['store_id']
        
        if not custom_query:
            return ToolResult(
                success=False,
                error="Custom query is required when query_type is 'custom'"
            )
        
        # ផ្ទៀងផ្ទាត់តម្រងការសួរដើម្បីសុវត្ថិភាព
        validation = query_validator.validate_query(custom_query)
        
        if not validation['is_safe']:
            return ToolResult(
                success=False,
                error=f"Query validation failed: {', '.join(validation['issues'])}",
                metadata={
                    'validation_result': validation,
                    'risk_level': validation['risk_level'].value
                }
            )
        
        # អនុវត្តតម្រងការសួរដែលបានផ្ទៀងផ្ទាត់សុវត្ថិភាព
        result = await self.execute_query(custom_query, None, store_id)
        
        if result.success:
            result.metadata = {
                'query_type': 'custom',
                'store_id': store_id,
                'validation_warnings': validation.get('warnings', []),
                'analysis_type': 'custom'
            }
        
        return result
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for the sales analysis tool."""
        
        return {
            "type": "object",
            "properties": {
                "query_type": {
                    "type": "string",
                    "enum": list(self.query_templates.keys()) + ["custom"],
                    "description": "Type of sales analysis to perform",
                    "default": "daily_sales"
                },
                "store_id": {
                    "type": "string",
                    "description": "Store ID for data isolation",
                    "pattern": "^[a-zA-Z0-9_-]+$"
                },
                "start_date": {
                    "type": "string",
                    "format": "date",
                    "description": "Start date for analysis (YYYY-MM-DD)"
                },
                "end_date": {
                    "type": "string",
                    "format": "date",
                    "description": "End date for analysis (YYYY-MM-DD)"
                },
                "limit": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 1000,
                    "description": "Maximum number of results to return",
                    "default": 20
                },
                "query": {
                    "type": "string",
                    "description": "Custom SQL query (required when query_type is 'custom')"
                }
            },
            "required": ["store_id"],
            "additionalProperties": False
        }
```

### ឧបករណ៍ត្រួតពិនិត្យស្ដង់ដារតារាចរណ៍

```python
# mcp_server/tools/schema_introspection.py
"""
Database schema introspection and metadata tools.
"""
from typing import Dict, Any, List
from .base import DatabaseTool, ToolResult, ToolCategory

class SchemaIntrospectionTool(DatabaseTool):
    """Tool for exploring database schema and metadata."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="get_table_schema",
            description="Get detailed schema information for database tables",
            db_provider=db_provider
        )
        self.category = ToolCategory.SCHEMA_INTROSPECTION
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute schema introspection."""
        
        table_name = kwargs.get('table_name')
        include_constraints = kwargs.get('include_constraints', True)
        include_indexes = kwargs.get('include_indexes', True)
        include_statistics = kwargs.get('include_statistics', False)
        
        try:
            if table_name:
                return await self._get_single_table_schema(
                    table_name, include_constraints, include_indexes, include_statistics
                )
            else:
                return await self._get_all_tables_schema(include_constraints, include_indexes)
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Schema introspection failed: {str(e)}"
            )
    
    async def _get_single_table_schema(
        self, 
        table_name: str, 
        include_constraints: bool,
        include_indexes: bool,
        include_statistics: bool
    ) -> ToolResult:
        """Get detailed schema for a single table."""
        
        schema_info = {
            'table_name': table_name,
            'columns': [],
            'constraints': [],
            'indexes': [],
            'statistics': {}
        }
        
        async with self.get_connection() as conn:
            # ទទួលបានព័ត៌មានជួរឈរ
            columns_query = """
                SELECT 
                    column_name,
                    data_type,
                    is_nullable,
                    column_default,
                    character_maximum_length,
                    numeric_precision,
                    numeric_scale,
                    ordinal_position,
                    udt_name
                FROM information_schema.columns
                WHERE table_schema = 'retail' AND table_name = $1
                ORDER BY ordinal_position
            """
            
            columns = await conn.fetch(columns_query, table_name)
            schema_info['columns'] = [dict(col) for col in columns]
            
            # ទទួលបានស្តង់ដារ ប្រសិនបើត្រូវបានស្នើរសុំ
            if include_constraints:
                constraints_query = """
                    SELECT 
                        constraint_name,
                        constraint_type,
                        column_name,
                        foreign_table_name,
                        foreign_column_name
                    FROM information_schema.table_constraints tc
                    LEFT JOIN information_schema.key_column_usage kcu 
                        ON tc.constraint_name = kcu.constraint_name
                    LEFT JOIN information_schema.referential_constraints rc
                        ON tc.constraint_name = rc.constraint_name
                    LEFT JOIN information_schema.key_column_usage fkcu
                        ON rc.unique_constraint_name = fkcu.constraint_name
                    WHERE tc.table_schema = 'retail' AND tc.table_name = $1
                """
                
                constraints = await conn.fetch(constraints_query, table_name)
                schema_info['constraints'] = [dict(const) for const in constraints]
            
            # ទទួលបានស៊ុមការណ៍ ប្រសិនបើត្រូវបានស្នើរសុំ
            if include_indexes:
                indexes_query = """
                    SELECT 
                        indexname as index_name,
                        indexdef as index_definition,
                        tablespace
                    FROM pg_indexes
                    WHERE schemaname = 'retail' AND tablename = $1
                """
                
                indexes = await conn.fetch(indexes_query, table_name)
                schema_info['indexes'] = [dict(idx) for idx in indexes]
            
            # ទទួលបានស្ថិតិតារាង ប្រសិនបើត្រូវបានស្នើរសុំ
            if include_statistics:
                stats_query = """
                    SELECT 
                        n_tup_ins as inserts,
                        n_tup_upd as updates,
                        n_tup_del as deletes,
                        n_live_tup as live_tuples,
                        n_dead_tup as dead_tuples,
                        last_vacuum,
                        last_autovacuum,
                        last_analyze,
                        last_autoanalyze
                    FROM pg_stat_user_tables
                    WHERE schemaname = 'retail' AND relname = $1
                """
                
                stats = await conn.fetchrow(stats_query, table_name)
                if stats:
                    schema_info['statistics'] = dict(stats)
        
        return ToolResult(
            success=True,
            data=schema_info,
            metadata={
                'table_name': table_name,
                'schema': 'retail',
                'introspection_type': 'single_table'
            }
        )
    
    async def _get_all_tables_schema(
        self, 
        include_constraints: bool,
        include_indexes: bool
    ) -> ToolResult:
        """Get schema information for all tables."""
        
        async with self.get_connection() as conn:
            # ទទួលបានតារាងទាំងអស់នៅក្នុងស្កឹមលក់រាយ
            tables_query = """
                SELECT 
                    table_name,
                    table_type
                FROM information_schema.tables
                WHERE table_schema = 'retail'
                ORDER BY table_name
            """
            
            tables = await conn.fetch(tables_query)
            schema_info = {
                'schema_name': 'retail',
                'tables': []
            }
            
            for table in tables:
                table_info = {
                    'table_name': table['table_name'],
                    'table_type': table['table_type'],
                    'columns': []
                }
                
                # ទទួលបានជួរឈរសម្រាប់តារាងនីមួយៗ
                columns_query = """
                    SELECT 
                        column_name,
                        data_type,
                        is_nullable,
                        column_default
                    FROM information_schema.columns
                    WHERE table_schema = 'retail' AND table_name = $1
                    ORDER BY ordinal_position
                """
                
                columns = await conn.fetch(columns_query, table['table_name'])
                table_info['columns'] = [dict(col) for col in columns]
                
                schema_info['tables'].append(table_info)
        
        return ToolResult(
            success=True,
            data=schema_info,
            metadata={
                'schema': 'retail',
                'table_count': len(schema_info['tables']),
                'introspection_type': 'all_tables'
            }
        )
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for schema introspection tool."""
        
        return {
            "type": "object",
            "properties": {
                "table_name": {
                    "type": "string",
                    "description": "Specific table name to introspect (optional - if not provided, all tables are returned)",
                    "pattern": "^[a-zA-Z_][a-zA-Z0-9_]*$"
                },
                "include_constraints": {
                    "type": "boolean",
                    "description": "Include constraint information",
                    "default": True
                },
                "include_indexes": {
                    "type": "boolean",
                    "description": "Include index information",
                    "default": True
                },
                "include_statistics": {
                    "type": "boolean",
                    "description": "Include table statistics",
                    "default": False
                }
            },
            "additionalProperties": False
        }

class MultiTableSchemaTool(DatabaseTool):
    """Tool for getting schema information for multiple tables at once."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="get_multiple_table_schemas",
            description="Get schema information for multiple tables efficiently",
            db_provider=db_provider
        )
        self.category = ToolCategory.SCHEMA_INTROSPECTION
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute multi-table schema introspection."""
        
        table_names = kwargs.get('table_names', [])
        
        if not table_names:
            return ToolResult(
                success=False,
                error="At least one table name is required"
            )
        
        try:
            schemas = {}
            
            async with self.get_connection() as conn:
                for table_name in table_names:
                    # ទទួលបានស្កឹមតារាង
                    schema_query = """
                        SELECT 
                            c.column_name,
                            c.data_type,
                            c.is_nullable,
                            c.column_default,
                            c.character_maximum_length,
                            tc.constraint_type,
                            kcu.constraint_name
                        FROM information_schema.columns c
                        LEFT JOIN information_schema.key_column_usage kcu
                            ON c.table_name = kcu.table_name 
                            AND c.column_name = kcu.column_name
                            AND c.table_schema = kcu.table_schema
                        LEFT JOIN information_schema.table_constraints tc
                            ON kcu.constraint_name = tc.constraint_name
                            AND kcu.table_schema = tc.table_schema
                        WHERE c.table_schema = 'retail' AND c.table_name = $1
                        ORDER BY c.ordinal_position
                    """
                    
                    columns = await conn.fetch(schema_query, table_name)
                    
                    if columns:
                        schemas[table_name] = {
                            'table_name': table_name,
                            'columns': [dict(col) for col in columns]
                        }
                    else:
                        schemas[table_name] = {
                            'table_name': table_name,
                            'error': 'Table not found or not accessible'
                        }
            
            return ToolResult(
                success=True,
                data=schemas,
                metadata={
                    'requested_tables': table_names,
                    'found_tables': [name for name, info in schemas.items() if 'error' not in info],
                    'missing_tables': [name for name, info in schemas.items() if 'error' in info]
                }
            )
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Multi-table schema introspection failed: {str(e)}"
            )
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for multi-table schema tool."""
        
        return {
            "type": "object",
            "properties": {
                "table_names": {
                    "type": "array",
                    "items": {
                        "type": "string",
                        "pattern": "^[a-zA-Z_][a-zA-Z0-9_]*$"
                    },
                    "description": "List of table names to get schema information for",
                    "minItems": 1,
                    "maxItems": 20
                }
            },
            "required": ["table_names"],
            "additionalProperties": False
        }
```

## 📊 ឧបករណ៍វិភាគ និងជំនួយ

### ឧបករណ៍បញ្ញាអាជីវកម្ម

```python
# mcp_server/tools/business_intelligence.py
"""
Advanced business intelligence and analytics tools.
"""
from typing import Dict, Any, List
from datetime import datetime, timedelta
from .base import DatabaseTool, ToolResult, ToolCategory

class BusinessIntelligenceTool(DatabaseTool):
    """Advanced analytics tool for business intelligence queries."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="generate_business_insights",
            description="Generate comprehensive business intelligence reports and insights",
            db_provider=db_provider
        )
        self.category = ToolCategory.ANALYTICS
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute business intelligence analysis."""
        
        analysis_type = kwargs.get('analysis_type', 'summary')
        store_id = kwargs.get('store_id')
        
        if not store_id:
            return ToolResult(
                success=False,
                error="store_id is required for business intelligence analysis"
            )
        
        try:
            if analysis_type == 'summary':
                return await self._generate_business_summary(kwargs)
            elif analysis_type == 'customer_segmentation':
                return await self._analyze_customer_segmentation(kwargs)
            elif analysis_type == 'product_performance':
                return await self._analyze_product_performance(kwargs)
            elif analysis_type == 'seasonal_trends':
                return await self._analyze_seasonal_trends(kwargs)
            else:
                return ToolResult(
                    success=False,
                    error=f"Unknown analysis type: {analysis_type}"
                )
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Business intelligence analysis failed: {str(e)}"
            )
    
    async def _generate_business_summary(self, kwargs: Dict[str, Any]) -> ToolResult:
        """Generate comprehensive business summary."""
        
        store_id = kwargs['store_id']
        days = kwargs.get('days', 30)
        
        summary_query = """
            WITH date_range AS (
                SELECT CURRENT_DATE - INTERVAL '%s days' as start_date,
                       CURRENT_DATE as end_date
            ),
            sales_summary AS (
                SELECT 
                    COUNT(*) as total_transactions,
                    COUNT(DISTINCT customer_id) as unique_customers,
                    SUM(total_amount) as total_revenue,
                    AVG(total_amount) as avg_transaction_value,
                    COUNT(DISTINCT DATE(transaction_date)) as active_days
                FROM retail.sales_transactions st, date_range dr
                WHERE st.transaction_date >= dr.start_date 
                  AND st.transaction_date <= dr.end_date
                  AND st.transaction_type = 'sale'
            ),
            product_summary AS (
                SELECT 
                    COUNT(DISTINCT p.product_id) as products_sold,
                    SUM(sti.quantity) as total_items_sold
                FROM retail.sales_transaction_items sti
                JOIN retail.sales_transactions st ON sti.transaction_id = st.transaction_id
                JOIN retail.products p ON sti.product_id = p.product_id
                CROSS JOIN date_range dr
                WHERE st.transaction_date >= dr.start_date 
                  AND st.transaction_date <= dr.end_date
                  AND st.transaction_type = 'sale'
            ),
            top_category AS (
                SELECT 
                    pc.category_name,
                    SUM(sti.total_price) as category_revenue
                FROM retail.product_categories pc
                JOIN retail.products p ON pc.category_id = p.category_id
                JOIN retail.sales_transaction_items sti ON p.product_id = sti.product_id
                JOIN retail.sales_transactions st ON sti.transaction_id = st.transaction_id
                CROSS JOIN date_range dr
                WHERE st.transaction_date >= dr.start_date 
                  AND st.transaction_date <= dr.end_date
                  AND st.transaction_type = 'sale'
                GROUP BY pc.category_name
                ORDER BY category_revenue DESC
                LIMIT 1
            )
            SELECT 
                ss.*,
                ps.products_sold,
                ps.total_items_sold,
                tc.category_name as top_category,
                tc.category_revenue as top_category_revenue,
                CASE 
                    WHEN ss.active_days > 0 THEN ss.total_revenue / ss.active_days
                    ELSE 0
                END as avg_daily_revenue
            FROM sales_summary ss
            CROSS JOIN product_summary ps
            CROSS JOIN top_category tc
        """ % days
        
        result = await self.execute_query(summary_query, None, store_id)
        
        if result.success and result.data:
            summary = result.data[0]
            
            # បន្ថែមចំណេះដឹងដែលបានគិត
            insights = {
                'revenue_trend': 'stable',  # នឹងគណនាលើមូលដ្ឋានទិន្នន័យប្រវត្តិសាស្ត្រ
                'customer_retention': f"{summary.get('unique_customers', 0)} active customers",
                'performance_indicators': {
                    'transactions_per_day': round(summary.get('total_transactions', 0) / max(summary.get('active_days', 1), 1), 2),
                    'revenue_per_customer': round(summary.get('total_revenue', 0) / max(summary.get('unique_customers', 1), 1), 2),
                    'items_per_transaction': round(summary.get('total_items_sold', 0) / max(summary.get('total_transactions', 1), 1), 2)
                }
            }
            
            summary['insights'] = insights
            
            result.data = [summary]
            result.metadata = {
                'analysis_type': 'business_summary',
                'period_days': days,
                'store_id': store_id
            }
        
        return result
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for business intelligence tool."""
        
        return {
            "type": "object",
            "properties": {
                "analysis_type": {
                    "type": "string",
                    "enum": ["summary", "customer_segmentation", "product_performance", "seasonal_trends"],
                    "description": "Type of business intelligence analysis to perform",
                    "default": "summary"
                },
                "store_id": {
                    "type": "string",
                    "description": "Store ID for analysis",
                    "pattern": "^[a-zA-Z0-9_-]+$"
                },
                "days": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 365,
                    "description": "Number of days to analyze",
                    "default": 30
                }
            },
            "required": ["store_id"],
            "additionalProperties": False
        }

class UtilityTool(DatabaseTool):
    """Utility tool for common operations."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="get_current_utc_date",
            description="Get current UTC date and time for reference",
            db_provider=db_provider
        )
        self.category = ToolCategory.UTILITY
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute utility operation."""
        
        format_type = kwargs.get('format', 'iso')
        
        try:
            async with self.get_connection() as conn:
                if format_type == 'iso':
                    query = "SELECT CURRENT_TIMESTAMP AT TIME ZONE 'UTC' as current_utc_datetime"
                elif format_type == 'epoch':
                    query = "SELECT EXTRACT(EPOCH FROM CURRENT_TIMESTAMP AT TIME ZONE 'UTC') as current_utc_epoch"
                elif format_type == 'date_only':
                    query = "SELECT CURRENT_DATE as current_date"
                else:
                    return ToolResult(
                        success=False,
                        error=f"Unknown format type: {format_type}"
                    )
                
                result = await conn.fetchrow(query)
                
                return ToolResult(
                    success=True,
                    data=dict(result),
                    metadata={
                        'format_type': format_type,
                        'timezone': 'UTC'
                    }
                )
        
        except Exception as e:
            return ToolResult(
                success=False,
                error=f"Utility operation failed: {str(e)}"
            )
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for utility tool."""
        
        return {
            "type": "object",
            "properties": {
                "format": {
                    "type": "string",
                    "enum": ["iso", "epoch", "date_only"],
                    "description": "Format for the returned date/time",
                    "default": "iso"
                }
            },
            "additionalProperties": False
        }
```

## 🎯 ចំណុចសង្ខេបសំខាន់ៗ

បន្ទាប់ពីបញ្ចប់មេរៀននេះ អ្នកគួរតែមាន៖

✅ **សំណុំរចនាឧបករណ៍កម្រិតខ្ពស់**៖ អនុវត្តឧបករណ៍ MCP ដ៏ស្មុគស្មាញជាមួយការដោះស្រាយកំហុសយ៉ាងពេញលេញ  
✅ **ការត្រួតពិនិត្យសំណួរ**៖ បង្កើតការត្រួតពិនិត្យ SQL ដែលមានសុវត្ថិភាពដើម្បីទប់ស្កាត់ការវាយប្រហារ injection  
✅ **ឧបករណ៍ទិន្នន័យ**៖ បង្កើតសមត្ថភាពវិភាគការលក់ និងត្រួតពិនិត្យស្ដង់ដារតារាចរណ៍ដ៏មានអំណាច  
✅ **បញ្ញាអាជីវកម្ម**៖ អភិវឌ្ឍឧបករណ៍វិភាគសម្រាប់ទស្សនវិស័យអាជីវកម្មដ៏ទូលំទូលាយ  
✅ **បង្កើនប្រសិទ្ធភាព**៖ អនុវត្តការកាន់កាប់ដូចជា caching ការបង្ហាប់ការតភ្ជាប់ និងបង្កើនបញ្ជោតសំណួរ  
✅ **ការវាយតម្លៃសុវត្ថិភាព**៖ អនុវត្តការគ្រប់គ្រងការចូលប្រើដោយផ្អែកលើតួនាទី និងការចុះកំណត់ហេតុ audit logging  

## 🚀 បន្ទាប់មក

បន្តជាមួយ **[Lab 07: Semantic Search Integration](../07-Semantic-Search/README.md)** ដើម្បី៖

- អនុវត្តសមត្ថភាពស្វែងរកវ៉ិចទ័រជាមួយឧបករណ៍ MCP
- សាងសង់មុខងារស្វែងរកផលិតផលចំណាំស្មារតី
- អនុវត្តការយល់ដឹងសំណួរដោយឧបករណ៍ AI
- បង្កើតការស្វែងរកបញ្ចូលគ្នារវាងសំណួរបែបប្រពៃណី និងវ៉ិចទ័រ

## 📚 ធនធានបន្ថែម

### ការអភិវឌ្ឍឧបករណ៍ MCP
- [Model Context Protocol Documentation](https://modelcontextprotocol.io/docs) - វិចារណកថា MCP ផ្លូវការជាភាសាខ្មែរ
- [FastMCP Framework](https://github.com/jlowin/fastmcp) - ការអនុវត្ត MCP ជាភាសា Python
- [MCP Tool Patterns](https://github.com/modelcontextprotocol/servers) - ឧទាហរណ៍ការអនុវត្តឧបករណ៍

### សុវត្ថិភាពទិន្នន័យ
- [ការការពារ SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection) - មគ្គុទេសក៍សុវត្ថិភាព OWASP
- [សុវត្ថិភាព PostgreSQL](https://www.postgresql.org/docs/current/security.html) - ពិធីការសុវត្ថិភាពដ៏ល្អបំផុតសម្រាប់ទិន្នន័យ
- [បច្ចេកទេសត្រួតពិនិត្យសំណួរ](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html) - លំនាំសំណួរដែលមានសុវត្ថិភាព

### ការបង្កើនប្រសិទ្ធភាព
- [ការបង្កើនប្រសិទ្ធភាពស្វែងរកទិន្នន័យ](https://www.postgresql.org/docs/current/performance-tips.html) - មគ្គុទេសក៍ប្រសិទ្ធភាព PostgreSQL
- [វិធីសាស្ត្រប្រើ Connection Pooling ល្អបំផុត](https://www.postgresql.org/docs/current/runtime-config-connection.html) - ការគ្រប់គ្រងការតភ្ជាប់
- [លំនាំ Python Async](https://docs.python.org/3/library/asyncio.html) - មគ្គុទេសក៍កម្មវិធីអាសីងខ្លួន

---

**មុននេះ**៖ [Lab 05: MCP Server Implementation](../05-MCP-Server/README.md)  
**បន្ទាប់**៖ [Lab 07: Semantic Search Integration](../07-Semantic-Search/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបញ្ចាក់**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលដែលយើងខិតខំប្រឹងប្រែងដើម្បីឲ្យមានភាពត្រឹមត្រូវ សូមអោយយល់ថាការបកប្រែស្វ័យប្រវត្តិនេះអាចមានកំហុស ឬភាពមិនត្រឹមត្រូវ។ ឯកសារដើមនៅភាសាទេលើ ត្រូវបានគេយកជាដើមទាញសំខាន់។ សម្រាប់ព័ត៌មានដែលមានសារៈសំខាន់ គឺជាការផ្ដល់អនុសាសន៍ឲ្យប្រើការបកប្រែដោយមនុស្សជំនាញ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំនៃតួអក្សរឬការបកប្រែ ខណៈដែលបានប្រើការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->