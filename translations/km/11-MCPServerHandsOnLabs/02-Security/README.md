# សុវត្ថិភាព និង ច្រើនអតិថិជន

## 🎯 អ្វីដែលមូលដ្ឋាននេះគ្របដណ្តប់

មូលដ្ឋាននេះផ្តល់ការណែនាំដ៏ទូលំទូលាយអំពីការអនុវត្តសុវត្ថិភាពថ្នាក់សហគ្រាស និងច្រើនអតិថិជនសម្រាប់ម៉ាស៊ីនមេ MCP។ អ្នកនឹងរៀនរចនាប្រព័ន្ធដែលមានសុវត្ថិភាព និងអនុលោមដែលការពារទិន្នន័យលំអិតនៅក្នុងការលក់រាយខណៈដែលអនុញ្ញាតឲ្យមានលំនាំចូលបត់បែនក្នុងចន្លោះអតិថិជនច្រើននាក់។

## សេចក្តីផ្ដល់មុន

សុវត្ថិភាពគឺជារឿងសំខាន់នៅក្នុងកម្មវិធីលក់រាយដែលថែក្សទិន្នន័យអតិថិជន ព័ត៌មានបង់ប្រាក់ និងឯកទេសអាជីវកម្ម។ មូលដ្ឋាននេះគ្របដណ្តប់ស្ថាបត្យកម្មសុវត្ថិភាពពេញលេញចាប់ពីការផ្ទៀងផ្ទាត់អត្តសញ្ញាណ និងអនុញ្ញាតកម្ម ដល់ការបំបែកទិន្នន័យ និងការត្រួតពិនិត្យការអនុលោម។

យើងអនុវត្តយុទ្ធសាស្ត្រការពារជម្រះជ្រៅដែលផ្សំគ្នារវាងសេវាអត្តសញ្ញាណ Azure សុវត្ថិភាពកម្រិតជួរដទៃ PostgreSQL ការគ្រប់គ្រងកម្រិតកម្មវិធី និងកំណត់ហេតុត្រួតពិនិត្យទូលំទូលាយ ដើម្បីបង្កើតវេទិកាដែលរឹងមាំ និងដំណើរការអនុលោម។

## គោលបំណងសិក្សា

នៅចុងបង្អស់នៃមូលដ្ឋាននេះ អ្នកនឹងអាចធ្វើបាន៖

- **អនុវត្ត** សុវត្ថិភាពកម្រិតជួរដទៃថ្នាក់សហគ្រាសសម្រាប់ការបំបែកទិន្នន័យច្រើនអតិថិជន  
- **រចនា** លំនាំផ្ទៀងផ្ទាត់អត្តសញ្ញាណ និងអនុញ្ញាតកម្មដែលមានសុវត្ថិភាពជាមួយ Azure  
- **កំណត់រចនាសម្ព័ន្ធ** កំណត់ហេតុត្រួតពិនិត្យទូលំទូលាយសម្រាប់តម្រូវការអនុលោម  
- **អនុវត្ត** យុទ្ធសាស្ត្រការពារជម្រះជ្រៅនៅលើស្រទាប់កម្មវិធីទាំងអស់  
- **ផ្ទៀងផ្ទាត់** ការអនុវត្តសុវត្ថិភាពតាមរយៈការធ្វើតេស្តប្រព័ន្ធ  
- **ត្រួតពិនិត្យ** ព្រឹត្តិការណ៍សុវត្ថិភាព និងឆ្លើយតបចំពោះគ្រោះថ្នាក់អាចកើតមាន

## 🔐 ស្ថាបត្យកម្មសុវត្ថិភាពច្រើនអតិថិជន

### ទិដ្ឋភាពទូលំទូលាយស្រទាប់សុវត្ថិភាព

```
┌─────────────────────────────────────────────────┐
│               Azure Front Door                  │ ← WAF, DDoS Protection
├─────────────────────────────────────────────────┤
│              Application Gateway                │ ← SSL Termination, Rate Limiting
├─────────────────────────────────────────────────┤
│                MCP Server                       │ ← Authentication, Authorization
│  ┌─────────────────────────────────────────────┤
│  │           Connection Layer                  │ ← Connection Pooling, Circuit Breakers
│  ├─────────────────────────────────────────────┤
│  │         Business Logic Layer               │ ← Input Validation, Business Rules
│  ├─────────────────────────────────────────────┤
│  │           Data Access Layer                │ ← Query Sanitization, RLS Context
│  └─────────────────────────────────────────────┤
├─────────────────────────────────────────────────┤
│              PostgreSQL RLS                    │ ← Row Level Security, Audit Triggers
└─────────────────────────────────────────────────┘
```

### ម៉ូដែលច្រើនអតិថិជន

ការអនុវត្តរបស់យើងប្រើម៉ូដែល **មូលដ្ឋានទិន្នន័យរួម, ស្កេមរួម** ជាមួយសុវត្ថិភាពកម្រិតជួរដទៃ (RLS):

**អត្ថប្រយោជន៍៖**  
- ការប្រើប្រាស់ធនធានមានប្រសិទ្ធភាព  
- ការថែទាំនិងបច្ចុប្បន្នភាពមានភាពស្រួល  
- ការបំបែកទិន្នន័យខ្លាំងតាមរយៈ RLS  
- ដំណើរការសុវត្ថិភាពដែលអនុលោមនូវច្បាប់

**អត្រាបំណុល៖**  
- តម្រូវអោយមានការរចនា​គោលការណ៍ RLS ដោយប្រុងប្រយ័ត្ន  
- ការផ្លាស់ប្តូរស្កេមប៉ះពាល់ទៅលើអតិថិជនទាំងអស់  
- តម្រូវឲ្យមាននីតិវិធីបម្រុងទុក និងស្ដារដែលរឹងមាំ

## 🛡️ ការអនុវត្តសុវត្ថិភាពកម្រិតជួរដទៃ

### មូលដ្ឋាន RLS

