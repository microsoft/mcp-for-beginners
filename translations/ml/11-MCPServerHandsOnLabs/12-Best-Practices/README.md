# മികച്ച പ്രാക്ടീസുകളും ഓപ്റ്റിമൈസേഷനും

## 🎯 ഈ ലാബ് എന്താണ് ഉൾക്കൊള്ളുന്നത്

ഈ ക്യാപ്സ്റ്റോൺ ലാബ് ശക്തമായ, സ്കെയിലബിൾ, സുരക്ഷിതമായ MCP സെർവറുകൾ ഡാറ്റാബേസ് ഇന്റഗ്രേഷനോടുകൂടി നിർമ്മിക്കുന്നതിനുള്ള മികച്ച പ്രാക്ടീസുകൾ, ഓപ്റ്റിമൈസേഷൻ സാങ്കേതികവിദ്യകൾ, പ്രൊഡക്ഷൻ മാർഗ്ഗനിർദ്ദേശങ്ങൾ എന്നിവ സംയോജിപ്പിക്കുന്നു. നിങ്ങളുടെ നടപ്പാക്കൽ പ്രൊഡക്ഷൻ-റെഡി ആകാൻ യാഥാർത്ഥ്യാനുഭവത്തിലും വ്യവസായ മാനദണ്ഡങ്ങളിലും നിന്നുള്ള അറിവുകൾ നിങ്ങൾക്ക് ലഭിക്കും.

## അവലോകനം

വിജയകരമായ MCP സെർവർ നിർമ്മിക്കുന്നത് കോഡ് പ്രവർത്തിപ്പിക്കുന്നതിൽ മാത്രം ഒതുങ്ങുന്ന കാര്യമല്ല. സ്കെയിൽ ചെയ്യാൻ കഴിയുന്ന, വിശ്വസനീയമായി പ്രവർത്തിക്കുന്ന, സുരക്ഷാ മാനദണ്ഡങ്ങൾ പാലിക്കുന്ന പ്രൊഡക്ഷൻ-റെഡി സിസ്റ്റങ്ങൾ നിർമ്മിക്കുന്നതിനുള്ള അടിസ്ഥാന പ്രാക്ടീസുകൾ ഈ ലാബ് ഉൾക്കൊള്ളുന്നു.

ഈ മികച്ച പ്രാക്ടീസുകൾ യാഥാർത്ഥ്യപ്രയോഗങ്ങൾ, കമ്മ്യൂണിറ്റി പ്രതികരണങ്ങൾ, എന്റർപ്രൈസ് നടപ്പാക്കലുകളിൽ നിന്നുള്ള പാഠങ്ങൾ എന്നിവയിൽ നിന്നാണ് ലഭിച്ചത്.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ ലാബ് പൂർത്തിയാക്കിയാൽ, നിങ്ങൾക്ക് കഴിയും:

- **പ്രയോഗിക്കുക** MCP സെർവറുകൾക്കും ഡാറ്റാബേസുകൾക്കും പ്രകടന ഓപ്റ്റിമൈസേഷൻ സാങ്കേതികവിദ്യകൾ  
- **നടപ്പിലാക്കുക** സമഗ്രമായ സുരക്ഷാ ഹാർഡനിംഗ് നടപടികൾ  
- **ഡിസൈൻ ചെയ്യുക** പ്രൊഡക്ഷൻ പരിസ്ഥിതികൾക്കായി സ്കെയിലബിൾ ആർക്കിടെക്ചർ പാറ്റേണുകൾ  
- **സ്ഥാപിക്കുക** നിരീക്ഷണം, പരിപാലനം, പ്രവർത്തന നടപടിക്രമങ്ങൾ  
- **ഓപ്റ്റിമൈസ് ചെയ്യുക** പ്രകടനവും വിശ്വസനീയതയും നിലനിർത്തിക്കൊണ്ട് ചെലവുകൾ  
- **സംഭാവന നൽകുക** MCP കമ്മ്യൂണിറ്റിക്കും ഇക്കോസിസ്റ്റത്തിനും  

## 🚀 പ്രകടന ഓപ്റ്റിമൈസേഷൻ

### ഡാറ്റാബേസ് പ്രകടനം

#### കണക്ഷൻ പൂൾ ഓപ്റ്റിമൈസേഷൻ

```python
# മെച്ചപ്പെടുത്തിയ കണക്ഷൻ പൂൾ കോൺഫിഗറേഷൻ
POOL_CONFIG = {
    # വലുപ്പം കോൺഫിഗറേഷൻ
    "min_size": max(2, cpu_count()),           # കുറഞ്ഞത് 2, CPU അനുസരിച്ച് സ്കെയിൽ ചെയ്യുക
    "max_size": min(20, cpu_count() * 4),     # യുക്തിസഹമായ പരമാവധി പരിധി
    
    # സമയക്രമ കോൺഫിഗറേഷൻ
    "max_inactive_connection_lifetime": 300,   # 5 മിനിറ്റ്
    "command_timeout": 30,                     # 30 സെക്കൻഡ്
    "max_queries": 50000,                      # കണക്ഷനുകൾ റോട്ടേറ്റ് ചെയ്യുക
    
    # പോസ്റ്റ്‌ഗ്രെഎസ്‌ക്യു‌എൽ ക്രമീകരണങ്ങൾ
    "server_settings": {
        "application_name": "mcp-server-prod",
        "jit": "off",                          # സുസ്ഥിരതയ്ക്കായി അപ്രാപ്തമാക്കുക
        "work_mem": "8MB",                     # ക്വെറികൾക്ക് മെച്ചപ്പെടുത്തുക
        "shared_preload_libraries": "pg_stat_statements",
        "log_statement": "mod",                # മാറ്റങ്ങൾ മാത്രം ലോഗ് ചെയ്യുക
        "log_min_duration_statement": "1s",   # മന്ദഗതിയിലുള്ള ക്വെറികൾ ലോഗ് ചെയ്യുക
    }
}
```

