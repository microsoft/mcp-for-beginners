<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5300fd1b5e84520d500b2a8f568a1d8",
  "translation_date": "2025-11-18T19:22:51+00:00",
  "source_file": "02-Security/azure-content-safety.md",
  "language_code": "pcm"
}
-->
# Advanced MCP Security wit Azure Content Safety

Azure Content Safety dey provide plenty strong tools wey fit help make di security of your MCP setup beta:

## Prompt Shields

Microsoft AI Prompt Shields dey give strong protection against direct and indirect prompt injection attacks through:

1. **Advanced Detection**: E dey use machine learning to sabi bad instructions wey dey inside content.
2. **Spotlighting**: E dey change input text so AI systems fit sabi di difference between correct instructions and outside inputs.
3. **Delimiters and Datamarking**: E dey mark di boundary between trusted and untrusted data.
4. **Content Safety Integration**: E dey work wit Azure AI Content Safety to catch jailbreak attempts and bad content.
5. **Continuous Updates**: Microsoft dey always update di protection system to fight new threats.

## How to Use Azure Content Safety wit MCP

Dis method dey provide protection wey get many layers:
- E dey scan inputs before e process dem
- E dey check outputs before e return dem
- E dey use blocklists for harmful patterns wey dem don sabi
- E dey use Azure content safety models wey dey always dey updated

## Azure Content Safety Resources

If you wan sabi more about how to use Azure Content Safety wit your MCP servers, check dis official resources:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Di official documentation for Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Learn how to stop prompt injection attacks.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Detailed API reference for how to use Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Quick guide for how to use am wit C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Client libraries for different programming languages.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Specific guide on how to catch and stop jailbreak attempts.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Best practices for how to use content safety well.

If you wan sabi more about di implementation, check our [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transleshion service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transleshion. Even as we dey try make am accurate, abeg make you sabi say machine transleshion fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go fit trust. For important informashon, e good make you use professional human transleshion. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transleshion.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->