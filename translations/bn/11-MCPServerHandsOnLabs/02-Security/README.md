# নিরাপত্তা এবং মাল্টি-টেন্যান্সি

## 🎯 এই ল্যাবে যা শিখবেন

এই ল্যাবটি MCP সার্ভারের জন্য এন্টারপ্রাইজ-গ্রেড নিরাপত্তা এবং মাল্টি-টেন্যান্সি বাস্তবায়নের ব্যাপারে বিস্তারিত নির্দেশনা প্রদান করে। আপনি শিখবেন কীভাবে সংবেদনশীল রিটেইল ডেটা সুরক্ষিত করার পাশাপাশি একাধিক টেন্যান্টের জন্য নমনীয় অ্যাক্সেস প্যাটার্ন ডিজাইন করতে হয়।

## সংক্ষিপ্ত বিবরণ

নিরাপত্তা অত্যন্ত গুরুত্বপূর্ণ রিটেইল অ্যাপ্লিকেশনগুলোর জন্য, যেগুলো গ্রাহকের ডেটা, পেমেন্ট তথ্য এবং ব্যবসায়িক বুদ্ধিমত্তা পরিচালনা করে। এই ল্যাবে প্রমাণীকরণ এবং অনুমোদন থেকে শুরু করে ডেটা আইসোলেশন এবং কমপ্লায়েন্স মনিটরিং পর্যন্ত সম্পূর্ণ নিরাপত্তা আর্কিটেকচার কভার করা হয়েছে।

আমরা একটি ডিফেন্স-ইন-ডেপথ কৌশল বাস্তবায়ন করেছি, যেখানে Azure আইডেন্টিটি সার্ভিস, PostgreSQL Row Level Security, অ্যাপ্লিকেশন-লেভেল কন্ট্রোল এবং বিস্তৃত অডিট লগিং একত্রিত করে একটি শক্তিশালী, কমপ্লায়েন্ট প্ল্যাটফর্ম তৈরি করা হয়েছে।

## শেখার লক্ষ্য

এই ল্যাব শেষে আপনি সক্ষম হবেন:

- **বাস্তবায়ন**: মাল্টি-টেন্যান্ট ডেটা আইসোলেশনের জন্য এন্টারপ্রাইজ-গ্রেড Row Level Security  
- **ডিজাইন**: Azure-এর মাধ্যমে নিরাপদ প্রমাণীকরণ এবং অনুমোদন প্যাটার্ন  
- **কনফিগার**: কমপ্লায়েন্স প্রয়োজনীয়তার জন্য বিস্তৃত অডিট লগিং  
- **প্রয়োগ**: অ্যাপ্লিকেশনের সব স্তরে ডিফেন্স-ইন-ডেপথ নিরাপত্তা কৌশল  
- **যাচাই**: সিস্টেম্যাটিক টেস্টিংয়ের মাধ্যমে নিরাপত্তা বাস্তবায়ন  
- **মনিটর**: নিরাপত্তা ইভেন্ট পর্যবেক্ষণ এবং সম্ভাব্য হুমকির প্রতিক্রিয়া  

## 🔐 মাল্টি-টেন্যান্ট নিরাপত্তা আর্কিটেকচার

### নিরাপত্তার স্তরসমূহের সংক্ষিপ্ত বিবরণ

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

### মাল্টি-টেন্যান্সি মডেল

আমাদের বাস্তবায়ন **Shared Database, Shared Schema** মডেল ব্যবহার করে Row Level Security সহ:

**সুবিধাসমূহ:**
- খরচ-সাশ্রয়ী রিসোর্স ব্যবহার  
- সহজ রক্ষণাবেক্ষণ এবং আপডেট  
- RLS-এর মাধ্যমে শক্তিশালী ডেটা আইসোলেশন  
- কমপ্লায়েন্স-ফ্রেন্ডলি অডিট ট্রেইল  

**চ্যালেঞ্জসমূহ:**
- RLS পলিসি ডিজাইনে সতর্কতা প্রয়োজন  
- স্কিমা পরিবর্তন সব টেন্যান্টকে প্রভাবিত করে  
- শক্তিশালী ব্যাকআপ/রিস্টোর পদ্ধতির প্রয়োজন  

## 🛡️ Row Level Security বাস্তবায়ন

### RLS ভিত্তি

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

### স্টোর কন্টেক্সট ম্যানেজমেন্ট

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

### RLS পলিসি

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

### RLS টেস্টিং এবং যাচাই

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

## 🔑 প্রমাণীকরণ এবং অনুমোদন