#### ക്വറി ഓപ്റ്റിമൈസേഷൻ പാറ്റേണുകൾ

```python
class QueryOptimizer:
    """Database query optimization utilities."""
    
    def __init__(self):
        self.query_cache = {}
        self.slow_query_threshold = 1.0  # സെക്കൻഡുകൾ
        
    async def execute_optimized_query(
        self, 
        query: str, 
        params: tuple = None,
        cache_key: str = None,
        cache_ttl: int = 300
    ):
        """Execute query with optimization and caching."""
        
        # ആദ്യം കാഷെ പരിശോധിക്കുക
        if cache_key and cache_key in self.query_cache:
            cache_entry = self.query_cache[cache_key]
            if time.time() - cache_entry['timestamp'] < cache_ttl:
                return cache_entry['result']
        
        # നിരീക്ഷണത്തോടെ പ്രവർത്തിപ്പിക്കുക
        start_time = time.time()
        
        try:
            async with db_provider.get_connection() as conn:
                # ക്വറി നിർവഹണം മെച്ചപ്പെടുത്തുക
                await conn.execute("SET enable_seqscan = off")  # സൂചികകൾ മുൻഗണന നൽകുക
                await conn.execute("SET work_mem = '16MB'")     # ഈ ക്വറിയ്ക്ക് കൂടുതൽ മെമ്മറി
                
                result = await conn.fetch(query, *params if params else ())
                
                duration = time.time() - start_time
                
                # മന്ദഗതിയിലുള്ള ക്വറികൾ ലോഗ് ചെയ്യുക
                if duration > self.slow_query_threshold:
                    logger.warning(f"Slow query detected: {duration:.2f}s", extra={
                        "query": query[:200],
                        "duration": duration,
                        "params_count": len(params) if params else 0
                    })
                
                # വിജയകരമായ ഫലങ്ങൾ കാഷെ ചെയ്യുക
                if cache_key and len(result) < 1000:  # വലിയ ഫലങ്ങൾ കാഷെ ചെയ്യരുത്
                    self.query_cache[cache_key] = {
                        'result': result,
                        'timestamp': time.time()
                    }
                
                return result
                
        except Exception as e:
            logger.error(f"Query optimization failed: {e}")
            raise

# സൂചിക ശിപാർശകൾ
RECOMMENDED_INDEXES = [
    # കോർ ബിസിനസ് സൂചികകൾ
    "CREATE INDEX CONCURRENTLY idx_orders_store_date ON retail.orders (store_id, order_date DESC);",
    "CREATE INDEX CONCURRENTLY idx_order_items_product ON retail.order_items (product_id);",
    "CREATE INDEX CONCURRENTLY idx_customers_store_email ON retail.customers (store_id, email);",
    
    # അനലിറ്റിക്സ് സൂചികകൾ
    "CREATE INDEX CONCURRENTLY idx_orders_date_amount ON retail.orders (order_date, total_amount);",
    "CREATE INDEX CONCURRENTLY idx_products_category_price ON retail.products (category_id, unit_price);",
    
    # വെക്ടർ തിരയൽ മെച്ചപ്പെടുത്തൽ
    "CREATE INDEX CONCURRENTLY idx_embeddings_vector ON retail.product_description_embeddings USING ivfflat (description_embedding vector_cosine_ops) WITH (lists = 100);",
]
```

### അപ്ലിക്കേഷൻ പ്രകടനം

#### അസിങ്ക് പ്രോഗ്രാമിംഗ് മികച്ച പ്രാക്ടീസുകൾ

```python
import asyncio
from asyncio import Semaphore
from typing import List, Any

class AsyncOptimizer:
    """Async operation optimization patterns."""
    
    def __init__(self, max_concurrent: int = 10):
        self.semaphore = Semaphore(max_concurrent)
        self.circuit_breaker = CircuitBreaker()
    
    async def batch_process(
        self, 
        items: List[Any], 
        process_func: callable,
        batch_size: int = 100
    ):
        """Process items in optimized batches."""
        
        async def process_batch(batch):
            async with self.semaphore:
                return await asyncio.gather(
                    *[process_func(item) for item in batch],
                    return_exceptions=True
                )
        
        # സിസ്റ്റം ഭാരം കൂടാതിരിക്കാൻ ബാച്ചുകളായി പ്രോസസ് ചെയ്യുക
        results = []
        for i in range(0, len(items), batch_size):
            batch = items[i:i + batch_size]
            batch_results = await process_batch(batch)
            results.extend(batch_results)
            
            # റിസോഴ്‌സ് ക്ഷയം തടയാൻ ബാച്ചുകൾക്കിടയിൽ ചെറിയ വൈകിപ്പ്
            if i + batch_size < len(items):
                await asyncio.sleep(0.1)
        
        return results
    
    @circuit_breaker_decorator
    async def resilient_operation(self, operation: callable, *args, **kwargs):
        """Execute operation with circuit breaker protection."""
        return await operation(*args, **kwargs)

# സർക്യൂട്ട് ബ്രേക്കർ നടപ്പാക്കൽ
class CircuitBreaker:
    """Circuit breaker for external service calls."""
    
    def __init__(self, failure_threshold: int = 5, recovery_timeout: int = 60):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.failure_count = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # ക്ലോസ്, ഓപ്പൺ, ഹാഫ്_ഓപ്പൺ
    
    async def call(self, func, *args, **kwargs):
        """Execute function with circuit breaker protection."""
        
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_timeout:
                self.state = "HALF_OPEN"
            else:
                raise Exception("Circuit breaker is OPEN")
        
        try:
            result = await func(*args, **kwargs)
            
            # വിജയത്തിൽ റീസെറ്റ് ചെയ്യുക
            if self.state == "HALF_OPEN":
                self.state = "CLOSED"
                self.failure_count = 0
            
            return result
            
        except Exception as e:
            self.failure_count += 1
            self.last_failure_time = time.time()
            
            if self.failure_count >= self.failure_threshold:
                self.state = "OPEN"
            
            raise
```

