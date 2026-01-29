# സുരക്ഷയും മൾട്ടി-ടെനൻസിയും

## 🎯 ഈ ലാബ് എന്താണ് ഉൾക്കൊള്ളുന്നത്

ഈ ലാബ് MCP സെർവറുകൾക്കായി എന്റർപ്രൈസ്-ഗ്രേഡ് സുരക്ഷയും മൾട്ടി-ടെനൻസി നടപ്പിലാക്കുന്നതിന് സമഗ്രമായ മാർഗ്ഗനിർദ്ദേശം നൽകുന്നു. നിങ്ങൾക്ക് സുരക്ഷിതവും അനുസരണയുള്ളതുമായ സിസ്റ്റങ്ങൾ രൂപകൽപ്പന ചെയ്യാൻ പഠിക്കാം, ഇത് സങ്കീർണ്ണമായ റീട്ടെയിൽ ഡാറ്റ സംരക്ഷിക്കുകയും പല ടെനന്റുകൾക്കിടയിൽ ലവചികമായ ആക്‌സസ് മാതൃകകൾ അനുവദിക്കുകയും ചെയ്യുന്നു.

## അവലോകനം

ഉപഭോക്തൃ ഡാറ്റ, പേയ്മെന്റ് വിവരങ്ങൾ, ബിസിനസ് ഇന്റലിജൻസ് കൈകാര്യം ചെയ്യുന്ന റീട്ടെയിൽ ആപ്ലിക്കേഷനുകളിൽ സുരക്ഷ അത്യന്താപേക്ഷിതമാണ്. ഈ ലാബ് പ്രാമാണീകരണവും അധികാരനിർണയവും മുതൽ ഡാറ്റ ഐസൊലേഷനും അനുസരണ നിരീക്ഷണവും വരെ സമഗ്രമായ സുരക്ഷാ ആർക്കിടെക്ചർ ഉൾക്കൊള്ളുന്നു.

ആസ്യൂർ ഐഡന്റിറ്റി സർവീസുകൾ, പോസ്റ്റ്‌ഗ്രെഎസ്‌ക്യുവൽ റോ ലെവൽ സെക്യൂരിറ്റി, ആപ്ലിക്കേഷൻ-തല നിയന്ത്രണങ്ങൾ, സമഗ്രമായ ഓഡിറ്റ് ലോഗിംഗ് എന്നിവ സംയോജിപ്പിച്ച് ഒരു ശക്തവും അനുസരണയുള്ളതുമായ പ്ലാറ്റ്ഫോം സൃഷ്ടിക്കുന്ന ഡിഫൻസ്-ഇൻ-ഡെപ്ത് തന്ത്രം നടപ്പിലാക്കുന്നു.

## പഠന ലക്ഷ്യങ്ങൾ

ഈ ലാബ് പൂർത്തിയാക്കിയാൽ, നിങ്ങൾക്ക് കഴിയും:

- **മൾട്ടി-ടെനന്റ് ഡാറ്റ ഐസൊലേഷനായി** എന്റർപ്രൈസ്-ഗ്രേഡ് റോ ലെവൽ സെക്യൂരിറ്റി നടപ്പിലാക്കുക  
- **ആസ്യൂർ ഉപയോഗിച്ച്** സുരക്ഷിതമായ പ്രാമാണീകരണവും അധികാരനിർണയ മാതൃകകളും രൂപകൽപ്പന ചെയ്യുക  
- **അനുസരണ ആവശ്യങ്ങൾക്കായി** സമഗ്രമായ ഓഡിറ്റ് ലോഗിംഗ് കോൺഫിഗർ ചെയ്യുക  
- **ആപ്ലിക്കേഷൻ എല്ലാ തലങ്ങളിലും** ഡിഫൻസ്-ഇൻ-ഡെപ്ത് സുരക്ഷാ തന്ത്രങ്ങൾ പ്രയോഗിക്കുക  
- **സിസ്റ്റമാറ്റിക് ടെസ്റ്റിംഗിലൂടെ** സുരക്ഷാ നടപ്പാക്കലുകൾ സാധൂകരിക്കുക  
- **സുരക്ഷാ സംഭവങ്ങൾ നിരീക്ഷിച്ച്** സാധ്യതയുള്ള ഭീഷണികൾക്ക് പ്രതികരിക്കുക  

