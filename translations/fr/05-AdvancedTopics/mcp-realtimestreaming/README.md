# Protocole de Contexte de Modèle pour le Streaming de Données en Temps Réel

## Vue d'ensemble

Le streaming de données en temps réel est devenu essentiel dans le monde axé sur les données d’aujourd’hui, où les entreprises et les applications ont besoin d’un accès immédiat à l’information pour prendre des décisions rapides. Le Model Context Protocol (MCP) représente une avancée majeure dans l’optimisation de ces processus de streaming en temps réel, améliorant l’efficacité du traitement des données, préservant l’intégrité contextuelle et renforçant la performance globale des systèmes.

Ce module explore comment MCP transforme le streaming de données en temps réel en offrant une approche standardisée de la gestion du contexte entre les modèles d’IA, les plateformes de streaming et les applications.

## Introduction au Streaming de Données en Temps Réel

Le streaming de données en temps réel est un paradigme technologique qui permet le transfert, le traitement et l’analyse continus des données dès leur génération, permettant aux systèmes de réagir immédiatement aux nouvelles informations. Contrairement au traitement par lots traditionnel qui opère sur des ensembles de données statiques, le streaming traite les données en mouvement, fournissant des insights et des actions avec une latence minimale.

### Concepts clés du Streaming de Données en Temps Réel :

- **Flux de Données Continu** : Les données sont traitées comme un flux continu et ininterrompu d’événements ou d’enregistrements.
- **Traitement à Faible Latence** : Les systèmes sont conçus pour minimiser le délai entre la génération et le traitement des données.
- **Scalabilité** : Les architectures de streaming doivent gérer des volumes et des vitesses de données variables.
- **Tolérance aux Pannes** : Les systèmes doivent être résilients face aux défaillances pour garantir un flux de données ininterrompu.
- **Traitement Stateful** : Maintenir le contexte entre les événements est crucial pour une analyse pertinente.

### Le Model Context Protocol et le Streaming en Temps Réel

Le Model Context Protocol (MCP) répond à plusieurs défis majeurs dans les environnements de streaming en temps réel :

1. **Continuité Contextuelle** : MCP standardise la manière dont le contexte est maintenu à travers les composants distribués du streaming, garantissant que les modèles d’IA et les nœuds de traitement ont accès au contexte historique et environnemental pertinent.

2. **Gestion Efficace de l’État** : En fournissant des mécanismes structurés pour la transmission du contexte, MCP réduit la charge liée à la gestion de l’état dans les pipelines de streaming.

3. **Interopérabilité** : MCP crée un langage commun pour le partage du contexte entre différentes technologies de streaming et modèles d’IA, permettant des architectures plus flexibles et extensibles.

4. **Contexte Optimisé pour le Streaming** : Les implémentations MCP peuvent prioriser les éléments de contexte les plus pertinents pour la prise de décision en temps réel, optimisant à la fois la performance et la précision.

5. **Traitement Adaptatif** : Grâce à une gestion appropriée du contexte via MCP, les systèmes de streaming peuvent ajuster dynamiquement leur traitement en fonction des conditions et des tendances évolutives des données.

Dans les applications modernes, allant des réseaux de capteurs IoT aux plateformes de trading financier, l’intégration de MCP avec les technologies de streaming permet un traitement plus intelligent et contextuel, capable de répondre de manière appropriée à des situations complexes et évolutives en temps réel.

## Objectifs d’apprentissage

À la fin de cette leçon, vous serez capable de :

- Comprendre les fondamentaux du streaming de données en temps réel et ses défis
- Expliquer comment le Model Context Protocol (MCP) améliore le streaming de données en temps réel
- Implémenter des solutions de streaming basées sur MCP avec des frameworks populaires comme Kafka et Pulsar
- Concevoir et déployer des architectures de streaming tolérantes aux pannes et performantes avec MCP
- Appliquer les concepts MCP aux cas d’usage IoT, trading financier et analyses pilotées par l’IA
- Évaluer les tendances émergentes et les innovations futures dans les technologies de streaming basées sur MCP

