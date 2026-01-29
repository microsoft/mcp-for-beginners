# ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟ ಏಕೀಕರಣ

## 🎯 ಈ ಪ್ರಯೋಗಶಾಲೆ ಏನು ಒಳಗೊಂಡಿದೆ

ಈ ಪ್ರಯೋಗಶಾಲೆ Azure OpenAI embeddings ಮತ್ತು PostgreSQL ನ pgvector ವಿಸ್ತರಣೆ ಬಳಸಿ ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟ ಸಾಮರ್ಥ್ಯಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸುವ ಬಗ್ಗೆ ಸಮಗ್ರ ಮಾರ್ಗದರ್ಶನವನ್ನು ಒದಗಿಸುತ್ತದೆ. ನೀವು ನೈಸರ್ಗಿಕ ಭಾಷಾ ಪ್ರಶ್ನೆಗಳನ್ನು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವ ಮತ್ತು ಸಾಂದರ್ಭಿಕ ಸಾದೃಶ್ಯದ ಆಧಾರದ ಮೇಲೆ ಸಂಬಂಧಿತ ಫಲಿತಾಂಶಗಳನ್ನು ನೀಡುವ AI-ಚಾಲಿತ ಉತ್ಪನ್ನ ಹುಡುಕಾಟವನ್ನು ನಿರ್ಮಿಸುವುದನ್ನು ಕಲಿಯುತ್ತೀರಿ.

## ಅವಲೋಕನ

ಪಾರಂಪರಿಕ ಕೀವರ್ಡ್ ಆಧಾರಿತ ಹುಡುಕಾಟವು ಬಳಕೆದಾರರ ಉದ್ದೇಶ ಮತ್ತು ಸಾಂದರ್ಭಿಕ ಅರ್ಥವನ್ನು ಹಿಡಿಯಲು ವಿಫಲವಾಗುತ್ತದೆ. ವೆಕ್ಟರ್ embeddings ಬಳಸಿ ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟವು "ಮಳೆಗಾಲದ ಹವಾಮಾನಕ್ಕೆ ಅನುಕೂಲಕರವಾದ ಓಟದ ಶೂಗಳು" ಎಂಬ ನೈಸರ್ಗಿಕ ಭಾಷಾ ಪ್ರಶ್ನೆಗಳನ್ನು ಉತ್ಪನ್ನ ವಿವರಣೆಗಳಲ್ಲಿ ಆ ನಿಖರ ಪದಗಳು ಕಾಣಿಸದಿದ್ದರೂ ಸಹ ಸಂಬಂಧಿತ ಉತ್ಪನ್ನಗಳನ್ನು ಹುಡುಕಲು ಸಾಧ್ಯವಾಗಿಸುತ್ತದೆ.

ನಮ್ಮ ಅನುಷ್ಠಾನವು Azure OpenAI ನ ಶಕ್ತಿಶಾಲಿ embedding ಮಾದರಿಗಳನ್ನು PostgreSQL ನ pgvector ವಿಸ್ತರಣೆಯೊಂದಿಗೆ ಸಂಯೋಜಿಸಿ, ಬುದ್ಧಿವಂತ ಉತ್ಪನ್ನ ಅನ್ವೇಷಣೆಯೊಂದಿಗೆ ಚಿಲ್ಲರೆ ಅನುಭವವನ್ನು ಸುಧಾರಿಸುವ ಉನ್ನತ ಕಾರ್ಯಕ್ಷಮತೆ, ವಿಸ್ತಾರಗೊಳ್ಳುವ ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟ ವ್ಯವಸ್ಥೆಯನ್ನು ರಚಿಸುತ್ತದೆ.

## ಕಲಿಕೆಯ ಉದ್ದೇಶಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯ ಅಂತ್ಯಕ್ಕೆ, ನೀವು ಸಾಧ್ಯವಾಗುತ್ತದೆ:

