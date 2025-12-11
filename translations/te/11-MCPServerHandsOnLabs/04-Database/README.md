<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9525f06ed164e10f29e0f6b055d4f3d3",
  "translation_date": "2025-12-11T13:52:41+00:00",
  "source_file": "11-MCPServerHandsOnLabs/04-Database/README.md",
  "language_code": "te"
}
-->
# డేటాబేస్ డిజైన్ మరియు స్కీమా

## 🎯 ఈ ప్రయోగశాలలో ఏమి ఉంటుంది

ఈ ప్రయోగశాల Zava రిటైల్ సిస్టమ్ కోసం PostgreSQL డేటాబేస్ డిజైన్ లో లోతుగా ప్రవేశిస్తుంది. మీరు వెక్టర్ సెర్చ్ సామర్థ్యాలు, బహుళ-టెనెంట్ డేటా మోడలింగ్, మరియు డేటా వేరుపాటు కోసం రో లెవల్ సెక్యూరిటీ (RLS) అమలు చేయడం నేర్చుకుంటారు.

## అవలోకనం

డేటాబేస్ మా MCP సర్వర్ యొక్క పునాది, ఇది అనేక స్టోర్లలో రిటైల్ డేటాను నిల్వ చేస్తుంది మరియు కఠినమైన డేటా వేరుపాటును నిర్వహిస్తుంది. మేము సహజ భాషా ప్రశ్నలతో ఉత్పత్తులను కనుగొనడానికి సెమాంటిక్ సెర్చ్ సామర్థ్యాలను సక్రియం చేయడానికి pgvector విస్తరణతో PostgreSQL ఉపయోగిస్తాము.

మా స్కీమా ఆధునిక బహుళ-టెనెంట్ నమూనాలను అనుసరిస్తుంది, రో లెవల్ సెక్యూరిటీ ద్వారా వినియోగదారులు తమ అనుమతిప్రాప్తి ఉన్న స్టోర్ల డేటాకు మాత్రమే ప్రాప్యత కలిగి ఉంటారు. ఈ విధానం సంస్థ స్థాయి భద్రతను అందిస్తుంది మరియు ఉత్తమ పనితీరును కాపాడుతుంది.

## నేర్చుకునే లక్ష్యాలు

ఈ ప్రయోగశాల ముగిసిన తర్వాత, మీరు చేయగలుగుతారు:

- **డిజైన్ చేయడం** స్కేలబుల్ బహుళ-టెనెంట్ రిటైల్ డేటాబేస్ స్కీమాలు  
- **అమలు చేయడం** వెక్టర్ సెర్చ్ కోసం pgvector తో PostgreSQL  
- **కాన్ఫిగర్ చేయడం** డేటా వేరుపాటు కోసం రో లెవల్ సెక్యూరిటీ  
- **సృష్టించడం** పరీక్ష కోసం వాస్తవిక నమూనా డేటా  
- **ఆప్టిమైజ్ చేయడం** రిటైల్ వర్క్‌లోడ్స్ కోసం డేటాబేస్ పనితీరు  
- **అమలు చేయడం** బ్యాకప్ మరియు రికవరీ వ్యూహాలు  

## 🗃️ డేటాబేస్ ఆర్కిటెక్చర్

### pgvector తో PostgreSQL

మా డేటాబేస్ PostgreSQL యొక్క సంస్థ ఫీచర్లను pgvector విస్తరణతో కలిపి AI ఆధారిత సెర్చ్ కోసం ఉపయోగిస్తుంది:

```sql
-- Enable required extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";
CREATE EXTENSION IF NOT EXISTS "vector";

-- Verify vector extension installation
SELECT * FROM pg_extension WHERE extname = 'vector';
```

### బహుళ-టెనెంట్ ఆర్కిటెక్చర్

డేటాబేస్ రో లెవల్ సెక్యూరిటీతో **షేర్డ్ డేటాబేస్, షేర్డ్ స్కీమా** బహుళ-టెనెన్సీ మోడల్ ఉపయోగిస్తుంది:

```
┌─────────────────────────────────────────────────┐
│                 PostgreSQL                      │
├─────────────────────────────────────────────────┤
│  retail Schema (Shared)                        │
│  ├── stores (Master tenant data)               │
│  ├── customers (RLS by store_id)               │
│  ├── products (RLS by store_id)                │
│  ├── sales_transactions (RLS by store_id)      │
│  ├── sales_transaction_items (RLS via join)    │
│  └── product_embeddings (RLS by store_id)      │
└─────────────────────────────────────────────────┘
```

## 📊 కోర్ స్కీమా డిజైన్

### స్టోర్స్ టేబుల్ (టెనెంట్ మాస్టర్)

```sql
-- Stores table: Master tenant registry
CREATE TABLE retail.stores (
    store_id VARCHAR(50) PRIMARY KEY,
    store_name VARCHAR(100) NOT NULL,
    store_location VARCHAR(100),
    store_type VARCHAR(50),
    region VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Sample stores data
INSERT INTO retail.stores (store_id, store_name, store_location, store_type, region) VALUES
('seattle', 'Zava Retail Seattle', 'Seattle, WA', 'flagship', 'west'),
('redmond', 'Zava Retail Redmond', 'Redmond, WA', 'standard', 'west'),
('bellevue', 'Zava Retail Bellevue', 'Bellevue, WA', 'standard', 'west'),
('online', 'Zava Retail Online', 'Digital', 'ecommerce', 'global');

-- Create index for performance
CREATE INDEX idx_stores_region ON retail.stores(region);
CREATE INDEX idx_stores_active ON retail.stores(is_active) WHERE is_active = TRUE;
```

### కస్టమర్స్ టేబుల్