```sql
-- Enable RLS on all multi-tenant tables
ALTER TABLE retail.customers ENABLE ROW LEVEL SECURITY;
ALTER TABLE retail.products ENABLE ROW LEVEL SECURITY;
ALTER TABLE retail.sales_transactions ENABLE ROW LEVEL SECURITY;
ALTER TABLE retail.sales_transaction_items ENABLE ROW LEVEL SECURITY;
ALTER TABLE retail.product_embeddings ENABLE ROW LEVEL SECURITY;

-- Create application role for MCP server
CREATE ROLE mcp_user LOGIN;
GRANT USAGE ON SCHEMA retail TO mcp_user;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA retail TO mcp_user;
```

### ការគ្រប់គ្រងបរិបទហាង

```sql
-- Function to securely set store context
CREATE OR REPLACE FUNCTION retail.set_store_context(store_id_param VARCHAR(50))
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
SET search_path = retail, pg_temp
AS $$
DECLARE
    user_info RECORD;
BEGIN
    -- Validate store exists and is active
    SELECT store_id, store_name, is_active 
    INTO user_info
    FROM retail.stores 
    WHERE store_id = store_id_param;
    
    IF NOT FOUND THEN
        RAISE EXCEPTION 'Store not found: %', store_id_param
            USING ERRCODE = 'invalid_parameter_value',
                  HINT = 'Verify store ID and ensure it exists in the system';
    END IF;
    
    IF NOT user_info.is_active THEN
        RAISE EXCEPTION 'Store is inactive: %', store_id_param
            USING ERRCODE = 'insufficient_privilege',
                  HINT = 'Contact administrator to activate store';
    END IF;
    
    -- Set the secure context
    PERFORM set_config('app.current_store_id', store_id_param, false);
    PERFORM set_config('app.store_name', user_info.store_name, false);
    PERFORM set_config('app.context_set_at', extract(epoch from current_timestamp)::text, false);
    
    -- Log context change for audit
    INSERT INTO retail.security_audit_log (
        event_type,
        user_name,
        store_id,
        ip_address,
        user_agent,
        details,
        severity
    ) VALUES (
        'store_context_set',
        current_user,
        store_id_param,
        inet_client_addr()::text,
        current_setting('application_name', true),
        jsonb_build_object(
            'store_name', user_info.store_name,
            'timestamp', current_timestamp,
            'session_id', pg_backend_pid()
        ),
        'INFO'
    );
END;
$$;

-- Grant execute to MCP user
GRANT EXECUTE ON FUNCTION retail.set_store_context TO mcp_user;
```

### គោលការណ៍ RLS

```sql
-- Customers RLS Policy
CREATE POLICY customers_store_isolation ON retail.customers
    FOR ALL
    TO mcp_user
    USING (
        store_id = current_setting('app.current_store_id', true)
        AND current_setting('app.current_store_id', true) IS NOT NULL
        AND current_setting('app.current_store_id', true) != ''
    )
    WITH CHECK (
        store_id = current_setting('app.current_store_id', true)
        AND current_setting('app.current_store_id', true) IS NOT NULL
        AND current_setting('app.current_store_id', true) != ''
    );

-- Products RLS Policy with additional business rules
CREATE POLICY products_store_isolation ON retail.products
    FOR ALL
    TO mcp_user
    USING (
        store_id = current_setting('app.current_store_id', true)
        AND current_setting('app.current_store_id', true) IS NOT NULL
        AND current_setting('app.current_store_id', true) != ''
        AND is_active = TRUE  -- Additional business rule
    )
    WITH CHECK (
        store_id = current_setting('app.current_store_id', true)
        AND current_setting('app.current_store_id', true) IS NOT NULL
        AND current_setting('app.current_store_id', true) != ''
    );

-- Sales Transactions RLS Policy
CREATE POLICY sales_transactions_store_isolation ON retail.sales_transactions
    FOR ALL
    TO mcp_user
    USING (
        store_id = current_setting('app.current_store_id', true)
        AND current_setting('app.current_store_id', true) IS NOT NULL
        AND current_setting('app.current_store_id', true) != ''
    )
    WITH CHECK (
        store_id = current_setting('app.current_store_id', true)
        AND current_setting('app.current_store_id', true) IS NOT NULL
        AND current_setting('app.current_store_id', true) != ''
    );

-- Transaction Items RLS Policy (via join)
CREATE POLICY sales_transaction_items_store_isolation ON retail.sales_transaction_items
    FOR ALL
    TO mcp_user
    USING (
        transaction_id IN (
            SELECT transaction_id 
            FROM retail.sales_transactions 
            WHERE store_id = current_setting('app.current_store_id', true)
        )
    )
    WITH CHECK (
        transaction_id IN (
            SELECT transaction_id 
            FROM retail.sales_transactions 
            WHERE store_id = current_setting('app.current_store_id', true)
        )
    );

-- Product Embeddings RLS Policy
CREATE POLICY product_embeddings_store_isolation ON retail.product_embeddings
    FOR ALL
    TO mcp_user
    USING (
        store_id = current_setting('app.current_store_id', true)
        AND current_setting('app.current_store_id', true) IS NOT NULL
        AND current_setting('app.current_store_id', true) != ''
    )
    WITH CHECK (
        store_id = current_setting('app.current_store_id', true)
        AND current_setting('app.current_store_id', true) IS NOT NULL
        AND current_setting('app.current_store_id', true) != ''
    );
```

### ការធ្វើតេស្ត និងផ្ទៀងផ្ទាត់ RLS

```sql
-- Test RLS policies with different store contexts
DO $$
DECLARE
    test_result RECORD;
    customer_count INTEGER;
    product_count INTEGER;
BEGIN
    -- Test Seattle store context
    PERFORM retail.set_store_context('seattle');
    
    SELECT COUNT(*) INTO customer_count FROM retail.customers;
    SELECT COUNT(*) INTO product_count FROM retail.products;
    
    RAISE NOTICE 'Seattle store - Customers: %, Products: %', customer_count, product_count;
    
    -- Test Redmond store context
    PERFORM retail.set_store_context('redmond');
    
    SELECT COUNT(*) INTO customer_count FROM retail.customers;
    SELECT COUNT(*) INTO product_count FROM retail.products;
    
    RAISE NOTICE 'Redmond store - Customers: %, Products: %', customer_count, product_count;
    
    -- Verify data isolation
    IF customer_count > 0 AND product_count > 0 THEN
        RAISE NOTICE 'RLS policies are working correctly';
    ELSE
        RAISE WARNING 'RLS policies may not be configured correctly';
    END IF;
END;
$$;
```

