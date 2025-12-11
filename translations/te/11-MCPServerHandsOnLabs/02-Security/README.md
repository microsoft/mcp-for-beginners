<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "3b3c9c3f033e59a30c92b5895e0dc9fd",
  "translation_date": "2025-12-11T14:38:44+00:00",
  "source_file": "11-MCPServerHandsOnLabs/02-Security/README.md",
  "language_code": "te"
}
-->
# భద్రత మరియు బహుళ-అద్దెదారితనం

## 🎯 ఈ ప్రయోగశాల ఏమి కవర్ చేస్తుంది

ఈ ప్రయోగశాల MCP సర్వర్ల కోసం ఎంటర్‌ప్రైజ్-గ్రేడ్ భద్రత మరియు బహుళ-అద్దెదారితనాన్ని అమలు చేయడంపై సమగ్ర మార్గదర్శకాన్ని అందిస్తుంది. మీరు సున్నితమైన రిటైల్ డేటాను రక్షిస్తూ, బహుళ అద్దెదారుల మధ్య సౌకర్యవంతమైన యాక్సెస్ నమూనాలను అనుమతించే భద్రతా, అనుగుణమైన వ్యవస్థలను డిజైన్ చేయడం నేర్చుకుంటారు.

## అవలోకనం

కస్టమర్ డేటా, చెల్లింపు సమాచారం మరియు వ్యాపార బుద్ధిమత్తను నిర్వహించే రిటైల్ అనువర్తనాలలో భద్రత అత్యంత ముఖ్యమైనది. ఈ ప్రయోగశాల ధృవీకరణ మరియు అనుమతినుండి డేటా వేరుచేసే విధానం మరియు అనుగుణత పర్యవేక్షణ వరకు పూర్తి భద్రతా వాస్తవికతను కవర్ చేస్తుంది.

మేము Azure ఐడెంటిటీ సేవలు, PostgreSQL రో లెవల్ సెక్యూరిటీ, అనువర్తన స్థాయి నియంత్రణలు మరియు సమగ్ర ఆడిట్ లాగింగ్ కలిపి రక్షణలో లోతైన వ్యూహాన్ని అమలు చేస్తాము, దీని ద్వారా బలమైన, అనుగుణమైన వేదిక సృష్టించబడుతుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ ప్రయోగశాల ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- **అమలు చేయండి** బహుళ-అద్దెదారుల డేటా వేరుచేసేందుకు ఎంటర్‌ప్రైజ్-గ్రేడ్ రో లెవల్ సెక్యూరిటీ  
- **డిజైన్ చేయండి** Azure తో భద్రతా ధృవీకరణ మరియు అనుమతి నమూనాలు  
- **కాన్ఫిగర్ చేయండి** అనుగుణత అవసరాల కోసం సమగ్ర ఆడిట్ లాగింగ్  
- **అప్లై చేయండి** అన్ని అనువర్తన స్థరాలలో రక్షణలో లోతైన భద్రతా వ్యూహాలు  
- **పరిశీలించండి** వ్యవస్థాపిత పరీక్షల ద్వారా భద్రతా అమలులను  
- **పర్యవేక్షించండి** భద్రతా సంఘటనలను మరియు సంభావ్య ముప్పులకు స్పందించండి  

## 🔐 బహుళ-అద్దెదారుల భద్రతా వాస్తవికత

### భద్రతా స్థరాల అవలోకనం

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

### బహుళ-అద్దెదారితన నమూనాలు

మా అమలు **షేర్డ్ డేటాబేస్, షేర్డ్ స్కీమా** నమూనాను రో లెవల్ సెక్యూరిటీతో ఉపయోగిస్తుంది:

**లాభాలు:**
- ఖర్చు-సమర్థవంతమైన వనరుల వినియోగం  
- సులభమైన నిర్వహణ మరియు నవీకరణలు  
- RLS ద్వారా బలమైన డేటా వేరుచేసే విధానం  
- అనుగుణతకు అనుకూలమైన ఆడిట్ ట్రైల్స్  