```sql
-- Customers table with RLS
CREATE TABLE retail.customers (
    customer_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    store_id VARCHAR(50) NOT NULL REFERENCES retail.stores(store_id),
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    date_of_birth DATE,
    gender VARCHAR(20),
    customer_since DATE DEFAULT CURRENT_DATE,
    loyalty_tier VARCHAR(20) DEFAULT 'bronze',
    total_lifetime_value DECIMAL(10,2) DEFAULT 0.00,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Enable RLS
ALTER TABLE retail.customers ENABLE ROW LEVEL SECURITY;

-- RLS Policy: Users can only see customers from their store
CREATE POLICY customers_store_isolation ON retail.customers
    FOR ALL
    TO mcp_user
    USING (store_id = current_setting('app.current_store_id', true));

-- Indexes for performance
CREATE INDEX idx_customers_store_id ON retail.customers(store_id);
CREATE INDEX idx_customers_email ON retail.customers(email);
CREATE INDEX idx_customers_loyalty_tier ON retail.customers(loyalty_tier);
CREATE INDEX idx_customers_created_at ON retail.customers(created_at);
```

### కేటగిరీలతో ఉత్పత్తుల టేబుల్

```sql
-- Product categories
CREATE TABLE retail.product_categories (
    category_id SERIAL PRIMARY KEY,
    category_name VARCHAR(100) NOT NULL UNIQUE,
    parent_category_id INTEGER REFERENCES retail.product_categories(category_id),
    description TEXT,
    is_active BOOLEAN DEFAULT TRUE
);

-- Insert sample categories
INSERT INTO retail.product_categories (category_name, description) VALUES
('Electronics', 'Electronic devices and accessories'),
('Clothing', 'Apparel and fashion items'),
('Home & Garden', 'Home improvement and garden supplies'),
('Sports & Outdoors', 'Sports equipment and outdoor gear'),
('Books & Media', 'Books, movies, and digital media'),
('Health & Beauty', 'Health and beauty products'),
('Automotive', 'Car parts and automotive accessories');

-- Products table with rich metadata
CREATE TABLE retail.products (
    product_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    store_id VARCHAR(50) NOT NULL REFERENCES retail.stores(store_id),
    sku VARCHAR(50) NOT NULL,
    product_name VARCHAR(200) NOT NULL,
    product_description TEXT,
    category_id INTEGER REFERENCES retail.product_categories(category_id),
    brand VARCHAR(100),
    model VARCHAR(100),
    color VARCHAR(50),
    size VARCHAR(50),
    weight_kg DECIMAL(8,3),
    dimensions_cm VARCHAR(50), -- e.g., "30x20x15"
    price DECIMAL(10,2) NOT NULL,
    cost DECIMAL(10,2),
    current_stock INTEGER DEFAULT 0,
    minimum_stock INTEGER DEFAULT 0,
    maximum_stock INTEGER DEFAULT 1000,
    reorder_point INTEGER DEFAULT 10,
    supplier_name VARCHAR(100),
    supplier_sku VARCHAR(50),
    is_active BOOLEAN DEFAULT TRUE,
    is_featured BOOLEAN DEFAULT FALSE,
    rating_average DECIMAL(3,2) DEFAULT 0.00,
    rating_count INTEGER DEFAULT 0,
    tags TEXT[], -- Array of tags for flexible categorization
    metadata JSONB, -- Flexible metadata storage
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Ensure SKU uniqueness within store
    CONSTRAINT unique_sku_per_store UNIQUE (store_id, sku)
);

-- Enable RLS for products
ALTER TABLE retail.products ENABLE ROW LEVEL SECURITY;

-- RLS Policy for products
CREATE POLICY products_store_isolation ON retail.products
    FOR ALL
    TO mcp_user
    USING (store_id = current_setting('app.current_store_id', true));

-- Comprehensive indexes
CREATE INDEX idx_products_store_id ON retail.products(store_id);
CREATE INDEX idx_products_sku ON retail.products(sku);
CREATE INDEX idx_products_category ON retail.products(category_id);
CREATE INDEX idx_products_brand ON retail.products(brand);
CREATE INDEX idx_products_price ON retail.products(price);
CREATE INDEX idx_products_stock ON retail.products(current_stock);
CREATE INDEX idx_products_active ON retail.products(is_active) WHERE is_active = TRUE;
CREATE INDEX idx_products_featured ON retail.products(is_featured) WHERE is_featured = TRUE;
CREATE INDEX idx_products_tags ON retail.products USING GIN(tags);
CREATE INDEX idx_products_metadata ON retail.products USING GIN(metadata);
CREATE INDEX idx_products_text_search ON retail.products USING GIN(
    to_tsvector('english', product_name || ' ' || COALESCE(product_description, '') || ' ' || COALESCE(brand, ''))
);
```

### సేల్స్ లావాదేవీలు