## 🔑 ការផ្ទៀងផ្ទាត់អត្តសញ្ញាណ និងអនុញ្ញាតកម្ម

### ការរួមបញ្ចូល Azure Entra ID

```python
# mcp_server/security/authentication.py
"""
Azure Entra ID authentication for MCP server.
"""
import os
import jwt
import aiohttp
import asyncio
from typing import Dict, Optional, List
from datetime import datetime, timezone
from azure.identity.aio import DefaultAzureCredential
from azure.keyvault.secrets.aio import SecretClient
import logging

logger = logging.getLogger(__name__)

class AzureAuthenticator:
    """Handle Azure Entra ID authentication and token validation."""
    
    def __init__(self):
        self.tenant_id = os.getenv('AZURE_TENANT_ID')
        self.client_id = os.getenv('AZURE_CLIENT_ID')
        self.audience = os.getenv('AZURE_AUDIENCE', self.client_id)
        self.issuer = f"https://login.microsoftonline.com/{self.tenant_id}/v2.0"
        
        # កែច់សម្រាប់ JWKS (JSON Web Key Set)
        self._jwks_cache = None
        self._jwks_cache_expiry = None
        
        # តុរកម្មសម្រាប់សម្ងាត់
        self.key_vault_url = os.getenv('AZURE_KEY_VAULT_URL')
        self.credential = DefaultAzureCredential()
        
        if self.key_vault_url:
            self.secret_client = SecretClient(
                vault_url=self.key_vault_url,
                credential=self.credential
            )
    
    async def validate_token(self, token: str) -> Dict:
        """Validate JWT token from Azure Entra ID."""
        
        try:
            # ទទួលបានកូនសោសម្រាប់ចុះហត្ថលេខា
            signing_keys = await self._get_signing_keys()
            
            # វាយបកខ្នងតូដែលដើម្បីទទួលបានអត្តសញ្ញាណកូនសោ
            unverified_header = jwt.get_unverified_header(token)
            key_id = unverified_header.get('kid')
            
            if not key_id:
                raise ValueError("Token missing key ID")
            
            # ស្វែងរកកូនសោដែលសមរម្យ
            signing_key = None
            for key in signing_keys:
                if key['kid'] == key_id:
                    signing_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
                    break
            
            if not signing_key:
                raise ValueError(f"Unable to find signing key for kid: {key_id}")
            
            # ផ្ទៀងផ្ទាត់ និងវាយបកតូដែល
            payload = jwt.decode(
                token,
                signing_key,
                algorithms=['RS256'],
                audience=self.audience,
                issuer=self.issuer,
                options={
                    'verify_exp': True,
                    'verify_aud': True,
                    'verify_iss': True
                }
            )
            
            # ដកយកព័ត៌មានអ្នកប្រើ
            user_info = self._extract_user_info(payload)
            
            # កត់ត្រាការផ្ទៀងផ្ទាត់ជោគជ័យ
            logger.info(
                "User authenticated successfully",
                extra={
                    'user_id': user_info['user_id'],
                    'email': user_info.get('email'),
                    'tenant_id': payload.get('tid')
                }
            )
            
            return user_info
            
        except jwt.ExpiredSignatureError:
            logger.warning("Token has expired")
            raise ValueError("Token has expired")
        except jwt.InvalidAudienceError:
            logger.warning(f"Invalid audience in token. Expected: {self.audience}")
            raise ValueError("Invalid token audience")
        except jwt.InvalidIssuerError:
            logger.warning(f"Invalid issuer in token. Expected: {self.issuer}")
            raise ValueError("Invalid token issuer")
        except Exception as e:
            logger.error(f"Token validation failed: {str(e)}")
            raise ValueError(f"Token validation failed: {str(e)}")
    
    async def _get_signing_keys(self) -> List[Dict]:
        """Get JWKS from Azure Entra ID with caching."""
        
        current_time = datetime.now(timezone.utc)
        
        # ពិនិត្យមើលថាគែច់ត្រឹមត្រូវរឺទេ
        if (self._jwks_cache and self._jwks_cache_expiry and 
            current_time < self._jwks_cache_expiry):
            return self._jwks_cache
        
        # ទាញយក JWKS ថ្មី
        jwks_url = f"{self.issuer}/keys"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(jwks_url) as response:
                if response.status != 200:
                    raise Exception(f"Failed to fetch JWKS: {response.status}")
                
                jwks_data = await response.json()
                
        # កែច់សម្រាប់មួយម៉ោង
        self._jwks_cache = jwks_data['keys']
        self._jwks_cache_expiry = current_time.replace(
            hour=current_time.hour + 1
        )
        
        return self._jwks_cache
    
    def _extract_user_info(self, payload: Dict) -> Dict:
        """Extract user information from JWT payload."""
        
        return {
            'user_id': payload.get('oid') or payload.get('sub'),
            'email': payload.get('email') or payload.get('preferred_username'),
            'name': payload.get('name'),
            'tenant_id': payload.get('tid'),
            'roles': payload.get('roles', []),
            'groups': payload.get('groups', []),
            'app_roles': payload.get('app_roles', []),
            'scope': payload.get('scp', '').split() if payload.get('scp') else [],
            'expires_at': datetime.fromtimestamp(payload['exp'], timezone.utc),
            'issued_at': datetime.fromtimestamp(payload['iat'], timezone.utc)
        }
    
    async def get_user_store_access(self, user_id: str) -> List[str]:
        """Get list of stores the user has access to."""
        
        try:
            # នេះជាទូទៅដើម្បីសួរសំណួរពីការចងក្រងអ្នកប្រើ/ហាងរបស់អ្នក
            # សម្រាប់ករណីសាកល្បង យើងនឹងប្រើសម្ងាត់តូចមួយក្នុងតុរកម្មសោ
            secret_name = f"user-{user_id}-stores"
            
            if self.secret_client:
                secret = await self.secret_client.get_secret(secret_name)
                store_list = secret.value.split(',')
                return [store.strip() for store in store_list if store.strip()]
            
            # ជម្រើសបញ្ចេញ: ត្រឡប់ការចូលហាងលំនាំដើម
            logger.warning(f"No store mapping found for user {user_id}, using default")
            return ['seattle']  # ការចូលហាងលំនាំដើម
            
        except Exception as e:
            logger.error(f"Failed to get store access for user {user_id}: {e}")
            return []  # គ្មានការចូលប្រើប្រសិនបើយើងមិនអាចកំណត់ហាងបាន

# វត្ថុប្រើប្រាស់អ្នកផ្ទៀងផ្ទាត់លើកលែងសកល
azure_authenticator = AzureAuthenticator()
```