### കാഷിംഗ് തന്ത്രങ്ങൾ

```python
import redis
import pickle
from typing import Union, Optional

class SmartCache:
    """Multi-level caching system."""
    
    def __init__(self, redis_url: Optional[str] = None):
        self.memory_cache = {}
        self.redis_client = redis.Redis.from_url(redis_url) if redis_url else None
        self.max_memory_items = 1000
    
    async def get(self, key: str) -> Optional[Any]:
        """Get from cache with fallback levels."""
        
        # ലെവൽ 1: മെമ്മറി കാഷെ
        if key in self.memory_cache:
            return self.memory_cache[key]['value']
        
        # ലെവൽ 2: റെഡിസ് കാഷെ
        if self.redis_client:
            try:
                cached_data = self.redis_client.get(key)
                if cached_data:
                    value = pickle.loads(cached_data)
                    
                    # മെമ്മറി കാഷിലേക്ക് പ്രോത്സാഹിപ്പിക്കുക
                    self._set_memory_cache(key, value)
                    return value
            except Exception as e:
                logger.warning(f"Redis cache error: {e}")
        
        return None
    
    async def set(
        self, 
        key: str, 
        value: Any, 
        ttl: int = 300,
        cache_level: str = "both"
    ):
        """Set cache value at specified levels."""
        
        if cache_level in ["memory", "both"]:
            self._set_memory_cache(key, value, ttl)
        
        if cache_level in ["redis", "both"] and self.redis_client:
            try:
                self.redis_client.setex(
                    key, 
                    ttl, 
                    pickle.dumps(value)
                )
            except Exception as e:
                logger.warning(f"Redis set error: {e}")
    
    def _set_memory_cache(self, key: str, value: Any, ttl: int = 300):
        """Set value in memory cache with LRU eviction."""
        
        # LRU എവിക്ഷൻ നടപ്പിലാക്കുക
        if len(self.memory_cache) >= self.max_memory_items:
            oldest_key = min(
                self.memory_cache.keys(),
                key=lambda k: self.memory_cache[k]['timestamp']
            )
            del self.memory_cache[oldest_key]
        
        self.memory_cache[key] = {
            'value': value,
            'timestamp': time.time(),
            'ttl': ttl
        }

# കാഷെ കീ ജനറേഷൻ
def generate_cache_key(query: str, user_context: str, params: dict = None) -> str:
    """Generate consistent cache keys."""
    key_components = [
        query.strip().lower(),
        user_context,
        json.dumps(params, sort_keys=True) if params else ""
    ]
    
    key_string = "|".join(key_components)
    return hashlib.sha256(key_string.encode()).hexdigest()
```

## 🔒 സുരക്ഷാ ഹാർഡനിംഗ്

### ഓതന്റിക്കേഷൻ ആൻഡ് ഓതറൈസേഷൻ

