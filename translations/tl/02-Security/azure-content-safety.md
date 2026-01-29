# Advanced MCP Security with Azure Content Safety

Nagbibigay ang Azure Content Safety ng ilang makapangyarihang kasangkapan na maaaring magpahusay sa seguridad ng iyong mga implementasyon ng MCP:

## Prompt Shields

Nagbibigay ang AI Prompt Shields ng Microsoft ng matibay na proteksyon laban sa direktang at di-direktang prompt injection attacks sa pamamagitan ng:

1. **Advanced Detection**: Gumagamit ng machine learning para matukoy ang mga malisyosong utos na nakapaloob sa nilalaman.
2. **Spotlighting**: Binabago ang input na teksto upang matulungan ang mga AI system na makilala ang mga wastong utos mula sa mga panlabas na input.
3. **Delimiters and Datamarking**: Nagtatakda ng mga hangganan sa pagitan ng pinagkakatiwalaang data at hindi pinagkakatiwalaang data.
4. **Content Safety Integration**: Nakikipagtulungan sa Azure AI Content Safety para matukoy ang mga pagtatangkang jailbreak at mapanganib na nilalaman.
5. **Continuous Updates**: Regular na ina-update ng Microsoft ang mga mekanismo ng proteksyon laban sa mga bagong banta.

## Implementing Azure Content Safety with MCP

Nagbibigay ang pamamaraang ito ng maraming patong ng proteksyon:
- Sinusuri ang mga input bago iproseso
- Pinapatunayan ang mga output bago ibalik
- Gumagamit ng blocklists para sa mga kilalang mapanganib na pattern
- Pinapakinabangan ang patuloy na ina-update na mga modelo ng content safety ng Azure

## Azure Content Safety Resources

Para matuto pa tungkol sa pag-implementa ng Azure Content Safety sa iyong mga MCP server, tingnan ang mga opisyal na sanggunian na ito:

1. [Azure AI Content Safety Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/) - Opisyal na dokumentasyon para sa Azure Content Safety.
2. [Prompt Shield Documentation](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/prompt-shield) - Alamin kung paano pigilan ang prompt injection attacks.
3. [Content Safety API Reference](https://learn.microsoft.com/rest/api/contentsafety/) - Detalyadong API reference para sa pag-implementa ng Content Safety.
4. [Quickstart: Azure Content Safety with C#](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-csharp) - Mabilisang gabay sa implementasyon gamit ang C#.
5. [Content Safety Client Libraries](https://learn.microsoft.com/azure/ai-services/content-safety/quickstart-client-libraries-rest-api) - Mga client library para sa iba't ibang programming language.
6. [Detecting Jailbreak Attempts](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/jailbreak-detection) - Tiyak na gabay sa pagtukoy at pagpigil sa mga pagtatangkang jailbreak.
7. [Best Practices for Content Safety](https://learn.microsoft.com/azure/ai-services/content-safety/concepts/best-practices) - Mga pinakamahusay na kasanayan para sa epektibong pag-implementa ng content safety.

Para sa mas malalim na implementasyon, tingnan ang aming [Azure Content Safety Implementation guide](./azure-content-safety-implementation.md).

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.