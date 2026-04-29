# ការលៃតម្រូវស្វែងរកសមាសភាព អត្តបទ

## 🎯 អ្វីដែលមន្ទីរពិសោធន៍នេះគ្របដណ្តប់

មន្ទីរពិសោធន៍នេះផ្តល់ជូនការណែនាំលម្អិតអំពីការអនុវត្តសមត្ថភាពស្វែងរកសមាសភាពដោយប្រើ Azure OpenAI embeddings និងកម្មវិធីបន្ថែម pgvector របស់ PostgreSQL។ អ្នកនឹងរៀនរបៀបបង្កើតការស្វែងរកផលិតផលដែលបង្កើតដោយ AI ដែលអាចយល់បានសំណួរភាសាធម្មជាតិ និងផ្ដល់លទ្ធផលដែលពាក់ព័ន្ធដោយផ្អែកលើសមត្ថភាពស្មើសម្រង់អត្តបទ។

## ទិដ្ឋភាពទូទៅ

ការស្វែងរកផ្អែកលើពាក្យគន្លឹះក្នុងរបៀបបុរាណជាញឹកញាប់មិនអាចចាប់យល់បំណងអ្នកប្រើ និងន័យដ៏ស្មុគស្មាញបាន។ ការស្វែងរកសមាសភាពដោយប្រើ vector embeddings អនុញ្ញាតឱ្យសំណួរភាសាធម្មជាតិដូចជា "ស្បែកជើងរត់ដែលមានការពាក់ពាន់សមស្របសម្រាប់អាកាសធាតុភ្លៀង" រកឃើញផលិតផលដែលពាក់ព័ន្ធទោះបីពាក្យទាំងនោះមិនបង្ហាញក្នុងការពិពណ៌នាផលិតផលដោយផ្ទាល់ក៏ដោយ។

ការអនុវត្តរបស់យើងរួមបញ្ចូលគ្នាចន្លោះម៉ូដែល embedding សមត្ថភាពខ្លាំងរបស់ Azure OpenAI ជាមួយកម្មវិធីបន្ថែម pgvector របស់ PostgreSQL ដើម្បីបង្កើតប្រព័ន្ធស្វែងរកសមាសភាពមានសមត្ថភាពខ្ពស់ និងអាចជាធាតុដំណើរការឧស្សាហកម្មដែលពង្រីកបានទំហំ ដែលលើកកម្ពស់បទពិសោធន៍លក់រាយជាមួយការស្វែងរកផលិតផលដោយប្រាជ្ញា។

## គោលបំណងការរៀន

នៅចុងបញ្ចប់នៃមន្ទីរពិសោធន៍នេះ អ្នកនឹងអាច:

- **បញ្ចូល** ម៉ូដែល embedding របស់ Azure OpenAI សម្រាប់ vectorization អត្ថបទ  
- **អនុវត្ត** pgvector សម្រាប់ប្រតិបត្តិការ​ស្វែងរកស្មើភាពប្រសើរ  
- **បង្កើត** ឧបករណ៍ស្វែងរកសមាសភាពសម្រាប់សំណួរផលិតផលភាសាធម្មជាតិ  
- **បង្កើត** ស្វែងរកផ្សំរវាងទម្រង់បុរាណ និងស្វែងរក vector  
- **បង្កើត** ការអូបទីម៉ាថ៍សំណួរជាវ៉ិចត័រដើម្បីអភិវឌ្ឍកម្លាំងផលិតកម្ម  
- **រចនា** ប្រព័ន្ធផ្តល់អនុសាសន៍ដោយប្រើស្មើភាព embedding  

## 🧠 ស្ថាបត្យកម្មស្វែងរកសមាសភាព

### ប៉ុំពីញស្វែងរកវ៉ិចត័រ

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