- **ಸಂಯೋಜಿಸು** ಪಠ್ಯ ವೆಕ್ಟರೀಕರಣಕ್ಕಾಗಿ Azure OpenAI embedding ಮಾದರಿಗಳನ್ನು  
- **ಅನುಷ್ಠಾನಗೊಳಿಸು** ಪರಿಣಾಮಕಾರಿ ಸಾದೃಶ್ಯ ಹುಡುಕಾಟ ಕಾರ್ಯಾಚರಣೆಗಳಿಗೆ pgvector  
- **ನಿರ್ಮಿಸು** ನೈಸರ್ಗಿಕ ಭಾಷಾ ಉತ್ಪನ್ನ ಪ್ರಶ್ನೆಗಳಿಗೆ ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟ ಸಾಧನಗಳನ್ನು  
- **ರಚಿಸು** ಪಾರಂಪರಿಕ ಮತ್ತು ವೆಕ್ಟರ್ ಹುಡುಕಾಟವನ್ನು ಸಂಯೋಜಿಸುವ ಸಂಯುಕ್ತ ಹುಡುಕಾಟ  
- **ಆಪ್ಟಿಮೈಸ್** ಉತ್ಪಾದನಾ ಕಾರ್ಯಕ್ಷಮತೆಯಿಗಾಗಿ ವೆಕ್ಟರ್ ಪ್ರಶ್ನೆಗಳನ್ನು  
- **ರಚಿಸು** embedding ಸಾದೃಶ್ಯವನ್ನು ಬಳಸಿ ಶಿಫಾರಸು ವ್ಯವಸ್ಥೆಗಳನ್ನು  

## 🧠 ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟ ವಾಸ್ತುಶಿಲ್ಪ

### ವೆಕ್ಟರ್ ಹುಡುಕಾಟ ಪೈಪ್ಲೈನ್

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