### Middleware អនុញ្ញាតកម្ម

```python
# mcp_server/security/authorization.py
"""
Authorization middleware and decorators for MCP server.
"""
import functools
from typing import Dict, List, Optional, Callable, Any
from fastapi import HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import logging

logger = logging.getLogger(__name__)

security = HTTPBearer()

class AuthorizationError(Exception):
    """Custom authorization error."""
    pass

class RoleBasedAuth:
    """Role-based access control implementation."""
    
    # កំណត់ជួរដឹកនាំតួនាទី
    ROLE_HIERARCHY = {
        'store_admin': ['store_manager', 'store_user', 'store_readonly'],
        'store_manager': ['store_user', 'store_readonly'],
        'store_user': ['store_readonly'],
        'store_readonly': []
    }
    
    # កំណត់សិទ្ធិសម្រាប់តួនាទីមួយៗ
    ROLE_PERMISSIONS = {
        'store_admin': [
            'read_all', 'write_all', 'delete_all', 'manage_users'
        ],
        'store_manager': [
            'read_all', 'write_transactions', 'write_inventory', 'read_reports'
        ],
        'store_user': [
            'read_products', 'read_customers', 'write_transactions'
        ],
        'store_readonly': [
            'read_products', 'read_basic_reports'
        ]
    }
    
    @classmethod
    def has_permission(cls, user_roles: List[str], required_permission: str) -> bool:
        """Check if user has required permission."""
        
        user_permissions = set()
        
        for role in user_roles:
            # បន្ថែមសិទិ្ធដោយផ្ទាល់
            user_permissions.update(cls.ROLE_PERMISSIONS.get(role, []))
            
            # បន្ថែមសិទិ្ធដែលទទួលបានពីម្តាយ
            inherited_roles = cls.ROLE_HIERARCHY.get(role, [])
            for inherited_role in inherited_roles:
                user_permissions.update(cls.ROLE_PERMISSIONS.get(inherited_role, []))
        
        return required_permission in user_permissions
    
    @classmethod
    def get_user_stores(cls, user_info: Dict) -> List[str]:
        """Extract stores user has access to from user info."""
        
        # នេះធម្មតានឹងមកពីប្រព័ន្ធគ្រប់គ្រងអ្នកប្រើរបស់អ្នក
        # សម្រាប់សាកល្បង យើងនឹងដកស្រង់ពីការអះអាងលំនាំផ្ទាល់ខ្លួនឬក្រុម
        
        stores = []
        
        # ពិនិត្យការចាត់ចែងហាងដោយផ្ទាល់ក្នុងក្រុម
        for group in user_info.get('groups', []):
            if group.startswith('store_'):
                store_id = group.replace('store_', '')
                stores.append(store_id)
        
        # ពិនិត្យតួនាទីពាក់ព័ន្ធកម្មវិធី
        for role in user_info.get('app_roles', []):
            if 'store:' in role:
                _, store_id = role.split('store:', 1)
                stores.append(store_id)
        
        return list(set(stores))  # លុបចោលការចម្លង

def require_auth(required_permission: str = None, require_store_access: bool = True):
    """Decorator to require authentication and authorization."""
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # ដកយកការស្នើសុំពី args (ការInjectពឹងផ្អែកFastAPI)
            request = None
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break
            
            if not request:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Request object not found"
                )
            
            # ទទួលបានក្បាលអតិថិជនសម្ងាត់
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Missing or invalid authorization header",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            
            token = auth_header.split(' ')[1]
            
            try:
                # ត្រួតពិនិត្យសញ្ញាបត្រ
                user_info = await azure_authenticator.validate_token(token)
                
                # ពិនិត្យសិទ្ធិចាំបាច់
                if required_permission:
                    user_roles = user_info.get('roles', [])
                    if not RoleBasedAuth.has_permission(user_roles, required_permission):
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Insufficient permissions. Required: {required_permission}"
                        )
                
                # ពិនិត្យការចូលដំណើរការហាង
                if require_store_access:
                    user_stores = RoleBasedAuth.get_user_stores(user_info)
                    if not user_stores:
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail="No store access configured for user"
                        )
                    
                    # កំណត់បរិបទហាងលំនាំដើម (ហាងដំបូងដែលចូលដំណើរការ)
                    request.state.current_store = user_stores[0]
                    request.state.accessible_stores = user_stores
                
                # បន្ថែមព័ត៌មានអ្នកប្រើទៅស្ថានភាពស្នើសុំ
                request.state.user_info = user_info
                request.state.user_id = user_info['user_id']
                
                # ហៅមុខងារដើម
                return await func(*args, **kwargs)
                
            except ValueError as e:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=str(e),
                    headers={"WWW-Authenticate": "Bearer"}
                )
            except AuthorizationError as e:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=str(e)
                )
        
        return wrapper
    return decorator

def require_store_context(store_param: str = 'store_id'):
    """Decorator to validate and set store context."""
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # ទទួល store_id ពី kwargs
            store_id = kwargs.get(store_param)
            
            if not store_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Missing required parameter: {store_param}"
                )
            
            # ដកស្រង់សំណើពី args
            request = None
            for arg in args:
                if isinstance(arg, Request):
                    request = arg
                    break
            
            if not request or not hasattr(request.state, 'accessible_stores'):
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Authentication required before store context validation"
                )
            
            # ត្រួតពិនិត្យអ្នកប្រើមានការចូលដំណើរការហាងដែលបានស្នើសុំដែរឬទេ
            if store_id not in request.state.accessible_stores:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Access denied to store: {store_id}"
                )
            
            # កំណត់បរិបទហាងនៅក្នុងស្ថានភាពស្នើសុំ
            request.state.current_store = store_id
            
            return await func(*args, **kwargs)
        
        return wrapper
    return decorator
```

