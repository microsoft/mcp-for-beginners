<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "772b18b1ca4fb34af68e12eb2f2defda",
  "translation_date": "2025-12-11T14:02:23+00:00",
  "source_file": "11-MCPServerHandsOnLabs/07-Semantic-Search/README.md",
  "language_code": "te"
}
-->
# సేమాంటిక్ సెర్చ్ ఇంటిగ్రేషన్

## 🎯 ఈ ల్యాబ్ ఏమి కవర్ చేస్తుంది

ఈ ల్యాబ్ Azure OpenAI ఎంబెడ్డింగ్స్ మరియు PostgreSQL యొక్క pgvector ఎక్స్‌టెన్షన్ ఉపయోగించి సేమాంటిక్ సెర్చ్ సామర్థ్యాలను అమలు చేయడానికి సమగ్ర మార్గదర్శకాన్ని అందిస్తుంది. మీరు సహజ భాషా ప్రశ్నలను అర్థం చేసుకునే మరియు సేమాంటిక్ సారూప్యత ఆధారంగా సంబంధిత ఫలితాలను అందించే AI-శక్తివంతమైన ఉత్పత్తి సెర్చ్‌ను నిర్మించడం నేర్చుకుంటారు.

## అవలోకనం

సాంప్రదాయ కీవర్డ్-ఆధారిత సెర్చ్ తరచుగా వినియోగదారుల ఉద్దేశ్యం మరియు సేమాంటిక్ అర్థాన్ని పట్టుకోలేకపోతుంది. వెక్టర్ ఎంబెడ్డింగ్స్ ఉపయోగించి సేమాంటిక్ సెర్చ్ "వర్షాకాలంలో సౌకర్యవంతమైన పరుగుల షూస్" వంటి సహజ భాషా ప్రశ్నలను ఉత్పత్తి వివరణల్లో ఆ ఖచ్చితమైన పదాలు లేకపోయినా సంబంధిత ఉత్పత్తులను కనుగొనడానికి అనుమతిస్తుంది.

మా అమలు Azure OpenAI యొక్క శక్తివంతమైన ఎంబెడ్డింగ్ మోడల్స్‌ను PostgreSQL యొక్క pgvector ఎక్స్‌టెన్షన్‌తో కలిపి, తెలివైన ఉత్పత్తి కనుగొనడాన్ని మెరుగుపరచే అధిక పనితీరు, స్కేలబుల్ సేమాంటిక్ సెర్చ్ సిస్టమ్‌ను సృష్టిస్తుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ ల్యాబ్ ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- **ఇంటిగ్రేట్ చేయండి** Azure OpenAI ఎంబెడ్డింగ్ మోడల్స్‌ను టెక్స్ట్ వెక్టరైజేషన్ కోసం  
- **అమలు చేయండి** pgvector ను సమర్థవంతమైన సారూప్యత సెర్చ్ ఆపరేషన్ల కోసం  
- **నిర్మించండి** సహజ భాష ఉత్పత్తి ప్రశ్నల కోసం సేమాంటిక్ సెర్చ్ టూల్స్  
- **సృష్టించండి** సాంప్రదాయ మరియు వెక్టర్ సెర్చ్‌లను కలిపిన హైబ్రిడ్ సెర్చ్  
- **ఆప్టిమైజ్ చేయండి** ఉత్పత్తి పనితీరు కోసం వెక్టర్ ప్రశ్నలను  
- **డిజైన్ చేయండి** ఎంబెడ్డింగ్ సారూప్యత ఉపయోగించి సిఫార్సు వ్యవస్థలను  

## 🧠 సేమాంటిక్ సెర్చ్ ఆర్కిటెక్చర్

### వెక్టర్ సెర్చ్ పైప్‌లైన్

```
┌─────────────────────────────────────────────────┐
│                User Query                       │
│         "comfortable running shoes"            │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│           Azure OpenAI API                     │
│        text-embedding-3-small                  │
│        Input: Query Text                       │
│        Output: 1536-dimensional vector         │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│              pgvector Search                   │
│      Cosine Similarity: embedding <=> vector   │
│      WHERE similarity > threshold              │
│      ORDER BY similarity DESC                  │
└─────────────────────┬───────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────┐
│            Ranked Results                      │
│    1. Nike Air Zoom (0.89 similarity)         │
│    2. Adidas Ultraboost (0.85 similarity)     │
│    3. New Balance Fresh Foam (0.82 similarity) │
└─────────────────────────────────────────────────┘
```

### ఎంబెడ్డింగ్ జనరేషన్ వ్యూహం