### embedding ತಯಾರಿಕೆ ತಂತ್ರ

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
        
        # ಎम्बೆಡ್ಡಿಂಗ್ ಸಂರಚನೆ
        self.embedding_dimension = 1536  # ಪಠ್ಯ-ಎಂಬೆಡ್ಡಿಂಗ್-3-ಸಣ್ಣ ಆಯಾಮ
        self.max_tokens = 8000  # ಪ್ರತಿ ವಿನಂತಿಗೆ ಗರಿಷ್ಠ ಟೋಕನ್ಗಳು
        self.batch_size = 100  # ಬ್ಯಾಚ್ ಪ್ರಕ್ರಿಯೆ ಗಾತ್ರ
        
        # ಕ್ಯಾಶಿಂಗ್ ಸಂರಚನೆ
        self.embedding_cache = {}
        self.cache_ttl = timedelta(hours=24)
        
        # ದರ ಮಿತಿ ನಿಗ್ರಹಣೆ
        self.rate_limit_requests = 1000  # ಪ್ರತಿ ನಿಮಿಷ
        self.rate_limit_tokens = 150000  # ಪ್ರತಿ ನಿಮಿಷ
        
    async def initialize(self):
        """Initialize the Azure AI client."""
        
        try:
            self.client = AIProjectClient(
                endpoint=self.project_endpoint,
                credential=self.credential
            )
            
            # ಸಂಪರ್ಕವನ್ನು ಪರೀಕ್ಷಿಸಿ
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
        
        # ಮೊದಲು ಕ್ಯಾಶ್ ಪರಿಶೀಲಿಸಿ
        if use_cache:
            cache_key = self._get_cache_key(text)
            cached_embedding = self._get_cached_embedding(cache_key)
            if cached_embedding:
                return cached_embedding
        
        try:
            # ಕ್ಲೈಂಟ್ ಪ್ರಾರಂಭಗೊಂಡಿರುವುದನ್ನು ಖಚಿತಪಡಿಸಿಕೊಳ್ಳಿ
            if not self.client:
                await self.initialize()
            
            # ಎम्बೆಡ್ಡಿಂಗ್ ರಚಿಸಿ
            response = await self.client.embeddings.create(
                model=self.deployment_name,
                input=text.strip()
            )
            
            embedding = response.data[0].embedding
            
            # ಫಲಿತಾಂಶವನ್ನು ಕ್ಯಾಶ್ ಮಾಡಿ
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
        
        # ಪ್ರತಿ ಪಠ್ಯಕ್ಕಾಗಿ ಕ್ಯಾಶ್ ಪರಿಶೀಲಿಸಿ
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
            
            # ಕ್ಯಾಶ್ ಮಿಸ್‌ಗಳನ್ನು ಟ್ರ್ಯಾಕ್ ಮಾಡಿ
            embeddings.append(None)  # ಪ್ಲೇಸ್‌ಹೋಲ್ಡರ್
            cache_misses.append(text.strip())
            cache_miss_indices.append(i)
        
        # ಕ್ಯಾಶ್ ಮಿಸ್‌ಗಳಿಗೆ ಎम्बೆಡ್ಡಿಂಗ್‌ಗಳನ್ನು ರಚಿಸಿ
        if cache_misses:
            try:
                # API ಮಿತಿಗಳನ್ನು ಗೌರವಿಸಲು ಬ್ಯಾಚ್‌ಗಳಲ್ಲಿ ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ
                for batch_start in range(0, len(cache_misses), self.batch_size):
                    batch_end = min(batch_start + self.batch_size, len(cache_misses))
                    batch_texts = cache_misses[batch_start:batch_end]
                    
                    # ಬ್ಯಾಚ್ ಎम्बೆಡ್ಡಿಂಗ್‌ಗಳನ್ನು ರಚಿಸಿ
                    response = await self.client.embeddings.create(
                        model=self.deployment_name,
                        input=batch_texts
                    )
                    
                    # ಬ್ಯಾಚ್ ಫಲಿತಾಂಶಗಳನ್ನು ಪ್ರಕ್ರಿಯೆ ಮಾಡಿ
                    for j, embedding_data in enumerate(response.data):
                        actual_index = cache_miss_indices[batch_start + j]
                        embedding = embedding_data.embedding
                        embeddings[actual_index] = embedding
                        
                        # ಫಲಿತಾಂಶವನ್ನು ಕ್ಯಾಶ್ ಮಾಡಿ
                        if use_cache:
                            text = batch_texts[j]
                            cache_key = self._get_cache_key(text)
                            self._cache_embedding(cache_key, embedding)
                    
                    # ದರ ಮಿತಿ ನಿಗ್ರಹಣೆ - ಬ್ಯಾಚ್‌ಗಳ ನಡುವೆ ಸಣ್ಣ ವಿಳಂಬ
                    if batch_end < len(cache_misses):
                        await asyncio.sleep(0.1)
                
                logger.info(f"Generated {len(cache_misses)} embeddings in batch")
                
            except Exception as e:
                logger.error(f"Batch embedding generation failed: {e}")
                raise
        
        return embeddings
    
    def _get_cache_key(self, text: str) -> str:
        """Generate cache key for text."""
        
        # ಕ್ಯಾಶ್ ಕೀಗಾಗಿ ಪಠ್ಯ + ಮಾದರಿಯ SHA-256 ಹ್ಯಾಶ್ ಬಳಸಿ
        content = f"{self.deployment_name}:{text.strip()}"
        return hashlib.sha256(content.encode()).hexdigest()
    
    def _get_cached_embedding(self, cache_key: str) -> Optional[List[float]]:
        """Get embedding from cache if not expired."""
        
        if cache_key in self.embedding_cache:
            embedding_data = self.embedding_cache[cache_key]
            
            # ಕ್ಯಾಶ್ ಎಂಟ್ರಿ ಇನ್ನೂ ಮಾನ್ಯವಿದೆಯೇ ಎಂದು ಪರಿಶೀಲಿಸಿ
            if datetime.now() - embedding_data['timestamp'] < self.cache_ttl:
                return embedding_data['embedding']
            else:
                # ಅವಧಿ ಮುಗಿದ ಎಂಟ್ರಿಯನ್ನು ತೆಗೆದುಹಾಕಿ
                del self.embedding_cache[cache_key]
        
        return None
    
    def _cache_embedding(self, cache_key: str, embedding: List[float]):
        """Cache embedding with timestamp."""
        
        self.embedding_cache[cache_key] = {
            'embedding': embedding,
            'timestamp': datetime.now()
        }
        
        # ಕ್ಯಾಶ್ ಗಾತ್ರವನ್ನು ಮಿತಿಗೊಳಿಸಿ
        if len(self.embedding_cache) > 10000:
            # ಹಳೆಯ ಎಂಟ್ರಿಗಳನ್ನು ತೆಗೆದುಹಾಕಿ
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