## 🔍 ការត្រួតពិនិត្យ និងអនុលោមសុវត្ថិភាព

### កំណត់ហេតុ Audit ទូលំទូលាយ

```sql
-- Security audit log table
CREATE TABLE retail.security_audit_log (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_type VARCHAR(100) NOT NULL,
    user_name VARCHAR(100) NOT NULL,
    user_id VARCHAR(100),
    store_id VARCHAR(50),
    ip_address INET,
    user_agent TEXT,
    request_id VARCHAR(100),
    session_id VARCHAR(100),
    resource_type VARCHAR(100),
    resource_id VARCHAR(100),
    action VARCHAR(50) NOT NULL,
    success BOOLEAN NOT NULL DEFAULT TRUE,
    failure_reason TEXT,
    details JSONB,
    severity VARCHAR(20) DEFAULT 'INFO',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Ensure proper indexing for security queries
    CONSTRAINT valid_severity CHECK (severity IN ('DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'))
);

-- Indexes for security audit queries
CREATE INDEX idx_security_audit_event_type ON retail.security_audit_log(event_type);
CREATE INDEX idx_security_audit_user_name ON retail.security_audit_log(user_name);
CREATE INDEX idx_security_audit_store_id ON retail.security_audit_log(store_id);
CREATE INDEX idx_security_audit_created_at ON retail.security_audit_log(created_at);
CREATE INDEX idx_security_audit_success ON retail.security_audit_log(success);
CREATE INDEX idx_security_audit_severity ON retail.security_audit_log(severity);
CREATE INDEX idx_security_audit_details ON retail.security_audit_log USING GIN(details);

-- Function to log security events
CREATE OR REPLACE FUNCTION retail.log_security_event(
    p_event_type VARCHAR(100),
    p_user_name VARCHAR(100),
    p_user_id VARCHAR(100) DEFAULT NULL,
    p_store_id VARCHAR(50) DEFAULT NULL,
    p_ip_address TEXT DEFAULT NULL,
    p_action VARCHAR(50) DEFAULT 'unknown',
    p_success BOOLEAN DEFAULT TRUE,
    p_failure_reason TEXT DEFAULT NULL,
    p_details JSONB DEFAULT NULL,
    p_severity VARCHAR(20) DEFAULT 'INFO'
)
RETURNS UUID
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
DECLARE
    log_id UUID;
BEGIN
    INSERT INTO retail.security_audit_log (
        event_type,
        user_name,
        user_id,
        store_id,
        ip_address,
        action,
        success,
        failure_reason,
        details,
        severity
    ) VALUES (
        p_event_type,
        p_user_name,
        p_user_id,
        p_store_id,
        p_ip_address::INET,
        p_action,
        p_success,
        p_failure_reason,
        p_details,
        p_severity
    ) RETURNING log_id INTO log_id;
    
    RETURN log_id;
END;
$$;

-- Grant execute to MCP user
GRANT EXECUTE ON FUNCTION retail.log_security_event TO mcp_user;
```

### ទិដ្ឋភាពត្រួតពិនិត្យសុវត្ថិភាព

```sql
-- Failed authentication attempts
CREATE VIEW retail.security_failed_auth AS
SELECT 
    event_type,
    user_name,
    ip_address,
    COUNT(*) as attempt_count,
    MIN(created_at) as first_attempt,
    MAX(created_at) as last_attempt,
    ARRAY_AGG(DISTINCT failure_reason) as failure_reasons
FROM retail.security_audit_log
WHERE success = FALSE 
  AND event_type IN ('authentication_failed', 'token_validation_failed')
  AND created_at >= CURRENT_TIMESTAMP - INTERVAL '24 hours'
GROUP BY event_type, user_name, ip_address
HAVING COUNT(*) >= 3  -- 3 or more failures
ORDER BY attempt_count DESC, last_attempt DESC;

-- Suspicious access patterns
CREATE VIEW retail.security_suspicious_access AS
SELECT 
    user_name,
    user_id,
    COUNT(DISTINCT ip_address) as ip_count,
    COUNT(DISTINCT store_id) as store_count,
    ARRAY_AGG(DISTINCT ip_address::TEXT) as ip_addresses,
    ARRAY_AGG(DISTINCT store_id) as stores_accessed,
    MIN(created_at) as first_access,
    MAX(created_at) as last_access
FROM retail.security_audit_log
WHERE created_at >= CURRENT_TIMESTAMP - INTERVAL '1 hour'
  AND success = TRUE
GROUP BY user_name, user_id
HAVING COUNT(DISTINCT ip_address) > 3  -- Access from multiple IPs
   OR COUNT(DISTINCT store_id) > 2     -- Access to multiple stores
ORDER BY ip_count DESC, store_count DESC;

-- Data access patterns
CREATE VIEW retail.security_data_access_summary AS
SELECT 
    DATE_TRUNC('hour', created_at) as access_hour,
    store_id,
    resource_type,
    action,
    COUNT(*) as access_count,
    COUNT(DISTINCT user_id) as unique_users
FROM retail.security_audit_log
WHERE resource_type IS NOT NULL
  AND created_at >= CURRENT_TIMESTAMP - INTERVAL '24 hours'
GROUP BY DATE_TRUNC('hour', created_at), store_id, resource_type, action
ORDER BY access_hour DESC, access_count DESC;
```

### ការត្រួតពិនិត្យព្រឹត្តិការណ៍សុវត្ថិភាព