```python
# mcp_server/embeddings/embedding_manager.py
"""
Comprehensive embedding management for semantic search.
"""
import asyncio
import hashlib
import json
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta
import numpy as np
from azure.ai.projects.aio import AIProjectClient
from azure.identity.aio import DefaultAzureCredential
from azure.core.exceptions import HttpResponseError
import logging

logger = logging.getLogger(__name__)

class EmbeddingManager:
    """Manage text embeddings for semantic search."""
    
    def __init__(self, project_endpoint: str, deployment_name: str = "text-embedding-3-small"):
        self.project_endpoint = project_endpoint
        self.deployment_name = deployment_name
        self.credential = DefaultAzureCredential()
        self.client = None
        
        # ఎంబెడ్డింగ్ కాన్ఫిగరేషన్
        self.embedding_dimension = 1536  # text-embedding-3-small కొలత
        self.max_tokens = 8000  # ప్రతి అభ్యర్థనకు గరిష్ట టోకెన్లు
        self.batch_size = 100  # బ్యాచ్ ప్రాసెసింగ్ పరిమాణం
        
        # క్యాషింగ్ కాన్ఫిగరేషన్
        self.embedding_cache = {}
        self.cache_ttl = timedelta(hours=24)
        
        # రేట్ పరిమితి
        self.rate_limit_requests = 1000  # ప్రతి నిమిషం
        self.rate_limit_tokens = 150000  # ప్రతి నిమిషం
        
    async def initialize(self):
        """Initialize the Azure AI client."""
        
        try:
            self.client = AIProjectClient(
                endpoint=self.project_endpoint,
                credential=self.credential
            )
            
            # కనెక్షన్ పరీక్షించండి
            await self._test_connection()
            
            logger.info("Embedding manager initialized successfully")
            
        except Exception as e:
            logger.error(f"Failed to initialize embedding manager: {e}")
            raise
    
    async def _test_connection(self):
        """Test Azure OpenAI connection."""
        
        try:
            test_embedding = await self.generate_embedding("test connection")
            if len(test_embedding) != self.embedding_dimension:
                raise ValueError(f"Unexpected embedding dimension: {len(test_embedding)}")
            
            logger.info("Azure OpenAI connection test successful")
            
        except Exception as e:
            logger.error(f"Azure OpenAI connection test failed: {e}")
            raise
    
    async def generate_embedding(self, text: str, use_cache: bool = True) -> List[float]:
        """Generate embedding for a single text."""
        
        if not text or not text.strip():
            raise ValueError("Text cannot be empty")
        
        # ముందుగా క్యాష్ తనిఖీ చేయండి
        if use_cache:
            cache_key = self._get_cache_key(text)
            cached_embedding = self._get_cached_embedding(cache_key)
            if cached_embedding:
                return cached_embedding
        
        try:
            # క్లయింట్ ప్రారంభించబడిందని నిర్ధారించుకోండి
            if not self.client:
                await self.initialize()
            
            # ఎంబెడ్డింగ్ సృష్టించండి
            response = await self.client.embeddings.create(
                model=self.deployment_name,
                input=text.strip()
            )
            
            embedding = response.data[0].embedding
            
            # ఫలితాన్ని క్యాష్ చేయండి
            if use_cache:
                self._cache_embedding(cache_key, embedding)
            
            logger.debug(f"Generated embedding for text (length: {len(text)})")
            
            return embedding
            
        except HttpResponseError as e:
            logger.error(f"Azure OpenAI API error: {e}")
            raise Exception(f"Embedding generation failed: {e}")
        except Exception as e:
            logger.error(f"Embedding generation error: {e}")
            raise
    
    async def generate_embeddings_batch(
        self, 
        texts: List[str], 
        use_cache: bool = True
    ) -> List[List[float]]:
        """Generate embeddings for multiple texts efficiently."""
        
        if not texts:
            return []
        
        embeddings = []
        cache_misses = []
        cache_miss_indices = []
        
        # ప్రతి టెక్స్ట్ కోసం క్యాష్ తనిఖీ చేయండి
        for i, text in enumerate(texts):
            if not text or not text.strip():
                embeddings.append([])
                continue
                
            if use_cache:
                cache_key = self._get_cache_key(text)
                cached_embedding = self._get_cached_embedding(cache_key)
                if cached_embedding:
                    embeddings.append(cached_embedding)
                    continue
            
            # క్యాష్ మిస్సులను ట్రాక్ చేయండి
            embeddings.append(None)  # ప్లేస్‌హోల్డర్
            cache_misses.append(text.strip())
            cache_miss_indices.append(i)
        
        # క్యాష్ మిస్సుల కోసం ఎంబెడ్డింగ్స్ సృష్టించండి
        if cache_misses:
            try:
                # API పరిమితులను గౌరవించడానికి బ్యాచ్‌లలో ప్రాసెస్ చేయండి
                for batch_start in range(0, len(cache_misses), self.batch_size):
                    batch_end = min(batch_start + self.batch_size, len(cache_misses))
                    batch_texts = cache_misses[batch_start:batch_end]
                    
                    # బ్యాచ్ ఎంబెడ్డింగ్స్ సృష్టించండి
                    response = await self.client.embeddings.create(
                        model=self.deployment_name,
                        input=batch_texts
                    )
                    
                    # బ్యాచ్ ఫలితాలను ప్రాసెస్ చేయండి
                    for j, embedding_data in enumerate(response.data):
                        actual_index = cache_miss_indices[batch_start + j]
                        embedding = embedding_data.embedding
                        embeddings[actual_index] = embedding
                        
                        # ఫలితాన్ని క్యాష్ చేయండి
                        if use_cache:
                            text = batch_texts[j]
                            cache_key = self._get_cache_key(text)
                            self._cache_embedding(cache_key, embedding)
                    
                    # రేట్ పరిమితి - బ్యాచ్‌ల మధ్య చిన్న ఆలస్యం
                    if batch_end < len(cache_misses):
                        await asyncio.sleep(0.1)
                
                logger.info(f"Generated {len(cache_misses)} embeddings in batch")
                
            except Exception as e:
                logger.error(f"Batch embedding generation failed: {e}")
                raise
        
        return embeddings
    
    def _get_cache_key(self, text: str) -> str:
        """Generate cache key for text."""
        
        # క్యాష్ కీ కోసం టెక్స్ట్ + మోడల్ యొక్క SHA-256 హ్యాష్ ఉపయోగించండి
        content = f"{self.deployment_name}:{text.strip()}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def _get_cached_embedding(self, cache_key: str) -> Optional[List[float]]:
        """Get embedding from cache if not expired."""
        
        if cache_key in self.embedding_cache:
            embedding_data = self.embedding_cache[cache_key]
            
            # క్యాష్ ఎంట్రీ ఇంకా చెల్లుబాటు అయ్యిందో తనిఖీ చేయండి
            if datetime.now() - embedding_data['timestamp'] < self.cache_ttl:
                return embedding_data['embedding']
            else:
                # కాలం ముగిసిన ఎంట్రీని తొలగించండి
                del self.embedding_cache[cache_key]
        
        return None
    
    def _cache_embedding(self, cache_key: str, embedding: List[float]):
        """Cache embedding with timestamp."""
        
        self.embedding_cache[cache_key] = {
            'embedding': embedding,
            'timestamp': datetime.now()
        }
        
        # క్యాష్ పరిమాణాన్ని పరిమితం చేయండి
        if len(self.embedding_cache) > 10000:
            # పాత ఎంట్రీలను తొలగించండి
            oldest_keys = sorted(
                self.embedding_cache.keys(),
                key=lambda k: self.embedding_cache[k]['timestamp']
            )[:1000]
            
            for key in oldest_keys:
                del self.embedding_cache[key]
    
    async def cleanup(self):
        """Cleanup resources."""
        
        if self.client:
            await self.client.close()
        
        logger.info("Embedding manager cleanup completed")

# గ్లోబల్ ఎంబెడ్డింగ్ మేనేజర్ ఉదాహరణ
embedding_manager = EmbeddingManager(
    project_endpoint=os.getenv('PROJECT_ENDPOINT'),
    deployment_name=os.getenv('EMBEDDING_DEPLOYMENT_NAME', 'text-embedding-3-small')
)
```

## 🔍 ఉత్పత్తి ఎంబెడ్డింగ్ జనరేషన్

### ఆటోమేటెడ్ ఎంబెడ్డింగ్ పైప్‌లైన్