```sql
-- Sales transactions table
CREATE TABLE retail.sales_transactions (
    transaction_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    store_id VARCHAR(50) NOT NULL REFERENCES retail.stores(store_id),
    customer_id UUID REFERENCES retail.customers(customer_id),
    transaction_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    transaction_type VARCHAR(20) DEFAULT 'sale', -- 'sale', 'return', 'exchange'
    payment_method VARCHAR(50), -- 'cash', 'credit_card', 'debit_card', 'digital_wallet'
    subtotal DECIMAL(10,2) NOT NULL,
    tax_amount DECIMAL(10,2) DEFAULT 0.00,
    discount_amount DECIMAL(10,2) DEFAULT 0.00,
    total_amount DECIMAL(10,2) NOT NULL,
    cashier_id VARCHAR(50),
    register_id VARCHAR(50),
    receipt_number VARCHAR(50),
    notes TEXT,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Sales transaction items (line items)
CREATE TABLE retail.sales_transaction_items (
    item_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    transaction_id UUID NOT NULL REFERENCES retail.sales_transactions(transaction_id) ON DELETE CASCADE,
    product_id UUID NOT NULL REFERENCES retail.products(product_id),
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    discount_amount DECIMAL(10,2) DEFAULT 0.00,
    tax_amount DECIMAL(10,2) DEFAULT 0.00,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Ensure positive quantities and prices
    CONSTRAINT positive_quantity CHECK (quantity > 0),
    CONSTRAINT positive_unit_price CHECK (unit_price >= 0),
    CONSTRAINT positive_total_price CHECK (total_price >= 0)
);

-- Enable RLS for transactions
ALTER TABLE retail.sales_transactions ENABLE ROW LEVEL SECURITY;

-- RLS Policy for sales transactions
CREATE POLICY sales_transactions_store_isolation ON retail.sales_transactions
    FOR ALL
    TO mcp_user
    USING (store_id = current_setting('app.current_store_id', true));

-- RLS for transaction items (via join with transactions)
ALTER TABLE retail.sales_transaction_items ENABLE ROW LEVEL SECURITY;

CREATE POLICY sales_transaction_items_store_isolation ON retail.sales_transaction_items
    FOR ALL
    TO mcp_user
    USING (
        transaction_id IN (
            SELECT transaction_id 
            FROM retail.sales_transactions 
            WHERE store_id = current_setting('app.current_store_id', true)
        )
    );

-- Performance indexes
CREATE INDEX idx_sales_transactions_store_id ON retail.sales_transactions(store_id);
CREATE INDEX idx_sales_transactions_customer_id ON retail.sales_transactions(customer_id);
CREATE INDEX idx_sales_transactions_date ON retail.sales_transactions(transaction_date);
CREATE INDEX idx_sales_transactions_type ON retail.sales_transactions(transaction_type);
CREATE INDEX idx_sales_transactions_payment ON retail.sales_transactions(payment_method);

CREATE INDEX idx_sales_transaction_items_transaction_id ON retail.sales_transaction_items(transaction_id);
CREATE INDEX idx_sales_transaction_items_product_id ON retail.sales_transaction_items(product_id);
```

## 🔍 వెక్టర్ సెర్చ్ అమలు

### ఉత్పత్తి ఎంబెడ్డింగ్స్ టేబుల్

```sql
-- Product embeddings for semantic search
CREATE TABLE retail.product_embeddings (
    embedding_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    product_id UUID NOT NULL REFERENCES retail.products(product_id) ON DELETE CASCADE,
    store_id VARCHAR(50) NOT NULL REFERENCES retail.stores(store_id),
    embedding_text TEXT NOT NULL, -- The text that was embedded
    embedding vector(1536), -- OpenAI text-embedding-3-small dimension
    embedding_model VARCHAR(100) NOT NULL DEFAULT 'text-embedding-3-small',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    
    -- Ensure one embedding per product per model
    CONSTRAINT unique_product_embedding UNIQUE (product_id, embedding_model)
);

-- Enable RLS for embeddings
ALTER TABLE retail.product_embeddings ENABLE ROW LEVEL SECURITY;

-- RLS Policy for embeddings
CREATE POLICY product_embeddings_store_isolation ON retail.product_embeddings
    FOR ALL
    TO mcp_user
    USING (store_id = current_setting('app.current_store_id', true));

-- Vector similarity index (HNSW for fast approximate search)
CREATE INDEX idx_product_embeddings_vector ON retail.product_embeddings 
USING hnsw (embedding vector_cosine_ops);

-- Additional indexes
CREATE INDEX idx_product_embeddings_product_id ON retail.product_embeddings(product_id);
CREATE INDEX idx_product_embeddings_store_id ON retail.product_embeddings(store_id);
CREATE INDEX idx_product_embeddings_model ON retail.product_embeddings(embedding_model);
```

### వెక్టర్ సెర్చ్ ఫంక్షన్లు

```sql
-- Function to search products by similarity
CREATE OR REPLACE FUNCTION retail.search_products_by_similarity(
    search_embedding vector(1536),
    similarity_threshold float DEFAULT 0.7,
    max_results integer DEFAULT 20
)
RETURNS TABLE (
    product_id UUID,
    product_name VARCHAR(200),
    product_description TEXT,
    brand VARCHAR(100),
    price DECIMAL(10,2),
    similarity_score float
) 
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    RETURN QUERY
    SELECT 
        p.product_id,
        p.product_name,
        p.product_description,
        p.brand,
        p.price,
        1 - (pe.embedding <=> search_embedding) as similarity_score
    FROM retail.product_embeddings pe
    JOIN retail.products p ON pe.product_id = p.product_id
    WHERE 
        pe.store_id = current_setting('app.current_store_id', true)
        AND p.is_active = TRUE
        AND 1 - (pe.embedding <=> search_embedding) >= similarity_threshold
    ORDER BY pe.embedding <=> search_embedding
    LIMIT max_results;
END;
$$;

-- Grant execute permission
GRANT EXECUTE ON FUNCTION retail.search_products_by_similarity TO mcp_user;
```

## 🔐 రో లెవల్ సెక్యూరిటీ సెటప్

### డేటాబేస్ పాత్రలు మరియు అనుమతులు

