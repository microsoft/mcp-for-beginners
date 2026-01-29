# Implementando Azure Content Safety com MCP

Para fortalecer a segurança do MCP contra injeção de prompt, envenenamento de ferramentas e outras vulnerabilidades específicas de IA, é altamente recomendada a integração do Azure Content Safety.

## Integração com o Servidor MCP

Para integrar o Azure Content Safety ao seu servidor MCP, adicione o filtro de segurança de conteúdo como middleware no pipeline de processamento de requisições:

1. Inicialize o filtro durante a inicialização do servidor  
2. Valide todas as requisições de ferramentas recebidas antes do processamento  
3. Verifique todas as respostas enviadas antes de retorná-las aos clientes  
4. Registre e alerte sobre violações de segurança  
5. Implemente tratamento de erros adequado para falhas nas verificações de segurança de conteúdo  

Isso oferece uma defesa robusta contra:  
- Ataques de injeção de prompt  
- Tentativas de envenenamento de ferramentas  
- Exfiltração de dados por meio de entradas maliciosas  
- Geração de conteúdo prejudicial  

## Melhores Práticas para Integração do Azure Content Safety

1. **Listas de bloqueio personalizadas**: Crie listas de bloqueio específicas para padrões de injeção no MCP  
2. **Ajuste de severidade**: Ajuste os limiares de severidade conforme seu caso de uso e tolerância a riscos  
3. **Cobertura abrangente**: Aplique verificações de segurança de conteúdo em todas as entradas e saídas  
4. **Otimização de desempenho**: Considere implementar cache para verificações repetidas de segurança de conteúdo  
5. **Mecanismos de fallback**: Defina comportamentos claros de fallback quando os serviços de segurança de conteúdo estiverem indisponíveis  
6. **Feedback ao usuário**: Forneça feedback claro aos usuários quando o conteúdo for bloqueado por questões de segurança  
7. **Melhoria contínua**: Atualize regularmente as listas de bloqueio e padrões com base em ameaças emergentes

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.