# ಜಾಗತಿಕ ಎम्बೆಡ್ಡಿಂಗ್ ಮ್ಯಾನೇಜರ್ ಉದಾಹರಣೆ
embedding_manager = EmbeddingManager(
    project_endpoint=os.getenv('PROJECT_ENDPOINT'),
    deployment_name=os.getenv('EMBEDDING_DEPLOYMENT_NAME', 'text-embedding-3-small')
)
```

## 🔍 ಉತ್ಪನ್ನ embedding ತಯಾರಿಕೆ

### ಸ್ವಯಂಚಾಲಿತ embedding ಪೈಪ್ಲೈನ್

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
        
        # ಉತ್ಪನ್ನಗಳಿಗಾಗಿ ಪಠ್ಯ ಸಂಯೋಜನೆ ತಂತ್ರ
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
                # ಅಂಗಡಿ ಸನ್ನಿವೇಶವನ್ನು ಹೊಂದಿಸಿ
                await conn.execute("SELECT retail.set_store_context($1)", store_id)
                
                # ಎम्बೆಡ್ಡಿಂಗ್ ಅಗತ್ಯವಿರುವ ಉತ್ಪನ್ನಗಳನ್ನು ಪಡೆಯಿರಿ
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
                
                # ಉತ್ಪನ್ನಗಳನ್ನು ಬ್ಯಾಚ್‌ಗಳಲ್ಲಿ ಪ್ರಕ್ರಿಯೆಗೊಳಿಸಿ
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
        
        # ಎम्बೆಡ್ಡಿಂಗ್‌ಗಾಗಿ ಪಠ್ಯಗಳನ್ನು ತಯಾರಿಸಿ
        texts = []
        product_ids = []
        
        for product in products:
            # ಹುಡುಕಬಹುದಾದ ಪಠ್ಯಕ್ಕೆ ಉತ್ಪನ್ನ ಮಾಹಿತಿಯನ್ನು ಸಂಯೋಜಿಸಿ
            combined_text = self._create_product_text(product)
            texts.append(combined_text)
            product_ids.append(product['product_id'])
        
        # ಎम्बೆಡ್ಡಿಂಗ್‌ಗಳನ್ನು ರಚಿಸಿ
        embeddings = await self.embedding_manager.generate_embeddings_batch(texts)
        
        # ಡೇಟಾಬೇಸ್‌ನಲ್ಲಿ ಎम्बೆಡ್ಡಿಂಗ್‌ಗಳನ್ನು ಸಂಗ್ರಹಿಸಿ
        for i, (product_id, embedding) in enumerate(zip(product_ids, embeddings)):
            if embedding:  # ವಿಫಲವಾದ ಎम्बೆಡ್ಡಿಂಗ್‌ಗಳನ್ನು ಬಿಟ್ಟುಬಿಡಿ
                await self._store_product_embedding(
                    conn, 
                    product_id, 
                    store_id, 
                    texts[i], 
                    embedding
                )
    
    def _create_product_text(self, product: Dict[str, Any]) -> str:
        """Create combined text for product embedding."""
        
        # None ಮೌಲ್ಯಗಳನ್ನು ನಿರ್ವಹಿಸಿ
        product_name = product.get('product_name') or ''
        brand = product.get('brand') or ''
        description = product.get('product_description') or ''
        category = product.get('category_name') or ''
        tags = product.get('tags_text') or ''
        
        # ಹುಡುಕಬಹುದಾದ ಪಠ್ಯದಲ್ಲಿ ಸಂಯೋಜಿಸಿ
        combined_text = self.text_template.format(
            product_name=product_name,
            brand=brand,
            description=description,
            category=category,
            tags=tags
        )
        
        # ಹೆಚ್ಚುವರಿ ಖಾಲಿ ಜಾಗವನ್ನು ಸ್ವಚ್ಛಗೊಳಿಸಿ
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
        
        # ಎम्बೆಡ್ಡಿಂಗ್ ಅನ್ನು pgvector ಸ್ವರೂಪಕ್ಕೆ ಪರಿವರ್ತಿಸಿ
        embedding_vector = f"[{','.join(map(str, embedding))}]"
        
        # ಎम्बೆಡ್ಡಿಂಗ್ ಅನ್ನು ಅಪ್ಸರ್ಟ್ ಮಾಡಿ
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
                # ಅಂಗಡಿ ಸನ್ನಿವೇಶವನ್ನು ಹೊಂದಿಸಿ
                await conn.execute("SELECT retail.set_store_context($1)", store_id)
                
                # ಉತ್ಪನ್ನ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಿರಿ
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
                
                # ಎम्बೆಡ್ಡಿಂಗ್ ರಚಿಸಿ
                combined_text = self._create_product_text(dict(product))
                embedding = await self.embedding_manager.generate_embedding(combined_text)
                
                # ಎम्बೆಡ್ಡಿಂಗ್ ಅನ್ನು ಸಂಗ್ರಹಿಸಿ
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

# ಜಾಗತಿಕ ಉತ್ಪನ್ನ ಎम्बೆಡ್ಡರ್ ಉದಾಹರಣೆ
product_embedder = ProductEmbedder(db_provider)
```