### វិធីសាស្រ្តបង្កើត Embedding

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
        
        # ការកំណត់រចនាសម្ព័ន្ធបញ្ចូល
        self.embedding_dimension = 1536  # ទម្រង់ text-embedding-3-small
        self.max_tokens = 8000  # ចំនួនតួអក្សរជាមូលដ្ឋានក្នុងមួយសំណើ
        self.batch_size = 100  # ទំហំក្រុមការងារ
        
        # ការកំណត់រចនាសម្ព័ន្ធផ្ទុកបណ្ដុំ
        self.embedding_cache = {}
        self.cache_ttl = timedelta(hours=24)
        
        # កំណត់អត្រា
        self.rate_limit_requests = 1000  # ក្នុងមួយនាទី
        self.rate_limit_tokens = 150000  # ក្នុងមួយនាទី
        
    async def initialize(self):
        """Initialize the Azure AI client."""
        
        try:
            self.client = AIProjectClient(
                endpoint=self.project_endpoint,
                credential=self.credential
            )
            
            # សាកល្បងការតភ្ជាប់
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
        
        # ពិនិត្យផ្ទុកបណ្ដុំជាចម្បង
        if use_cache:
            cache_key = self._get_cache_key(text)
            cached_embedding = self._get_cached_embedding(cache_key)
            if cached_embedding:
                return cached_embedding
        
        try:
            # ធានាថាអតិថិជនត្រូវបានចាប់ផ្តើម
            if not self.client:
                await self.initialize()
            
            # បង្កើតបញ្ចូល
            response = await self.client.embeddings.create(
                model=self.deployment_name,
                input=text.strip()
            )
            
            embedding = response.data[0].embedding
            
            # ផ្ទុកលទ្ធផល
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
        
        # ពិនិត្យផ្ទុកបណ្ដុំសម្រាប់អត្ថបទរៀងរាល់
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
            
            # តាមដានការខកខានក្នុងផ្ទុកបណ្ដុំ
            embeddings.append(None)  # ទីតាំងទុក
            cache_misses.append(text.strip())
            cache_miss_indices.append(i)
        
        # បង្កើតបញ្ចូលសម្រាប់ការខកខានក្នុងផ្ទុកបណ្ដុំ
        if cache_misses:
            try:
                # ដំណើរការជាក្រុមដើម្បីគោរពដល់ដែនកំណត់ API
                for batch_start in range(0, len(cache_misses), self.batch_size):
                    batch_end = min(batch_start + self.batch_size, len(cache_misses))
                    batch_texts = cache_misses[batch_start:batch_end]
                    
                    # បង្កើតបញ្ចូលជាក្រុម
                    response = await self.client.embeddings.create(
                        model=self.deployment_name,
                        input=batch_texts
                    )
                    
                    # ដំណើរការលទ្ធផលក្រុម
                    for j, embedding_data in enumerate(response.data):
                        actual_index = cache_miss_indices[batch_start + j]
                        embedding = embedding_data.embedding
                        embeddings[actual_index] = embedding
                        
                        # ផ្ទុកលទ្ធផល
                        if use_cache:
                            text = batch_texts[j]
                            cache_key = self._get_cache_key(text)
                            self._cache_embedding(cache_key, embedding)
                    
                    # ការកំណត់អត្រា - ពន្យារពេលតិចម្នាក់រវាងក្រុម
                    if batch_end < len(cache_misses):
                        await asyncio.sleep(0.1)
                
                logger.info(f"Generated {len(cache_misses)} embeddings in batch")
                
            except Exception as e:
                logger.error(f"Batch embedding generation failed: {e}")
                raise
        
        return embeddings
    
    def _get_cache_key(self, text: str) -> str:
        """Generate cache key for text."""
        
        # ប្រើ SHA-256 នៃអត្ថបទ + ម៉ូដែលសម្រាប់ក្តារផ្ទុកតម្លៃផ្ទុកបណ្ដុំ
        content = f"{self.deployment_name}:{text.strip()}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def _get_cached_embedding(self, cache_key: str) -> Optional[List[float]]:
        """Get embedding from cache if not expired."""
        
        if cache_key in self.embedding_cache:
            embedding_data = self.embedding_cache[cache_key]
            
            # ពិនិត្យមើលថាតើការចំរូងផ្ទុកបណ្ដុំតើយោងតាម
            if datetime.now() - embedding_data['timestamp'] < self.cache_ttl:
                return embedding_data['embedding']
            else:
                # លុបការចំរូងផ្ទុកបណ្ដុំផុតកំណត់
                del self.embedding_cache[cache_key]
        
        return None
    
    def _cache_embedding(self, cache_key: str, embedding: List[float]):
        """Cache embedding with timestamp."""
        
        self.embedding_cache[cache_key] = {
            'embedding': embedding,
            'timestamp': datetime.now()
        }
        
        # កំណត់ទំហំផ្ទុកបណ្ដុំ
        if len(self.embedding_cache) > 10000:
            # លុបការចំរូងចាស់បំផុត
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