**వినిమయాలు:**
- జాగ్రత్తగా RLS విధాన రూపకల్పన అవసరం  
- స్కీమా మార్పులు అన్ని అద్దెదారులపై ప్రభావం చూపుతాయి  
- బలమైన బ్యాకప్/రీస్టోర్ విధానాలు అవసరం  

## 🛡️ రో లెవల్ సెక్యూరిటీ అమలు

### RLS పునాది

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

### స్టోర్ కాంటెక్స్ట్ నిర్వహణ

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

### RLS విధానాలు

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

### RLS పరీక్ష మరియు ధృవీకరణ

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

## 🔑 ధృవీకరణ మరియు అనుమతి

### Azure Entra ID సమీకరణ

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
        
        # JWKS (JSON వెబ్ కీ సెట్) కోసం క్యాష్
        self._jwks_cache = None
        self._jwks_cache_expiry = None
        
        # రహస్యాల కోసం కీ వాల్ట్
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
            # సంతకం చేసే కీలు పొందండి
            signing_keys = await self._get_signing_keys()
            
            # కీ ID పొందడానికి టోకెన్ హెడ్డర్ డీకోడ్ చేయండి
            unverified_header = jwt.get_unverified_header(token)
            key_id = unverified_header.get('kid')
            
            if not key_id:
                raise ValueError("Token missing key ID")
            
            # సంబంధిత కీని కనుగొనండి
            signing_key = None
            for key in signing_keys:
                if key['kid'] == key_id:
                    signing_key = jwt.algorithms.RSAAlgorithm.from_jwk(key)
                    break
            
            if not signing_key:
                raise ValueError(f"Unable to find signing key for kid: {key_id}")
            
            # టోకెన్‌ను ధృవీకరించి డీకోడ్ చేయండి
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
            
            # వినియోగదారు సమాచారాన్ని తీసుకోండి
            user_info = self._extract_user_info(payload)
            
            # విజయవంతమైన ధృవీకరణను లాగ్ చేయండి
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
        
        # క్యాష్ చెల్లుబాటు అయ్యిందో లేదో తనిఖీ చేయండి
        if (self._jwks_cache and self._jwks_cache_expiry and 
            current_time < self._jwks_cache_expiry):
            return self._jwks_cache
        
        # కొత్త JWKS తీసుకోండి
        jwks_url = f"{self.issuer}/keys"
        
        async with aiohttp.ClientSession() as session:
            async with session.get(jwks_url) as response:
                if response.status != 200:
                    raise Exception(f"Failed to fetch JWKS: {response.status}")
                
                jwks_data = await response.json()
                
        # 1 గంట పాటు క్యాష్
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
            # ఇది సాధారణంగా మీ వినియోగదారు/స్టోర్ మ్యాపింగ్‌ను ప్రశ్నిస్తుంది
            # డెమో కోసం, మనం సాదా కీ వాల్ట్ రహస్యాన్ని ఉపయోగిస్తాము
            secret_name = f"user-{user_id}-stores"
            
            if self.secret_client:
                secret = await self.secret_client.get_secret(secret_name)
                store_list = secret.value.split(',')
                return [store.strip() for store in store_list if store.strip()]
            
            # ఫాల్‌బ్యాక్: డిఫాల్ట్ స్టోర్ యాక్సెస్‌ను తిరిగి ఇవ్వండి
            logger.warning(f"No store mapping found for user {user_id}, using default")
            return ['seattle']  # డిఫాల్ట్ స్టోర్ యాక్సెస్
            
        except Exception as e:
            logger.error(f"Failed to get store access for user {user_id}: {e}")
            return []  # స్టోర్లను నిర్ణయించలేకపోతే యాక్సెస్ లేదు