## 🔎 ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟ ಸಾಧನಗಳು

### ಸಾಂದರ್ಭಿಕ ಉತ್ಪನ್ನ ಹುಡುಕಾಟ ಸಾಧನ

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
            # ಪ್ರಶ್ನೆ ಎम्बೆಡ್ಡಿಂಗ್ ರಚಿಸಿ
            query_embedding = await self.embedding_manager.generate_embedding(query)
            
            # ಅರ್ಥಪೂರ್ಣ ಹುಡುಕಾಟ ನಡೆಸಿ
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
        
        # ಎम्बೆಡ್ಡಿಂಗ್ ಅನ್ನು PostgreSQL ವೆಕ್ಟರ್ ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸಿ
        embedding_vector = f"[{','.join(map(str, query_embedding))}]"
        
        # ಹುಡುಕಾಟ ಪ್ರಶ್ನೆಯನ್ನು ನಿರ್ಮಿಸಿ
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
            # ಸ್ಟೋರ್ ಸಂದರ್ಭವನ್ನು ಸೆಟ್ ಮಾಡಿ
            await conn.execute("SELECT retail.set_store_context($1)", store_id)
            
            # ಹುಡುಕಾಟವನ್ನು ನಿರ್ವಹಿಸಿ
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
            # ಅರ್ಥಪೂರ್ಣ ಹುಡುಕಾಟಕ್ಕಾಗಿ ಪ್ರಶ್ನೆ ಎम्बೆಡ್ಡಿಂಗ್ ರಚಿಸಿ
            query_embedding = await self.embedding_manager.generate_embedding(query)
            
            # ಸಂಯೋಜಿತ ಹುಡುಕಾಟ ನಡೆಸಿ
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
        
        # ಎम्बೆಡ್ಡಿಂಗ್ ಅನ್ನು PostgreSQL ವೆಕ್ಟರ್ ಫಾರ್ಮ್ಯಾಟ್‌ಗೆ ಪರಿವರ್ತಿಸಿ
        embedding_vector = f"[{','.join(map(str, query_embedding))}]"
        
        # ಕೀವರ್ಡ್ ಹೊಂದಾಣಿಕೆಗೆ ಹುಡುಕಾಟ ಪದಗಳನ್ನು ರಚಿಸಿ
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
            # ಸ್ಟೋರ್ ಸಂದರ್ಭವನ್ನು ಸೆಟ್ ಮಾಡಿ
            await conn.execute("SELECT retail.set_store_context($1)", store_id)
            
            # ಸಂಯೋಜಿತ ಹುಡುಕಾಟವನ್ನು ನಿರ್ವಹಿಸಿ
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