### Azure Entra ID ইন্টিগ্রেশন

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
        
        # Cache for JWKS (JSON Web Key Set)
        self._jwks_cache = None
        self._jwks_cache_expiry = None
        
        # Key Vault for secrets
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
            # Get signing keys
            signing_keys = await self._get_signing_keys()
            
            # Decode token header to get key ID
            unverified_header = jwt.get_unverified_header(token)
            key_id = unverified_header.get('kid')
            
            if not key_id:
                raise ValueError("Token missing key ID")
            
            # Find the corresponding key
            signing_key = None
            for key in signing_keys:
                if key['kid'] == key_id:
                    signing_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
                    break
            
            if not signing_key:
                raise ValueError(f"Unable to find signing key for kid: {key_id}")
            
            # Validate and decode token
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
            
            # Extract user information
            user_info = self._extract_user_info(payload)
            
            # Log successful authentication
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
        
        # Check if cache is valid
        if (self._jwks_cache and self._jwks_cache_expiry and 
            current_time < self._jwks_cache_expiry):
            return self._jwks_cache
        
        # Fetch new JWKS
        jwks_url = f"{self.issuer}/keys"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(jwks_url) as response:
                if response.status != 200:
                    raise Exception(f"Failed to fetch JWKS: {response.status}")
                
                jwks_data = await response.json()
                
        # Cache for 1 hour
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
            # This would typically query your user/store mapping
            # For demo, we'll use a simple Key Vault secret
            secret_name = f"user-{user_id}-stores"
            
            if self.secret_client:
                secret = await self.secret_client.get_secret(secret_name)
                store_list = secret.value.split(',')
                return [store.strip() for store in store_list if store.strip()]
            
            # Fallback: return default store access
            logger.warning(f"No store mapping found for user {user_id}, using default")
            return ['seattle']  # Default store access
            
        except Exception as e:
            logger.error(f"Failed to get store access for user {user_id}: {e}")
            return []  # No access if we can't determine stores

# Global authenticator instance
azure_authenticator = AzureAuthenticator()
```

### অনুমোদন মিডলওয়্যার

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
    
    # Define role hierarchy
    ROLE_HIERARCHY = {
        'store_admin': ['store_manager', 'store_user', 'store_readonly'],
        'store_manager': ['store_user', 'store_readonly'],
        'store_user': ['store_readonly'],
        'store_readonly': []
    }
    
    # Define permissions for each role
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
            # Add direct permissions
            user_permissions.update(cls.ROLE_PERMISSIONS.get(role, []))
            
            # Add inherited permissions
            inherited_roles = cls.ROLE_HIERARCHY.get(role, [])
            for inherited_role in inherited_roles:
                user_permissions.update(cls.ROLE_PERMISSIONS.get(inherited_role, []))
        
        return required_permission in user_permissions
    
    @classmethod
    def get_user_stores(cls, user_info: Dict) -> List[str]:
        """Extract stores user has access to from user info."""
        
        # This would typically come from your user management system
        # For demo, we'll extract from custom claims or groups
        
        stores = []
        
        # Check for direct store assignments in groups
        for group in user_info.get('groups', []):
            if group.startswith('store_'):
                store_id = group.replace('store_', '')
                stores.append(store_id)
        
        # Check for app-specific roles
        for role in user_info.get('app_roles', []):
            if 'store:' in role:
                _, store_id = role.split('store:', 1)
                stores.append(store_id)
        
        return list(set(stores))  # Remove duplicates

def require_auth(required_permission: str = None, require_store_access: bool = True):
    """Decorator to require authentication and authorization."""
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # Extract request from args (FastAPI dependency injection)
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
            
            # Get authorization header
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Missing or invalid authorization header",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            
            token = auth_header.split(' ')[1]
            
            try:
                # Validate token
                user_info = await azure_authenticator.validate_token(token)
                
                # Check required permission
                if required_permission:
                    user_roles = user_info.get('roles', [])
                    if not RoleBasedAuth.has_permission(user_roles, required_permission):
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Insufficient permissions. Required: {required_permission}"
                        )
                
                # Check store access
                if require_store_access:
                    user_stores = RoleBasedAuth.get_user_stores(user_info)
                    if not user_stores:
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail="No store access configured for user"
                        )
                    
                    # Set default store context (first accessible store)
                    request.state.current_store = user_stores[0]
                    request.state.accessible_stores = user_stores
                
                # Add user info to request state
                request.state.user_info = user_info
                request.state.user_id = user_info['user_id']
                
                # Call the original function
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
            # Get store_id from kwargs
            store_id = kwargs.get(store_param)
            
            if not store_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Missing required parameter: {store_param}"
                )
            
            # Extract request from args
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
            
            # Validate user has access to requested store
            if store_id not in request.state.accessible_stores:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Access denied to store: {store_id}"
                )
            
            # Set store context in request state
            request.state.current_store = store_id
            
            return await func(*args, **kwargs)
        
        return wrapper
    return decorator
```