```python
from azure.identity import DefaultAzureCredential, ClientSecretCredential
from azure.keyvault.secrets import SecretClient
import jwt
from typing import Dict, List

class SecurityManager:
    """Comprehensive security management."""
    
    def __init__(self):
        self.key_vault_client = self._setup_key_vault()
        self.token_blacklist = set()
        
    def _setup_key_vault(self) -> SecretClient:
        """Initialize Azure Key Vault client."""
        credential = DefaultAzureCredential()
        vault_url = os.getenv("AZURE_KEY_VAULT_URL")
        
        if vault_url:
            return SecretClient(vault_url=vault_url, credential=credential)
        return None
    
    async def validate_request(self, request_headers: Dict[str, str]) -> Dict[str, Any]:
        """Comprehensive request validation."""
        
        # പ്രാമാണീകരണം എടുക്കുകയും സാധുത പരിശോധിക്കുകയും ചെയ്യുക
        auth_token = request_headers.get("authorization", "").replace("Bearer ", "")
        if not auth_token:
            raise AuthenticationError("Missing authentication token")
        
        # ടോക്കൺ സാധുത പരിശോധിക്കുക
        user_context = await self._validate_token(auth_token)
        
        # നിരക്ക് പരിധി പരിശോധിക്കുക
        await self._check_rate_limit(user_context["user_id"])
        
        # RLS സാന്ദർഭ്യം സാധുത പരിശോധിക്കുക
        rls_user_id = request_headers.get("x-rls-user-id")
        if not self._validate_rls_access(user_context, rls_user_id):
            raise AuthorizationError("Invalid RLS context for user")
        
        return {
            "user_id": user_context["user_id"],
            "roles": user_context["roles"],
            "rls_user_id": rls_user_id,
            "permissions": user_context["permissions"]
        }
    
    async def _validate_token(self, token: str) -> Dict[str, Any]:
        """Validate JWT token."""
        
        if token in self.token_blacklist:
            raise AuthenticationError("Token has been revoked")
        
        try:
            # കീ വാൾട്ടിൽ നിന്നോ കാഷെയിൽ നിന്നോ പബ്ലിക് കീ നേടുക
            public_key = await self._get_public_key()
            
            # ടോക്കൺ ഡികോഡ് ചെയ്ത് സാധുത പരിശോധിക്കുക
            payload = jwt.decode(
                token, 
                public_key, 
                algorithms=["RS256"],
                audience="mcp-server",
                issuer="zava-auth"
            )
            
            return {
                "user_id": payload["sub"],
                "roles": payload.get("roles", []),
                "permissions": payload.get("permissions", []),
                "expires_at": payload["exp"]
            }
            
        except jwt.InvalidTokenError as e:
            raise AuthenticationError(f"Invalid token: {e}")
    
    def _validate_rls_access(self, user_context: Dict, rls_user_id: str) -> bool:
        """Validate RLS context access."""
        
        # സൂപ്പർ അഡ്മിനുകൾക്ക് ഏതെങ്കിലും സാന്ദർഭ്യത്തിൽ പ്രവേശനം ലഭിക്കും
        if "super_admin" in user_context["roles"]:
            return True
        
        # സ്റ്റോർ മാനേജർമാർക്ക് അവരുടെ സ്വന്തം സ്റ്റോറിൽ മാത്രമേ പ്രവേശനം ലഭിക്കൂ
        if "store_manager" in user_context["roles"]:
            allowed_stores = user_context.get("allowed_stores", [])
            return rls_user_id in allowed_stores
        
        # പ്രാദേശിക മാനേജർമാർക്ക് പല സ്റ്റോറുകളിലും പ്രവേശനം ലഭിക്കും
        if "regional_manager" in user_context["roles"]:
            allowed_regions = user_context.get("allowed_regions", [])
            return self._check_store_in_regions(rls_user_id, allowed_regions)
        
        return False

# ഇൻപുട്ട് സാധുതയും ശുദ്ധീകരണവും
class InputValidator:
    """SQL injection prevention and input validation."""
    
    @staticmethod
    def validate_sql_query(query: str) -> bool:
        """Validate SQL query for safety."""
        
        # നിരോധിത മാതൃകകൾ
        forbidden_patterns = [
            r";\s*(DROP|DELETE|UPDATE|INSERT|ALTER|CREATE)\s+",
            r"--.*",
            r"/\*.*\*/",
            r"xp_cmdshell",
            r"sp_executesql",
            r"EXEC\s*\(",
        ]
        
        query_upper = query.upper()
        
        for pattern in forbidden_patterns:
            if re.search(pattern, query_upper, re.IGNORECASE):
                logger.warning(f"Blocked potentially dangerous query: {pattern}")
                return False
        
        # SELECT പ്രസ്താവനകൾ മാത്രമേ അനുവദിക്കൂ
        if not query_upper.strip().startswith("SELECT"):
            return False
        
        return True
    
    @staticmethod
    def sanitize_table_name(table_name: str) -> str:
        """Sanitize table name input."""
        
        # അക്ഷരസംഖ്യ, അണ്ടർസ്കോർ, ഡോട്ട് മാത്രമേ അനുവദിക്കൂ
        if not re.match(r"^[a-zA-Z0-9_.]+$", table_name):
            raise ValueError("Invalid table name format")
        
        # അനുവദിച്ച പട്ടികകളെതിരെ സാധുത പരിശോധിക്കുക
        if table_name not in VALID_TABLES:
            raise ValueError(f"Table {table_name} not allowed")
        
        return table_name
```

### ഡാറ്റ സംരക്ഷണം

```python
from cryptography.fernet import Fernet
import hashlib

class DataProtection:
    """Data encryption and protection utilities."""
    
    def __init__(self):
        self.encryption_key = self._get_encryption_key()
        self.cipher_suite = Fernet(self.encryption_key)
    
    def _get_encryption_key(self) -> bytes:
        """Get encryption key from secure storage."""
        
        # പ്രൊഡക്ഷനിൽ, Azure കീ വോൾട്ടിൽ നിന്ന് നേടുക
        key_vault_secret = os.getenv("ENCRYPTION_KEY_SECRET_NAME")
        if key_vault_secret and self.key_vault_client:
            secret = self.key_vault_client.get_secret(key_vault_secret)
            return secret.value.encode()
        
        # ഡെവലപ്പ്മെന്റിനുള്ള ഫാൾബാക്ക് (പ്രൊഡക്ഷനിനല്ല!)
        dev_key = os.getenv("DEV_ENCRYPTION_KEY")
        if dev_key:
            return dev_key.encode()
        
        raise ValueError("No encryption key available")
    
    def encrypt_sensitive_data(self, data: str) -> str:
        """Encrypt sensitive data."""
        return self.cipher_suite.encrypt(data.encode()).decode()
    
    def decrypt_sensitive_data(self, encrypted_data: str) -> str:
        """Decrypt sensitive data."""
        return self.cipher_suite.decrypt(encrypted_data.encode()).decode()
    
    @staticmethod
    def hash_password(password: str, salt: str = None) -> tuple:
        """Hash password with salt."""
        if not salt:
            salt = os.urandom(32).hex()
        
        password_hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            salt.encode(),
            100000  # ആവർത്തനങ്ങൾ
        ).hex()
        
        return password_hash, salt
    
    @staticmethod
    def mask_sensitive_logs(log_data: dict) -> dict:
        """Mask sensitive information in logs."""
        
        sensitive_fields = [
            'password', 'token', 'secret', 'key', 'authorization',
            'x-api-key', 'client_secret', 'connection_string'
        ]
        
        masked_data = log_data.copy()
        
        for field in sensitive_fields:
            if field in masked_data:
                value = str(masked_data[field])
                if len(value) > 4:
                    masked_data[field] = value[:2] + "*" * (len(value) - 4) + value[-2:]
                else:
                    masked_data[field] = "***"
        
        return masked_data
```

## 📊 പ്രൊഡക്ഷൻ ഡിപ്ലോയ്മെന്റ് മാർഗ്ഗനിർദ്ദേശങ്ങൾ