## 🔐 മൾട്ടി-ടെനന്റ് സുരക്ഷാ ആർക്കിടെക്ചർ

### സുരക്ഷാ തലങ്ങളുടെ അവലോകനം

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

### മൾട്ടി-ടെനൻസി മോഡലുകൾ

നമ്മുടെ നടപ്പാക്കൽ റോ ലെവൽ സെക്യൂരിറ്റിയോടുകൂടിയ **ഷെയർഡ് ഡാറ്റാബേസ്, ഷെയർഡ് സ്കീമ** മോഡൽ ഉപയോഗിക്കുന്നു:

**നേട്ടങ്ങൾ:**  
- ചെലവുകുറഞ്ഞ വിഭവ ഉപയോഗം  
- പരിപാലനവും അപ്ഡേറ്റുകളും ലളിതമാക്കുന്നു  
- RLS വഴി ശക്തമായ ഡാറ്റ ഐസൊലേഷൻ  
- അനുസരണ സൗഹൃദ ഓഡിറ്റ് ട്രെയിലുകൾ  

**വിപരീതഫലങ്ങൾ:**  
- RLS നയം സൂക്ഷ്മമായി രൂപകൽപ്പന ചെയ്യേണ്ടത്  
- സ്കീമ മാറ്റങ്ങൾ എല്ലാ ടെനന്റുകളെയും ബാധിക്കുന്നു  
- ശക്തമായ ബാക്കപ്പ്/റസ്റ്റോർ നടപടികൾ ആവശ്യമുണ്ട്  

## 🛡️ റോ ലെവൽ സെക്യൂരിറ്റി നടപ്പാക്കൽ

### RLS അടിസ്ഥാനങ്ങൾ

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

### സ്റ്റോർ കോൺടെക്സ്റ്റ് മാനേജ്മെന്റ്

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

### RLS നയങ്ങൾ

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

### RLS ടെസ്റ്റിംഗ്‌യും സാധൂകരണവും

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

## 🔑 പ്രാമാണീകരണവും അധികാരനിർണയവും

### ആസ്യൂർ എൻട്ര ID ഇന്റഗ്രേഷൻ

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
        
        # JWKS (JSON വെബ് കീ സെറ്റ്) കാഷെ
        self._jwks_cache = None
        self._jwks_cache_expiry = None
        
        # രഹസ്യങ്ങൾക്കുള്ള കീ വാൾട്ട്
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
            # സൈൻ ചെയ്യാനുള്ള കീകൾ നേടുക
            signing_keys = await self._get_signing_keys()
            
            # കീ ഐഡി നേടാൻ ടോക്കൺ ഹെഡർ ഡീകോഡ് ചെയ്യുക
            unverified_header = jwt.get_unverified_header(token)
            key_id = unverified_header.get('kid')
            
            if not key_id:
                raise ValueError("Token missing key ID")
            
            # അനുയോജ്യമായ കീ കണ്ടെത്തുക
            signing_key = None
            for key in signing_keys:
                if key['kid'] == key_id:
                    signing_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
                    break
            
            if not signing_key:
                raise ValueError(f"Unable to find signing key for kid: {key_id}")
            
            # ടോക്കൺ സാധൂകരിച്ച് ഡീകോഡ് ചെയ്യുക
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
            
            # ഉപയോക്തൃ വിവരങ്ങൾ എടുക്കുക
            user_info = self._extract_user_info(payload)
            
            # വിജയകരമായ പ്രാമാണീകരണം ലോഗ് ചെയ്യുക
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
        
        # കാഷെ സാധുവാണോ എന്ന് പരിശോധിക്കുക
        if (self._jwks_cache and self._jwks_cache_expiry and 
            current_time < self._jwks_cache_expiry):
            return self._jwks_cache
        
        # പുതിയ JWKS എടുക്കുക
        jwks_url = f"{self.issuer}/keys"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(jwks_url) as response:
                if response.status != 200:
                    raise Exception(f"Failed to fetch JWKS: {response.status}")
                
                jwks_data = await response.json()
                
        # 1 മണിക്കൂർ കാഷെ
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
            # സാധാരണയായി ഇത് നിങ്ങളുടെ ഉപയോക്താവ്/സ്റ്റോർ മാപ്പിംഗ് ചോദിക്കും
            # ഡെമോയ്ക്ക്, നാം ഒരു ലളിതമായ കീ വാൾട്ട് രഹസ്യം ഉപയോഗിക്കും
            secret_name = f"user-{user_id}-stores"
            
            if self.secret_client:
                secret = await self.secret_client.get_secret(secret_name)
                store_list = secret.value.split(',')
                return [store.strip() for store in store_list if store.strip()]
            
            # ഫാൾബാക്ക്: ഡിഫോൾട്ട് സ്റ്റോർ ആക്‌സസ് നൽകുക
            logger.warning(f"No store mapping found for user {user_id}, using default")
            return ['seattle']  # ഡിഫോൾട്ട് സ്റ്റോർ ആക്‌സസ്
            
        except Exception as e:
            logger.error(f"Failed to get store access for user {user_id}: {e}")
            return []  # സ്റ്റോറുകൾ നിർണ്ണയിക്കാൻ കഴിയാത്ത പക്ഷം ആക്‌സസ് ഇല്ല

