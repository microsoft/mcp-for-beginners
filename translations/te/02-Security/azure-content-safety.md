<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "f5300fd1b5e84520d500b2a8f568a1d8",
  "translation_date": "2025-12-11T11:28:12+00:00",
  "source_file": "02-Security/azure-content-safety.md",
  "language_code": "te"
}
-->
# Azure Content Safetyతో అధునాతన MCP భద్రత

Azure Content Safety మీ MCP అమలులను మెరుగుపరచగల కొన్ని శక్తివంతమైన సాధనాలను అందిస్తుంది:

## ప్రాంప్ట్ షీల్డ్స్

Microsoft యొక్క AI ప్రాంప్ట్ షీల్డ్స్ ప్రత్యక్ష మరియు పరోక్ష ప్రాంప్ట్ ఇంజెక్షన్ దాడుల నుండి బలమైన రక్షణను అందిస్తాయి:

1. **అధునాతన గుర్తింపు**: కంటెంట్‌లో దుర్మార్గ సూచనలను గుర్తించడానికి మెషీన్ లెర్నింగ్ ఉపయోగిస్తుంది.
2. **స్పాట్‌లైటింగ్**: AI వ్యవస్థలు చెల్లుబాటు అయ్యే సూచనలు మరియు బాహ్య ఇన్‌పుట్‌లను వేరుచేసుకోవడానికి ఇన్‌పుట్ టెక్స్ట్‌ను మార్చుతుంది.
3. **డెలిమిటర్స్ మరియు డేటామార్కింగ్**: నమ్మకమైన మరియు నమ్మకంలేని డేటా మధ్య సరిహద్దులను గుర్తిస్తుంది.
4. **కంటెంట్ సేఫ్టీ ఇంటిగ్రేషన్**: జైల్బ్రేక్ ప్రయత్నాలు మరియు హానికరమైన కంటెంట్‌ను గుర్తించడానికి Azure AI Content Safetyతో కలిసి పనిచేస్తుంది.
5. **నిరంతర నవీకరణలు**: Microsoft కొత్త ముప్పులపై రక్షణ యంత్రాంగాలను తరచుగా నవీకరిస్తుంది.

## MCPతో Azure Content Safety అమలు

ఈ విధానం బహుళ-స్థాయి రక్షణను అందిస్తుంది:
- ప్రాసెసింగ్‌కు ముందు ఇన్‌పుట్‌లను స్కాన్ చేయడం
- తిరిగి ఇవ్వడానికి ముందు అవుట్‌పుట్‌లను ధృవీకరించడం
- తెలిసిన హానికర నమూనాల కోసం బ్లాక్‌లిస్ట్‌లను ఉపయోగించడం
- Azure యొక్క నిరంతర నవీకరించబడుతున్న కంటెంట్ సేఫ్టీ మోడల్స్‌ను వినియోగించడం

## Azure Content Safety వనరులు

మీ MCP సర్వర్లతో Azure Content Safetyని అమలు చేయడం గురించి మరింత తెలుసుకోవడానికి, ఈ అధికారిక వనరులను సంప్రదించండి:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safetyకి సంబంధించిన అధికారిక డాక్యుమెంటేషన్.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - ప్రాంప్ట్ ఇంజెక్షన్ దాడులను నివారించడానికి నేర్చుకోండి.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safetyని అమలు చేయడానికి వివరమైన API సూచిక.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# ఉపయోగించి త్వరిత అమలుకు గైడ్.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - వివిధ ప్రోగ్రామింగ్ భాషల కోసం క్లయింట్ లైబ్రరీలు.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - జైల్బ్రేక్ ప్రయత్నాలను గుర్తించడం మరియు నివారించడానికి ప్రత్యేక మార్గదర్శకాలు.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - కంటెంట్ సేఫ్టీని సమర్థవంతంగా అమలు చేయడానికి ఉత్తమ పద్ధతులు.

మరింత లోతైన అమలుకు, మా [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md)ని చూడండి.

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్పష్టత**:  
ఈ పత్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నించినప్పటికీ, ఆటోమేటెడ్ అనువాదాల్లో పొరపాట్లు లేదా తప్పిదాలు ఉండవచ్చు. మూల పత్రం దాని స్వదేశీ భాషలో అధికారిక మూలంగా పరిగణించాలి. ముఖ్యమైన సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదం సిఫార్సు చేయబడుతుంది. ఈ అనువాదం వాడకంలో ఏర్పడిన ఏవైనా అపార్థాలు లేదా తప్పుదారితీసే అర్థాలు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->