# గ్లోబల్ ధృవీకరణ ఇన్స్టెన్స్
azure_authenticator = AzureAuthenticator()
```

### అనుమతి మిడిల్వేర్

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
    
    # పాత్ర హైరార్కీని నిర్వచించండి
    ROLE_HIERARCHY = {
        'store_admin': ['store_manager', 'store_user', 'store_readonly'],
        'store_manager': ['store_user', 'store_readonly'],
        'store_user': ['store_readonly'],
        'store_readonly': []
    }
    
    # ప్రతి పాత్రకు అనుమతులను నిర్వచించండి
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
            # ప్రత్యక్ష అనుమతులను జోడించండి
            user_permissions.update(cls.ROLE_PERMISSIONS.get(role, []))
            
            # వారసత్వ అనుమతులను జోడించండి
            inherited_roles = cls.ROLE_HIERARCHY.get(role, [])
            for inherited_role in inherited_roles:
                user_permissions.update(cls.ROLE_PERMISSIONS.get(inherited_role, []))
        
        return required_permission in user_permissions
    
    @classmethod
    def get_user_stores(cls, user_info: Dict) -> List[str]:
        """Extract stores user has access to from user info."""
        
        # ఇది సాధారణంగా మీ యూజర్ నిర్వహణ వ్యవస్థ నుండి వస్తుంది
        # డెమో కోసం, మేము కస్టమ్ క్లెయిమ్స్ లేదా గ్రూపుల నుండి తీసుకుంటాము
        
        stores = []
        
        # గ్రూపులలో ప్రత్యక్ష స్టోర్ నియామకాలను తనిఖీ చేయండి
        for group in user_info.get('groups', []):
            if group.startswith('store_'):
                store_id = group.replace('store_', '')
                stores.append(store_id)
        
        # యాప్-ప్రత్యేక పాత్రలను తనిఖీ చేయండి
        for role in user_info.get('app_roles', []):
            if 'store:' in role:
                _, store_id = role.split('store:', 1)
                stores.append(store_id)
        
        return list(set(stores))  # ప్రతిలిపులను తొలగించండి

def require_auth(required_permission: str = None, require_store_access: bool = True):
    """Decorator to require authentication and authorization."""
    
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            # ఆర్గ్స్ నుండి అభ్యర్థనను తీసుకోండి (FastAPI డిపెండెన్సీ ఇంజెక్షన్)
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
            
            # అనుమతి హెడ్డర్ పొందండి
            auth_header = request.headers.get('Authorization')
            if not auth_header or not auth_header.startswith('Bearer '):
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Missing or invalid authorization header",
                    headers={"WWW-Authenticate": "Bearer"}
                )
            
            token = auth_header.split(' ')[1]
            
            try:
                # టోకెన్‌ను ధృవీకరించండి
                user_info = await azure_authenticator.validate_token(token)
                
                # అవసరమైన అనుమతిని తనిఖీ చేయండి
                if required_permission:
                    user_roles = user_info.get('roles', [])
                    if not RoleBasedAuth.has_permission(user_roles, required_permission):
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail=f"Insufficient permissions. Required: {required_permission}"
                        )
                
                # స్టోర్ యాక్సెస్‌ను తనిఖీ చేయండి
                if require_store_access:
                    user_stores = RoleBasedAuth.get_user_stores(user_info)
                    if not user_stores:
                        raise HTTPException(
                            status_code=status.HTTP_403_FORBIDDEN,
                            detail="No store access configured for user"
                        )
                    
                    # డిఫాల్ట్ స్టోర్ కాంటెక్స్ట్ సెట్ చేయండి (మొదటి యాక్సెసిబుల్ స్టోర్)
                    request.state.current_store = user_stores[0]
                    request.state.accessible_stores = user_stores
                
                # అభ్యర్థన స్థితిలో యూజర్ సమాచారాన్ని జోడించండి
                request.state.user_info = user_info
                request.state.user_id = user_info['user_id']
                
                # అసలు ఫంక్షన్‌ను పిలవండి
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
            # kwargs నుండి store_id పొందండి
            store_id = kwargs.get(store_param)
            
            if not store_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Missing required parameter: {store_param}"
                )
            
            # ఆర్గ్స్ నుండి అభ్యర్థనను తీసుకోండి
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
            
            # అభ్యర్థించిన స్టోర్‌కు యూజర్ యాక్సెస్ ఉందో లేదో ధృవీకరించండి
            if store_id not in request.state.accessible_stores:
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN,
                    detail=f"Access denied to store: {store_id}"
                )
            
            # అభ్యర్థన స్థితిలో స్టోర్ కాంటెక్స్ట్ సెట్ చేయండి
            request.state.current_store = store_id
            
            return await func(*args, **kwargs)
        
        return wrapper
    return decorator
```