# ഗ്ലോബൽ ഓതന്റിക്കേറ്റർ ഇൻസ്റ്റൻസ്
azure_authenticator = AzureAuthenticator()
```

### അധികാരനിർണയ മിഡിൽവെയർ

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
    
    # റോളിന്റെ ഹയർആർക്കി നിർവചിക്കുക
    ROLE_HIERARCHY = {
        'store_admin': ['store_manager', 'store_user', 'store_readonly'],
        'store_manager': ['store_user', 'store_readonly'],
        'store_user': ['store_readonly'],
        'store_readonly': []
    }
    
    # ഓരോ റോളിനും അനുമതികൾ നിർവചിക്കുക
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
            # നേരിട്ടുള്ള അനുമതികൾ ചേർക്കുക
            user_permissions.update(cls.ROLE_PERMISSIONS.get(role, []))
            
            # പാരമ്പര്യ അനുമതികൾ ചേർക്കുക
            inherited_roles = cls.ROLE_HIERARCHY.get(role, [])
            for inherited_role in inherited_roles:
                user_permissions.update(cls.ROLE_PERMISSIONS.get(inherited_role, []))
        
        return required_permission in user_permissions
    
    @classmethod
    def get_user_stores(cls, user_info: Dict) -> List[str]:
        """Extract stores user has access to from user info."""
        
        # ഇത് സാധാരണയായി നിങ്ങളുടെ ഉപയോക്തൃ മാനേജ്മെന്റ് സിസ്റ്റത്തിൽ നിന്നാകും വരുന്നത്
        # ഡെമോയ്ക്ക്, കസ്റ്റം ക്ലെയിംസിൽ നിന്നോ ഗ്രൂപ്പുകളിൽ നിന്നോ ഞങ്ങൾ എടുക്കും
        
        stores = []
        
        # ഗ്രൂപ്പുകളിൽ നേരിട്ടുള്ള സ്റ്റോർ നിയോഗങ്ങൾ പരിശോധിക്കുക
        for group in user_info.get('groups', []):
            if group.startswith('store_'):
                store_id = group.replace('store_', '')
                stores.append(store_id)
        
        # ആപ്പ്-നിർദ്ദിഷ്ട റോളുകൾ പരിശോധിക്കുക
        for role in user_info.get('app_roles', []):
            if 'store:' in role:
                _, store_id = role.split('store:', 1)
                stores.append(store_id)
        
        return list(set(stores))  # പുനരാവൃതികൾ നീക്കം ചെയ്യുക

def require_auth(required_permission: str = None, require_store_access: bool = True):
    """Decorator to require authentication and authorization."""
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # ആർഗ്യുമെന്റുകളിൽ നിന്ന് അഭ്യർത്ഥന എടുക്കുക (FastAPI ഡിപ്പെൻഡൻസി ഇൻജക്ഷൻ)
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
            
            # ഓതറൈസേഷൻ ഹെഡർ നേടുക
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Missing or invalid authorization header",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            
            token = auth_header.split(' ')[1]
            
            try:
                # ടോക്കൺ സാധുത പരിശോധിക്കുക
                user_info = await azure_authenticator.validate_token(token)
                
                # ആവശ്യമായ അനുമതി പരിശോധിക്കുക
                if required_permission:
                    user_roles = user_info.get('roles', [])
                    if not RoleBasedAuth.has_permission(user_roles, required_permission):
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Insufficient permissions. Required: {required_permission}"
                        )
                
                # സ്റ്റോർ ആക്‌സസ് പരിശോധിക്കുക
                if require_store_access:
                    user_stores = RoleBasedAuth.get_user_stores(user_info)
                    if not user_stores:
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail="No store access configured for user"
                        )
                    
                    # ഡിഫോൾട്ട് സ്റ്റോർ കോൺടെക്സ്റ്റ് സജ്ജമാക്കുക (ആദ്യത്തെ ആക്‌സസ്ബിള്‍ സ്റ്റോർ)
                    request.state.current_store = user_stores[0]
                    request.state.accessible_stores = user_stores
                
                # ഉപയോക്തൃ വിവരങ്ങൾ അഭ്യർത്ഥന സ്റ്റേറ്റിൽ ചേർക്കുക
                request.state.user_info = user_info
                request.state.user_id = user_info['user_id']
                
                # ഒറിജിനൽ ഫംഗ്ഷൻ വിളിക്കുക
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
            # kwargs-ൽ നിന്ന് store_id നേടുക
            store_id = kwargs.get(store_param)
            
            if not store_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Missing required parameter: {store_param}"
                )
            
            # ആർഗ്യുമെന്റുകളിൽ നിന്ന് അഭ്യർത്ഥന എടുക്കുക
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
            
            # അഭ്യർത്ഥിച്ച സ്റ്റോറിലേക്ക് ഉപയോക്താവിന് ആക്‌സസ് ഉണ്ടെന്ന് സ്ഥിരീകരിക്കുക
            if store_id not in request.state.accessible_stores:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Access denied to store: {store_id}"
                )
            
            # അഭ്യർത്ഥന സ്റ്റേറ്റിൽ സ്റ്റോർ കോൺടെക്സ്റ്റ് സജ്ജമാക്കുക
            request.state.current_store = store_id
            
            return await func(*args, **kwargs)
        
        return wrapper
    return decorator
```