### Définition et Importance

Le streaming de données en temps réel implique la génération, le traitement et la livraison continus des données avec une latence minimale. Contrairement au traitement par lots, où les données sont collectées et traitées en groupes, les données en streaming sont traitées de manière incrémentale dès leur arrivée, permettant des insights et des actions immédiats.

Les caractéristiques clés du streaming de données en temps réel incluent :

- **Faible Latence** : Traitement et analyse des données en quelques millisecondes à secondes
- **Flux Continu** : Flux ininterrompus de données provenant de diverses sources
- **Traitement Immédiat** : Analyse des données dès leur arrivée plutôt qu’en lots
- **Architecture Événementielle** : Réponse aux événements dès leur occurrence

### Défis du Streaming de Données Traditionnel

Les approches traditionnelles de streaming de données rencontrent plusieurs limites :

1. **Perte de Contexte** : Difficulté à maintenir le contexte dans des systèmes distribués
2. **Problèmes de Scalabilité** : Difficultés à gérer des volumes et vitesses de données élevés
3. **Complexité d’Intégration** : Problèmes d’interopérabilité entre différents systèmes
4. **Gestion de la Latence** : Équilibrer le débit et le temps de traitement
5. **Cohérence des Données** : Assurer l’exactitude et la complétude des données dans le flux

## Comprendre le Model Context Protocol (MCP)

### Qu’est-ce que MCP ?

Le Model Context Protocol (MCP) est un protocole de communication standardisé conçu pour faciliter une interaction efficace entre les modèles d’IA et les applications. Dans le contexte du streaming de données en temps réel, MCP fournit un cadre pour :

- Préserver le contexte tout au long du pipeline de données
- Standardiser les formats d’échange de données
- Optimiser la transmission de grands ensembles de données
- Améliorer la communication modèle-à-modèle et modèle-à-application

### Composants clés et Architecture

L’architecture MCP pour le streaming en temps réel comprend plusieurs composants essentiels :

1. **Gestionnaires de Contexte** : Gèrent et maintiennent les informations contextuelles à travers le pipeline de streaming
2. **Processeurs de Flux** : Traitent les flux de données entrants en utilisant des techniques conscientes du contexte
3. **Adaptateurs de Protocole** : Convertissent entre différents protocoles de streaming tout en préservant le contexte
4. **Stockage de Contexte** : Stocke et récupère efficacement les informations contextuelles
5. **Connecteurs de Streaming** : Se connectent à diverses plateformes de streaming (Kafka, Pulsar, Kinesis, etc.)

```mermaid
graph TD
    subgraph "Data Sources"
        IoT[IoT Devices]
        APIs[APIs]
        DB[Databases]
        Apps[Applications]
    end

    subgraph "MCP Streaming Layer"
        SC[Streaming Connectors]
        PA[Protocol Adapters]
        CH[Context Handlers]
        SP[Stream Processors]
        CS[Context Store]
    end

    subgraph "Processing & Analytics"
        RT[Real-time Analytics]
        ML[ML Models]
        CEP[Complex Event Processing]
        Viz[Visualization]
    end

    subgraph "Applications & Services"
        DA[Decision Automation]
        Alerts[Alerting Systems]
        DL[Data Lake/Warehouse]
        API[API Services]
    end

    IoT -->|Data| SC
    APIs -->|Data| SC
    DB -->|Changes| SC
    Apps -->|Events| SC
    
    SC -->|Raw Streams| PA
    PA -->|Normalized Streams| CH
    CH <-->|Context Operations| CS
    CH -->|Context-Enriched Data| SP
    SP -->|Processed Streams| RT
    SP -->|Features| ML
    SP -->|Events| CEP
    
    RT -->|Insights| Viz
    ML -->|Predictions| DA
    CEP -->|Complex Events| Alerts
    Viz -->|Dashboards| Users((Users))
    
    RT -.->|Historical Data| DL
    ML -.->|Model Results| DL
    CEP -.->|Event Logs| DL
    
    DA -->|Actions| API
    Alerts -->|Notifications| API
    DL <-->|Data Access| API
    
    classDef sources fill:#f9f,stroke:#333,stroke-width:2px
    classDef mcp fill:#bbf,stroke:#333,stroke-width:2px
    classDef processing fill:#bfb,stroke:#333,stroke-width:2px
    classDef apps fill:#fbb,stroke:#333,stroke-width:2px
    
    class IoT,APIs,DB,Apps sources
    class SC,PA,CH,SP,CS mcp
    class RT,ML,CEP,Viz processing
    class DA,Alerts,DL,API apps
```

