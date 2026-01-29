# Segurança Avançada MCP com Azure Content Safety

O Azure Content Safety oferece várias ferramentas poderosas que podem aumentar a segurança das suas implementações MCP:

## Prompt Shields

Os AI Prompt Shields da Microsoft fornecem proteção robusta contra ataques de injeção de prompt, tanto diretos quanto indiretos, por meio de:

1. **Detecção Avançada**: Utiliza aprendizado de máquina para identificar instruções maliciosas embutidas no conteúdo.
2. **Destaque**: Transforma o texto de entrada para ajudar os sistemas de IA a distinguir entre instruções válidas e entradas externas.
3. **Delimitadores e Marcação de Dados**: Marca os limites entre dados confiáveis e não confiáveis.
4. **Integração com Content Safety**: Funciona com o Azure AI Content Safety para detectar tentativas de jailbreak e conteúdo prejudicial.
5. **Atualizações Contínuas**: A Microsoft atualiza regularmente os mecanismos de proteção contra ameaças emergentes.

## Implementando Azure Content Safety com MCP

Essa abordagem oferece proteção em múltiplas camadas:
- Escaneando entradas antes do processamento
- Validando saídas antes de retornar
- Usando listas de bloqueio para padrões conhecidos de risco
- Aproveitando os modelos de segurança de conteúdo do Azure, que são atualizados continuamente

## Recursos do Azure Content Safety

Para saber mais sobre como implementar o Azure Content Safety com seus servidores MCP, consulte estes recursos oficiais:

1. [Documentação do Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Documentação oficial do Azure Content Safety.
2. [Documentação do Prompt Shield](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Aprenda como prevenir ataques de injeção de prompt.
3. [Referência da API Content Safety](https://learn.microsoft.com/rest/api/contentsafety/) - Referência detalhada da API para implementar Content Safety.
4. [Início Rápido: Azure Content Safety com C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Guia rápido de implementação usando C#.
5. [Bibliotecas Cliente Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Bibliotecas cliente para várias linguagens de programação.
6. [Detectando Tentativas de Jailbreak](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Orientações específicas para detectar e prevenir tentativas de jailbreak.
7. [Melhores Práticas para Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Melhores práticas para implementar segurança de conteúdo de forma eficaz.

Para uma implementação mais detalhada, veja nosso [guia de implementação do Azure Content Safety](./azure-content-safety-implementation.md).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.