# Segurança Avançada MCP com Azure Content Safety

O Azure Content Safety oferece várias ferramentas poderosas que podem melhorar a segurança das suas implementações MCP:

## Prompt Shields

Os AI Prompt Shields da Microsoft fornecem uma proteção robusta contra ataques de injeção de prompt, tanto diretos como indiretos, através de:

1. **Deteção Avançada**: Utiliza machine learning para identificar instruções maliciosas incorporadas no conteúdo.
2. **Destaque**: Transforma o texto de entrada para ajudar os sistemas de IA a distinguir entre instruções válidas e entradas externas.
3. **Delimitadores e Marcação de Dados**: Marca os limites entre dados confiáveis e não confiáveis.
4. **Integração com Content Safety**: Funciona com o Azure AI Content Safety para detetar tentativas de jailbreak e conteúdos prejudiciais.
5. **Atualizações Contínuas**: A Microsoft atualiza regularmente os mecanismos de proteção contra ameaças emergentes.

## Implementação do Azure Content Safety com MCP

Esta abordagem oferece proteção em múltiplas camadas:
- Análise das entradas antes do processamento
- Validação das saídas antes de serem devolvidas
- Utilização de listas de bloqueio para padrões conhecidos como prejudiciais
- Aproveitamento dos modelos de content safety do Azure, continuamente atualizados

## Recursos do Azure Content Safety

Para saber mais sobre como implementar o Azure Content Safety nos seus servidores MCP, consulte estes recursos oficiais:

1. [Documentação do Azure AI Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/) - Documentação oficial do Azure Content Safety.
2. [Documentação do Prompt Shield](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Saiba como prevenir ataques de injeção de prompt.
3. [Referência da API Content Safety](https://learn.microsoft.com/rest/api/contentsafety/) - Referência detalhada da API para implementar Content Safety.
4. [Início Rápido: Azure Content Safety com C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Guia rápido de implementação usando C#.
5. [Bibliotecas Cliente Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Bibliotecas cliente para várias linguagens de programação.
6. [Detetar Tentativas de Jailbreak](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Orientações específicas para detetar e prevenir tentativas de jailbreak.
7. [Melhores Práticas para Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Melhores práticas para implementar content safety de forma eficaz.

Para uma implementação mais detalhada, consulte o nosso [guia de implementação do Azure Content Safety](./azure-content-safety-implementation.md).

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.