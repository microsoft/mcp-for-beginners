<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1b6c746d9e190deba4d8765267ffb94e",
  "translation_date": "2025-11-18T19:22:23+00:00",
  "source_file": "02-Security/azure-content-safety-implementation.md",
  "language_code": "pcm"
}
-->
# How to Use Azure Content Safety with MCP

To make MCP more secure against things like prompt injection, tool poisoning, and other AI wahala, e good to add Azure Content Safety.

## How to Join Azure Content Safety with MCP Server

To join Azure Content Safety with your MCP server, you go need put the content safety filter as middleware for your request processing pipeline:

1. Set up the filter when the server dey start
2. Check all the tool requests wey dey come in before you process dem
3. Check all the responses wey dey go out before you send dem give clients
4. Log and send alert if safety rules no dey follow
5. Add better error handling for when content safety check fail

This go help protect against:
- Prompt injection wahala
- Tool poisoning plans
- Data wey bad people wan carry go through bad inputs
- Creation of harmful content

## Best Ways to Use Azure Content Safety

1. **Custom Blocklists**: Make your own blocklists wey go focus on MCP injection patterns
2. **Severity Tuning**: Adjust how strict the rules go be based on wetin you dey do and how much risk you fit take
3. **Comprehensive Coverage**: Make sure you dey check all inputs and outputs for safety
4. **Performance Optimization**: Fit use caching to make repeated content safety checks faster
5. **Fallback Mechanisms**: Plan wetin go happen if content safety service no dey work
6. **User Feedback**: Tell users why their content no pass if safety block am
7. **Continuous Improvement**: Always update your blocklists and patterns as new threats dey show

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don translate wit AI translation service [Co-op Translator](https://github.com/Azure/co-op-translator). Even as we dey try make am accurate, abeg make you sabi say machine translation fit get mistake or no dey correct well. Di original dokyument for im native language na di main source wey you go trust. For important mata, na beta make you use professional human translation. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen from di use of dis translation.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->