```python
# mcp_server/embeddings/product_embedder.py
"""
Product embedding generation and management.
"""
import asyncio
import asyncpg
from typing import List, Dict, Any, Optional
from datetime import datetime
import logging
from .embedding_manager import embedding_manager

logger = logging.getLogger(__name__)

class ProductEmbedder:
    """Generate and manage product embeddings for semantic search."""
    
    def __init__(self, db_provider):
        self.db_provider = db_provider
        self.embedding_manager = embedding_manager
        
        # ఉత్పత్తుల కోసం టెక్స్ట్ కలయిక వ్యూహం
        self.text_template = "{product_name} {brand} {description} {category} {tags}"
        
    async def generate_product_embeddings(
        self, 
        store_id: str,
        batch_size: int = 50,
        force_regenerate: bool = False
    ) -> Dict[str, Any]:
        """Generate embeddings for all products in a store."""
        
        async with self.db_provider.get_connection() as conn:
            try:
                # స్టోర్ సందర్భాన్ని సెట్ చేయండి
                await conn.execute("SELECT retail.set_store_context($1)", store_id)
                
                # ఎంబెడ్డింగ్స్ అవసరమైన ఉత్పత్తులను పొందండి
                if force_regenerate:
                    products_query = """
                        SELECT 
                            p.product_id,
                            p.product_name,
                            p.product_description,
                            p.brand,
                            pc.category_name,
                            array_to_string(p.tags, ' ') as tags_text
                        FROM retail.products p
                        LEFT JOIN retail.product_categories pc ON p.category_id = pc.category_id
                        WHERE p.is_active = TRUE
                        ORDER BY p.created_at DESC
                    """
                else:
                    products_query = """
                        SELECT 
                            p.product_id,
                            p.product_name,
                            p.product_description,
                            p.brand,
                            pc.category_name,
                            array_to_string(p.tags, ' ') as tags_text
                        FROM retail.products p
                        LEFT JOIN retail.product_categories pc ON p.category_id = pc.category_id
                        LEFT JOIN retail.product_embeddings pe ON p.product_id = pe.product_id
                        WHERE p.is_active = TRUE
                          AND (pe.product_id IS NULL OR pe.updated_at < p.updated_at)
                        ORDER BY p.created_at DESC
                    """
                
                products = await conn.fetch(products_query)
                
                if not products:
                    return {
                        'success': True,
                        'message': 'No products need embedding generation',
                        'processed_count': 0,
                        'store_id': store_id
                    }
                
                logger.info(f"Generating embeddings for {len(products)} products in store {store_id}")
                
                # ఉత్పత్తులను బ్యాచ్‌లలో ప్రాసెస్ చేయండి
                processed_count = 0
                
                for i in range(0, len(products), batch_size):
                    batch = products[i:i + batch_size]
                    await self._process_product_batch(conn, batch, store_id)
                    processed_count += len(batch)
                    
                    logger.info(f"Processed {processed_count}/{len(products)} products")
                
                return {
                    'success': True,
                    'message': f'Successfully generated embeddings for {processed_count} products',
                    'processed_count': processed_count,
                    'store_id': store_id,
                    'total_products': len(products)
                }
                
            except Exception as e:
                logger.error(f"Product embedding generation failed: {e}")
                return {
                    'success': False,
                    'error': str(e),
                    'store_id': store_id
                }
    
    async def _process_product_batch(
        self, 
        conn: asyncpg.Connection, 
        products: List[Dict], 
        store_id: str
    ):
        """Process a batch of products for embedding generation."""
        
        # ఎంబెడ్డింగ్ కోసం టెక్స్ట్‌లను సిద్ధం చేయండి
        texts = []
        product_ids = []
        
        for product in products:
            # ఉత్పత్తి సమాచారాన్ని శోధించదగిన టెక్స్ట్‌గా కలపండి
            combined_text = self._create_product_text(product)
            texts.append(combined_text)
            product_ids.append(product['product_id'])
        
        # ఎంబెడ్డింగ్స్ సృష్టించండి
        embeddings = await self.embedding_manager.generate_embeddings_batch(texts)
        
        # డేటాబేస్‌లో ఎంబెడ్డింగ్స్ నిల్వ చేయండి
        for i, (product_id, embedding) in enumerate(zip(product_ids, embeddings)):
            if embedding:  # విఫలమైన ఎంబెడ్డింగ్స్‌ను దాటవేయండి
                await self._store_product_embedding(
                    conn, 
                    product_id, 
                    store_id, 
                    texts[i], 
                    embedding
                )
    
    def _create_product_text(self, product: Dict[str, Any]) -> str:
        """Create combined text for product embedding."""
        
        # None విలువలను నిర్వహించండి
        product_name = product.get('product_name') or ''
        brand = product.get('brand') or ''
        description = product.get('product_description') or ''
        category = product.get('category_name') or ''
        tags = product.get('tags_text') or ''
        
        # శోధించదగిన టెక్స్ట్‌గా కలపండి
        combined_text = self.text_template.format(
            product_name=product_name,
            brand=brand,
            description=description,
            category=category,
            tags=tags
        )
        
        # అదనపు ఖాళీలను శుభ్రపరచండి
        return ' '.join(combined_text.split())
    
    async def _store_product_embedding(
        self,
        conn: asyncpg.Connection,
        product_id: str,
        store_id: str,
        embedding_text: str,
        embedding: List[float]
    ):
        """Store product embedding in database."""
        
        # ఎంబెడ్డింగ్‌ను pgvector ఫార్మాట్‌కు మార్చండి
        embedding_vector = f"[{','.join(map(str, embedding))}]"
        
        # ఎంబెడ్డింగ్‌ను అప్‌సర్ట్ చేయండి
        upsert_query = """
            INSERT INTO retail.product_embeddings (
                product_id, store_id, embedding_text, embedding, embedding_model
            ) VALUES ($1, $2, $3, $4, $5)
            ON CONFLICT (product_id, embedding_model) 
            DO UPDATE SET
                store_id = EXCLUDED.store_id,
                embedding_text = EXCLUDED.embedding_text,
                embedding = EXCLUDED.embedding,
                updated_at = CURRENT_TIMESTAMP
        """
        
        await conn.execute(
            upsert_query,
            product_id,
            store_id,
            embedding_text,
            embedding_vector,
            self.embedding_manager.deployment_name
        )
    
    async def update_product_embedding(
        self, 
        product_id: str, 
        store_id: str
    ) -> Dict[str, Any]:
        """Update embedding for a single product."""
        
        async with self.db_provider.get_connection() as conn:
            try:
                # స్టోర్ సందర్భాన్ని సెట్ చేయండి
                await conn.execute("SELECT retail.set_store_context($1)", store_id)
                
                # ఉత్పత్తి సమాచారాన్ని పొందండి
                product_query = """
                    SELECT 
                        p.product_id,
                        p.product_name,
                        p.product_description,
                        p.brand,
                        pc.category_name,
                        array_to_string(p.tags, ' ') as tags_text
                    FROM retail.products p
                    LEFT JOIN retail.product_categories pc ON p.category_id = pc.category_id
                    WHERE p.product_id = $1 AND p.is_active = TRUE
                """
                
                product = await conn.fetchrow(product_query, product_id)
                
                if not product:
                    return {
                        'success': False,
                        'error': f'Product {product_id} not found or inactive'
                    }
                
                # ఎంబెడ్డింగ్ సృష్టించండి
                combined_text = self._create_product_text(dict(product))
                embedding = await self.embedding_manager.generate_embedding(combined_text)
                
                # ఎంబెడ్డింగ్ నిల్వ చేయండి
                await self._store_product_embedding(
                    conn, product_id, store_id, combined_text, embedding
                )
                
                return {
                    'success': True,
                    'message': f'Successfully updated embedding for product {product_id}',
                    'product_id': product_id,
                    'store_id': store_id
                }
                
            except Exception as e:
                logger.error(f"Single product embedding update failed: {e}")
                return {
                    'success': False,
                    'error': str(e),
                    'product_id': product_id
                }

# గ్లోబల్ ఉత్పత్తి ఎంబెడ్డర్ ఉదాహరణ
product_embedder = ProductEmbedder(db_provider)
```