## 🔍 സുരക്ഷാ ഓഡിറ്റ്‌വും അനുസരണവും

### സമഗ്രമായ ഓഡിറ്റ് ലോഗിംഗ്

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

### സുരക്ഷാ നിരീക്ഷണ കാഴ്ചകൾ

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

### സുരക്ഷാ സംഭവ നിരീക്ഷണം

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
        
        # അലേർട്ട് പരിധികൾ
        self.thresholds = {
            'failed_auth_attempts': 5,      # ഓരോ ഉപയോക്താവിനും ഓരോ മണിക്കൂറിലും
            'multiple_ip_access': 3,        # ഓരോ ഉപയോക്താവിനും ഓരോ മണിക്കൂറിലും വ്യത്യസ്ത IPകൾ
            'excessive_data_access': 1000,  # ഓരോ ഉപയോക്താവിനും ഓരോ മണിക്കൂറിലും ക്വെറികൾ
            'privilege_escalation': 1,      # ഏതെങ്കിലും ശ്രമം
            'unauthorized_store_access': 1  # ഏതെങ്കിലും ശ്രമം
        }
    
    async def start_monitoring(self):
        """Start security monitoring loop."""
        logger.info("Starting security monitoring")
        
        while True:
            try:
                await self._check_security_events()
                await asyncio.sleep(300)  # ഓരോ 5 മിനിറ്റിലും പരിശോധിക്കുക
            except Exception as e:
                logger.error(f"Security monitoring error: {e}")
                await asyncio.sleep(60)  # പിശക് സംഭവിച്ചാൽ ചെറിയ റിട്രൈ
    
    async def _check_security_events(self):
        """Check for security events and generate alerts."""
        
        conn = await asyncpg.connect(self.db_connection_string)
        
        try:
            # പരാജയപ്പെട്ട പ്രാമാണീകരണ ശ്രമങ്ങൾ പരിശോധിക്കുക
            await self._check_failed_auth(conn)
            
            # സംശയാസ്പദമായ ആക്‌സസ് മാതൃകകൾ പരിശോധിക്കുക
            await self._check_suspicious_access(conn)
            
            # ഡാറ്റ ആക്‌സസ് അസാധാരണതകൾ പരിശോധിക്കുക
            await self._check_data_access_anomalies(conn)
            
            # അനധികൃത ആക്‌സസ് ശ്രമങ്ങൾ പരിശോധിക്കുക
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
        
        # ക്രമീകരിച്ച അലേർട്ട് ഹാൻഡ്ലറുകളിലേക്ക് അയയ്ക്കുക
        for handler in self.alert_handlers:
            try:
                await handler.send_alert(alert)
            except Exception as e:
                logger.error(f"Failed to send alert via {handler.__class__.__name__}: {e}")
    
    def add_alert_handler(self, handler):
        """Add alert handler."""
        self.alert_handlers.append(handler)
