<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5300fd1b5e84520d500b2a8f568a1d8",
  "translation_date": "2025-12-11T11:28:41+00:00",
  "source_file": "02-Security/azure-content-safety.md",
  "language_code": "ml"
}
-->
# Azure Content Safety ഉപയോഗിച്ച് ആധുനിക MCP സുരക്ഷ

നിങ്ങളുടെ MCP നടപ്പാക്കലുകളുടെ സുരക്ഷ മെച്ചപ്പെടുത്താൻ Azure Content Safety നിരവധി ശക്തമായ ഉപകരണങ്ങൾ നൽകുന്നു:

## പ്രോംപ്റ്റ് ഷീൽഡുകൾ

Microsoft-ന്റെ AI പ്രോംപ്റ്റ് ഷീൽഡുകൾ നേരിട്ടും പരോക്ഷമായും പ്രോംപ്റ്റ് ഇൻജക്ഷൻ ആക്രമണങ്ങളിൽ നിന്ന് ശക്തമായ സംരക്ഷണം നൽകുന്നു:

1. **ആധുനിക കണ്ടെത്തൽ**: ഉള്ളടക്കത്തിൽ ഉൾപ്പെടുത്തിയ ദുഷ്പ്രവർത്തന നിർദ്ദേശങ്ങൾ തിരിച്ചറിയാൻ മെഷീൻ ലേണിംഗ് ഉപയോഗിക്കുന്നു.
2. **സ്പോട്ട്ലൈറ്റിംഗ്**: സാധുവായ നിർദ്ദേശങ്ങളും ബാഹ്യ ഇൻപുട്ടുകളും തിരിച്ചറിയാൻ AI സിസ്റ്റങ്ങൾ സഹായിക്കുന്നതിന് ഇൻപുട്ട് ടെക്സ്റ്റ് മാറ്റുന്നു.
3. **ഡെലിമിറ്ററുകളും ഡാറ്റാമാർക്കിംഗും**: വിശ്വസനീയവും വിശ്വസനീയമല്ലാത്തതുമായ ഡാറ്റയുടെ അതിരുകൾ അടയാളപ്പെടുത്തുന്നു.
4. **Content Safety സംയോജനം**: ജെയിൽബ്രേക്ക് ശ്രമങ്ങളും ഹാനികരമായ ഉള്ളടക്കവും കണ്ടെത്താൻ Azure AI Content Safety-യുമായി പ്രവർത്തിക്കുന്നു.
5. **തുടർച്ചയായ അപ്‌ഡേറ്റുകൾ**: ഉയർന്ന ഭീഷണികളോട് പ്രതികരിച്ച് Microsoft സംരക്ഷണ സംവിധാനങ്ങൾ സ്ഥിരമായി അപ്‌ഡേറ്റ് ചെയ്യുന്നു.

## MCP-യുമായി Azure Content Safety നടപ്പാക്കൽ

ഈ സമീപനം ബഹുസ്ഥര സംരക്ഷണം നൽകുന്നു:
- പ്രോസസ്സ് ചെയ്യുന്നതിന് മുമ്പ് ഇൻപുട്ടുകൾ സ്കാൻ ചെയ്യൽ
- തിരിച്ചറിയുന്നതിന് മുമ്പ് ഔട്ട്പുട്ടുകൾ സാധൂകരിക്കൽ
- അറിയപ്പെട്ട ഹാനികരമായ മാതൃകകൾക്കായി ബ്ലോക്ക്ലിസ്റ്റുകൾ ഉപയോഗിക്കൽ
- Azure-യുടെ തുടർച്ചയായി അപ്‌ഡേറ്റ് ചെയ്യുന്ന content safety മോഡലുകൾ പ്രയോജനപ്പെടുത്തൽ

## Azure Content Safety വിഭവങ്ങൾ

നിങ്ങളുടെ MCP സെർവറുകളുമായി Azure Content Safety നടപ്പാക്കുന്നതിനെക്കുറിച്ച് കൂടുതൽ അറിയാൻ, ഈ ഔദ്യോഗിക വിഭവങ്ങൾ പരിശോധിക്കുക:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety-യുടെ ഔദ്യോഗിക ഡോക്യുമെന്റേഷൻ.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - പ്രോംപ്റ്റ് ഇൻജക്ഷൻ ആക്രമണങ്ങൾ തടയുന്നതെങ്ങനെ എന്നത് പഠിക്കുക.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety നടപ്പാക്കുന്നതിനുള്ള വിശദമായ API റഫറൻസ്.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# ഉപയോഗിച്ച് വേഗത്തിൽ നടപ്പാക്കാനുള്ള ഗൈഡ്.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - വിവിധ പ്രോഗ്രാമിംഗ് ഭാഷകൾക്കുള്ള ക്ലയന്റ് ലൈബ്രറികൾ.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - ജെയിൽബ്രേക്ക് ശ്രമങ്ങൾ കണ്ടെത്താനും തടയാനും പ്രത്യേക മാർഗ്ഗനിർദ്ദേശങ്ങൾ.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - content safety ഫലപ്രദമായി നടപ്പാക്കുന്നതിനുള്ള മികച്ച രീതികൾ.

കൂടുതൽ വിശദമായ നടപ്പാക്കലിനായി, ഞങ്ങളുടെ [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) കാണുക.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**അസൂയാ**:  
ഈ രേഖ AI വിവർത്തന സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് വിവർത്തനം ചെയ്തതാണ്. നാം കൃത്യതയ്ക്ക് ശ്രമിച്ചിട്ടുണ്ടെങ്കിലും, സ്വയം പ്രവർത്തിക്കുന്ന വിവർത്തനങ്ങളിൽ പിശകുകൾ അല്ലെങ്കിൽ തെറ്റുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. അതിന്റെ മാതൃഭാഷയിലുള്ള യഥാർത്ഥ രേഖയാണ് പ്രാമാണികമായ ഉറവിടം എന്ന് പരിഗണിക്കേണ്ടതാണ്. നിർണായകമായ വിവരങ്ങൾക്ക്, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം ശുപാർശ ചെയ്യപ്പെടുന്നു. ഈ വിവർത്തനം ഉപയോഗിക്കുന്നതിൽ നിന്നുണ്ടാകുന്ന ഏതെങ്കിലും തെറ്റിദ്ധാരണകൾക്കോ തെറ്റായ വ്യാഖ്യാനങ്ങൾക്കോ ഞങ്ങൾ ഉത്തരവാദികളല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->