### Comment MCP Améliore la Gestion des Données en Temps Réel

MCP répond aux défis traditionnels du streaming par :

- **Intégrité Contextuelle** : Maintenir les relations entre les points de données sur l’ensemble du pipeline
- **Transmission Optimisée** : Réduire la redondance dans l’échange de données grâce à une gestion intelligente du contexte
- **Interfaces Standardisées** : Fournir des API cohérentes pour les composants de streaming
- **Latence Réduite** : Minimiser la surcharge de traitement grâce à une gestion efficace du contexte
- **Scalabilité Améliorée** : Supporter la montée en charge horizontale tout en préservant le contexte

## Intégration et Mise en Œuvre

Les systèmes de streaming de données en temps réel nécessitent une conception architecturale et une mise en œuvre soignées pour maintenir à la fois la performance et l’intégrité contextuelle. Le Model Context Protocol offre une approche standardisée pour intégrer les modèles d’IA et les technologies de streaming, permettant des pipelines de traitement plus sophistiqués et conscients du contexte.

### Vue d’ensemble de l’Intégration MCP dans les Architectures de Streaming

La mise en œuvre de MCP dans les environnements de streaming en temps réel implique plusieurs considérations clés :

1. **Sérialisation et Transport du Contexte** : MCP fournit des mécanismes efficaces pour encoder les informations contextuelles dans les paquets de données en streaming, garantissant que le contexte essentiel accompagne les données tout au long du pipeline de traitement. Cela inclut des formats de sérialisation standardisés optimisés pour le transport en streaming.

2. **Traitement Stateful des Flux** : MCP permet un traitement stateful plus intelligent en maintenant une représentation cohérente du contexte entre les nœuds de traitement. Ceci est particulièrement précieux dans les architectures de streaming distribuées où la gestion de l’état est traditionnellement complexe.

3. **Temps d’Événement vs Temps de Traitement** : Les implémentations MCP dans les systèmes de streaming doivent gérer le défi courant de différencier le moment où les événements se sont produits et celui où ils sont traités. Le protocole peut intégrer un contexte temporel qui préserve la sémantique du temps d’événement.

4. **Gestion du Backpressure** : En standardisant la gestion du contexte, MCP aide à gérer le backpressure dans les systèmes de streaming, permettant aux composants de communiquer leurs capacités de traitement et d’ajuster le flux en conséquence.

5. **Fenêtrage et Agrégation du Contexte** : MCP facilite des opérations de fenêtrage plus sophistiquées en fournissant des représentations structurées des contextes temporels et relationnels, permettant des agrégations plus significatives à travers les flux d’événements.

6. **Traitement Exactly-Once** : Dans les systèmes de streaming nécessitant une sémantique exactly-once, MCP peut intégrer des métadonnées de traitement pour aider à suivre et vérifier le statut du traitement à travers les composants distribués.

La mise en œuvre de MCP à travers diverses technologies de streaming crée une approche unifiée de la gestion du contexte, réduisant le besoin de code d’intégration personnalisé tout en améliorant la capacité du système à maintenir un contexte pertinent au fur et à mesure que les données circulent dans le pipeline.

### MCP dans Divers Frameworks de Streaming de Données