## 🔎 సేమాంటిక్ సెర్చ్ టూల్స్

### సేమాంటిక్ ఉత్పత్తి సెర్చ్ టూల్

```python
# mcp_server/tools/semantic_search.py
"""
Semantic search tools for natural language product queries.
"""
from typing import Dict, Any, List, Optional
from ..tools.base import DatabaseTool, ToolResult, ToolCategory
from ..embeddings.embedding_manager import embedding_manager
import logging

logger = logging.getLogger(__name__)

class SemanticProductSearchTool(DatabaseTool):
    """Advanced semantic search tool for products using vector similarity."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="semantic_search_products",
            description="Search products using natural language queries with semantic understanding",
            db_provider=db_provider
        )
        self.category = ToolCategory.DATABASE_QUERY
        self.embedding_manager = embedding_manager
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute semantic product search."""
        
        query = kwargs.get('query')
        store_id = kwargs.get('store_id')
        limit = kwargs.get('limit', 20)
        similarity_threshold = kwargs.get('similarity_threshold', 0.7)
        include_metadata = kwargs.get('include_metadata', True)
        
        if not query:
            return ToolResult(
                success=False,
                error="Search query is required"
            )
        
        if not store_id:
            return ToolResult(
                success=False,
                error="store_id is required for semantic search"
            )
        
        try:
            # క్వెరీ ఎంబెడ్డింగ్ సృష్టించండి
            query_embedding = await self.embedding_manager.generate_embedding(query)
            
            # సేమాంటిక్ శోధన నిర్వహించండి
            search_results = await self._perform_semantic_search(
                query_embedding,
                store_id,
                limit,
                similarity_threshold,
                include_metadata
            )
            
            return ToolResult(
                success=True,
                data=search_results,
                row_count=len(search_results),
                metadata={
                    'query': query,
                    'store_id': store_id,
                    'similarity_threshold': similarity_threshold,
                    'search_type': 'semantic'
                }
            )
            
        except Exception as e:
            logger.error(f"Semantic search failed: {e}")
            return ToolResult(
                success=False,
                error=f"Semantic search failed: {str(e)}"
            )
    
    async def _perform_semantic_search(
        self,
        query_embedding: List[float],
        store_id: str,
        limit: int,
        similarity_threshold: float,
        include_metadata: bool
    ) -> List[Dict[str, Any]]:
        """Perform vector similarity search."""
        
        # ఎంబెడ్డింగ్‌ను PostgreSQL వెక్టర్ ఫార్మాట్‌కు మార్చండి
        embedding_vector = f"[{','.join(map(str, query_embedding))}]"
        
        # శోధన క్వెరీని నిర్మించండి
        if include_metadata:
            search_query = """
                SELECT 
                    p.product_id,
                    p.product_name,
                    p.brand,
                    p.price,
                    p.product_description,
                    p.current_stock,
                    p.rating_average,
                    p.rating_count,
                    p.tags,
                    pc.category_name,
                    pe.embedding_text,
                    1 - (pe.embedding <=> $1::vector) as similarity_score
                FROM retail.product_embeddings pe
                JOIN retail.products p ON pe.product_id = p.product_id
                LEFT JOIN retail.product_categories pc ON p.category_id = pc.category_id
                WHERE pe.store_id = $2
                  AND p.is_active = TRUE
                  AND 1 - (pe.embedding <=> $1::vector) >= $3
                ORDER BY pe.embedding <=> $1::vector
                LIMIT $4
            """
        else:
            search_query = """
                SELECT 
                    p.product_id,
                    p.product_name,
                    p.brand,
                    p.price,
                    1 - (pe.embedding <=> $1::vector) as similarity_score
                FROM retail.product_embeddings pe
                JOIN retail.products p ON pe.product_id = p.product_id
                WHERE pe.store_id = $2
                  AND p.is_active = TRUE
                  AND 1 - (pe.embedding <=> $1::vector) >= $3
                ORDER BY pe.embedding <=> $1::vector
                LIMIT $4
            """
        
        async with self.get_connection() as conn:
            # స్టోర్ సందర్భాన్ని సెట్ చేయండి
            await conn.execute("SELECT retail.set_store_context($1)", store_id)
            
            # శోధనను అమలు చేయండి
            results = await conn.fetch(
                search_query,
                embedding_vector,
                store_id,
                similarity_threshold,
                limit
            )
            
            return [dict(result) for result in results]
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for semantic search tool."""
        
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Natural language search query",
                    "minLength": 1,
                    "maxLength": 500
                },
                "store_id": {
                    "type": "string",
                    "description": "Store ID for search scope",
                    "pattern": "^[a-zA-Z0-9_-]+$"
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of results to return",
                    "minimum": 1,
                    "maximum": 100,
                    "default": 20
                },
                "similarity_threshold": {
                    "type": "number",
                    "description": "Minimum similarity score (0.0 to 1.0)",
                    "minimum": 0.0,
                    "maximum": 1.0,
                    "default": 0.7
                },
                "include_metadata": {
                    "type": "boolean",
                    "description": "Include detailed product metadata in results",
                    "default": True
                }
            },
            "required": ["query", "store_id"],
            "additionalProperties": False
        }

class HybridSearchTool(DatabaseTool):
    """Hybrid search combining traditional keyword and semantic search."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="hybrid_product_search",
            description="Hybrid search combining keyword matching and semantic similarity for optimal results",
            db_provider=db_provider
        )
        self.category = ToolCategory.DATABASE_QUERY
        self.embedding_manager = embedding_manager
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute hybrid product search."""
        
        query = kwargs.get('query')
        store_id = kwargs.get('store_id')
        limit = kwargs.get('limit', 20)
        semantic_weight = kwargs.get('semantic_weight', 0.7)
        keyword_weight = kwargs.get('keyword_weight', 0.3)
        
        if not query:
            return ToolResult(
                success=False,
                error="Search query is required"
            )
        
        if not store_id:
            return ToolResult(
                success=False,
                error="store_id is required for hybrid search"
            )
        
        try:
            # సేమాంటిక్ శోధన కోసం క్వెరీ ఎంబెడ్డింగ్ సృష్టించండి
            query_embedding = await self.embedding_manager.generate_embedding(query)
            
            # హైబ్రిడ్ శోధన నిర్వహించండి
            search_results = await self._perform_hybrid_search(
                query,
                query_embedding,
                store_id,
                limit,
                semantic_weight,
                keyword_weight
            )
            
            return ToolResult(
                success=True,
                data=search_results,
                row_count=len(search_results),
                metadata={
                    'query': query,
                    'store_id': store_id,
                    'semantic_weight': semantic_weight,
                    'keyword_weight': keyword_weight,
                    'search_type': 'hybrid'
                }
            )
            
        except Exception as e:
            logger.error(f"Hybrid search failed: {e}")
            return ToolResult(
                success=False,
                error=f"Hybrid search failed: {str(e)}"
            )
    
    async def _perform_hybrid_search(
        self,
        query: str,
        query_embedding: List[float],
        store_id: str,
        limit: int,
        semantic_weight: float,
        keyword_weight: float
    ) -> List[Dict[str, Any]]:
        """Perform hybrid search combining keyword and semantic similarity."""
        
        # ఎంబెడ్డింగ్‌ను PostgreSQL వెక్టర్ ఫార్మాట్‌కు మార్చండి
        embedding_vector = f"[{','.join(map(str, query_embedding))}]"
        
        # కీవర్డ్ మ్యాచ్ కోసం శోధన పదాలు సృష్టించండి
        search_terms = ' & '.join(query.lower().split())
        
        hybrid_query = """
            WITH keyword_scores AS (
                SELECT 
                    p.product_id,
                    ts_rank(
                        to_tsvector('english', 
                            p.product_name || ' ' || 
                            COALESCE(p.product_description, '') || ' ' || 
                            COALESCE(p.brand, '') || ' ' ||
                            COALESCE(array_to_string(p.tags, ' '), '')
                        ),
                        plainto_tsquery('english', $2)
                    ) as keyword_score
                FROM retail.products p
                WHERE p.is_active = TRUE
                  AND p.store_id = $3
                  AND (
                    to_tsvector('english', 
                        p.product_name || ' ' || 
                        COALESCE(p.product_description, '') || ' ' || 
                        COALESCE(p.brand, '') || ' ' ||
                        COALESCE(array_to_string(p.tags, ' '), '')
                    ) @@ plainto_tsquery('english', $2)
                    OR p.product_name ILIKE '%' || $2 || '%'
                    OR p.brand ILIKE '%' || $2 || '%'
                  )
            ),
            semantic_scores AS (
                SELECT 
                    pe.product_id,
                    1 - (pe.embedding <=> $1::vector) as semantic_score
                FROM retail.product_embeddings pe
                WHERE pe.store_id = $3
                  AND 1 - (pe.embedding <=> $1::vector) >= 0.5
            ),
            combined_scores AS (
                SELECT 
                    COALESCE(ks.product_id, ss.product_id) as product_id,
                    COALESCE(ks.keyword_score, 0) * $4 as weighted_keyword_score,
                    COALESCE(ss.semantic_score, 0) * $5 as weighted_semantic_score,
                    COALESCE(ks.keyword_score, 0) * $4 + COALESCE(ss.semantic_score, 0) * $5 as combined_score
                FROM keyword_scores ks
                FULL OUTER JOIN semantic_scores ss ON ks.product_id = ss.product_id
                WHERE COALESCE(ks.keyword_score, 0) * $4 + COALESCE(ss.semantic_score, 0) * $5 > 0
            )
            SELECT 
                p.product_id,
                p.product_name,
                p.brand,
                p.price,
                p.product_description,
                p.current_stock,
                p.rating_average,
                p.rating_count,
                p.tags,
                pc.category_name,
                cs.weighted_keyword_score,
                cs.weighted_semantic_score,
                cs.combined_score
            FROM combined_scores cs
            JOIN retail.products p ON cs.product_id = p.product_id
            LEFT JOIN retail.product_categories pc ON p.category_id = pc.category_id
            WHERE p.is_active = TRUE
            ORDER BY cs.combined_score DESC
            LIMIT $6
        """
        
        async with self.get_connection() as conn:
            # స్టోర్ సందర్భాన్ని సెట్ చేయండి
            await conn.execute("SELECT retail.set_store_context($1)", store_id)
            
            # హైబ్రిడ్ శోధనను అమలు చేయండి
            results = await conn.fetch(
                hybrid_query,
                embedding_vector,  # $1
                query,            # $2
                store_id,         # $3
                keyword_weight,   # $4
                semantic_weight,  # $5
                limit            # $6
            )
            
            return [dict(result) for result in results]
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for hybrid search tool."""
        
        return {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Search query (supports both keywords and natural language)",
                    "minLength": 1,
                    "maxLength": 500
                },
                "store_id": {
                    "type": "string",
                    "description": "Store ID for search scope",
                    "pattern": "^[a-zA-Z0-9_-]+$"
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of results to return",
                    "minimum": 1,
                    "maximum": 100,
                    "default": 20
                },
                "semantic_weight": {
                    "type": "number",
                    "description": "Weight for semantic similarity (0.0 to 1.0)",
                    "minimum": 0.0,
                    "maximum": 1.0,
                    "default": 0.7
                },
                "keyword_weight": {
                    "type": "number",
                    "description": "Weight for keyword matching (0.0 to 1.0)",
                    "minimum": 0.0,
                    "maximum": 1.0,
                    "default": 0.3
                }
            },
            "required": ["query", "store_id"],
            "additionalProperties": False
        }
```