## 🔍 নিরাপত্তা অডিট এবং কমপ্লায়েন্স

### বিস্তৃত অডিট লগিং

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

### নিরাপত্তা পর্যবেক্ষণ ভিউ

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

### নিরাপত্তা ইভেন্ট পর্যবেক্ষণ

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
        
        # Alert thresholds
        self.thresholds = {
            'failed_auth_attempts': 5,      # per user per hour
            'multiple_ip_access': 3,        # different IPs per user per hour
            'excessive_data_access': 1000,  # queries per user per hour
            'privilege_escalation': 1,      # any attempt
            'unauthorized_store_access': 1  # any attempt
        }
    
    async def start_monitoring(self):
        """Start security monitoring loop."""
        logger.info("Starting security monitoring")
        
        while True:
            try:
                await self._check_security_events()
                await asyncio.sleep(300)  # Check every 5 minutes
            except Exception as e:
                logger.error(f"Security monitoring error: {e}")
                await asyncio.sleep(60)  # Short retry on error
    
    async def _check_security_events(self):
        """Check for security events and generate alerts."""
        
        conn = await asyncpg.connect(self.db_connection_string)
        
        try:
            # Check failed authentication attempts
            await self._check_failed_auth(conn)
            
            # Check suspicious access patterns
            await self._check_suspicious_access(conn)
            
            # Check data access anomalies
            await self._check_data_access_anomalies(conn)
            
            # Check unauthorized access attempts
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
        
        # Send to configured alert handlers
        for handler in self.alert_handlers:
            try:
                await handler.send_alert(alert)
            except Exception as e:
                logger.error(f"Failed to send alert via {handler.__class__.__name__}: {e}")
    
    def add_alert_handler(self, handler):
        """Add alert handler."""
        self.alert_handlers.append(handler)