```sql
-- Create MCP application role
CREATE ROLE mcp_user LOGIN;

-- Grant schema usage
GRANT USAGE ON SCHEMA retail TO mcp_user;

-- Grant table permissions
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA retail TO mcp_user;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA retail TO mcp_user;

-- Grant permissions on future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA retail GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO mcp_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA retail GRANT USAGE, SELECT ON SEQUENCES TO mcp_user;

-- Function to set store context
CREATE OR REPLACE FUNCTION retail.set_store_context(store_id_param VARCHAR(50))
RETURNS void
LANGUAGE plpgsql
SECURITY DEFINER
AS $$
BEGIN
    -- Verify store exists and user has access
    IF NOT EXISTS (SELECT 1 FROM retail.stores WHERE store_id = store_id_param AND is_active = TRUE) THEN
        RAISE EXCEPTION 'Invalid or inactive store: %', store_id_param;
    END IF;
    
    -- Set the store context
    PERFORM set_config('app.current_store_id', store_id_param, false);
    
    -- Log the context change
    INSERT INTO retail.audit_log (
        table_name,
        action,
        user_name,
        store_id,
        metadata
    ) VALUES (
        'security_context',
        'store_context_set',
        current_user,
        store_id_param,
        jsonb_build_object('timestamp', current_timestamp)
    );
END;
$$;

-- Grant execute permission
GRANT EXECUTE ON FUNCTION retail.set_store_context TO mcp_user;
```

### ఆడిట్ లాగింగ్

```sql
-- Audit log table for security and compliance
CREATE TABLE retail.audit_log (
    log_id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    table_name VARCHAR(100) NOT NULL,
    action VARCHAR(50) NOT NULL, -- INSERT, UPDATE, DELETE, SELECT
    user_name VARCHAR(100) NOT NULL DEFAULT current_user,
    store_id VARCHAR(50),
    record_id UUID,
    old_values JSONB,
    new_values JSONB,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Index for audit queries
CREATE INDEX idx_audit_log_table_name ON retail.audit_log(table_name);
CREATE INDEX idx_audit_log_action ON retail.audit_log(action);
CREATE INDEX idx_audit_log_user_name ON retail.audit_log(user_name);
CREATE INDEX idx_audit_log_store_id ON retail.audit_log(store_id);
CREATE INDEX idx_audit_log_created_at ON retail.audit_log(created_at);

-- Audit trigger function
CREATE OR REPLACE FUNCTION retail.audit_trigger()
RETURNS trigger AS $$
BEGIN
    IF TG_OP = 'DELETE' THEN
        INSERT INTO retail.audit_log (
            table_name,
            action,
            store_id,
            record_id,
            old_values
        ) VALUES (
            TG_TABLE_NAME,
            TG_OP,
            COALESCE(OLD.store_id, current_setting('app.current_store_id', true)),
            COALESCE(OLD.customer_id, OLD.product_id, OLD.transaction_id),
            row_to_json(OLD)
        );
        RETURN OLD;
    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO retail.audit_log (
            table_name,
            action,
            store_id,
            record_id,
            old_values,
            new_values
        ) VALUES (
            TG_TABLE_NAME,
            TG_OP,
            COALESCE(NEW.store_id, current_setting('app.current_store_id', true)),
            COALESCE(NEW.customer_id, NEW.product_id, NEW.transaction_id),
            row_to_json(OLD),
            row_to_json(NEW)
        );
        RETURN NEW;
    ELSIF TG_OP = 'INSERT' THEN
        INSERT INTO retail.audit_log (
            table_name,
            action,
            store_id,
            record_id,
            new_values
        ) VALUES (
            TG_TABLE_NAME,
            TG_OP,
            COALESCE(NEW.store_id, current_setting('app.current_store_id', true)),
            COALESCE(NEW.customer_id, NEW.product_id, NEW.transaction_id),
            row_to_json(NEW)
        );
        RETURN NEW;
    END IF;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;

-- Create audit triggers
CREATE TRIGGER customers_audit_trigger
    AFTER INSERT OR UPDATE OR DELETE ON retail.customers
    FOR EACH ROW EXECUTE FUNCTION retail.audit_trigger();

CREATE TRIGGER products_audit_trigger
    AFTER INSERT OR UPDATE OR DELETE ON retail.products
    FOR EACH ROW EXECUTE FUNCTION retail.audit_trigger();

CREATE TRIGGER sales_transactions_audit_trigger
    AFTER INSERT OR UPDATE OR DELETE ON retail.sales_transactions
    FOR EACH ROW EXECUTE FUNCTION retail.audit_trigger();
```

## 📊 నమూనా డేటా సృష్టి

### వాస్తవిక పరీక్ష డేటా స్క్రిప్ట్