## 🎯 సిఫార్సు వ్యవస్థలు

### ఉత్పత్తి సిఫార్సు ఇంజిన్

```python
# mcp_server/tools/recommendations.py
"""
Product recommendation system using embedding similarity.
"""
from typing import Dict, Any, List, Optional
from ..tools.base import DatabaseTool, ToolResult, ToolCategory
import logging

logger = logging.getLogger(__name__)

class ProductRecommendationTool(DatabaseTool):
    """Generate product recommendations based on similarity and user behavior."""
    
    def __init__(self, db_provider):
        super().__init__(
            name="get_product_recommendations",
            description="Generate personalized product recommendations using similarity analysis",
            db_provider=db_provider
        )
        self.category = ToolCategory.ANALYTICS
    
    async def execute(self, **kwargs) -> ToolResult:
        """Execute product recommendation generation."""
        
        recommendation_type = kwargs.get('type', 'similar_products')
        store_id = kwargs.get('store_id')
        
        if not store_id:
            return ToolResult(
                success=False,
                error="store_id is required for recommendations"
            )
        
        try:
            if recommendation_type == 'similar_products':
                return await self._get_similar_products(kwargs)
            elif recommendation_type == 'customer_based':
                return await self._get_customer_recommendations(kwargs)
            elif recommendation_type == 'trending':
                return await self._get_trending_products(kwargs)
            elif recommendation_type == 'cross_sell':
                return await self._get_cross_sell_recommendations(kwargs)
            else:
                return ToolResult(
                    success=False,
                    error=f"Unknown recommendation type: {recommendation_type}"
                )
        
        except Exception as e:
            logger.error(f"Product recommendation failed: {e}")
            return ToolResult(
                success=False,
                error=f"Recommendation generation failed: {str(e)}"
            )
    
    async def _get_similar_products(self, kwargs: Dict[str, Any]) -> ToolResult:
        """Get products similar to a given product using embedding similarity."""
        
        product_id = kwargs.get('product_id')
        store_id = kwargs['store_id']
        limit = kwargs.get('limit', 10)
        similarity_threshold = kwargs.get('similarity_threshold', 0.7)
        
        if not product_id:
            return ToolResult(
                success=False,
                error="product_id is required for similar product recommendations"
            )
        
        similar_products_query = """
            WITH target_product AS (
                SELECT embedding
                FROM retail.product_embeddings
                WHERE product_id = $1 AND store_id = $2
            )
            SELECT 
                p.product_id,
                p.product_name,
                p.brand,
                p.price,
                p.product_description,
                p.rating_average,
                p.rating_count,
                pc.category_name,
                1 - (pe.embedding <=> tp.embedding) as similarity_score
            FROM retail.product_embeddings pe
            CROSS JOIN target_product tp
            JOIN retail.products p ON pe.product_id = p.product_id
            LEFT JOIN retail.product_categories pc ON p.category_id = pc.category_id
            WHERE pe.store_id = $2
              AND pe.product_id != $1  -- Exclude the target product itself
              AND p.is_active = TRUE
              AND 1 - (pe.embedding <=> tp.embedding) >= $3
            ORDER BY pe.embedding <=> tp.embedding
            LIMIT $4
        """
        
        result = await self.execute_query(
            similar_products_query,
            (product_id, store_id, similarity_threshold, limit),
            store_id
        )
        
        if result.success:
            result.metadata = {
                'recommendation_type': 'similar_products',
                'target_product_id': product_id,
                'similarity_threshold': similarity_threshold,
                'store_id': store_id
            }
        
        return result
    
    async def _get_customer_recommendations(self, kwargs: Dict[str, Any]) -> ToolResult:
        """Get personalized recommendations based on customer purchase history."""
        
        customer_id = kwargs.get('customer_id')
        store_id = kwargs['store_id']
        limit = kwargs.get('limit', 10)
        days_back = kwargs.get('days_back', 90)
        
        if not customer_id:
            return ToolResult(
                success=False,
                error="customer_id is required for customer-based recommendations"
            )
        
        customer_recommendations_query = """
            WITH customer_purchases AS (
                -- Get products purchased by the customer
                SELECT DISTINCT p.product_id, pe.embedding
                FROM retail.sales_transactions st
                JOIN retail.sales_transaction_items sti ON st.transaction_id = sti.transaction_id
                JOIN retail.products p ON sti.product_id = p.product_id
                JOIN retail.product_embeddings pe ON p.product_id = pe.product_id
                WHERE st.customer_id = $1
                  AND st.transaction_date >= CURRENT_DATE - INTERVAL '%s days'
                  AND st.transaction_type = 'sale'
            ),
            avg_customer_embedding AS (
                -- Calculate average embedding vector for customer preferences
                SELECT 
                    (
                        SELECT ARRAY(
                            SELECT AVG(embedding_element)
                            FROM customer_purchases cp,
                                 LATERAL unnest(cp.embedding) WITH ORDINALITY AS t(embedding_element, ordinality)
                            GROUP BY ordinality
                            ORDER BY ordinality
                        )
                    )::vector as avg_embedding
                FROM (SELECT 1) dummy
                WHERE EXISTS (SELECT 1 FROM customer_purchases)
            )
            SELECT 
                p.product_id,
                p.product_name,
                p.brand,
                p.price,
                p.product_description,
                p.rating_average,
                p.rating_count,
                pc.category_name,
                1 - (pe.embedding <=> ace.avg_embedding) as preference_score
            FROM retail.product_embeddings pe
            CROSS JOIN avg_customer_embedding ace
            JOIN retail.products p ON pe.product_id = p.product_id
            LEFT JOIN retail.product_categories pc ON p.category_id = pc.category_id
            WHERE pe.store_id = $2
              AND p.is_active = TRUE
              AND pe.product_id NOT IN (SELECT product_id FROM customer_purchases)
              AND 1 - (pe.embedding <=> ace.avg_embedding) >= 0.6
            ORDER BY pe.embedding <=> ace.avg_embedding
            LIMIT $3
        """ % days_back
        
        result = await self.execute_query(
            customer_recommendations_query,
            (customer_id, store_id, limit),
            store_id
        )
        
        if result.success:
            result.metadata = {
                'recommendation_type': 'customer_based',
                'customer_id': customer_id,
                'days_back': days_back,
                'store_id': store_id
            }
        
        return result
    
    def get_input_schema(self) -> Dict[str, Any]:
        """Get input schema for recommendation tool."""
        
        return {
            "type": "object",
            "properties": {
                "type": {
                    "type": "string",
                    "enum": ["similar_products", "customer_based", "trending", "cross_sell"],
                    "description": "Type of recommendation to generate",
                    "default": "similar_products"
                },
                "store_id": {
                    "type": "string",
                    "description": "Store ID for recommendations",
                    "pattern": "^[a-zA-Z0-9_-]+$"
                },
                "product_id": {
                    "type": "string",
                    "description": "Product ID for similar product recommendations"
                },
                "customer_id": {
                    "type": "string",
                    "description": "Customer ID for personalized recommendations"
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum number of recommendations",
                    "minimum": 1,
                    "maximum": 50,
                    "default": 10
                },
                "similarity_threshold": {
                    "type": "number",
                    "description": "Minimum similarity score",
                    "minimum": 0.0,
                    "maximum": 1.0,
                    "default": 0.7
                },
                "days_back": {
                    "type": "integer",
                    "description": "Days of purchase history to consider",
                    "minimum": 1,
                    "maximum": 365,
                    "default": 90
                }
            },
            "required": ["store_id"],
            "additionalProperties": False
        }
```