# ឧបករណ៍គ្រប់គ្រងបញ្ចូលពិភពលោក
embedding_manager = EmbeddingManager(
    project_endpoint=os.getenv('PROJECT_ENDPOINT'),
    deployment_name=os.getenv('EMBEDDING_DEPLOYMENT_NAME', 'text-embedding-3-small')
)
```

## 🔍 ការបង្កើត Embedding ផលិតផល

### ប៉ុំពីញបង្កើត Embedding ស្វ័យប្រវត្តិ

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
        
        # กลยุทธ์การผสมข้อความสำหรับផលិតផល
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
                # ตั้งค่าบริบทร้านค้า
                await conn.execute("SELECT retail.set_store_context($1)", store_id)
                
                # รับផលិតภัณฑ์ที่จำเป็นต้องฝัง
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
                
                # ดำเนินการผลิตภัณฑ์เป็นชุด
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
        
        # เตรียมข้อความสำหรับการฝัง
        texts = []
        product_ids = []
        
        for product in products:
            # รวมข้อมูลผลิตภัณฑ์เป็นข้อความที่ค้นหาได้
            combined_text = self._create_product_text(product)
            texts.append(combined_text)
            product_ids.append(product['product_id'])
        
        # สร้างการฝัง
        embeddings = await self.embedding_manager.generate_embeddings_batch(texts)
        
        # เก็บการฝังในฐานข้อมูล
        for i, (product_id, embedding) in enumerate(zip(product_ids, embeddings)):
            if embedding:  # ข้ามการฝังที่ล้มเหลว
                await self._store_product_embedding(
                    conn, 
                    product_id, 
                    store_id, 
                    texts[i], 
                    embedding
                )
    
    def _create_product_text(self, product: Dict[str, Any]) -> str:
        """Create combined text for product embedding."""
        
        # จัดการค่าที่เป็น None
        product_name = product.get('product_name') or ''
        brand = product.get('brand') or ''
        description = product.get('product_description') or ''
        category = product.get('category_name') or ''
        tags = product.get('tags_text') or ''
        
        # รวมเป็นข้อความที่ค้นหาได้
        combined_text = self.text_template.format(
            product_name=product_name,
            brand=brand,
            description=description,
            category=category,
            tags=tags
        )
        
        # ทำความสะอาดช่องว่างเกิน
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
        
        # แปลงการฝังเป็นรูปแบบ pgvector
        embedding_vector = f"[{','.join(map(str, embedding))}]"
        
        # อัพเซิร์ตการฝัง
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
                # ตั้งค่าบริบทร้านค้า
                await conn.execute("SELECT retail.set_store_context($1)", store_id)
                
                # รับข้อมูลผลิตภัณฑ์
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
                
                # สร้างการฝัง
                combined_text = self._create_product_text(dict(product))
                embedding = await self.embedding_manager.generate_embedding(combined_text)
                
                # เก็บการฝัง
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

# อินสแตนซ์ตัวฝังผลิตภัณฑ์ทั่วโลก
product_embedder = ProductEmbedder(db_provider)
```

## 🔎 ឧបករណ៍ស្វែងរកសមាសភាព