```python
# scripts/generate_sample_data.py
"""
Generate realistic sample data for the Zava Retail database.
"""
import asyncio
import asyncpg
import random
import json
from datetime import datetime, timedelta
from faker import Faker
from typing import List, Dict, Any
import numpy as np

fake = Faker()

class SampleDataGenerator:
    """Generate realistic retail sample data."""
    
    def __init__(self, connection_string: str):
        self.connection_string = connection_string
        self.stores = ['seattle', 'redmond', 'bellevue', 'online']
        
        # వాస్తవిక వస్తువులతో ఉత్పత్తి వర్గాలు
        self.product_data = {
            'Electronics': {
                'brands': ['Apple', 'Samsung', 'Sony', 'LG', 'HP', 'Dell'],
                'items': [
                    'Smartphone', 'Laptop', 'Tablet', 'Headphones', 'Smart TV',
                    'Gaming Console', 'Smartwatch', 'Bluetooth Speaker'
                ]
            },
            'Clothing': {
                'brands': ['Nike', 'Adidas', 'Zara', 'H&M', 'Levi\'s', 'Gap'],
                'items': [
                    'T-Shirt', 'Jeans', 'Dress', 'Jacket', 'Sneakers',
                    'Sweater', 'Shorts', 'Blouse'
                ]
            },
            'Home & Garden': {
                'brands': ['IKEA', 'Home Depot', 'Wayfair', 'Target', 'Walmart'],
                'items': [
                    'Sofa', 'Dining Table', 'Lamp', 'Garden Tool', 'Plant Pot',
                    'Curtains', 'Rug', 'Kitchen Appliance'
                ]
            }
        }
    
    async def generate_all_data(self):
        """Generate complete sample dataset."""
        
        conn = await asyncpg.connect(self.connection_string)
        
        try:
            print("🏪 Generating stores data...")
            await self._ensure_stores_exist(conn)
            
            print("👥 Generating customers...")
            customers = await self._generate_customers(conn, 2000)
            
            print("📦 Generating products...")
            products = await self._generate_products(conn, 500)
            
            print("🛒 Generating sales transactions...")
            await self._generate_sales_transactions(conn, customers, products, 5000)
            
            print("✅ Sample data generation complete!")
            
        finally:
            await conn.close()
    
    async def _ensure_stores_exist(self, conn):
        """Ensure all stores exist in the database."""
        
        stores_data = [
            ('seattle', 'Zava Retail Seattle', 'Seattle, WA', 'flagship', 'west'),
            ('redmond', 'Zava Retail Redmond', 'Redmond, WA', 'standard', 'west'),
            ('bellevue', 'Zava Retail Bellevue', 'Bellevue, WA', 'standard', 'west'),
            ('online', 'Zava Retail Online', 'Digital', 'ecommerce', 'global')
        ]
        
        for store_data in stores_data:
            await conn.execute("""
                INSERT INTO retail.stores (store_id, store_name, store_location, store_type, region)
                VALUES ($1, $2, $3, $4, $5)
                ON CONFLICT (store_id) DO NOTHING
            """, *store_data)
    
    async def _generate_customers(self, conn, count: int) -> List[Dict]:
        """Generate realistic customer data."""
        
        customers = []
        
        for _ in range(count):
            store_id = random.choice(self.stores)
            customer_data = {
                'store_id': store_id,
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'email': fake.unique.email(),
                'phone': fake.phone_number()[:20],
                'date_of_birth': fake.date_of_birth(minimum_age=18, maximum_age=80),
                'gender': random.choice(['Male', 'Female', 'Other', 'Prefer not to say']),
                'customer_since': fake.date_between(start_date='-5y', end_date='today'),
                'loyalty_tier': random.choices(
                    ['bronze', 'silver', 'gold', 'platinum'],
                    weights=[50, 30, 15, 5]
                )[0]
            }
            
            customer_id = await conn.fetchval("""
                INSERT INTO retail.customers (
                    store_id, first_name, last_name, email, phone,
                    date_of_birth, gender, customer_since, loyalty_tier
                ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9)
                RETURNING customer_id
            """, *customer_data.values())
            
            customer_data['customer_id'] = customer_id
            customers.append(customer_data)
        
        return customers
    
    async def _generate_products(self, conn, count: int) -> List[Dict]:
        """Generate realistic product data."""
        
        # వర్గ ID లను పొందండి
        categories = await conn.fetch("SELECT category_id, category_name FROM retail.product_categories")
        category_map = {cat['category_name']: cat['category_id'] for cat in categories}
        
        products = []
        
        for _ in range(count):
            store_id = random.choice(self.stores)
            category_name = random.choice(list(self.product_data.keys()))
            category_id = category_map.get(category_name)
            
            if not category_id:
                continue
            
            brand = random.choice(self.product_data[category_name]['brands'])
            item_type = random.choice(self.product_data[category_name]['items'])
            
            # వాస్తవిక ధరలను సృష్టించండి
            base_price = random.uniform(10, 1000)
            cost = base_price * random.uniform(0.4, 0.7)  # 40-70% ఖర్చు మార్జిన్
            
            product_data = {
                'store_id': store_id,
                'sku': f"{brand[:3].upper()}-{fake.unique.random_number(digits=6)}",
                'product_name': f"{brand} {item_type}",
                'product_description': fake.text(max_nb_chars=500),
                'category_id': category_id,
                'brand': brand,
                'model': f"Model {fake.random_number(digits=4)}",
                'color': fake.color_name(),
                'size': random.choice(['XS', 'S', 'M', 'L', 'XL', 'XXL', 'One Size']),
                'weight_kg': round(random.uniform(0.1, 10.0), 2),
                'price': round(base_price, 2),
                'cost': round(cost, 2),
                'current_stock': random.randint(0, 100),
                'minimum_stock': random.randint(5, 20),
                'reorder_point': random.randint(10, 30),
                'supplier_name': fake.company(),
                'is_featured': random.choice([True, False]),
                'rating_average': round(random.uniform(3.0, 5.0), 2),
                'rating_count': random.randint(0, 500),
                'tags': random.sample([
                    'popular', 'new', 'sale', 'limited', 'bestseller', 
                    'eco-friendly', 'premium', 'budget'
                ], k=random.randint(1, 3))
            }
            
            product_id = await conn.fetchval("""
                INSERT INTO retail.products (
                    store_id, sku, product_name, product_description, category_id,
                    brand, model, color, size, weight_kg, price, cost,
                    current_stock, minimum_stock, reorder_point, supplier_name,
                    is_featured, rating_average, rating_count, tags
                ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14, $15, $16, $17, $18, $19, $20)
                RETURNING product_id
            """, *product_data.values())
            
            product_data['product_id'] = product_id
            products.append(product_data)
        
        return products
    
    async def _generate_sales_transactions(self, conn, customers: List[Dict], products: List[Dict], count: int):
        """Generate realistic sales transaction data."""
        
        for _ in range(count):
            # కస్టమర్ మరియు సరిపోయే స్టోర్ ఉత్పత్తులను ఎంచుకోండి
            customer = random.choice(customers)
            store_products = [p for p in products if p['store_id'] == customer['store_id']]
            
            if not store_products:
                continue
            
            # లావాదేవీ ప్రాథమికాలను సృష్టించండి
            transaction_date = fake.date_time_between(start_date='-1y', end_date='now')
            transaction_type = random.choices(
                ['sale', 'return', 'exchange'],
                weights=[90, 7, 3]
            )[0]
            
            payment_method = random.choices(
                ['credit_card', 'debit_card', 'cash', 'digital_wallet'],
                weights=[45, 25, 20, 10]
            )[0]
            
            # లావాదేవీ వస్తువులను సృష్టించండి (ప్రతి లావాదేవీకి 1-5 వస్తువులు)
            num_items = random.choices([1, 2, 3, 4, 5], weights=[40, 30, 20, 7, 3])[0]
            selected_products = random.sample(store_products, min(num_items, len(store_products)))
            
            subtotal = 0
            transaction_items = []
            
            for product in selected_products:
                quantity = random.randint(1, 3)
                unit_price = product['price']
                
                # యాదృచ్ఛిక రాయితీలు అప్పుడప్పుడు వర్తించండి
                discount_amount = 0
                if random.random() < 0.2:  # 20% రాయితీ అవకాశం
                    discount_amount = unit_price * quantity * random.uniform(0.05, 0.25)
                
                total_price = (unit_price * quantity) - discount_amount
                subtotal += total_price
                
                transaction_items.append({
                    'product_id': product['product_id'],
                    'quantity': quantity,
                    'unit_price': unit_price,
                    'total_price': total_price,
                    'discount_amount': discount_amount
                })
            
            # మొత్తం లెక్కించండి
            discount_amount = sum(item['discount_amount'] for item in transaction_items)
            tax_amount = subtotal * 0.08  # 8% పన్ను రేటు
            total_amount = subtotal + tax_amount
            
            # లావాదేవీని చొప్పించండి
            transaction_id = await conn.fetchval("""
                INSERT INTO retail.sales_transactions (
                    store_id, customer_id, transaction_date, transaction_type,
                    payment_method, subtotal, tax_amount, discount_amount, total_amount,
                    cashier_id, register_id, receipt_number
                ) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12)
                RETURNING transaction_id
            """, 
                customer['store_id'], customer['customer_id'], transaction_date,
                transaction_type, payment_method, subtotal, tax_amount,
                discount_amount, total_amount, f"CASHIER{random.randint(1, 10)}",
                f"REG{random.randint(1, 5)}", f"RCP{fake.random_number(digits=8)}"
            )
            
            # లావాదేవీ వస్తువులను చొప్పించండి
            for item in transaction_items:
                await conn.execute("""
                    INSERT INTO retail.sales_transaction_items (
                        transaction_id, product_id, quantity, unit_price,
                        total_price, discount_amount
                    ) VALUES ($1, $2, $3, $4, $5, $6)
                """, 
                    transaction_id, item['product_id'], item['quantity'],
                    item['unit_price'], item['total_price'], item['discount_amount']
                )

# ఉపయోగం ఉదాహరణ
if __name__ == "__main__":
    import os
    from config import Config
    
    config = Config()
    generator = SampleDataGenerator(config.database.connection_string)
    
    asyncio.run(generator.generate_all_data())
```