Ces exemples suivent la spécification MCP actuelle qui se concentre sur un protocole basé sur JSON-RPC avec des mécanismes de transport distincts. Le code montre comment vous pouvez implémenter des transports personnalisés qui intègrent des plateformes de streaming comme Kafka et Pulsar tout en conservant une compatibilité totale avec le protocole MCP.

Les exemples sont conçus pour montrer comment les plateformes de streaming peuvent être intégrées avec MCP afin de fournir un traitement de données en temps réel tout en préservant la conscience contextuelle qui est au cœur de MCP. Cette approche garantit que les exemples de code reflètent fidèlement l’état actuel de la spécification MCP à la date de juin 2025.

MCP peut être intégré avec des frameworks de streaming populaires, notamment :

#### Intégration Apache Kafka

```python
import asyncio
import json
from typing import Dict, Any, Optional
from confluent_kafka import Consumer, Producer, KafkaError
from mcp.client import Client, ClientCapabilities
from mcp.core.message import JsonRpcMessage
from mcp.core.transports import Transport

# Custom transport class to bridge MCP with Kafka
class KafkaMCPTransport(Transport):
    def __init__(self, bootstrap_servers: str, input_topic: str, output_topic: str):
        self.bootstrap_servers = bootstrap_servers
        self.input_topic = input_topic
        self.output_topic = output_topic
        self.producer = Producer({'bootstrap.servers': bootstrap_servers})
        self.consumer = Consumer({
            'bootstrap.servers': bootstrap_servers,
            'group.id': 'mcp-client-group',
            'auto.offset.reset': 'earliest'
        })
        self.message_queue = asyncio.Queue()
        self.running = False
        self.consumer_task = None
        
    async def connect(self):
        """Connect to Kafka and start consuming messages"""
        self.consumer.subscribe([self.input_topic])
        self.running = True
        self.consumer_task = asyncio.create_task(self._consume_messages())
        return self
        
    async def _consume_messages(self):
        """Background task to consume messages from Kafka and queue them for processing"""
        while self.running:
            try:
                msg = self.consumer.poll(1.0)
                if msg is None:
                    await asyncio.sleep(0.1)
                    continue
                
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    print(f"Consumer error: {msg.error()}")
                    continue
                
                # Parse the message value as JSON-RPC
                try:
                    message_str = msg.value().decode('utf-8')
                    message_data = json.loads(message_str)
                    mcp_message = JsonRpcMessage.from_dict(message_data)
                    await self.message_queue.put(mcp_message)
                except Exception as e:
                    print(f"Error parsing message: {e}")
            except Exception as e:
                print(f"Error in consumer loop: {e}")
                await asyncio.sleep(1)
    
    async def read(self) -> Optional[JsonRpcMessage]:
        """Read the next message from the queue"""
        try:
            message = await self.message_queue.get()
            return message
        except Exception as e:
            print(f"Error reading message: {e}")
            return None
    
    async def write(self, message: JsonRpcMessage) -> None:
        """Write a message to the Kafka output topic"""
        try:
            message_json = json.dumps(message.to_dict())
            self.producer.produce(
                self.output_topic,
                message_json.encode('utf-8'),
                callback=self._delivery_report
            )
            self.producer.poll(0)  # Trigger callbacks
        except Exception as e:
            print(f"Error writing message: {e}")
    
    def _delivery_report(self, err, msg):
        """Kafka producer delivery callback"""
        if err is not None:
            print(f'Message delivery failed: {err}')
        else:
            print(f'Message delivered to {msg.topic()} [{msg.partition()}]')
    
    async def close(self) -> None:
        """Close the transport"""
        self.running = False
        if self.consumer_task:
            self.consumer_task.cancel()
            try:
                await self.consumer_task
            except asyncio.CancelledError:
                pass
        self.consumer.close()
        self.producer.flush()

# Example usage of the Kafka MCP transport
async def kafka_mcp_example():
    # Create MCP client with Kafka transport
    client = Client(
        {"name": "kafka-mcp-client", "version": "1.0.0"},
        ClientCapabilities({})
    )
    
    # Create and connect the Kafka transport
    transport = KafkaMCPTransport(
        bootstrap_servers="localhost:9092",
        input_topic="mcp-responses",
        output_topic="mcp-requests"
    )
    
    await client.connect(transport)
    
    try:
        # Initialize the MCP session
        await client.initialize()
        
        # Example of executing a tool via MCP
        response = await client.execute_tool(
            "process_data",
            {
                "data": "sample data",
                "metadata": {
                    "source": "sensor-1",
                    "timestamp": "2025-06-12T10:30:00Z"
                }
            }
        )
        
        print(f"Tool execution response: {response}")
        
        # Clean shutdown
        await client.shutdown()
    finally:
        await transport.close()

# Run the example
if __name__ == "__main__":
    asyncio.run(kafka_mcp_example())
```