## ⚡ పనితీరు ఆప్టిమైజేషన్

### వెక్టర్ ప్రశ్న ఆప్టిమైజేషన్

```sql
-- Optimize pgvector performance
-- Add to postgresql.conf

# Increase work_mem for vector operations
work_mem = '256MB'

# Optimize shared_buffers for vector data
shared_buffers = '512MB'

# Enable parallel query execution
max_parallel_workers_per_gather = 4
max_parallel_workers = 8

# Vector-specific optimizations
SET maintenance_work_mem = '1GB';
SET max_parallel_maintenance_workers = 4;

-- Optimize HNSW index parameters
CREATE INDEX CONCURRENTLY idx_product_embeddings_vector_optimized 
ON retail.product_embeddings 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 200);

-- Create partial indexes for active products only
CREATE INDEX CONCURRENTLY idx_product_embeddings_active
ON retail.product_embeddings 
USING hnsw (embedding vector_cosine_ops)
WHERE store_id IN (SELECT store_id FROM retail.stores WHERE is_active = TRUE);

-- Analyze vector distribution for optimization
ANALYZE retail.product_embeddings;

-- Vector search performance monitoring
CREATE OR REPLACE FUNCTION retail.analyze_vector_performance()
RETURNS TABLE (
    avg_search_time_ms NUMERIC,
    index_size TEXT,
    total_vectors BIGINT,
    cache_hit_ratio NUMERIC
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        (SELECT AVG(EXTRACT(MILLISECONDS FROM clock_timestamp() - query_start))
         FROM pg_stat_activity 
         WHERE query LIKE '%embedding <=> %'
         AND state = 'active') as avg_search_time_ms,
        pg_size_pretty(pg_relation_size('idx_product_embeddings_vector')) as index_size,
        COUNT(*)::BIGINT as total_vectors,
        (SELECT 100.0 * blks_hit / (blks_hit + blks_read) 
         FROM pg_stat_user_indexes 
         WHERE indexrelname = 'idx_product_embeddings_vector') as cache_hit_ratio
    FROM retail.product_embeddings;
END;
$$ LANGUAGE plpgsql;
```