## 🎯 ಶಿಫಾರಸು ವ್ಯವಸ್ಥೆಗಳು

### ಉತ್ಪನ್ನ ಶಿಫಾರಸು ಎಂಜಿನ್

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

## ⚡ ಕಾರ್ಯಕ್ಷಮತೆ ಆಪ್ಟಿಮೈಜೆಷನ್

### ವೆಕ್ಟರ್ ಪ್ರಶ್ನೆ ಆಪ್ಟಿಮೈಜೆಷನ್

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

### embedding ಕ್ಯಾಶೆ ತಂತ್ರ

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
        
        # ಕ್ಯಾಶೆ TTL ಸೆಟ್ಟಿಂಗ್‌ಗಳು
        self.embedding_ttl = timedelta(days=7)  # 1 ವಾರದ ಕಾಲ ಎम्बೆಡ್ಡಿಂಗ್‌ಗಳನ್ನು ಕ್ಯಾಶೆ ಮಾಡಲಾಗಿದೆ
        self.search_ttl = timedelta(hours=1)    # 1 ಗಂಟೆಯ ಕಾಲ ಹುಡುಕಾಟ ಫಲಿತಾಂಶಗಳನ್ನು ಕ್ಯಾಶೆ ಮಾಡಲಾಗಿದೆ
        self.recommendation_ttl = timedelta(hours=4)  # 4 ಗಂಟೆಗಳ ಕಾಲ ಶಿಫಾರಸುಗಳನ್ನು ಕ್ಯಾಶೆ ಮಾಡಲಾಗಿದೆ
        
        # ಕ್ಯಾಶೆ ಕೀ ಪ್ರಿಫಿಕ್ಸ್‌ಗಳು
        self.EMBEDDING_PREFIX = "emb:"
        self.SEARCH_PREFIX = "search:"
        self.RECOMMENDATION_PREFIX = "rec:"
    
    async def initialize(self):
        """Initialize Redis connection."""
        
        try:
            self.redis_client = redis.from_url(self.redis_url)
            # ಸಂಪರ್ಕವನ್ನು ಪರೀಕ್ಷಿಸಿ
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
        
        # ಪ್ರಶ್ನೆ ಮತ್ತು ಪ್ಯಾರಾಮೀಟರ್‌ಗಳಿಂದ ಸ್ಥಿರ ಹ್ಯಾಶ್ ರಚಿಸಿ
        content = f"{query}:{store_id}:{json.dumps(params, sort_keys=True)}"
        hash_key = hashlib.sha256(content.encode()).hexdigest()
        return f"{self.SEARCH_PREFIX}{hash_key}"
    
    async def invalidate_store_cache(self, store_id: str):
        """Invalidate all cached data for a store."""
        
        if not self.redis_client:
            return
        
        try:
            # ಅಂಗಡಿಯೊಂದಿಗೆ ಸಂಬಂಧಿಸಿದ ಎಲ್ಲಾ ಕೀಗಳನ್ನು ಹುಡುಕಿ
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