## 🚀 పనితీరు ఆప్టిమైజేషన్

### డేటాబేస్ కాన్ఫిగరేషన్

```sql
-- Performance-oriented PostgreSQL settings
-- Add to postgresql.conf

# Memory settings
shared_buffers = '256MB'                # 25% of RAM for dedicated DB server
effective_cache_size = '1GB'           # Estimate of OS cache size
work_mem = '4MB'                       # Memory for sorts and hash joins
maintenance_work_mem = '64MB'          # Memory for VACUUM, CREATE INDEX

# Connection settings
max_connections = 100                  # Adjust based on application needs

# Write-ahead logging
wal_buffers = '16MB'
checkpoint_segments = 32               # PostgreSQL < 9.5
max_wal_size = '1GB'                   # PostgreSQL >= 9.5

# Query planner
random_page_cost = 1.1                 # SSD-optimized
effective_io_concurrency = 200         # SSD concurrent I/O capability

# Logging for performance monitoring
log_min_duration_statement = 1000      # Log queries > 1 second
log_checkpoints = on
log_connections = on
log_disconnections = on
log_line_prefix = '%t [%p-%l] %q%u@%d '
```

### క్వెరీ ఆప్టిమైజేషన్ వీక్షణలు

```sql
-- Create monitoring views for query performance
CREATE VIEW retail.slow_queries AS
SELECT 
    query,
    calls,
    total_exec_time,
    mean_exec_time,
    max_exec_time,
    stddev_exec_time,
    rows,
    100.0 * shared_blks_hit / nullif(shared_blks_hit + shared_blks_read, 0) AS hit_percent
FROM pg_stat_statements
WHERE mean_exec_time > 100  -- Queries taking more than 100ms on average
ORDER BY mean_exec_time DESC;

-- Table sizes and index usage
CREATE VIEW retail.table_stats AS
SELECT
    schemaname,
    tablename,
    pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename)) as size,
    pg_stat_get_tuples_inserted(c.oid) as inserts,
    pg_stat_get_tuples_updated(c.oid) as updates,
    pg_stat_get_tuples_deleted(c.oid) as deletes,
    pg_stat_get_live_tuples(c.oid) as live_tuples,
    pg_stat_get_dead_tuples(c.oid) as dead_tuples
FROM pg_tables pt
JOIN pg_class c ON c.relname = pt.tablename
WHERE schemaname = 'retail'
ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC;

-- Index usage statistics
CREATE VIEW retail.index_usage AS
SELECT
    schemaname,
    tablename,
    indexname,
    idx_tup_read,
    idx_tup_fetch,
    pg_size_pretty(pg_relation_size(indexrelname)) as size
FROM pg_stat_user_indexes
WHERE schemaname = 'retail'
ORDER BY idx_tup_read DESC;
```