#### Implémentation Apache Pulsar

```python
import asyncio
import json
import pulsar
from typing import Dict, Any, Optional
from mcp.core.message import JsonRpcMessage
from mcp.core.transports import Transport
from mcp.server import Server, ServerOptions
from mcp.server.tools import Tool, ToolExecutionContext, ToolMetadata

# Create a custom MCP transport that uses Pulsar
class PulsarMCPTransport(Transport):
    def __init__(self, service_url: str, request_topic: str, response_topic: str):
        self.service_url = service_url
        self.request_topic = request_topic
        self.response_topic = response_topic
        self.client = pulsar.Client(service_url)
        self.producer = self.client.create_producer(response_topic)
        self.consumer = self.client.subscribe(
            request_topic,
            "mcp-server-subscription",
            consumer_type=pulsar.ConsumerType.Shared
        )
        self.message_queue = asyncio.Queue()
        self.running = False
        self.consumer_task = None
    
    async def connect(self):
        """Connect to Pulsar and start consuming messages"""
        self.running = True
        self.consumer_task = asyncio.create_task(self._consume_messages())
        return self
    
    async def _consume_messages(self):
        """Background task to consume messages from Pulsar and queue them for processing"""
        while self.running:
            try:
                # Non-blocking receive with timeout
                msg = self.consumer.receive(timeout_millis=500)
                
                # Process the message
                try:
                    message_str = msg.data().decode('utf-8')
                    message_data = json.loads(message_str)
                    mcp_message = JsonRpcMessage.from_dict(message_data)
                    await self.message_queue.put(mcp_message)
                    
                    # Acknowledge the message
                    self.consumer.acknowledge(msg)
                except Exception as e:
                    print(f"Error processing message: {e}")
                    # Negative acknowledge if there was an error
                    self.consumer.negative_acknowledge(msg)
            except Exception as e:
                # Handle timeout or other exceptions
                await asyncio.sleep(0.1)
    
    async def read(self) -> Optional[JsonRpcMessage]:
        """Read the next message from the queue"""
        try:
            message = await self.message_queue.get()
            return message
        except Exception as e:
            print(f"Error reading message: {e}")
            return None
    
    async def write(self, message: JsonRpcMessage) -> None:
        """Write a message to the Pulsar output topic"""
        try:
            message_json = json.dumps(message.to_dict())
            self.producer.send(message_json.encode('utf-8'))
        except Exception as e:
            print(f"Error writing message: {e}")
    
    async def close(self) -> None:
        """Close the transport"""
        self.running = False
        if self.consumer_task:
            self.consumer_task.cancel()
            try:
                await self.consumer_task
            except asyncio.CancelledError:
                pass
        self.consumer.close()
        self.producer.close()
        self.client.close()

# Define a sample MCP tool that processes streaming data
@Tool(
    name="process_streaming_data",
    description="Process streaming data with context preservation",
    metadata=ToolMetadata(
        required_capabilities=["streaming"]
    )
)
async def process_streaming_data(
    ctx: ToolExecutionContext,
    data: str,
    source: str,
    priority: str = "medium"
) -> Dict[str, Any]:
    """
    Process streaming data while preserving context
    
    Args:
        ctx: Tool execution context
        data: The data to process
        source: The source of the data
        priority: Priority level (low, medium, high)
        
    Returns:
        Dict containing processed results and context information
    """
    # Example processing that leverages MCP context
    print(f"Processing data from {source} with priority {priority}")
    
    # Access conversation context from MCP
    conversation_id = ctx.conversation_id if hasattr(ctx, 'conversation_id') else "unknown"
    
    # Return results with enhanced context
    return {
        "processed_data": f"Processed: {data}",
        "context": {
            "conversation_id": conversation_id,
            "source": source,
            "priority": priority,
            "processing_timestamp": ctx.get_current_time_iso()
        }
    }

# Example MCP server implementation using Pulsar transport
async def run_mcp_server_with_pulsar():
    # Create MCP server
    server = Server(
        {"name": "pulsar-mcp-server", "version": "1.0.0"},
        ServerOptions(
            capabilities={"streaming": True}
        )
    )
    
    # Register our tool
    server.register_tool(process_streaming_data)
    
    # Create and connect Pulsar transport
    transport = PulsarMCPTransport(
        service_url="pulsar://localhost:6650",
        request_topic="mcp-requests",
        response_topic="mcp-responses"
    )
    
    try:
        # Start the server with the Pulsar transport
        await server.run(transport)
    finally:
        await transport.close()

# Run the server
if __name__ == "__main__":
    asyncio.run(run_mcp_server_with_pulsar())
```