```python
# mcp_server/security/monitoring.py
"""
Security monitoring and alerting for MCP server.
"""
import asyncio
import asyncpg
from typing import Dict, List, Any
from datetime import datetime, timedelta
from dataclasses import dataclass
import logging

logger = logging.getLogger(__name__)

@dataclass
class SecurityAlert:
    """Security alert data structure."""
    alert_type: str
    severity: str
    message: str
    details: Dict[str, Any]
    timestamp: datetime

class SecurityMonitor:
    """Monitor security events and generate alerts."""
    
    def __init__(self, db_connection_string: str):
        self.db_connection_string = db_connection_string
        self.alert_handlers = []
        
        # កម្រិតការព្រមាន
        self.thresholds = {
            'failed_auth_attempts': 5,      # តាមអ្នកប្រើប្រាស់មួយម្នាក់ក្នុងមួយម៉ោង
            'multiple_ip_access': 3,        # អាសយដ្ឋាន IP ផ្សេងៗតាមអ្នកប្រើប្រាស់មួយក្នុងមួយម៉ោង
            'excessive_data_access': 1000,  # សំណួរតាមអ្នកប្រើប្រាស់មួយក្នុងមួយម៉ោង
            'privilege_escalation': 1,      # ការឧ្យាយាមណាមួយ
            'unauthorized_store_access': 1  # ការឧ្យាយាមណាមួយ
        }
    
    async def start_monitoring(self):
        """Start security monitoring loop."""
        logger.info("Starting security monitoring")
        
        while True:
            try:
                await self._check_security_events()
                await asyncio.sleep(300)  # ពិនិត្យរៀងរាល់ ៥ នាទី
            except Exception as e:
                logger.error(f"Security monitoring error: {e}")
                await asyncio.sleep(60)  # សាកល្បងឡើងវិញយ៉ាងខ្លីនៅពេលមានកំហុស
    
    async def _check_security_events(self):
        """Check for security events and generate alerts."""
        
        conn = await asyncpg.connect(self.db_connection_string)
        
        try:
            # ពិនិត្យការឧ្យាយាមអះអាងកំណត់អត្តសញ្ញាណដែលបរាជ័យ
            await self._check_failed_auth(conn)
            
            # ពិនិត្យលំនាំចូលដែលគួរឲ្យសងងឹត
            await self._check_suspicious_access(conn)
            
            # ពិនិត្យអាសយដ្ឋានទិន្នន័យដែលមានភាពច្របូកច្របល់
            await self._check_data_access_anomalies(conn)
            
            # ពិនិត្យការឧ្យាយាមចូលដោយគ្មានសិទ្ធិ
            await self._check_unauthorized_access(conn)
            
        finally:
            await conn.close()
    
    async def _check_failed_auth(self, conn):
        """Check for excessive failed authentication attempts."""
        
        query = """
        SELECT 
            user_name,
            ip_address,
            COUNT(*) as attempt_count,
            MAX(created_at) as last_attempt
        FROM retail.security_audit_log
        WHERE success = FALSE 
          AND event_type IN ('authentication_failed', 'token_validation_failed')
          AND created_at >= CURRENT_TIMESTAMP - INTERVAL '1 hour'
        GROUP BY user_name, ip_address
        HAVING COUNT(*) >= $1
        """
        
        results = await conn.fetch(query, self.thresholds['failed_auth_attempts'])
        
        for record in results:
            alert = SecurityAlert(
                alert_type='failed_authentication',
                severity='HIGH',
                message=f"Excessive failed login attempts for user {record['user_name']}",
                details={
                    'user_name': record['user_name'],
                    'ip_address': str(record['ip_address']),
                    'attempt_count': record['attempt_count'],
                    'last_attempt': record['last_attempt'].isoformat()
                },
                timestamp=datetime.now()
            )
            
            await self._send_alert(alert)
    
    async def _check_suspicious_access(self, conn):
        """Check for suspicious access patterns."""
        
        query = """
        SELECT 
            user_name,
            user_id,
            COUNT(DISTINCT ip_address) as ip_count,
            ARRAY_AGG(DISTINCT ip_address::TEXT) as ip_addresses
        FROM retail.security_audit_log
        WHERE created_at >= CURRENT_TIMESTAMP - INTERVAL '1 hour'
          AND success = TRUE
        GROUP BY user_name, user_id
        HAVING COUNT(DISTINCT ip_address) >= $1
        """
        
        results = await conn.fetch(query, self.thresholds['multiple_ip_access'])
        
        for record in results:
            alert = SecurityAlert(
                alert_type='suspicious_access',
                severity='MEDIUM',
                message=f"User {record['user_name']} accessed from multiple IP addresses",
                details={
                    'user_name': record['user_name'],
                    'user_id': record['user_id'],
                    'ip_count': record['ip_count'],
                    'ip_addresses': record['ip_addresses']
                },
                timestamp=datetime.now()
            )
            
            await self._send_alert(alert)
    
    async def _check_unauthorized_access(self, conn):
        """Check for unauthorized store access attempts."""
        
        query = """
        SELECT 
            user_name,
            user_id,
            store_id,
            failure_reason,
            created_at
        FROM retail.security_audit_log
        WHERE success = FALSE 
          AND event_type = 'unauthorized_store_access'
          AND created_at >= CURRENT_TIMESTAMP - INTERVAL '1 hour'
        """
        
        results = await conn.fetch(query)
        
        for record in results:
            alert = SecurityAlert(
                alert_type='unauthorized_access',
                severity='HIGH',
                message=f"Unauthorized store access attempt by {record['user_name']}",
                details={
                    'user_name': record['user_name'],
                    'user_id': record['user_id'],
                    'store_id': record['store_id'],
                    'failure_reason': record['failure_reason'],
                    'timestamp': record['created_at'].isoformat()
                },
                timestamp=datetime.now()
            )
            
            await self._send_alert(alert)
    
    async def _send_alert(self, alert: SecurityAlert):
        """Send security alert to all configured handlers."""
        
        logger.warning(
            f"Security Alert: {alert.alert_type} - {alert.message}",
            extra={'alert_details': alert.details}
        )
        
        # ส่งទៅដល់អ្នកទទួលជូនសារព្រមានដែលបានកំណត់
        for handler in self.alert_handlers:
            try:
                await handler.send_alert(alert)
            except Exception as e:
                logger.error(f"Failed to send alert via {handler.__class__.__name__}: {e}")
    
    def add_alert_handler(self, handler):
        """Add alert handler."""
        self.alert_handlers.append(handler)
```

## 🧪 ការធ្វើតេស្ត និងផ្ទៀងផ្ទាត់សុវត្ថិភាព

### ការធ្វើតេស្តសុវត្ថិភាពស្វ័យប្រវត្តិ