### ഇൻഫ്രാസ്ട്രക്ചർ ആസ് കോഡ്

```yaml
# azure-pipelines.yml
trigger:
  branches:
    include:
      - main
      - release/*

variables:
  - group: mcp-server-secrets
  - name: imageRepository
    value: 'zava-mcp-server'
  - name: containerRegistry
    value: 'zavamcpregistry.azurecr.io'

stages:
- stage: Build
  displayName: Build and Test
  jobs:
  - job: Build
    displayName: Build
    pool:
      vmImage: ubuntu-latest
    
    steps:
    - task: UsePythonVersion@0
      inputs:
        versionSpec: '3.11'
        displayName: 'Use Python 3.11'
    
    - script: |
        python -m pip install --upgrade pip
        pip install -r requirements.lock.txt
        pip install pytest pytest-cov
      displayName: 'Install dependencies'
    
    - script: |
        pytest tests/ --cov=mcp_server --cov-report=xml
      displayName: 'Run tests with coverage'
    
    - task: PublishCodeCoverageResults@1
      inputs:
        codeCoverageTool: Cobertura
        summaryFileLocation: 'coverage.xml'
    
    - task: Docker@2
      displayName: Build Docker image
      inputs:
        command: build
        repository: $(imageRepository)
        dockerfile: Dockerfile
        tags: |
          $(Build.BuildId)
          latest

- stage: Deploy
  displayName: Deploy to Production
  dependsOn: Build
  condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
  
  jobs:
  - deployment: DeployProduction
    displayName: Deploy to Production
    environment: 'production'
    pool:
      vmImage: ubuntu-latest
    
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureContainerApps@1
            inputs:
              azureSubscription: $(azureServiceConnection)
              containerAppName: 'zava-mcp-server'
              resourceGroup: '$(resourceGroupName)'
              imageToDeploy: '$(containerRegistry)/$(imageRepository):$(Build.BuildId)'
```

### കണ്ടെയ്‌നർ ഓപ്റ്റിമൈസേഷൻ

```dockerfile
# Multi-stage Dockerfile for production
FROM python:3.11-slim as builder

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy requirements and install Python dependencies
COPY requirements.lock.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.lock.txt

# Production stage
FROM python:3.11-slim as production

# Create non-root user
RUN groupadd -r mcpserver && useradd -r -g mcpserver mcpserver

# Copy virtual environment from builder
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Set working directory
WORKDIR /app

# Copy application code
COPY mcp_server/ ./mcp_server/
COPY --chown=mcpserver:mcpserver . .

# Set security configurations
RUN chmod -R 755 /app && \
    chown -R mcpserver:mcpserver /app

# Switch to non-root user
USER mcpserver

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Expose port
EXPOSE 8000

# Start application
CMD ["python", "-m", "mcp_server.sales_analysis"]
```

### പരിസ്ഥിതി കോൺഫിഗറേഷൻ

```python
# ഉത്പാദന കോൺഫിഗറേഷൻ മാനേജ്മെന്റ്
class ProductionConfig:
    """Production-specific configuration."""
    
    def __init__(self):
        self.validate_production_requirements()
        self.setup_logging()
        self.configure_security()
    
    def validate_production_requirements(self):
        """Validate all required production settings."""
        
        required_settings = [
            "AZURE_CLIENT_ID",
            "AZURE_CLIENT_SECRET", 
            "AZURE_TENANT_ID",
            "PROJECT_ENDPOINT",
            "AZURE_OPENAI_ENDPOINT",
            "POSTGRES_HOST",
            "POSTGRES_PASSWORD",
            "APPLICATIONINSIGHTS_CONNECTION_STRING"
        ]
        
        missing_settings = [
            setting for setting in required_settings 
            if not os.getenv(setting)
        ]
        
        if missing_settings:
            raise EnvironmentError(
                f"Missing required production settings: {missing_settings}"
            )
    
    def setup_logging(self):
        """Configure production logging."""
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.StreamHandler(sys.stdout),
                logging.handlers.RotatingFileHandler(
                    '/var/log/mcp-server.log',
                    maxBytes=50*1024*1024,  # 50MB
                    backupCount=5
                )
            ]
        )
        
        # മൂന്നാംകക്ഷി ലോഗറുകൾ WARNING ആയി സജ്ജമാക്കുക
        logging.getLogger('azure').setLevel(logging.WARNING)
        logging.getLogger('urllib3').setLevel(logging.WARNING)
    
    def configure_security(self):
        """Configure production security settings."""
        
        # ഡീബഗ് മോഡ് അപ്രാപ്തമാക്കുക
        os.environ['DEBUG'] = 'False'
        
        # സുരക്ഷിത ഹെഡറുകൾ സജ്ജമാക്കുക
        os.environ['SECURE_SSL_REDIRECT'] = 'True'
        os.environ['SECURE_HSTS_SECONDS'] = '31536000'
        os.environ['SECURE_CONTENT_TYPE_NOSNIFF'] = 'True'
        os.environ['SECURE_BROWSER_XSS_FILTER'] = 'True'
```

## 💰 ചെലവ് ഓപ്റ്റിമൈസേഷൻ

### റിസോഴ്‌സ് മാനേജ്മെന്റ്