### ఎంబెడ్డింగ్ క్యాష్ వ్యూహం

```python
# mcp_server/embeddings/cache_manager.py
"""
Advanced caching strategy for embeddings and search results.
"""
import redis.asyncio as redis
import json
import hashlib
from typing import Dict, Any, List, Optional
from datetime import timedelta
import logging

logger = logging.getLogger(__name__)

class EmbeddingCacheManager:
    """Advanced caching for embeddings and search results."""
    
    def __init__(self, redis_url: str = "redis://localhost:6379"):
        self.redis_client = None
        self.redis_url = redis_url
        
        # క్యాష్ TTL సెట్టింగ్స్
        self.embedding_ttl = timedelta(days=7)  # 1 వారం పాటు ఎంబెడ్డింగ్స్ క్యాష్ చేయబడింది
        self.search_ttl = timedelta(hours=1)    # 1 గంట పాటు శోధన ఫలితాలు క్యాష్ చేయబడింది
        self.recommendation_ttl = timedelta(hours=4)  # 4 గంటలు పాటు సిఫార్సులు క్యాష్ చేయబడింది
        
        # క్యాష్ కీ ప్రిఫిక్సులు
        self.EMBEDDING_PREFIX = "emb:"
        self.SEARCH_PREFIX = "search:"
        self.RECOMMENDATION_PREFIX = "rec:"
    
    async def initialize(self):
        """Initialize Redis connection."""
        
        try:
            self.redis_client = redis.from_url(self.redis_url)
            # కనెక్షన్ పరీక్షించండి
            await self.redis_client.ping()
            logger.info("Embedding cache manager initialized")
        
        except Exception as e:
            logger.warning(f"Redis cache not available: {e}")
            self.redis_client = None
    
    async def cache_embedding(self, text: str, embedding: List[float], model: str):
        """Cache text embedding."""
        
        if not self.redis_client:
            return
        
        try:
            cache_key = self._get_embedding_key(text, model)
            cache_data = {
                'embedding': embedding,
                'model': model,
                'cached_at': str(datetime.utcnow())
            }
            
            await self.redis_client.setex(
                cache_key,
                self.embedding_ttl,
                json.dumps(cache_data)
            )
            
        except Exception as e:
            logger.warning(f"Failed to cache embedding: {e}")
    
    async def get_cached_embedding(self, text: str, model: str) -> Optional[List[float]]:
        """Get cached embedding."""
        
        if not self.redis_client:
            return None
        
        try:
            cache_key = self._get_embedding_key(text, model)
            cached_data = await self.redis_client.get(cache_key)
            
            if cached_data:
                data = json.loads(cached_data)
                return data['embedding']
        
        except Exception as e:
            logger.warning(f"Failed to retrieve cached embedding: {e}")
        
        return None
    
    async def cache_search_results(
        self, 
        query: str, 
        store_id: str, 
        results: List[Dict],
        search_params: Dict[str, Any]
    ):
        """Cache search results."""
        
        if not self.redis_client:
            return
        
        try:
            cache_key = self._get_search_key(query, store_id, search_params)
            cache_data = {
                'results': results,
                'query': query,
                'store_id': store_id,
                'params': search_params,
                'cached_at': str(datetime.utcnow())
            }
            
            await self.redis_client.setex(
                cache_key,
                self.search_ttl,
                json.dumps(cache_data, default=str)
            )
            
        except Exception as e:
            logger.warning(f"Failed to cache search results: {e}")
    
    async def get_cached_search_results(
        self, 
        query: str, 
        store_id: str, 
        search_params: Dict[str, Any]
    ) -> Optional[List[Dict]]:
        """Get cached search results."""
        
        if not self.redis_client:
            return None
        
        try:
            cache_key = self._get_search_key(query, store_id, search_params)
            cached_data = await self.redis_client.get(cache_key)
            
            if cached_data:
                data = json.loads(cached_data)
                return data['results']
        
        except Exception as e:
            logger.warning(f"Failed to retrieve cached search results: {e}")
        
        return None
    
    def _get_embedding_key(self, text: str, model: str) -> str:
        """Generate cache key for embedding."""
        
        content = f"{model}:{text.strip()}"
        hash_key = hashlib.sha256(content.encode()).hexdigest()
        return f"{self.EMBEDDING_PREFIX}{hash_key}"
    
    def _get_search_key(self, query: str, store_id: str, params: Dict[str, Any]) -> str:
        """Generate cache key for search results."""
        
        # క్వెరీ మరియు పారామితుల నుండి స్థిరమైన హ్యాష్ సృష్టించండి
        content = f"{query}:{store_id}:{json.dumps(params, sort_keys=True)}"
        hash_key = hashlib.sha256(content.encode()).hexdigest()
        return f"{self.SEARCH_PREFIX}{hash_key}"
    
    async def invalidate_store_cache(self, store_id: str):
        """Invalidate all cached data for a store."""
        
        if not self.redis_client:
            return
        
        try:
            # స్టోర్‌కు సంబంధించిన అన్ని కీలు కనుగొనండి
            pattern = f"*:{store_id}:*"
            keys = await self.redis_client.keys(pattern)
            
            if keys:
                await self.redis_client.delete(*keys)
                logger.info(f"Invalidated {len(keys)} cache entries for store {store_id}")
        
        except Exception as e:
            logger.warning(f"Failed to invalidate store cache: {e}")
    
    async def cleanup(self):
        """Cleanup cache resources."""
        
        if self.redis_client:
            await self.redis_client.close()

# గ్లోబల్ క్యాష్ మేనేజర్
cache_manager = EmbeddingCacheManager()
```