```python
# tests/security/test_security.py
"""
Comprehensive security tests for MCP server.
"""
import pytest
import asyncio
import asyncpg
from datetime import datetime, timezone
import jwt
from unittest.mock import Mock, patch

class TestRowLevelSecurity:
    """Test Row Level Security implementation."""
    
    @pytest.fixture
    async def db_connection(self):
        """Database connection for testing."""
        conn = await asyncpg.connect(
            "postgresql://mcp_user:password@localhost:5432/retail_test"
        )
        yield conn
        await conn.close()
    
    async def test_store_context_isolation(self, db_connection):
        """Test that RLS properly isolates data by store."""
        
        # កំណត់បរិបទហាង Seattle
        await db_connection.execute("SELECT retail.set_store_context('seattle')")
        
        # ទទួលបានចំនួនអតិថិជន
        seattle_customers = await db_connection.fetchval(
            "SELECT COUNT(*) FROM retail.customers"
        )
        
        # កំណត់បរិបទហាង Redmond
        await db_connection.execute("SELECT retail.set_store_context('redmond')")
        
        # ទទួលបានចំនួនអតិថិជន
        redmond_customers = await db_connection.fetchval(
            "SELECT COUNT(*) FROM retail.customers"
        )
        
        # ផ្ទៀងផ្ទាត់ការបំបែក (ចំនួនគួរតែខុសគ្នា)
        assert seattle_customers != redmond_customers or (
            seattle_customers == 0 and redmond_customers == 0
        )
    
    async def test_unauthorized_store_access(self, db_connection):
        """Test that invalid store access is blocked."""
        
        with pytest.raises(Exception) as exc_info:
            await db_connection.execute("SELECT retail.set_store_context('invalid_store')")
        
        assert "Store not found" in str(exc_info.value)
    
    async def test_cross_store_data_leakage(self, db_connection):
        """Test that users cannot access data from other stores."""
        
        # កំណត់បរិបទទៅហាងមួយ
        await db_connection.execute("SELECT retail.set_store_context('seattle')")
        
        # ព្យាយាមបញ្ចូលទិន្នន័យជាមួយ store_id ផ្សេង
        with pytest.raises(Exception):
            await db_connection.execute("""
                INSERT INTO retail.customers (store_id, first_name, last_name, email)
                VALUES ('redmond', 'Test', 'User', 'test@example.com')
            """)

class TestAuthentication:
    """Test authentication and authorization."""
    
    def test_valid_jwt_token(self):
        """Test valid JWT token validation."""
        
        # បង្កើតសញ្ញា Token ដែលត្រឹមត្រូវ
        token_payload = {
            'oid': 'user-123',
            'email': 'test@example.com',
            'name': 'Test User',
            'tid': 'tenant-123',
            'aud': 'app-client-id',
            'iss': 'https://login.microsoftonline.com/tenant-123/v2.0',
            'exp': int((datetime.now(timezone.utc)).timestamp()) + 3600,
            'iat': int((datetime.now(timezone.utc)).timestamp()),
            'roles': ['store_user']
        }
        
        # នេះតម្រូវឱ្យបង្កើតម៉ូកចង្អុល JWKS
        # ក្នុងការអនុវត្តពិត ប្រើ token JWT សម្រាប់ធ្វើតេស្តបានត្រឹមត្រូវ
        
    def test_expired_token_rejection(self):
        """Test that expired tokens are rejected."""
        
        token_payload = {
            'oid': 'user-123',
            'exp': int((datetime.now(timezone.utc)).timestamp()) - 3600,  # បានផុតកំណត់
            'iat': int((datetime.now(timezone.utc)).timestamp()) - 7200
        }
        
        # តេស្តនេះនឹងផ្ទៀងផ្ទាត់ថា token បានផុតកំណត់ត្រូវបានបដិសេធ
        
    def test_invalid_audience_rejection(self):
        """Test that tokens with wrong audience are rejected."""
        
        token_payload = {
            'oid': 'user-123',
            'aud': 'wrong-audience',  # ការព្រមទទួលមិនត្រឹមត្រូវ
            'exp': int((datetime.now(timezone.utc)).timestamp()) + 3600,
            'iat': int((datetime.now(timezone.utc)).timestamp())
        }
        
        # តេស្តនេះនឹងផ្ទៀងផ្ទាត់ថា token ជាមួយការព្រមទទួលខុសត្រូវបានបដិសេធ

class TestAuthorization:
    """Test role-based authorization."""
    
    def test_role_hierarchy(self):
        """Test that role hierarchy works correctly."""
        
        from mcp_server.security.authorization import RoleBasedAuth
        
        # អ្នកគ្រប់គ្រងហាងគួរតែមានសិទ្ធិពេញលេញ
        assert RoleBasedAuth.has_permission(['store_admin'], 'read_all')
        assert RoleBasedAuth.has_permission(['store_admin'], 'write_all')
        assert RoleBasedAuth.has_permission(['store_admin'], 'delete_all')
        
        # អ្នកប្រើហាងគួរតែមានសិទ្ធិសមរម្យ
        assert RoleBasedAuth.has_permission(['store_user'], 'read_products')
        assert not RoleBasedAuth.has_permission(['store_user'], 'delete_all')
        
        # អ្នកអានតែមានសិទ្ធិគ្មានច្រើន
        assert RoleBasedAuth.has_permission(['store_readonly'], 'read_products')
        assert not RoleBasedAuth.has_permission(['store_readonly'], 'write_transactions')
    
    def test_permission_inheritance(self):
        """Test that permissions are properly inherited."""
        
        from mcp_server.security.authorization import RoleBasedAuth
        
        # អ្នកគ្រប់គ្រងគួរតែទទួលសិទ្ធិអ្នកប្រើ
        assert RoleBasedAuth.has_permission(['store_manager'], 'read_products')
        assert RoleBasedAuth.has_permission(['store_manager'], 'write_transactions')

# អ្នកដំណើរការតេស្តសន្តិសុខ
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

### បញ្ជីត្រួតពិនិត្យការវាយប្រហារ

```yaml
# security-test-checklist.yml
penetration_testing:
  
  authentication_bypass:
    - name: "Test authentication bypass attempts"
      tests:
        - "Missing Authorization header"
        - "Malformed JWT tokens"
        - "Replay attack with expired tokens"
        - "Token signature manipulation"
        - "Audience/issuer manipulation"
    
  authorization_escalation:
    - name: "Test privilege escalation attempts"
      tests:
        - "Role manipulation in token"
        - "Store access boundary testing"
        - "Cross-tenant data access attempts"
        - "Administrative function access"
    
  sql_injection:
    - name: "Test SQL injection vulnerabilities"
      tests:
        - "Parameter injection in search queries"
        - "Store ID manipulation"
        - "JSON parameter injection"
        - "Union-based injection attempts"
    
  data_exposure:
    - name: "Test for data exposure vulnerabilities"
      tests:
        - "Error message information disclosure"
        - "Timing attack possibilities"
        - "Cross-store data leakage"
        - "Audit log exposure"
    
  rate_limiting:
    - name: "Test rate limiting and DoS protection"
      tests:
        - "Authentication endpoint flooding"
        - "API endpoint rate limits"
        - "Resource exhaustion attempts"
        - "Connection pool exhaustion"