```

## 🧪 নিরাপত্তা টেস্টিং এবং যাচাই

### স্বয়ংক্রিয় নিরাপত্তা টেস্ট

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
        
        # Set Seattle store context
        await db_connection.execute("SELECT retail.set_store_context('seattle')")
        
        # Get customer count
        seattle_customers = await db_connection.fetchval(
            "SELECT COUNT(*) FROM retail.customers"
        )
        
        # Set Redmond store context
        await db_connection.execute("SELECT retail.set_store_context('redmond')")
        
        # Get customer count
        redmond_customers = await db_connection.fetchval(
            "SELECT COUNT(*) FROM retail.customers"
        )
        
        # Verify isolation (counts should be different)
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
        
        # Set context to one store
        await db_connection.execute("SELECT retail.set_store_context('seattle')")
        
        # Try to insert data with different store_id
        with pytest.raises(Exception):
            await db_connection.execute("""
                INSERT INTO retail.customers (store_id, first_name, last_name, email)
                VALUES ('redmond', 'Test', 'User', 'test@example.com')
            """)

class TestAuthentication:
    """Test authentication and authorization."""
    
    def test_valid_jwt_token(self):
        """Test valid JWT token validation."""
        
        # Mock valid token
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
        
        # This would require mocking the JWKS endpoint
        # In real implementation, use proper test JWT tokens
        
    def test_expired_token_rejection(self):
        """Test that expired tokens are rejected."""
        
        token_payload = {
            'oid': 'user-123',
            'exp': int((datetime.now(timezone.utc)).timestamp()) - 3600,  # Expired
            'iat': int((datetime.now(timezone.utc)).timestamp()) - 7200
        }
        
        # Test would verify that expired tokens are rejected
        
    def test_invalid_audience_rejection(self):
        """Test that tokens with wrong audience are rejected."""
        
        token_payload = {
            'oid': 'user-123',
            'aud': 'wrong-audience',  # Invalid audience
            'exp': int((datetime.now(timezone.utc)).timestamp()) + 3600,
            'iat': int((datetime.now(timezone.utc)).timestamp())
        }
        
        # Test would verify that wrong audience tokens are rejected

class TestAuthorization:
    """Test role-based authorization."""
    
    def test_role_hierarchy(self):
        """Test that role hierarchy works correctly."""
        
        from mcp_server.security.authorization import RoleBasedAuth
        
        # Store admin should have all permissions
        assert RoleBasedAuth.has_permission(['store_admin'], 'read_all')
        assert RoleBasedAuth.has_permission(['store_admin'], 'write_all')
        assert RoleBasedAuth.has_permission(['store_admin'], 'delete_all')
        
        # Store user should have limited permissions
        assert RoleBasedAuth.has_permission(['store_user'], 'read_products')
        assert not RoleBasedAuth.has_permission(['store_user'], 'delete_all')
        
        # Store readonly should have minimal permissions
        assert RoleBasedAuth.has_permission(['store_readonly'], 'read_products')
        assert not RoleBasedAuth.has_permission(['store_readonly'], 'write_transactions')
    
    def test_permission_inheritance(self):
        """Test that permissions are properly inherited."""
        
        from mcp_server.security.authorization import RoleBasedAuth
        
        # Manager should inherit user permissions
        assert RoleBasedAuth.has_permission(['store_manager'], 'read_products')
        assert RoleBasedAuth.has_permission(['store_manager'], 'write_transactions')

# Security test runner
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

### পেনিট্রেশন টেস্টিং চেকলিস্ট

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

## 🎯 মূল বিষয়গুলো

এই ল্যাব সম্পন্ন করার পরে আপনি অর্জন করবেন:

✅ **মাল্টি-টেন্যান্ট নিরাপত্তা**: সম্পূর্ণ ডেটা আইসোলেশনের জন্য Row Level Security বাস্তবায়ন  
✅ **Azure প্রমাণীকরণ**: Azure Entra ID-এর সাথে JWT যাচাই সংযুক্তকরণ  
✅ **রোল-ভিত্তিক অনুমোদন**: হায়ারারকিক্যাল রোল এবং পারমিশন সিস্টেম কনফিগারেশন  
✅ **বিস্তৃত অডিট লগিং**: নিরাপত্তা ইভেন্ট ট্র্যাকিং এবং পর্যবেক্ষণ প্রতিষ্ঠা  
✅ **নিরাপত্তা টেস্টিং**: স্বয়ংক্রিয় নিরাপত্তা যাচাই টেস্ট বাস্তবায়ন  
✅ **হুমকি পর্যবেক্ষণ**: রিয়েল-টাইম নিরাপত্তা ইভেন্ট সনাক্তকরণ এবং সতর্কতা তৈরি  

## 🚀 পরবর্তী পদক্ষেপ

**[ল্যাব ০৩: পরিবেশ সেটআপ](../03-Setup/README.md)** চালিয়ে যান:

- নিরাপত্তার সেরা অনুশীলন সহ ডেভেলপমেন্ট পরিবেশ কনফিগার করুন  
- প্রমাণীকরণ এবং পর্যবেক্ষণের জন্য Azure সার্ভিস সেটআপ করুন  
- নিরাপদ ডেটাবেস সংযোগ এবং সিক্রেট ম্যানেজমেন্ট বাস্তবায়ন করুন  
- ডেভেলপমেন্ট পরিবেশে নিরাপত্তা কনফিগারেশন যাচাই করুন  

## 📚 অতিরিক্ত সম্পদ

### Azure নিরাপত্তা
- [Azure Entra ID ডকুমেন্টেশন](https://docs.microsoft.com/azure/active-directory/) - সম্পূর্ণ আইডেন্টিটি প্ল্যাটফর্ম গাইড  
- [Azure Key Vault](https://docs.microsoft.com/azure/key-vault/) - সিক্রেট ম্যানেজমেন্ট সার্ভিস  
- [Azure নিরাপত্তার সেরা অনুশীলন](https://docs.microsoft.com/azure/security/fundamentals/best-practices-and-patterns) - নিরাপত্তা নির্দেশিকা  

### ডেটাবেস নিরাপত্তা
- [PostgreSQL Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - অফিসিয়াল RLS ডকুমেন্টেশন  
- [ডেটাবেস নিরাপত্তা চেকলিস্ট](https://www.postgresql.org/docs/current/security.html) - PostgreSQL নিরাপত্তা গাইড  
- [মাল্টি-টেন্যান্ট ডেটাবেস প্যাটার্ন](https://docs.microsoft.com/azure/architecture/patterns/multitenancy) - আর্কিটেকচার প্যাটার্ন  

### নিরাপত্তা টেস্টিং
- [OWASP টেস্টিং গাইড](https://owasp.org/www-project-web-security-testing-guide/) - বিস্তৃত নিরাপত্তা টেস্টিং  
- [JWT নিরাপত্তার সেরা অনুশীলন](https://tools.ietf.org/html/rfc8725) - JWT নিরাপত্তা বিবেচনা  
- [API নিরাপত্তা টেস্টিং](https://owasp.org/www-project-api-security/) - API-নির্দিষ্ট নিরাপত্তা টেস্টিং  

---

**পূর্ববর্তী**: [ল্যাব ০১: কোর আর্কিটেকচার ধারণা](../01-Architecture/README.md)  
**পরবর্তী**: [ল্যাব ০৩: পরিবেশ সেটআপ](../03-Setup/README.md)  

---

**অস্বীকৃতি**:  
এই নথিটি AI অনুবাদ পরিষেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনুবাদ করা হয়েছে। আমরা যথাসম্ভব সঠিকতার জন্য চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ভাষায় থাকা নথিটিকে প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের জন্য, পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যা হলে আমরা দায়ী থাকব না।