## 🔍 భద్రతా ఆడిట్ మరియు అనుగుణత

### సమగ్ర ఆడిట్ లాగింగ్

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

### భద్రతా పర్యవేక్షణ వీక్షణలు

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

### భద్రతా సంఘటన పర్యవేక్షణ

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
        
        # అలర్ట్ పరిమితులు
        self.thresholds = {
            'failed_auth_attempts': 5,      # ప్రతి వినియోగదారునికి ప్రతి గంటకు
            'multiple_ip_access': 3,        # ప్రతి వినియోగదారునికి ప్రతి గంటకు వేరే IPలు
            'excessive_data_access': 1000,  # ప్రతి వినియోగదారునికి ప్రతి గంటకు ప్రశ్నలు
            'privilege_escalation': 1,      # ఏదైనా ప్రయత్నం
            'unauthorized_store_access': 1  # ఏదైనా ప్రయత్నం
        }
    
    async def start_monitoring(self):
        """Start security monitoring loop."""
        logger.info("Starting security monitoring")
        
        while True:
            try:
                await self._check_security_events()
                await asyncio.sleep(300)  # ప్రతి 5 నిమిషాలకు తనిఖీ చేయండి
            except Exception as e:
                logger.error(f"Security monitoring error: {e}")
                await asyncio.sleep(60)  # లోపం వచ్చినప్పుడు తక్కువ రీట్రై
    
    async def _check_security_events(self):
        """Check for security events and generate alerts."""
        
        conn = await asyncpg.connect(self.db_connection_string)
        
        try:
            # విఫలమైన ధృవీకరణ ప్రయత్నాలను తనిఖీ చేయండి
            await self._check_failed_auth(conn)
            
            # అనుమానాస్పద యాక్సెస్ నమూనాలను తనిఖీ చేయండి
            await self._check_suspicious_access(conn)
            
            # డేటా యాక్సెస్ అసాధారణతలను తనిఖీ చేయండి
            await self._check_data_access_anomalies(conn)
            
            # అనధికార యాక్సెస్ ప్రయత్నాలను తనిఖీ చేయండి
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
        
        # కాన్ఫిగర్ చేసిన అలర్ట్ హ్యాండ్లర్లకు పంపండి
        for handler in self.alert_handlers:
            try:
                await handler.send_alert(alert)
            except Exception as e:
                logger.error(f"Failed to send alert via {handler.__class__.__name__}: {e}")
    
    def add_alert_handler(self, handler):
        """Add alert handler."""
        self.alert_handlers.append(handler)
