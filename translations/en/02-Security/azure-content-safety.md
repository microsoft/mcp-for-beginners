# Advanced MCP Security with Azure Content Safety

Azure Content Safety offers several powerful tools to enhance the security of your MCP implementations:

## Prompt Shields

Microsoft's AI Prompt Shields provide strong protection against both direct and indirect prompt injection attacks by:

1. **Advanced Detection**: Utilizing machine learning to spot malicious instructions hidden within content.
2. **Spotlighting**: Modifying input text to help AI systems differentiate between valid commands and external inputs.
3. **Delimiters and Datamarking**: Defining clear boundaries between trusted and untrusted data.
4. **Content Safety Integration**: Collaborating with Azure AI Content Safety to identify jailbreak attempts and harmful content.
5. **Continuous Updates**: Microsoft regularly updates protection methods to counter new threats.

## Implementing Azure Content Safety with MCP

This method offers multi-layered protection by:
- Scanning inputs before processing
- Validating outputs before returning them
- Using blocklists for known harmful patterns
- Leveraging Azure’s continuously updated content safety models

## Azure Content Safety Resources

To learn more about integrating Azure Content Safety with your MCP servers, check out these official resources:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Official documentation for Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - How to prevent prompt injection attacks.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Detailed API reference for implementing Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Quickstart guide using C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Client libraries for various programming languages.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Guidance on detecting and preventing jailbreak attempts.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Recommended practices for effective content safety implementation.

For a more detailed implementation, see our [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Disclaimer**:  
This document has been translated using the AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.