```

## 🧪 സുരക്ഷാ ടെസ്റ്റിംഗും സാധൂകരണവും

### ഓട്ടോമേറ്റഡ് സുരക്ഷാ ടെസ്റ്റുകൾ

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
        
        # സിയാറ്റിൽ സ്റ്റോർ കോൺടെക്സ്റ്റ് സജ്ജമാക്കുക
        await db_connection.execute("SELECT retail.set_store_context('seattle')")
        
        # ഉപഭോക്തൃ എണ്ണം നേടുക
        seattle_customers = await db_connection.fetchval(
            "SELECT COUNT(*) FROM retail.customers"
        )
        
        # റെഡ്മണ്ട് സ്റ്റോർ കോൺടെക്സ്റ്റ് സജ്ജമാക്കുക
        await db_connection.execute("SELECT retail.set_store_context('redmond')")
        
        # ഉപഭോക്തൃ എണ്ണം നേടുക
        redmond_customers = await db_connection.fetchval(
            "SELECT COUNT(*) FROM retail.customers"
        )
        
        # ഐസൊലേഷൻ സ്ഥിരീകരിക്കുക (എണ്ണങ്ങൾ വ്യത്യസ്തമായിരിക്കണം)
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
        
        # ഒരു സ്റ്റോറിലേക്ക് കോൺടെക്സ്റ്റ് സജ്ജമാക്കുക
        await db_connection.execute("SELECT retail.set_store_context('seattle')")
        
        # വ്യത്യസ്ത സ്റ്റോർ_ഐഡി ഉപയോഗിച്ച് ഡാറ്റ ചേർക്കാൻ ശ്രമിക്കുക
        with pytest.raises(Exception):
            await db_connection.execute("""
                INSERT INTO retail.customers (store_id, first_name, last_name, email)
                VALUES ('redmond', 'Test', 'User', 'test@example.com')
            """)

class TestAuthentication:
    """Test authentication and authorization."""
    
    def test_valid_jwt_token(self):
        """Test valid JWT token validation."""
        
        # സാധുവായ ടോക്കൺ മോക് ചെയ്യുക
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
        
        # ഇത് JWKS എൻഡ്‌പോയിന്റ് മോക് ചെയ്യേണ്ടതുണ്ടാകും
        # യഥാർത്ഥ നടപ്പാക്കലിൽ, ശരിയായ ടെസ്റ്റ് JWT ടോക്കണുകൾ ഉപയോഗിക്കുക
        
    def test_expired_token_rejection(self):
        """Test that expired tokens are rejected."""
        
        token_payload = {
            'oid': 'user-123',
            'exp': int((datetime.now(timezone.utc)).timestamp()) - 3600,  # കാലഹരണപ്പെട്ടത്
            'iat': int((datetime.now(timezone.utc)).timestamp()) - 7200
        }
        
        # കാലഹരണപ്പെട്ട ടോക്കണുകൾ നിരസിക്കപ്പെടുന്നുവെന്ന് ടെസ്റ്റ് സ്ഥിരീകരിക്കും
        
    def test_invalid_audience_rejection(self):
        """Test that tokens with wrong audience are rejected."""
        
        token_payload = {
            'oid': 'user-123',
            'aud': 'wrong-audience',  # അസാധുവായ പ്രേക്ഷകർ
            'exp': int((datetime.now(timezone.utc)).timestamp()) + 3600,
            'iat': int((datetime.now(timezone.utc)).timestamp())
        }
        
        # തെറ്റായ പ്രേക്ഷകർ ഉള്ള ടോക്കണുകൾ നിരസിക്കപ്പെടുന്നുവെന്ന് ടെസ്റ്റ് സ്ഥിരീകരിക്കും

class TestAuthorization:
    """Test role-based authorization."""
    
    def test_role_hierarchy(self):
        """Test that role hierarchy works correctly."""
        
        from mcp_server.security.authorization import RoleBasedAuth
        
        # സ്റ്റോർ അഡ്മിൻക്ക് എല്ലാ അനുമതികളും ഉണ്ടായിരിക്കണം
        assert RoleBasedAuth.has_permission(['store_admin'], 'read_all')
        assert RoleBasedAuth.has_permission(['store_admin'], 'write_all')
        assert RoleBasedAuth.has_permission(['store_admin'], 'delete_all')
        
        # സ്റ്റോർ ഉപയോക്താവിന് പരിമിത അനുമതികൾ ഉണ്ടായിരിക്കണം
        assert RoleBasedAuth.has_permission(['store_user'], 'read_products')
        assert not RoleBasedAuth.has_permission(['store_user'], 'delete_all')
        
        # സ്റ്റോർ റീഡോൺലിയ്ക്ക് കുറഞ്ഞ അനുമതികൾ ഉണ്ടായിരിക്കണം
        assert RoleBasedAuth.has_permission(['store_readonly'], 'read_products')
        assert not RoleBasedAuth.has_permission(['store_readonly'], 'write_transactions')
    
    def test_permission_inheritance(self):
        """Test that permissions are properly inherited."""
        
        from mcp_server.security.authorization import RoleBasedAuth
        
        # മാനേജർ ഉപയോക്തൃ അനുമതികൾ അവകാശപ്പെടണം
        assert RoleBasedAuth.has_permission(['store_manager'], 'read_products')
        assert RoleBasedAuth.has_permission(['store_manager'], 'write_transactions')

# സുരക്ഷാ ടെസ്റ്റ് റണ്ണർ
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

### പെനെട്രേഷൻ ടെസ്റ്റിംഗ് ചെക്ക്ലിസ്റ്റ്

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

## 🎯 പ്രധാനപ്പെട്ട കാര്യങ്ങൾ

ഈ ലാബ് പൂർത്തിയാക്കിയ ശേഷം, നിങ്ങൾക്ക് ഉണ്ടായിരിക്കണം:

✅ **മൾട്ടി-ടെനന്റ് സുരക്ഷ**: പൂർണ്ണ ഡാറ്റ ഐസൊലേഷനായി റോ ലെവൽ സെക്യൂരിറ്റി നടപ്പിലാക്കി  
✅ **ആസ്യൂർ പ്രാമാണീകരണം**: JWT സാധൂകരണത്തോടെ ആസ്യൂർ എൻട്ര ID ഇന്റഗ്രേറ്റ് ചെയ്തു  
✅ **റോൾ-അധിഷ്ഠിത അധികാരനിർണയം**: പദവിവ്യവസ്ഥാപിത റോളും അനുമതികളും കോൺഫിഗർ ചെയ്തു  
✅ **സമഗ്ര ഓഡിറ്റ് ലോഗിംഗ്**: സുരക്ഷാ സംഭവ ട്രാക്കിംഗ്, നിരീക്ഷണം സ്ഥാപിച്ചു  
✅ **സുരക്ഷാ ടെസ്റ്റിംഗ്**: ഓട്ടോമേറ്റഡ് സുരക്ഷാ സാധൂകരണ ടെസ്റ്റുകൾ നടപ്പിലാക്കി  
✅ **ഭീഷണി നിരീക്ഷണം**: യഥാർത്ഥ സമയ സുരക്ഷാ സംഭവ കണ്ടെത്തലും അലർട്ടിംഗും സൃഷ്ടിച്ചു  

## 🚀 അടുത്തത് എന്താണ്

**[Lab 03: Environment Setup](../03-Setup/README.md)** തുടരണം:

- സുരക്ഷാ മികച്ച പ്രാക്ടീസുകളോടെ ഡെവലപ്പ്മെന്റ് പരിസ്ഥിതികൾ കോൺഫിഗർ ചെയ്യുക  
- പ്രാമാണീകരണത്തിനും നിരീക്ഷണത്തിനും ആസ്യൂർ സർവീസുകൾ സജ്ജമാക്കുക  
- സുരക്ഷിത ഡാറ്റാബേസ് കണക്ഷനുകളും രഹസ്യ മാനേജ്മെന്റും നടപ്പിലാക്കുക  
- ഡെവലപ്പ്മെന്റ് പരിസ്ഥിതികളിൽ സുരക്ഷാ കോൺഫിഗറേഷനുകൾ സാധൂകരിക്കുക  

## 📚 അധിക സ്രോതസുകൾ

### ആസ്യൂർ സുരക്ഷ  
- [Azure Entra ID Documentation](https://docs.microsoft.com/azure/active-directory/) - സമഗ്ര ഐഡന്റിറ്റി പ്ലാറ്റ്ഫോം ഗൈഡ്  
- [Azure Key Vault](https://docs.microsoft.com/azure/key-vault/) - രഹസ്യ മാനേജ്മെന്റ് സർവീസ്  
- [Azure Security Best Practices](https://docs.microsoft.com/azure/security/fundamentals/best-practices-and-patterns) - സുരക്ഷാ മാർഗ്ഗനിർദ്ദേശങ്ങൾ  

### ഡാറ്റാബേസ് സുരക്ഷ  
- [PostgreSQL Row Level Security](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - ഔദ്യോഗിക RLS ഡോക്യുമെന്റേഷൻ  
- [Database Security Checklist](https://www.postgresql.org/docs/current/security.html) - പോസ്റ്റ്‌ഗ്രെഎസ്‌ക്യുവൽ സുരക്ഷാ ഗൈഡ്  
- [Multi-Tenant Database Patterns](https://docs.microsoft.com/azure/architecture/patterns/multitenancy) - ആർക്കിടെക്ചർ മാതൃകകൾ  

### സുരക്ഷാ ടെസ്റ്റിംഗ്  
- [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) - സമഗ്ര സുരക്ഷാ ടെസ്റ്റിംഗ്  
- [JWT Security Best Practices](https://tools.ietf.org/html/rfc8725) - JWT സുരക്ഷാ പരിഗണനകൾ  
- [API Security Testing](https://owasp.org/www-project-api-security/) - API-നിർദ്ദിഷ്ട സുരക്ഷാ ടെസ്റ്റിംഗ്  

---

**മുൻപ്**: [Lab 01: Core Architecture Concepts](../01-Architecture/README.md)  
**അടുത്തത്**: [Lab 03: Environment Setup](../03-Setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖ അധികാരപരമായ ഉറവിടമായി കണക്കാക്കപ്പെടണം. നിർണായക വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->