```python
class CostOptimizer:
    """Cost optimization strategies."""
    
    def __init__(self):
        self.metrics_collector = MetricsCollector()
        self.auto_scaler = AutoScaler()
    
    async def optimize_database_connections(self):
        """Dynamically adjust connection pool based on load."""
        
        current_load = await self.metrics_collector.get_current_load()
        
        if current_load < 0.3:  # കുറഞ്ഞ ലോഡ്
            target_pool_size = max(2, int(current_load * 10))
        elif current_load < 0.7:  # മധ്യസ്ഥ ലോഡ്
            target_pool_size = max(5, int(current_load * 15))
        else:  # ഉയർന്ന ലോഡ്
            target_pool_size = min(20, int(current_load * 25))
        
        await db_provider.adjust_pool_size(target_pool_size)
        
        logger.info(f"Adjusted pool size to {target_pool_size} for load {current_load}")
    
    async def implement_smart_caching(self):
        """Implement intelligent caching to reduce compute costs."""
        
        # ക്യാഷ് ചെലവേറിയ പ്രവർത്തനങ്ങൾ
        expensive_queries = await self.identify_expensive_queries()
        
        for query in expensive_queries:
            cache_key = self.generate_cache_key(query)
            ttl = self.calculate_optimal_ttl(query)
            
            await smart_cache.set(cache_key, None, ttl=ttl)
    
    def calculate_azure_costs(self) -> Dict[str, float]:
        """Calculate estimated Azure resource costs."""
        
        return {
            "container_apps": self.estimate_container_costs(),
            "postgresql": self.estimate_database_costs(),
            "openai": self.estimate_ai_costs(),
            "application_insights": self.estimate_monitoring_costs(),
            "storage": self.estimate_storage_costs()
        }

# ഓട്ടോ-സ്കെയിലിംഗ് കോൺഫിഗറേഷൻ
class AutoScaler:
    """Automatic scaling based on metrics."""
    
    async def scale_decision(self) -> str:
        """Determine scaling action based on metrics."""
        
        metrics = await self.collect_scaling_metrics()
        
        # CPU അടിസ്ഥാനമാക്കിയുള്ള സ്കെയിലിംഗ്
        if metrics['cpu_usage'] > 80:
            return "scale_up"
        elif metrics['cpu_usage'] < 20 and metrics['instance_count'] > 1:
            return "scale_down"
        
        # മെമ്മറി അടിസ്ഥാനമാക്കിയുള്ള സ്കെയിലിംഗ്
        if metrics['memory_usage'] > 85:
            return "scale_up"
        
        # അഭ്യർത്ഥന ക്യൂ സ്കെയിലിംഗ്
        if metrics['queue_length'] > 100:
            return "scale_up"
        elif metrics['queue_length'] < 10 and metrics['instance_count'] > 1:
            return "scale_down"
        
        return "no_action"
```

## 🔧 പരിപാലനവും പ്രവർത്തനവും

### ഹെൽത്ത് നിരീക്ഷണം

```python
class OperationalHealth:
    """Comprehensive operational health monitoring."""
    
    def __init__(self):
        self.alert_manager = AlertManager()
        self.health_checks = {}
        
    async def comprehensive_health_check(self) -> Dict[str, Any]:
        """Perform comprehensive system health check."""
        
        health_report = {
            "timestamp": datetime.utcnow().isoformat(),
            "overall_status": "healthy",
            "components": {}
        }
        
        # ഡാറ്റാബേസ് ആരോഗ്യസ്ഥിതി
        db_health = await self.check_database_health()
        health_report["components"]["database"] = db_health
        
        # ബാഹ്യ സേവനങ്ങളുടെ ആരോഗ്യസ്ഥിതി
        ai_health = await self.check_ai_service_health()
        health_report["components"]["ai_service"] = ai_health
        
        # സിസ്റ്റം വിഭവങ്ങൾ
        system_health = await self.check_system_resources()
        health_report["components"]["system"] = system_health
        
        # അപ്ലിക്കേഷൻ മെട്രിക്‌സ്
        app_health = await self.check_application_health()
        health_report["components"]["application"] = app_health
        
        # മൊത്തം നില നിർണ്ണയിക്കുക
        failed_components = [
            name for name, status in health_report["components"].items()
            if status.get("status") != "healthy"
        ]
        
        if failed_components:
            health_report["overall_status"] = "unhealthy"
            health_report["failed_components"] = failed_components
            
            # അലർട്ടുകൾ പ്രേരിപ്പിക്കുക
            await self.alert_manager.send_alert(
                severity="high",
                message=f"Health check failed for: {failed_components}",
                details=health_report
            )
        
        return health_report
    
    async def check_database_health(self) -> Dict[str, Any]:
        """Check database connectivity and performance."""
        
        try:
            start_time = time.time()
            
            async with db_provider.get_connection() as conn:
                # അടിസ്ഥാന കണക്ടിവിറ്റി
                await conn.fetchval("SELECT 1")
                
                # മന്ദഗതിയിലുള്ള ക്വെറികൾ പരിശോധിക്കുക
                slow_queries = await conn.fetch("""
                    SELECT query, mean_exec_time, calls 
                    FROM pg_stat_statements 
                    WHERE mean_exec_time > 1000 
                    ORDER BY mean_exec_time DESC 
                    LIMIT 5
                """)
                
                # കണക്ഷൻ എണ്ണം പരിശോധിക്കുക
                connection_count = await conn.fetchval("""
                    SELECT count(*) FROM pg_stat_activity 
                    WHERE state = 'active'
                """)
                
                response_time = time.time() - start_time
                
                return {
                    "status": "healthy",
                    "response_time_ms": response_time * 1000,
                    "active_connections": connection_count,
                    "slow_queries_count": len(slow_queries),
                    "pool_size": db_provider.connection_pool.get_size()
                }
                
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e),
                "last_check": datetime.utcnow().isoformat()
            }

# സ്വയം പ്രവർത്തിക്കുന്ന ബാക്കപ്പ് மற்றும் പുനരുദ്ധാരണം
class BackupManager:
    """Database backup and recovery management."""
    
    async def create_backup(self, backup_type: str = "full") -> str:
        """Create database backup."""
        
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        backup_name = f"zava_backup_{backup_type}_{timestamp}"
        
        if backup_type == "full":
            await self.create_full_backup(backup_name)
        elif backup_type == "incremental":
            await self.create_incremental_backup(backup_name)
        
        # അസ്യൂർ ബ്ലോബ് സ്റ്റോറേജിലേക്ക് അപ്‌ലോഡ് ചെയ്യുക
        await self.upload_backup_to_azure(backup_name)
        
        return backup_name
    
    async def schedule_automated_backups(self):
        """Schedule regular automated backups."""
        
        # 2 AM UTC-യിൽ ദൈനംദിന പൂർണ്ണ ബാക്കപ്പ്
        schedule.every().day.at("02:00").do(
            lambda: asyncio.create_task(self.create_backup("full"))
        )
        
        # മണിക്കൂറിൽ ഒരു തവണ ഇൻക്രീമെന്റൽ ബാക്കപ്പുകൾ
        schedule.every().hour.do(
            lambda: asyncio.create_task(self.create_backup("incremental"))
        )
```

