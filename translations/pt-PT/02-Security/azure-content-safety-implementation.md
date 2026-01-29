# Implementação do Azure Content Safety com MCP

Para reforçar a segurança do MCP contra injeção de prompts, envenenamento de ferramentas e outras vulnerabilidades específicas de IA, é altamente recomendada a integração do Azure Content Safety.

## Integração com o Servidor MCP

Para integrar o Azure Content Safety com o seu servidor MCP, adicione o filtro de segurança de conteúdo como middleware na sua pipeline de processamento de pedidos:

1. Inicialize o filtro durante a inicialização do servidor  
2. Valide todos os pedidos de ferramentas recebidos antes de os processar  
3. Verifique todas as respostas enviadas antes de as devolver aos clientes  
4. Registe e alerte sobre violações de segurança  
5. Implemente um tratamento de erros adequado para falhas nas verificações de segurança de conteúdo  

Isto proporciona uma defesa robusta contra:  
- Ataques de injeção de prompts  
- Tentativas de envenenamento de ferramentas  
- Exfiltração de dados através de inputs maliciosos  
- Geração de conteúdo prejudicial  

## Boas Práticas para a Integração do Azure Content Safety

1. **Listas de bloqueio personalizadas**: Crie listas de bloqueio específicas para padrões de injeção MCP  
2. **Ajuste de severidade**: Ajuste os limiares de severidade com base no seu caso de uso e tolerância ao risco  
3. **Cobertura abrangente**: Aplique verificações de segurança de conteúdo a todos os inputs e outputs  
4. **Otimização de desempenho**: Considere implementar caching para verificações repetidas de segurança de conteúdo  
5. **Mecanismos de fallback**: Defina comportamentos claros de fallback quando os serviços de segurança de conteúdo não estiverem disponíveis  
6. **Feedback ao utilizador**: Forneça feedback claro aos utilizadores quando o conteúdo for bloqueado por motivos de segurança  
7. **Melhoria contínua**: Atualize regularmente as listas de bloqueio e padrões com base em ameaças emergentes

**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor tenha em conta que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.