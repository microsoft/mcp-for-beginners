# Azure Content Safety மூலம் மேம்பட்ட MCP பாதுகாப்பு

Azure Content Safety உங்கள் MCP செயல்பாடுகளின் பாதுகாப்பை மேம்படுத்த பல சக்திவாய்ந்த கருவிகளை வழங்குகிறது:

## Prompt Shields

Microsoft AI Prompt Shields நேரடி மற்றும் மறைமுக prompt injection தாக்குதல்களுக்கு எதிராக வலுவான பாதுகாப்பை வழங்குகிறது:

1. **மேம்பட்ட கண்டறிதல்**: உள்ளடக்கத்தில் உள்ள தீங்கிழைக்கும் வழிமுறைகளை கண்டறிய இயந்திர கற்றல் பயன்படுத்துகிறது.
2. **Spotlighting**: AI அமைப்புகள் சரியான வழிமுறைகள் மற்றும் வெளிப்புற உள்ளீடுகளை வேறுபடுத்த உதவுவதற்காக உள்ளீடு உரையை மாற்றுகிறது.
3. **Delimiters மற்றும் Datamarking**: நம்பகமான மற்றும் நம்பகமற்ற தரவுகளுக்கு இடையிலான எல்லைகளை குறிக்கிறது.
4. **Content Safety ஒருங்கிணைப்பு**: Jailbreak முயற்சிகள் மற்றும் தீங்கு விளைவிக்கும் உள்ளடக்கத்தை கண்டறிய Azure AI Content Safety உடன் வேலை செய்கிறது.
5. **தொடர்ச்சியான மேம்பாடுகள்**: Microsoft புதிய அச்சுறுத்தல்களுக்கு எதிராக பாதுகாப்பு முறைகளை தொடர்ந்து மேம்படுத்துகிறது.

## MCP உடன் Azure Content Safety செயல்படுத்துதல்

இந்த அணுகுமுறை பல அடுக்குகளைக் கொண்ட பாதுகாப்பை வழங்குகிறது:
- செயலாக்கத்திற்கு முன் உள்ளீடுகளை ஸ்கேன் செய்கிறது
- திருப்பி அனுப்புவதற்கு முன் வெளியீடுகளை சரிபார்க்கிறது
- தீங்கு விளைவிக்கும் முறைமைகள் பற்றிய தகவல்களுக்கான blocklists பயன்படுத்துகிறது
- Azure இன் தொடர்ந்து மேம்படுத்தப்படும் content safety மாதிரிகளை பயன்படுத்துகிறது

## Azure Content Safety வளங்கள்

உங்கள் MCP சர்வர்களுடன் Azure Content Safety செயல்படுத்துவது குறித்து மேலும் அறிய, இந்த அதிகாரப்பூர்வ வளங்களை அணுகவும்:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Azure Content Safety பற்றிய அதிகாரப்பூர்வ ஆவணங்கள்.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Prompt injection தாக்குதல்களைத் தடுக்க எப்படி என்பதை அறிக.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Content Safety செயல்படுத்துவதற்கான விரிவான API குறிப்புகள்.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - C# பயன்படுத்தி விரைவான செயல்படுத்தல் வழிகாட்டி.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - பல நிரலாக்க மொழிகளுக்கான client libraries.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Jailbreak முயற்சிகளை கண்டறிந்து தடுக்க குறிப்பிட்ட வழிகாட்டுதல்.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Content Safety ஐ திறமையாக செயல்படுத்த சிறந்த நடைமுறைகள்.

மேலும் விரிவான செயல்படுத்தலுக்காக, எங்கள் [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md) ஐ பார்க்கவும்.

---

**குறிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற AI மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிபெயர்க்கப்பட்டுள்ளது. எங்கள் நோக்கம் துல்லியமாக இருக்க வேண்டும் என்பதுதான், ஆனால் தானியங்கி மொழிபெயர்ப்புகளில் பிழைகள் அல்லது துல்லியமின்மைகள் இருக்கக்கூடும் என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். அதன் தாய்மொழியில் உள்ள மூல ஆவணம் அதிகாரப்பூர்வ ஆதாரமாக கருதப்பட வேண்டும். முக்கியமான தகவல்களுக்கு, தொழில்முறை மனித மொழிபெயர்ப்பு பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பைப் பயன்படுத்துவதால் ஏற்படும் எந்த தவறான புரிதல்கள் அல்லது தவறான விளக்கங்களுக்கு நாங்கள் பொறுப்பல்ல.