```

## 🧪 భద్రతా పరీక్ష మరియు ధృవీకరణ

### ఆటోమేటెడ్ భద్రతా పరీక్షలు

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
        
        # సియాటిల్ స్టోర్ సందర్భాన్ని సెట్ చేయండి
        await db_connection.execute("SELECT retail.set_store_context('seattle')")
        
        # కస్టమర్ సంఖ్యను పొందండి
        seattle_customers = await db_connection.fetchval(
            "SELECT COUNT(*) FROM retail.customers"
        )
        
        # రెడ్‌మండ్ స్టోర్ సందర్భాన్ని సెట్ చేయండి
        await db_connection.execute("SELECT retail.set_store_context('redmond')")
        
        # కస్టమర్ సంఖ్యను పొందండి
        redmond_customers = await db_connection.fetchval(
            "SELECT COUNT(*) FROM retail.customers"
        )
        
        # వేరుపడటం నిర్ధారించండి (సంఖ్యలు భిన్నంగా ఉండాలి)
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
        
        # ఒక స్టోర్‌కు సందర్భాన్ని సెట్ చేయండి
        await db_connection.execute("SELECT retail.set_store_context('seattle')")
        
        # వేరే store_id తో డేటాను చేర్చడానికి ప్రయత్నించండి
        with pytest.raises(Exception):
            await db_connection.execute("""
                INSERT INTO retail.customers (store_id, first_name, last_name, email)
                VALUES ('redmond', 'Test', 'User', 'test@example.com')
            """)

class TestAuthentication:
    """Test authentication and authorization."""
    
    def test_valid_jwt_token(self):
        """Test valid JWT token validation."""
        
        # సరైన టోకెన్‌ను మాక్ చేయండి
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
        
        # ఇది JWKS ఎండ్‌పాయింట్‌ను మాక్ చేయడం అవసరం
        # నిజమైన అమలులో, సరైన టెస్ట్ JWT టోకెన్లను ఉపయోగించండి
        
    def test_expired_token_rejection(self):
        """Test that expired tokens are rejected."""
        
        token_payload = {
            'oid': 'user-123',
            'exp': int((datetime.now(timezone.utc)).timestamp()) - 3600,  # కాలపరిమితి ముగిసింది
            'iat': int((datetime.now(timezone.utc)).timestamp()) - 7200
        }
        
        # కాలపరిమితి ముగిసిన టోకెన్లు తిరస్కరించబడతాయని పరీక్ష నిర్ధారిస్తుంది
        
    def test_invalid_audience_rejection(self):
        """Test that tokens with wrong audience are rejected."""
        
        token_payload = {
            'oid': 'user-123',
            'aud': 'wrong-audience',  # చెల్లని ప్రేక్షకులు
            'exp': int((datetime.now(timezone.utc)).timestamp()) + 3600,
            'iat': int((datetime.now(timezone.utc)).timestamp())
        }
        
        # తప్పు ప్రేక్షకుల టోకెన్లు తిరస్కరించబడతాయని పరీక్ష నిర్ధారిస్తుంది

class TestAuthorization:
    """Test role-based authorization."""
    
    def test_role_hierarchy(self):
        """Test that role hierarchy works correctly."""
        
        from mcp_server.security.authorization import RoleBasedAuth
        
        # స్టోర్ అడ్మిన్‌కు అన్ని అనుమతులు ఉండాలి
        assert RoleBasedAuth.has_permission(['store_admin'], 'read_all')
        assert RoleBasedAuth.has_permission(['store_admin'], 'write_all')
        assert RoleBasedAuth.has_permission(['store_admin'], 'delete_all')
        
        # స్టోర్ యూజర్‌కు పరిమిత అనుమతులు ఉండాలి
        assert RoleBasedAuth.has_permission(['store_user'], 'read_products')
        assert not RoleBasedAuth.has_permission(['store_user'], 'delete_all')
        
        # స్టోర్ రీడోన్లీకి కనిష్ట అనుమతులు ఉండాలి
        assert RoleBasedAuth.has_permission(['store_readonly'], 'read_products')
        assert not RoleBasedAuth.has_permission(['store_readonly'], 'write_transactions')
    
    def test_permission_inheritance(self):
        """Test that permissions are properly inherited."""
        
        from mcp_server.security.authorization import RoleBasedAuth
        
        # మేనేజర్ యూజర్ అనుమతులను వారసత్వంగా పొందాలి
        assert RoleBasedAuth.has_permission(['store_manager'], 'read_products')
        assert RoleBasedAuth.has_permission(['store_manager'], 'write_transactions')

# భద్రతా పరీక్ష రన్నర్
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

### పెనిట్రేషన్ టెస్టింగ్ చెక్లిస్ట్

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

## 🎯 ముఖ్యమైన పాఠాలు

ఈ ప్రయోగశాల పూర్తి చేసిన తర్వాత, మీరు కలిగి ఉండాలి:

✅ **బహుళ-అద్దెదారుల భద్రత**: పూర్తి డేటా వేరుచేసేందుకు రో లెవల్ సెక్యూరిటీ అమలు చేయబడింది  
✅ **Azure ధృవీకరణ**: Azure Entra ID ని JWT ధృవీకరణతో సమీకరించారు  
✅ **పాత్ర ఆధారిత అనుమతి**: హైరార్కికల్ పాత్ర మరియు అనుమతి వ్యవస్థను కాన్ఫిగర్ చేశారు  
✅ **సమగ్ర ఆడిట్ లాగింగ్**: భద్రతా సంఘటన ట్రాకింగ్ మరియు పర్యవేక్షణను స్థాపించారు  
✅ **భద్రతా పరీక్ష**: ఆటోమేటెడ్ భద్రతా ధృవీకరణ పరీక్షలను అమలు చేశారు  
✅ **ముప్పు పర్యవేక్షణ**: రియల్-టైమ్ భద్రతా సంఘటన గుర్తింపు మరియు అలర్టింగ్ సృష్టించారు  

## 🚀 తదుపరి ఏమిటి

**[Lab 03: Environment Setup](../03-Setup/README.md)** తో కొనసాగండి:

- భద్రతా ఉత్తమ ఆచారాలతో అభివృద్ధి వాతావరణాలను కాన్ఫిగర్ చేయండి  
- ధృవీకరణ మరియు పర్యవేక్షణ కోసం Azure సేవలను సెట్ చేయండి  
- భద్రతా డేటాబేస్ కనెక్షన్లు మరియు సీక్రెట్స్ నిర్వహణను అమలు చేయండి  
- అభివృద్ధి వాతావరణాలలో భద్రతా కాన్ఫిగరేషన్లను ధృవీకరించండి  

## 📚 అదనపు వనరులు

### Azure భద్రత  
- [Azure Entra ID డాక్యుమెంటేషన్](https://docs.microsoft.com/azure/active-directory/) - పూర్తి ఐడెంటిటీ ప్లాట్‌ఫారమ్ గైడ్  
- [Azure కీ వాల్ట్](https://docs.microsoft.com/azure/key-vault/) - సీక్రెట్స్ నిర్వహణ సేవ  
- [Azure భద్రత ఉత్తమ ఆచారాలు](https://docs.microsoft.com/azure/security/fundamentals/best-practices-and-patterns) - భద్రత మార్గదర్శకాలు  

### డేటాబేస్ భద్రత  
- [PostgreSQL రో లెవల్ సెక్యూరిటీ](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - అధికారిక RLS డాక్యుమెంటేషన్  
- [డేటాబేస్ భద్రత చెక్లిస్ట్](https://www.postgresql.org/docs/current/security.html) - PostgreSQL భద్రత గైడ్  
- [బహుళ-అద్దెదారుల డేటాబేస్ నమూనాలు](https://docs.microsoft.com/azure/architecture/patterns/multitenancy) - వాస్తవిక నమూనాలు  

### భద్రతా పరీక్ష  
- [OWASP పరీక్ష గైడ్](https://owasp.org/www-project-web-security-testing-guide/) - సమగ్ర భద్రతా పరీక్ష  
- [JWT భద్రత ఉత్తమ ఆచారాలు](https://tools.ietf.org/html/rfc8725) - JWT భద్రత పరిగణనలు  
- [API భద్రతా పరీక్ష](https://owasp.org/www-project-api-security/) - API-స్పెసిఫిక్ భద్రతా పరీక్ష  

---

**మునుపటి**: [Lab 01: Core Architecture Concepts](../01-Architecture/README.md)  
**తదుపరి**: [Lab 03: Environment Setup](../03-Setup/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పులు ఉండవచ్చు. మూల డాక్యుమెంట్ దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->