### ఆటోమేటెడ్ నిర్వహణ

```sql
-- Create function for automated maintenance
CREATE OR REPLACE FUNCTION retail.perform_maintenance()
RETURNS void
LANGUAGE plpgsql
AS $$
BEGIN
    -- Update table statistics
    ANALYZE retail.customers;
    ANALYZE retail.products;
    ANALYZE retail.sales_transactions;
    ANALYZE retail.sales_transaction_items;
    ANALYZE retail.product_embeddings;
    
    -- Vacuum tables with high update/delete activity
    VACUUM (ANALYZE, VERBOSE) retail.customers;
    VACUUM (ANALYZE, VERBOSE) retail.products;
    
    -- Reindex if needed (check for index bloat)
    REINDEX INDEX CONCURRENTLY idx_products_text_search;
    REINDEX INDEX CONCURRENTLY idx_product_embeddings_vector;
    
    -- Log maintenance completion
    INSERT INTO retail.audit_log (
        table_name,
        action,
        metadata
    ) VALUES (
        'maintenance',
        'automated_maintenance_completed',
        jsonb_build_object(
            'timestamp', current_timestamp,
            'database_size', pg_database_size(current_database())
        )
    );
END;
$$;

-- Schedule maintenance (would typically be done via cron or scheduled job)
-- Example cron entry: 0 2 * * 0 psql -d retail_db -c "SELECT retail.perform_maintenance();"
```

## 💾 బ్యాకప్ మరియు రికవరీ

### బ్యాకప్ వ్యూహం

```bash
#!/bin/bash
# scripts/backup_database.sh

# ఉత్పత్తి వాతావరణాల కోసం సమగ్ర బ్యాకప్ స్క్రిప్ట్

set -e

# కాన్ఫిగరేషన్
DB_HOST="${POSTGRES_HOST:-localhost}"
DB_PORT="${POSTGRES_PORT:-5432}"
DB_NAME="${POSTGRES_DB:-retail_db}"
DB_USER="${POSTGRES_USER:-postgres}"
BACKUP_DIR="/backups/postgresql"
RETENTION_DAYS=30

# బ్యాకప్ డైరెక్టరీ సృష్టించండి
mkdir -p "$BACKUP_DIR"

# టైమ్‌స్టాంప్‌తో బ్యాకప్ ఫైల్ పేరు రూపొందించండి
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/retail_backup_$TIMESTAMP.sql"
COMPRESSED_BACKUP="$BACKUP_FILE.gz"

echo "Starting database backup: $TIMESTAMP"

# సమగ్ర బ్యాకప్ సృష్టించండి
pg_dump \
    --host="$DB_HOST" \
    --port="$DB_PORT" \
    --username="$DB_USER" \
    --dbname="$DB_NAME" \
    --verbose \
    --clean \
    --create \
    --if-exists \
    --format=custom \
    --file="$BACKUP_FILE"

# బ్యాకప్‌ను కంప్రెస్ చేయండి
gzip "$BACKUP_FILE"

# బ్యాకప్ సమగ్రతను ధృవీకరించండి
echo "Verifying backup integrity..."
pg_restore --list "$COMPRESSED_BACKUP" > /dev/null

# పాత బ్యాకప్‌లను శుభ్రపరచండి
find "$BACKUP_DIR" -name "retail_backup_*.sql.gz" -mtime +$RETENTION_DAYS -delete

# బ్యాకప్ పరిమాణాన్ని లెక్కించండి
BACKUP_SIZE=$(du -h "$COMPRESSED_BACKUP" | cut -f1)

echo "Backup completed successfully:"
echo "  File: $COMPRESSED_BACKUP"
echo "  Size: $BACKUP_SIZE"
echo "  Timestamp: $TIMESTAMP"

# ఐచ్ఛికం: క్లౌడ్ స్టోరేజ్‌కు అప్‌లోడ్ చేయండి
if [ -n "$AZURE_STORAGE_ACCOUNT" ] && [ -n "$AZURE_STORAGE_KEY" ]; then
    echo "Uploading backup to Azure Storage..."
    az storage blob upload \
        --account-name "$AZURE_STORAGE_ACCOUNT" \
        --account-key "$AZURE_STORAGE_KEY" \
        --container-name "database-backups" \
        --name "retail_backup_$TIMESTAMP.sql.gz" \
        --file "$COMPRESSED_BACKUP"
fi
```

### రికవరీ ప్రక్రియలు