### Bonnes Pratiques pour le Déploiement

Lors de la mise en œuvre de MCP pour le streaming en temps réel :

1. **Concevoir pour la Tolérance aux Pannes** :
   - Mettre en place une gestion appropriée des erreurs
   - Utiliser des dead-letter queues pour les messages échoués
   - Concevoir des processeurs idempotents

2. **Optimiser la Performance** :
   - Configurer des tailles de buffers adaptées
   - Utiliser le batching lorsque c’est pertinent
   - Mettre en œuvre des mécanismes de backpressure

3. **Surveiller et Observer** :
   - Suivre les métriques de traitement des flux
   - Contrôler la propagation du contexte
   - Configurer des alertes pour les anomalies

4. **Sécuriser vos Flux** :
   - Mettre en place le chiffrement des données sensibles
   - Utiliser l’authentification et l’autorisation
   - Appliquer des contrôles d’accès appropriés

### MCP dans l’IoT et le Edge Computing

MCP améliore le streaming IoT en :

- Préservant le contexte des appareils tout au long du pipeline de traitement
- Permettant un streaming efficace du edge vers le cloud
- Supportant l’analyse en temps réel des flux de données IoT
- Facilitant la communication device-to-device avec contexte

Exemple : Réseaux de capteurs pour villes intelligentes  
```
Sensors → Edge Gateways → MCP Stream Processors → Real-time Analytics → Automated Responses
```

### Rôle dans les Transactions Financières et le Trading Haute Fréquence

MCP offre des avantages significatifs pour le streaming de données financières :

- Traitement à ultra-faible latence pour les décisions de trading
- Maintien du contexte transactionnel tout au long du traitement
- Support du traitement complexe d’événements avec conscience contextuelle
- Garantie de la cohérence des données dans les systèmes de trading distribués

### Amélioration de l’Analyse de Données Pilotée par l’IA

MCP ouvre de nouvelles possibilités pour l’analyse en streaming :

- Entraînement et inférence de modèles en temps réel
- Apprentissage continu à partir des données en streaming
- Extraction de caractéristiques consciente du contexte
- Pipelines d’inférence multi-modèles avec contexte préservé

## Tendances et Innovations Futures

### Évolution de MCP dans les Environnements Temps Réel

À l’avenir, nous anticipons que MCP évoluera pour répondre à :