## 🎯 ముఖ్యమైన పాఠాలు

ఈ ల్యాబ్ పూర్తి చేసిన తర్వాత, మీరు కలిగి ఉండాలి:

✅ **Azure OpenAI ఇంటిగ్రేషన్**: క్యాషింగ్ మరియు ఆప్టిమైజేషన్‌తో పూర్తి ఎంబెడ్డింగ్ జనరేషన్  
✅ **వెక్టర్ సెర్చ్ అమలు**: pgvector తో ఉత్పత్తి-సిద్ధమైన సేమాంటిక్ సెర్చ్  
✅ **హైబ్రిడ్ సెర్చ్ సామర్థ్యాలు**: ఉత్తమ ఫలితాల కోసం కీవర్డ్ మరియు సేమాంటిక్ సెర్చ్ కలయిక  
✅ **సిఫార్సు వ్యవస్థలు**: సారూప్యత ఆధారిత AI-శక్తివంతమైన ఉత్పత్తి సిఫార్సులు  
✅ **పనితీరు ఆప్టిమైజేషన్**: వెక్టర్ సూచిక ఆప్టిమైజేషన్ మరియు తెలివైన క్యాషింగ్  
✅ **స్కేలబుల్ ఆర్కిటెక్చర్**: ఎంటర్ప్రైజ్-సిద్ధమైన సేమాంటిక్ సెర్చ్ మౌలిక సదుపాయాలు  

## 🚀 తదుపరి ఏమిటి

**[ల్యాబ్ 08: టెస్టింగ్ మరియు డీబగ్గింగ్](../08-Testing/README.md)** తో కొనసాగండి:

- సేమాంటిక్ సెర్చ్ కోసం సమగ్ర టెస్టింగ్ వ్యూహాలను అమలు చేయండి  
- వెక్టర్ సెర్చ్ పనితీరు సమస్యలను డీబగ్ చేయండి  
- ఎంబెడ్డింగ్ నాణ్యత మరియు సంబంధితతను ధృవీకరించండి  
- సిఫార్సు వ్యవస్థ ఖచ్చితత్వాన్ని పరీక్షించండి  

## 📚 అదనపు వనరులు

### Azure OpenAI
- [Azure OpenAI సర్వీస్ డాక్యుమెంటేషన్](https://docs.microsoft.com/azure/cognitive-services/openai/) - పూర్తి సర్వీస్ గైడ్  
- [ఎంబెడ్డింగ్స్ API రిఫరెన్స్](https://platform.openai.com/docs/api-reference/embeddings) - API డాక్యుమెంటేషన్  
- [ఎంబెడ్డింగ్స్ కోసం ఉత్తమ పద్ధతులు](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings) - అమలు మార్గదర్శకాలు  

### వెక్టర్ డేటాబేసులు
- [pgvector డాక్యుమెంటేషన్](https://github.com/pgvector/pgvector) - PostgreSQL వెక్టర్ ఎక్స్‌టెన్షన్  
- [వెక్టర్ సెర్చ్ ఆప్టిమైజేషన్](https://www.pinecone.io/learn/vector-search-optimization/) - పనితీరు ట్యూనింగ్  
- [HNSW అల్గోరిథం](https://arxiv.org/abs/1603.09320) - హైయరార్కికల్ నావిగబుల్ స్మాల్ వరల్డ్ గ్రాఫ్స్  

### సేమాంటిక్ సెర్చ్
- [ఇన్ఫర్మేషన్ రిట్రీవల్ ఫండమెంటల్స్](https://nlp.stanford.edu/IR-book/) - స్టాన్ఫర్డ్ IR పాఠ్యపుస్తకం  
- [వెక్టర్ సెర్చ్ ఉత్తమ పద్ధతులు](https://weaviate.io/blog/vector-search-best-practices) - అమలు నమూనాలు  
- [హైబ్రిడ్ సెర్చ్ వ్యూహాలు](https://blog.vespa.ai/hybrid-search/) - వేర్వేరు సెర్చ్ విధానాల కలయిక  

---

**మునుపటి**: [ల్యాబ్ 06: టూల్ డెవలప్‌మెంట్](../06-Tools/README.md)  
**తదుపరి**: [ల్యాబ్ 08: టెస్టింగ్ మరియు డీబగ్గింగ్](../08-Testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ డాక్యుమెంట్‌ను AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పులు ఉండవచ్చు. మూల డాక్యుమెంట్ దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->