### ឧបករណ៍ស្វែងរកផលិតផលសមាសភាព

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
            # បង្កើត embedding សម្រាប់សំណួរ
            query_embedding = await self.embedding_manager.generate_embedding(query)
            
            # ប្រត្តិបត្ដិការស្វែងរកផ្នែកន័យ
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
        
        # បម្លែង embedding ទៅទ្រង់ទ្រាយវ៉ិចទ័រ PostgreSQL
        embedding_vector = f"[{','.join(map(str, query_embedding))}]"
        
        # បង្កើតសំណួរស្វែងរក
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
            # កំណត់បរិបទហាង
            await conn.execute("SELECT retail.set_store_context($1)", store_id)
            
            # ធ្វើការស្វែងរក
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
            # បង្កើត embedding សម្រាប់សំណួរដើម្បីស្វែងរកផ្នែកន័យ
            query_embedding = await self.embedding_manager.generate_embedding(query)
            
            # ប្រត្តិបត្ដិការស្វែងរកភ្ជាប់
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
        
        # បម្លែង embedding ទៅទ្រង់ទ្រាយវ៉ិចទ័រ PostgreSQL
        embedding_vector = f"[{','.join(map(str, query_embedding))}]"
        
        # បង្កើតពាក្យស្វែងរកសម្រាប់ការផ្គូផ្គងពាក្យគន្លឹះ
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
            # កំណត់បរិបទហាង
            await conn.execute("SELECT retail.set_store_context($1)", store_id)
            
            # ធ្វើការស្វែងរកភ្ជាប់
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

## 🎯 ប្រព័ន្ធផ្តល់អនុសាសន៍

### ម៉ាស៊ីនផ្តល់អនុសាសន៍ផលិតផល

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

## ⚡ ការអូបទីម៉ាថ៍ប្រសិទ្ធភាព

### ការអូបទីម៉ាថ៍សំណួរវ៉ិចត័រ

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

### វិធីសាស្រ្តឃ្លាំង Embedding Cache

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
        
        # ការកំណត់អាយុកាល Cache
        self.embedding_ttl = timedelta(days=7)  # Embeddings ដែលបានរក្សាទុកជាកាសសម្រាប់ 1 សប្តាហ៍
        self.search_ttl = timedelta(hours=1)    # លទ្ធផលស្វែងរកដែលបានរក្សាទុកជាកាសសម្រាប់ 1 ម៉ោង
        self.recommendation_ttl = timedelta(hours=4)  # ការផ្តល់អនុសាសន៍ដែលបានរក្សាទុកជាកាសសម្រាប់ 4 ម៉ោង
        
        # ក្បាលគន្លឹះ Cache
        self.EMBEDDING_PREFIX = "emb:"
        self.SEARCH_PREFIX = "search:"
        self.RECOMMENDATION_PREFIX = "rec:"
    
    async def initialize(self):
        """Initialize Redis connection."""
        
        try:
            self.redis_client = redis.from_url(self.redis_url)
            # សាកល្បងការតភ្ជាប់
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
        
        # បង្កើត hash មុតចុះពីសំណួរនិងប៉ារ៉ាម៉ែត្រ
        content = f"{query}:{store_id}:{json.dumps(params, sort_keys=True)}"
        hash_key = hashlib.sha256(content.encode()).hexdigest()
        return f"{self.SEARCH_PREFIX}{hash_key}"
    
    async def invalidate_store_cache(self, store_id: str):
        """Invalidate all cached data for a store."""
        
        if not self.redis_client:
            return
        
        try:
            # រកគន្លឹះទាំងអស់ដែលទាក់ទងនឹងឃ្លាំង
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