# ಜಾಗತಿಕ ಕ್ಯಾಶೆ ಮ್ಯಾನೇಜರ್
cache_manager = EmbeddingCacheManager()
```

## 🎯 ಪ್ರಮುಖ ಪಾಠಗಳು

ಈ ಪ್ರಯೋಗಶಾಲೆಯನ್ನು ಪೂರ್ಣಗೊಳಿಸಿದ ನಂತರ, ನೀವು ಹೊಂದಿರಬೇಕು:

✅ **Azure OpenAI ಏಕೀಕರಣ**: ಕ್ಯಾಶಿಂಗ್ ಮತ್ತು ಆಪ್ಟಿಮೈಜೆಷನ್ ಸಹಿತ ಸಂಪೂರ್ಣ embedding ತಯಾರಿಕೆ  
✅ **ವೆಕ್ಟರ್ ಹುಡುಕಾಟ ಅನುಷ್ಠಾನ**: pgvector ಬಳಸಿ ಉತ್ಪಾದನಾ-ಸಿದ್ಧ ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟ  
✅ **ಸಂಯುಕ್ತ ಹುಡುಕಾಟ ಸಾಮರ್ಥ್ಯಗಳು**: ಉತ್ತಮ ಫಲಿತಾಂಶಗಳಿಗಾಗಿ ಕೀವರ್ಡ್ ಮತ್ತು ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟ ಸಂಯೋಜನೆ  
✅ **ಶಿಫಾರಸು ವ್ಯವಸ್ಥೆಗಳು**: ಸಾದೃಶ್ಯವನ್ನು ಬಳಸಿ AI-ಚಾಲಿತ ಉತ್ಪನ್ನ ಶಿಫಾರಸುಗಳು  
✅ **ಕಾರ್ಯಕ್ಷಮತೆ ಆಪ್ಟಿಮೈಜೆಷನ್**: ವೆಕ್ಟರ್ ಸೂಚ್ಯಂಕ ಆಪ್ಟಿಮೈಜೆಷನ್ ಮತ್ತು ಬುದ್ಧಿವಂತ ಕ್ಯಾಶಿಂಗ್  
✅ **ವಿಸ್ತಾರಗೊಳ್ಳುವ ವಾಸ್ತುಶಿಲ್ಪ**: ಉದ್ಯಮ-ಸಿದ್ಧ ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟ ಮೂಲಸೌಕರ್ಯ  

## 🚀 ಮುಂದೇನು

**[ಪ್ರಯೋಗಶಾಲೆ 08: ಪರೀಕ್ಷೆ ಮತ್ತು ಡಿಬಗ್](../08-Testing/README.md)** ಜೊತೆಗೆ ಮುಂದುವರಿಯಿರಿ:

- ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟಕ್ಕಾಗಿ ಸಮಗ್ರ ಪರೀಕ್ಷಾ ತಂತ್ರಗಳನ್ನು ಅನುಷ್ಠಾನಗೊಳಿಸಿ  
- ವೆಕ್ಟರ್ ಹುಡುಕಾಟ ಕಾರ್ಯಕ್ಷಮತೆ ಸಮಸ್ಯೆಗಳನ್ನು ಡಿಬಗ್ ಮಾಡಿ  
- embedding ಗುಣಮಟ್ಟ ಮತ್ತು ಸಂಬಂಧಿತತೆಯನ್ನು ಪರಿಶೀಲಿಸಿ  
- ಶಿಫಾರಸು ವ್ಯವಸ್ಥೆಯ ನಿಖರತೆಯನ್ನು ಪರೀಕ್ಷಿಸಿ  

## 📚 ಹೆಚ್ಚುವರಿ ಸಂಪನ್ಮೂಲಗಳು

### Azure OpenAI
- [Azure OpenAI ಸೇವಾ ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://docs.microsoft.com/azure/cognitive-services/openai/) - ಸಂಪೂರ್ಣ ಸೇವಾ ಮಾರ್ಗದರ್ಶಿ  
- [Embeddings API ರೆಫರೆನ್ಸ್](https://platform.openai.com/docs/api-reference/embeddings) - API ಡಾಕ್ಯುಮೆಂಟೇಶನ್  
- [Embeddings ಗಾಗಿ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](https://platform.openai.com/docs/guides/embeddings/what-are-embeddings) - ಅನುಷ್ಠಾನ ಮಾರ್ಗದರ್ಶನ  

### ವೆಕ್ಟರ್ ಡೇಟಾಬೇಸ್‌ಗಳು
- [pgvector ಡಾಕ್ಯುಮೆಂಟೇಶನ್](https://github.com/pgvector/pgvector) - PostgreSQL ವೆಕ್ಟರ್ ವಿಸ್ತರಣೆ  
- [ವೆಕ್ಟರ್ ಹುಡುಕಾಟ ಆಪ್ಟಿಮೈಜೆಷನ್](https://www.pinecone.io/learn/vector-search-optimization/) - ಕಾರ್ಯಕ್ಷಮತೆ ಟ್ಯೂನಿಂಗ್  
- [HNSW ಅಲ್ಗಾರಿದಮ್](https://arxiv.org/abs/1603.09320) - ಹೈರಾರ್ಕಿಕಲ್ ನ್ಯಾವಿಗೇಬಲ್ ಸ್ಮಾಲ್ ವರ್ಲ್ಡ್ ಗ್ರಾಫ್‌ಗಳು  

### ಸಾಂದರ್ಭಿಕ ಹುಡುಕಾಟ
- [ಮಾಹಿತಿ ಹಿಂಪಡೆಯುವ ಮೂಲಭೂತಗಳು](https://nlp.stanford.edu/IR-book/) - ಸ್ಟಾನ್ಫರ್ಡ್ IR ಪಠ್ಯಪುಸ್ತಕ  
- [ವೆಕ್ಟರ್ ಹುಡುಕಾಟ ಉತ್ತಮ ಅಭ್ಯಾಸಗಳು](https://weaviate.io/blog/vector-search-best-practices) - ಅನುಷ್ಠಾನ ಮಾದರಿಗಳು  
- [ಸಂಯುಕ್ತ ಹುಡುಕಾಟ ತಂತ್ರಗಳು](https://blog.vespa.ai/hybrid-search/) - ವಿಭಿನ್ನ ಹುಡುಕಾಟ ವಿಧಾನಗಳನ್ನು ಸಂಯೋಜಿಸುವುದು  

---

**ಹಿಂದಿನ**: [ಪ್ರಯೋಗಶಾಲೆ 06: ಸಾಧನ ಅಭಿವೃದ್ಧಿ](../06-Tools/README.md)  
**ಮುಂದಿನ**: [ಪ್ರಯೋಗಶಾಲೆ 08: ಪರೀಕ್ಷೆ ಮತ್ತು ಡಿಬಗ್](../08-Testing/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ಅಸ್ವೀಕಾರ**:  
ಈ ದಸ್ತಾವೇಜು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಬಳಸಿ ಅನುವಾದಿಸಲಾಗಿದೆ. ನಾವು ನಿಖರತೆಯಿಗಾಗಿ ಪ್ರಯತ್ನಿಸುತ್ತಿದ್ದರೂ, ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ತಪ್ಪುಗಳು ಅಥವಾ ಅಸತ್ಯತೆಗಳು ಇರಬಹುದು ಎಂದು ದಯವಿಟ್ಟು ಗಮನಿಸಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಸ್ತಾವೇಜನ್ನು ಅಧಿಕೃತ ಮೂಲವೆಂದು ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ, ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗುತ್ತದೆ. ಈ ಅನುವಾದ ಬಳಕೆಯಿಂದ ಉಂಟಾಗುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳುವಿಕೆ ಅಥವಾ ತಪ್ಪು ವಿವರಣೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->