```

## 🎯 សេចក្ដីទាញយកសំខាន់ៗ

បន្ទាប់ពីបញ្ចប់មូលដ្ឋាននេះ អ្នកគួរតែមាន៖

✅ **សុវត្ថិភាពច្រើនអតិថិជន**៖ អនុវត្ត Row Level Security សម្រាប់ការបំបែកទិន្នន័យពេញលេញ  
✅ **ការផ្ទៀងផ្ទាត់ Azure**៖ រួមបញ្ចូល Azure Entra ID ជាមួយការផ្ទៀងផ្ទាត់ JWT  
✅ **អនុញ្ញាតកម្មផ្អែកលើតួនាទី**៖ កំណត់រចនាសម្ព័ន្ធតួនាទី និងសិទ្ធិជាន់ខ្ពស់  
✅ **កំណត់ហេតុ Audit ទូលំទូលាយ**៖ បង្កើតការតាមដាន និងត្រួតពិនិត្យព្រឹត្តិការណ៍សុវត្ថិភាព  
✅ **ការធ្វើតេស្តសុវត្ថិភាព**៖ អនុវត្តតេស្តផ្ទៀងផ្ទាត់សុវត្ថិភាពស្វ័យប្រវត្តិ  
✅ **ការត្រួតពិនិត្យគ្រោះថ្នាក់**៖ បង្កើតការរកឃើញ និងរំខានព្រឹត្ដិការណ៍សុវត្ថិភាពពេលវេលាពេញលេញ  

## 🚀 បន្ទាប់មក

បន្តជាមួយ **[Lab 03: Environment Setup](../03-Setup/README.md)** ដើម្បី៖

- កំណត់បរិយាកាសអភិវឌ្ឍន៍ជាមួយបទបញ្ជាសុវត្ថិភាពល្អបំផុត  
- កំណត់សេវាកម្ម Azure សម្រាប់ការផ្ទៀងផ្ទាត់ និងត្រួតពិនិត្យ  
- អនុវត្តការតភ្ជាប់មូលដ្ឋានទិន្នន័យដែលមានសុវត្ថិភាព និងការគ្រប់គ្រងអាថ៌កំបាំង  
- ផ្ទៀងផ្ទាត់ការកំណត់រចនាសម្ព័ន្ធសុវត្ថិភាពនៅបរិយាកាសអភិវឌ្ឍន៍

## 📚 ឯកសារបន្ថែម

### សុវត្ថិភាព Azure
- [ឯកសាររបស់ Azure Entra ID](https://docs.microsoft.com/azure/active-directory/) - មគ្គុទេសក៍វេទិកាអត្តសញ្ញាណពេញលេញ  
- [Azure Key Vault](https://docs.microsoft.com/azure/key-vault/) - សេវាកម្មគ្រប់គ្រងអាថ៌កំបាំង  
- [បទបញ្ជាសុវត្ថិភាពល្អបំផុតរបស់ Azure](https://docs.microsoft.com/azure/security/fundamentals/best-practices-and-patterns) - ការណែនាំសុវត្ថិភាព

### សុវត្ថិភាពមូលដ្ឋានទិន្នន័យ
- [PostgreSQL Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - ឯកសារប្រព័ន្ធ RLS ផ្លូវការណ៍  
- [បញ្ជីត្រួតពិនិត្យសុវត្ថិភាពមូលដ្ឋានទិន្នន័យ](https://www.postgresql.org/docs/current/security.html) - មគ្គុទេសក៍សុវត្ថិភាព PostgreSQL  
- [ម៉ូដែលមូលដ្ឋានទិន្នន័យច្រើនអតិថិជន](https://docs.microsoft.com/azure/architecture/patterns/multitenancy) - ម៉ូដែលស្ថាបត្យកម្ម

### ការធ្វើតេស្តសុវត្ថិភាព
- [មគ្គុទេសក៍ការធ្វើតេស្ត OWASP](https://owasp.org/www-project-web-security-testing-guide/) - ការធ្វើតេស្តសុវត្ថិភាពទូលំទូលាយ  
- [បទបញ្ជាសុវត្ថិភាព JWT](https://tools.ietf.org/html/rfc8725) - ការពិចារណាសុវត្ថិភាព JWT  
- [ការធ្វើតេស្តសុវត្ថិភាព API](https://owasp.org/www-project-api-security/) - ការធ្វើតេស្តសុវត្ថិភាពជាក់លាក់សម្រាប់ API  

---

**មុននេះ**: [Lab 01: Core Architecture Concepts](../01-Architecture/README.md)  
**បន្ទាប់**: [Lab 03: Environment Setup](../03-Setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធខ្លួន**៖  
ឯកសារនេះត្រូវបានបកប្រែដោយប្រើសេវាកម្មបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ខណៈពេលយើងខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ សូមយល់អញ្ជើញថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុសឬភាពមិនត្រឹមត្រូវខ្លះ។ ឯកសារដើមក្នុងភាសាមូលដ្ឋានគួរត្រូវបានពិចារណាជាមជ្ឈមណ្ឌលដែលមានអំណាច។ សម្រាប់ព័ត៌មានសំខាន់ៗ សូមផ្តល់អាទិភាពការបកប្រែដោយមនុស្សវិជ្ជាជីវៈ។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំឬការបកស្រាយខុសដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->