## 🌍 കമ്മ്യൂണിറ്റി സംഭാവനകൾ

### ഓപ്പൺ സോഴ്‌സ് മികച്ച പ്രാക്ടീസുകൾ

```markdown
# Contributing to MCP Database Integration

## Development Guidelines

### Code Quality Standards
- Follow PEP 8 for Python code style
- Maintain test coverage above 90%
- Use type hints throughout the codebase
- Write comprehensive docstrings

### Testing Requirements
- Unit tests for all new functionality
- Integration tests for database operations
- Performance benchmarks for critical paths
- Security tests for authentication/authorization

### Documentation Standards
- Update README.md for any new features
- Add inline code documentation
- Create examples for new tools or patterns
- Maintain API documentation

## Security Considerations

### Reporting Security Issues
- Report security vulnerabilities privately
- Use encrypted communication channels
- Provide detailed reproduction steps
- Include potential impact assessment

### Security Review Process
- All PRs undergo security review
- Static analysis tools required to pass
- Dependency vulnerability scanning
- Manual security testing for critical changes
```

### കമ്മ്യൂണിറ്റി ഏംഗേജ്‌മെന്റ്

```python
class CommunityContributor:
    """Tools for community engagement and contribution."""
    
    @staticmethod
    def generate_contribution_guide():
        """Generate personalized contribution guide."""
        
        return {
            "getting_started": {
                "setup": "Follow setup guide in Lab 03",
                "first_contribution": "Start with documentation improvements",
                "testing": "Run full test suite before submitting PR"
            },
            
            "contribution_areas": {
                "documentation": "Improve learning labs and examples",
                "testing": "Add test cases and improve coverage",
                "features": "Implement new MCP tools and capabilities",
                "performance": "Optimize queries and caching",
                "security": "Enhance security measures and validation"
            },
            
            "community_resources": {
                "discord": "https://discord.com/invite/ByRwuEEgH4",
                "discussions": "GitHub Discussions for Q&A",
                "issues": "GitHub Issues for bug reports",
                "examples": "Share your implementation examples"
            }
        }
    
    @staticmethod
    def validate_contribution(pr_data: Dict) -> Dict[str, bool]:
        """Validate contribution meets standards."""
        
        return {
            "has_tests": "test" in pr_data.get("files_changed", []),
            "has_documentation": "README" in str(pr_data.get("files_changed", [])),
            "follows_conventions": True,  # യഥാർത്ഥ പരിശോധനകൾ നടപ്പിലാക്കും
            "security_reviewed": pr_data.get("security_review", False),
            "performance_tested": pr_data.get("benchmark_results", False)
        }
```

## 🎯 പ്രധാന പഠനങ്ങൾ

ഈ സമഗ്ര പഠന പാത പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങൾക്ക് കൈവരിക്കേണ്ടത്:

✅ **പ്രകടന ഓപ്റ്റിമൈസേഷൻ**: ഡാറ്റാബേസ് ട്യൂണിംഗ്, അസിങ്ക് പാറ്റേണുകൾ, കാഷിംഗ് തന്ത്രങ്ങൾ  
✅ **സുരക്ഷാ ഹാർഡനിംഗ്**: ഓതന്റിക്കേഷൻ, ഓതറൈസേഷൻ, ഡാറ്റ സംരക്ഷണം  
✅ **പ്രൊഡക്ഷൻ ഡിപ്ലോയ്മെന്റ്**: ഇൻഫ്രാസ്ട്രക്ചർ ആസ് കോഡ്, കണ്ടെയ്‌നർ ഓപ്റ്റിമൈസേഷൻ  
✅ **ചെലവ് മാനേജ്മെന്റ്**: റിസോഴ്‌സ് ഓപ്റ്റിമൈസേഷൻ, ബുദ്ധിമുട്ടുള്ള സ്കെയിലിംഗ്  
✅ **പ്രവർത്തന മികവ്**: നിരീക്ഷണം, പരിപാലനം, ഓട്ടോമേഷൻ  
✅ **കമ്മ്യൂണിറ്റി ഏംഗേജ്‌മെന്റ്**: MCP ഇക്കോസിസ്റ്റത്തിലേക്ക് സംഭാവന നൽകൽ  

## 🏆 സർട്ടിഫിക്കേഷൻയും അടുത്ത ഘട്ടങ്ങളും

### പ്രായോഗിക മൂല്യനിർണ്ണയം

നിങ്ങളുടെ പ്രാവീണ്യം തെളിയിക്കാൻ ഈ അന്തിമ പ്രോജക്ട് പൂർത്തിയാക്കുക:

**പ്രൊഡക്ഷൻ-റെഡി MCP സെർവർ നിർമ്മിക്കുക** ഇതിൽ ഉൾപ്പെടുന്നു:  
- [ ] RLS ഉപയോഗിച്ചുള്ള മൾട്ടി-ടെനന്റ് റീട്ടെയിൽ അനലിറ്റിക്സ്  
- [ ] Azure OpenAI ഉപയോഗിച്ചുള്ള സെമാന്റിക് സെർച്ച്  
- [ ] സമഗ്രമായ സുരക്ഷാ നടപ്പാക്കൽ  
- [ ] Azure-യിൽ പ്രൊഡക്ഷൻ ഡിപ്ലോയ്മെന്റ്  
- [ ] നിരീക്ഷണവും അലർട്ടിംഗും സജ്ജീകരിക്കൽ  
- [ ] ഡോക്യുമെന്റേഷൻ, ടെസ്റ്റിംഗ്  

### ആധുനിക പഠന പാതകൾ

നിങ്ങളുടെ MCP യാത്ര തുടരുക:

- **MCP ആർക്കിടെക്ചർ പാറ്റേണുകൾ**: ആധുനിക സെർവർ ആർക്കിടെക്ചറുകൾ  
- **മൾട്ടി-മോഡൽ ഇന്റഗ്രേഷൻ**: വ്യത്യസ്ത AI മോഡലുകൾ സംയോജിപ്പിക്കൽ  
- **എന്റർപ്രൈസ് സ്കെയിൽ**: വലിയ തോതിലുള്ള MCP ഡിപ്ലോയ്മെന്റുകൾ  
- **കസ്റ്റം ടൂൾ ഡെവലപ്പ്മെന്റ്**: പ്രത്യേക MCP ടൂളുകൾ നിർമ്മിക്കൽ  
- **MCP ഇക്കോസിസ്റ്റം**: വ്യാപക കമ്മ്യൂണിറ്റിക്ക് സംഭാവന നൽകൽ  

### കമ്മ്യൂണിറ്റി അംഗീകാരം

നിങ്ങളുടെ നേട്ടം പങ്കുവെക്കുക:  
- **GitHub പോർട്ട്ഫോളിയോ**: നിങ്ങളുടെ നടപ്പാക്കൽ പ്രദർശിപ്പിക്കുക  
- **കമ്മ്യൂണിറ്റി സംഭാവനകൾ**: മെച്ചപ്പെടുത്തലുകൾ അല്ലെങ്കിൽ ഉദാഹരണങ്ങൾ സമർപ്പിക്കുക  
- **പ്രസംഗ അവസരങ്ങൾ**: മീറ്റപ്പുകളിലും സമ്മേളനങ്ങളിലും അവതരിപ്പിക്കുക  
- **മെന്ററിംഗ്**: മറ്റ് ഡെവലപ്പർമാർക്ക് MCP പഠിക്കാൻ സഹായിക്കുക  

## 📚 അധിക സ്രോതസുകൾ

### ആധുനിക വിഷയങ്ങൾ
- [PostgreSQL Performance Tuning](https://www.postgresql.org/docs/current/performance-tips.html) - ഡാറ്റാബേസ് ഓപ്റ്റിമൈസേഷൻ  
- [Azure Container Apps Best Practices](https://docs.microsoft.com/azure/container-apps/overview) - പ്രൊഡക്ഷൻ ഡിപ്ലോയ്മെന്റ്  
- [Python Async Best Practices](https://docs.python.org/3/library/asyncio-dev.html) - അസിങ്ക് പ്രോഗ്രാമിംഗ്  

### സുരക്ഷാ സ്രോതസുകൾ
- [OWASP Top 10](https://owasp.org/www-project-top-ten/) - സുരക്ഷാ ദുർബലതകൾ  
- [Azure Security Best Practices](https://docs.microsoft.com/azure/security/) - ക്ലൗഡ് സുരക്ഷ  
- [Python Security Guidelines](https://python.org/dev/security/) - സുരക്ഷിത കോഡിംഗ്  

### കമ്മ്യൂണിറ്റി
- [MCP Community Discord](https://discord.com/invite/ByRwuEEgH4) - ലൈവ് ചർച്ചകൾ  
- [GitHub Discussions](https://github.com/microsoft/MCP-Server-and-PostgreSQL-Sample-Retail/discussions) - ചോദ്യോത്തരങ്ങളും പങ്കുവെക്കലും  
- [Stack Overflow](https://stackoverflow.com/questions/tagged/model-context-protocol) - സാങ്കേതിക ചോദ്യങ്ങൾ  

---

**🎉 അഭിനന്ദനങ്ങൾ!** നിങ്ങൾ MCP ഡാറ്റാബേസ് ഇന്റഗ്രേഷൻ സമഗ്ര പഠന പാത പൂർത്തിയാക്കി. യാഥാർത്ഥ്യ ഡാറ്റാ സിസ്റ്റങ്ങളുമായി AI അസിസ്റ്റന്റുകളെ ബന്ധിപ്പിക്കുന്ന പ്രൊഡക്ഷൻ-റെഡി MCP സെർവർ നിർമ്മിക്കാൻ നിങ്ങൾക്ക് അറിവും കഴിവും ലഭിച്ചു.

**സംഭാവന നൽകാൻ തയ്യാറാണോ?** ഞങ്ങളുടെ കമ്മ്യൂണിറ്റിയിൽ ചേരുക, നിങ്ങളുടെ അനുഭവങ്ങൾ പങ്കുവെച്ച്, കോഡ് മെച്ചപ്പെടുത്തലുകൾ സംഭാവന ചെയ്ത്, അധിക പഠന സ്രോതസുകൾ സൃഷ്ടിച്ച് MCP പഠനത്തിൽ മറ്റുള്ളവരെ സഹായിക്കുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->