# អ្នកគ្រប់គ្រង cache ពិភពលោក
cache_manager = EmbeddingCacheManager()
```

## 🎯 ចំណុចសំខាន់ៗ

បន្ទាប់ពីបញ្ចប់មន្ទីរពិសោធន៍នេះ អ្នកគួរតែ មាន៖

✅ **ការបញ្ចូល Azure OpenAI**: បញ្ចប់ការបង្កើត embedding ជាមួយCaching និងការអូបទីម៉ាថ៍  
✅ **ការអនុវត្តស្វែងរកវ៉ិចត័រ**: ការស្វែងរកសមាសភាពដែលមានស្រាប់សម្រាប់ផលិតកម្មជាមួយ pgvector  
✅ **សមត្ថភាពស្វែងរកផ្សំ**: ស្វែងរកដោយពាក្យគន្លឹះ និងសមាសភាពសម្រាប់លទ្ធផលល្អបំផុត  
✅ **ប្រព័ន្ធផ្តល់អនុសាសន៍**: ការផ្តល់អនុសាសន៍ផលិតផលដោយ AI ប្រើស្មើភាព   
✅ **ការអូបទីម៉ាថ៍ប្រសិទ្ធភាព**: ការអូបទីម៉ាថ៍សន្ទស្សន៍វ៉ិចត័រ និង caching ដោយប្រាជ្ញា  
✅ **ស្ថាបត្យកម្មអាចពង្រីកបាន**: មូលដ្ឋានស្វែងរកសមាសភាពសម្រាប់ស្ថាប័ន  

## 🚀 បន្ទាប់មក

បន្តជាមួយ **[Lab 08: Testing and Debugging](../08-Testing/README.md)** ដើម្បី:

- អនុវត្តយុទ្ធសាស្ត្រតេស្តទូលំទូលាយសម្រាប់ការស្វែងរកសមាសភាព  
- ស្វែងរកកំហុសប្រសិទ្ធភាពស្វែងរកវ៉ិចត័រ  
- បញ្ជាក់គុណភាព និងភាពពាក់ព័ន្ធនៃ embedding  
- ពិនិត្យភាពត្រឹមត្រូវនៃប្រព័ន្ធផ្តល់អនុសាសន៍  

## 📚 អត្ថបទបន្ថែម

### Azure OpenAI
- [Azure OpenAI Service Documentation](https://docs.microsoft.com/azure/cognitive-services/openai/) - មគ្គុទ្ទេសក៍សេវាកម្មពេញលេញ  
- [Embeddings API Reference](https://platform.openai.com/docs/api-reference/embeddings) - ឯកសារ API  
- [Best Practices for Embeddings](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings) - ការណែនាំអនុវត្ត  

### មូលដ្ឋានទិន្នន័យវ៉ិចត័រ
- [pgvector Documentation](https://github.com/pgvector/pgvector) - កម្មវិធីបន្ថែមវ៉ិចត័ររបស់ PostgreSQL  
- [Vector Search Optimization](https://www.pinecone.io/learn/vector-search-optimization/) - ការកែលម្អប្រសិទ្ធភាព  
- [HNSW Algorithm](https://arxiv.org/abs/1603.09320) - គោលការណ៍ចងក្រងកំណត់មហាសាលតូចតាចចាប់ផ្តើម  

### Semantic Search
- [Information Retrieval Fundamentals](https://nlp.stanford.edu/IR-book/) - សៀវភៅសិក្សា Stanford IR  
- [Vector Search Best Practices](https://weaviate.io/blog/vector-search-best-practices) - លំនាំអនុវត្ត  
- [Hybrid Search Strategies](https://blog.vespa.ai/hybrid-search/) - ការរួមបញ្ចូលវិធីសាស្ត្រស្វែងរកផ្សេងៗ  

---

**មុននេះ**: [Lab 06: Tool Development](../06-Tools/README.md)  
**បន្ទាប់**: [Lab 08: Testing and Debugging](../08-Testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ចំណាំ**៖  
ឯកសារនេះត្រូវបានបកប្រែប្រើសេវាផ្ទេរប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ ទោះបីយើងខិតខម្ចីសម្រាប់ភាពត្រឹមត្រូវក៏ដោយ សូមជ្រាបថាការបកប្រែដោយស្វ័យប្រវត្តិសម្បូរតែមានកំហុសឬអច្បាប់ណាមួយ។ ឯកសារដើមដែលមានភាសាម្ចាស់របស់វាគួរត្រូវបានគិតថាជាតំណក់មូលដ្ឋាននៃភាពត្រឹមត្រូវ។ សម្រាប់ព័ត៌មានដ៏សំខាន់ ការបកប្រែដោយមនុស្សវិជ្ជាជីវៈត្រូវបានផ្តល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបស្ចាញ់ដែលកើតមានពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->