```bash
#!/bin/bash
# scripts/restore_database.sh

# డేటాబేస్ పునరుద్ధరణ స్క్రిప్ట్

set -e

if [ $# -lt 1 ]; then
    echo "Usage: $0 <backup_file> [target_database]"
    echo "Example: $0 /backups/retail_backup_20241001_120000.sql.gz retail_db_restored"
    exit 1
fi

BACKUP_FILE="$1"
TARGET_DB="${2:-retail_db_restored}"

# కాన్ఫిగరేషన్
DB_HOST="${POSTGRES_HOST:-localhost}"
DB_PORT="${POSTGRES_PORT:-5432}"
DB_USER="${POSTGRES_USER:-postgres}"

echo "Starting database restoration..."
echo "  Source: $BACKUP_FILE"
echo "  Target: $TARGET_DB"

# బ్యాకప్ ఫైల్ ఉన్నదని నిర్ధారించండి
if [ ! -f "$BACKUP_FILE" ]; then
    echo "Error: Backup file not found: $BACKUP_FILE"
    exit 1
fi

# లక్ష్య డేటాబేస్ సృష్టించండి
createdb \
    --host="$DB_HOST" \
    --port="$DB_PORT" \
    --username="$DB_USER" \
    --owner="$DB_USER" \
    "$TARGET_DB"

# బ్యాకప్ నుండి పునరుద్ధరించండి
if [[ "$BACKUP_FILE" == *.gz ]]; then
    # సంకుచిత బ్యాకప్
    gunzip -c "$BACKUP_FILE" | pg_restore \
        --host="$DB_HOST" \
        --port="$DB_PORT" \
        --username="$DB_USER" \
        --dbname="$TARGET_DB" \
        --verbose \
        --clean \
        --if-exists
else
    # అసంకుచిత బ్యాకప్
    pg_restore \
        --host="$DB_HOST" \
        --port="$DB_PORT" \
        --username="$DB_USER" \
        --dbname="$TARGET_DB" \
        --verbose \
        --clean \
        --if-exists \
        "$BACKUP_FILE"
fi

echo "Database restoration completed successfully!"
echo "Restored database: $TARGET_DB"

# పునరుద్ధరణను నిర్ధారించండి
echo "Verifying restoration..."
TABLES_COUNT=$(psql \
    --host="$DB_HOST" \
    --port="$DB_PORT" \
    --username="$DB_USER" \
    --dbname="$TARGET_DB" \
    --tuples-only \
    --command="SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'retail';"
)

echo "Verified $TABLES_COUNT tables in retail schema"
```

## 🎯 ముఖ్యమైన పాఠాలు

ఈ ప్రయోగశాల పూర్తి చేసిన తర్వాత, మీరు కలిగి ఉండాలి:

✅ **బహుళ-టెనెంట్ డేటాబేస్ డిజైన్**: భద్రతా డేటా వేరుపాటు కోసం రో లెవల్ సెక్యూరిటీ అమలు చేయబడింది  
✅ **వెక్టర్ సెర్చ్ సామర్థ్యాలు**: సెమాంటిక్ ఉత్పత్తి సెర్చ్ కోసం pgvector కాన్ఫిగర్ చేయబడింది  
✅ **సంపూర్ణ స్కీమా**: ఉత్పత్తి-సిద్ధ రిటైల్ డేటాబేస్ స్కీమా సృష్టించబడింది  
✅ **నమూనా డేటా సృష్టి**: అభివృద్ధి మరియు పరీక్ష కోసం వాస్తవిక పరీక్ష డేటా నిర్మించబడింది  
✅ **పనితీరు ఆప్టిమైజేషన్**: సూచికలు మరియు క్వెరీ ఆప్టిమైజేషన్ కాన్ఫిగర్ చేయబడింది  
✅ **బ్యాకప్ మరియు రికవరీ**: బలమైన డేటా రక్షణ వ్యూహాలు స్థాపించబడ్డాయి  

## 🚀 తదుపరి ఏమిటి

**[Lab 05: MCP Server Implementation](../05-MCP-Server/README.md)** తో కొనసాగండి:

- ఈ డేటాబేస్‌కు కనెక్ట్ అయ్యే FastMCP సర్వర్ నిర్మించండి  
- MCP ప్రోటోకాల్ కోసం డేటాబేస్ క్వెరీ టూల్స్ అమలు చేయండి  
- ఎంబెడ్డింగ్స్ ఉపయోగించి సెమాంటిక్ సెర్చ్ సామర్థ్యాలు జోడించండి  
- కనెక్షన్ పూలింగ్ మరియు లోపాల నిర్వహణ కాన్ఫిగర్ చేయండి  

## 📚 అదనపు వనరులు

### PostgreSQL & pgvector
- [PostgreSQL డాక్యుమెంటేషన్](https://www.postgresql.org/docs/) - పూర్తి PostgreSQL సూచిక  
- [pgvector విస్తరణ](https://github.com/pgvector/pgvector) - PostgreSQL కోసం వెక్టర్ సాదృశ్య సెర్చ్  
- [PostgreSQL పనితీరు ట్యూనింగ్](https://wiki.postgresql.org/wiki/Performance_Optimization) - ఆప్టిమైజేషన్ ఉత్తమ పద్ధతులు  

### బహుళ-టెనెంట్ ఆర్కిటెక్చర్
- [రో లెవల్ సెక్యూరిటీ](https://www.postgresql.org/docs/current/ddl-rowsecurity.html) - PostgreSQL RLS డాక్యుమెంటేషన్  
- [బహుళ-టెనెంట్ డేటా ఆర్కిటెక్చర్](https://docs.microsoft.com/azure/architecture/patterns/multitenancy) - Azure ఆర్కిటెక్చర్ నమూనాలు  
- [డేటాబేస్ భద్రత ఉత్తమ పద్ధతులు](https://www.postgresql.org/docs/current/security.html) - PostgreSQL భద్రత గైడ్  

### వెక్టర్ డేటాబేసులు
- [వెక్టర్ సెర్చ్ మౌలికాలు](https://www.pinecone.io/learn/vector-database/) - వెక్టర్ డేటాబేసులను అర్థం చేసుకోవడం  
- [ఎంబెడ్డింగ్ మోడల్స్](https://platform.openai.com/docs/guides/embeddings) - OpenAI ఎంబెడ్డింగ్స్ డాక్యుమెంటేషన్  
- [HNSW అల్గోరిథం](https://arxiv.org/abs/1603.09320) - హైరార్కికల్ నావిగబుల్ స్మాల్ వరల్డ్ గ్రాఫ్స్  

---

**మునుపటి**: [Lab 03: Environment Setup](../03-Setup/README.md)  
**తదుపరి**: [Lab 05: MCP Server Implementation](../05-MCP-Server/README.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->