- **Intégration de l’Informatique Quantique** : Préparation aux systèmes de streaming basés sur le quantique
- **Traitement Edge-Natif** : Déplacement de plus de traitements contextuels vers les appareils edge
- **Gestion Autonome des Flux** : Pipelines de streaming auto-optimisés
- **Streaming Fédéré** : Traitement distribué tout en préservant la confidentialité

### Avancées Technologiques Potentielles

Les technologies émergentes qui façonneront l’avenir du streaming MCP :

1. **Protocoles de Streaming Optimisés pour l’IA** : Protocoles personnalisés conçus spécifiquement pour les charges de travail IA
2. **Intégration de l’Informatique Neuromorphique** : Calcul inspiré du cerveau pour le traitement des flux
3. **Streaming Serverless** : Streaming scalable et événementiel sans gestion d’infrastructure
4. **Stores de Contexte Distribués** : Gestion du contexte globalement distribuée mais hautement cohérente

## Exercices Pratiques

### Exercice 1 : Mise en place d’un Pipeline de Streaming MCP Basique

Dans cet exercice, vous apprendrez à :  
- Configurer un environnement de streaming MCP basique  
- Implémenter des gestionnaires de contexte pour le traitement des flux  
- Tester et valider la préservation du contexte

### Exercice 2 : Création d’un Tableau de Bord d’Analyse en Temps Réel

Créez une application complète qui :  
- Ingest les données en streaming via MCP  
- Traite le flux tout en maintenant le contexte  
- Visualise les résultats en temps réel

### Exercice 3 : Implémentation du Traitement Complexe d’Événements avec MCP

Exercice avancé couvrant :  
- La détection de motifs dans les flux  
- La corrélation contextuelle entre plusieurs flux  
- La génération d’événements complexes avec contexte préservé

## Ressources Supplémentaires

- [Model Context Protocol Specification](https://github.com/modelcontextprotocol) - Spécification officielle MCP et documentation  
- [Apache Kafka Documentation](https://kafka.apache.org/documentation/) - Apprenez Kafka pour le traitement de flux  
- [Apache Pulsar](https://pulsar.apache.org/) - Plateforme unifiée de messagerie et streaming  
- [Streaming Systems: The What, Where, When, and How of Large-Scale Data Processing](https://www.oreilly.com/library/view/streaming-systems/9781491983867/) - Livre complet sur les architectures de streaming  
- [Microsoft Azure Event Hubs](https://learn.microsoft.com/azure/event-hubs/event-hubs-about) - Service de streaming d’événements managé  
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html) - Pour le suivi et le déploiement de modèles ML  
- [Real-Time Analytics with Apache Storm](https://storm.apache.org/releases/current/index.html) - Framework de traitement pour le calcul en temps réel  
- [Flink ML](https://nightlies.apache.org/flink/flink-ml-docs-master/) - Bibliothèque de machine learning pour Apache Flink  
- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction) - Construire des applications avec des LLM

## Résultats d’apprentissage

En complétant ce module, vous serez capable de :

- Comprendre les fondamentaux du streaming de données en temps réel et ses défis  
- Expliquer comment le Model Context Protocol (MCP) améliore le streaming de données en temps réel  
- Implémenter des solutions de streaming basées sur MCP avec des frameworks populaires comme Kafka et Pulsar  
- Concevoir et déployer des architectures de streaming tolérantes aux pannes et performantes avec MCP  
- Appliquer les concepts MCP aux cas d’usage IoT, trading financier et analyses pilotées par l’IA  
- Évaluer les tendances émergentes et les innovations futures dans les technologies de streaming basées sur MCP

## Et après ?

- [5.11 Realtime Search](../mcp-realtimesearch/README.md)

**Avertissement** :  
Ce document a été traduit à l’aide du service de traduction automatique [Co-op Translator](https://github.com/Azure/co-op-translator). Bien que nous nous efforcions d’assurer l’exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d’origine doit être considéré comme la source faisant foi. Pour les informations critiques, une traduction professionnelle réalisée par un humain est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l’utilisation de cette traduction.