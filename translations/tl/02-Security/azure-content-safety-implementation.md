# Pagpapatupad ng Azure Content Safety sa MCP

Upang palakasin ang seguridad ng MCP laban sa prompt injection, tool poisoning, at iba pang mga partikular na kahinaan ng AI, lubos na inirerekomenda ang pagsasama ng Azure Content Safety.

## Pagsasama sa MCP Server

Para isama ang Azure Content Safety sa iyong MCP server, idagdag ang content safety filter bilang middleware sa iyong request processing pipeline:

1. I-initialize ang filter sa pagsisimula ng server  
2. Suriin ang lahat ng papasok na tool requests bago iproseso  
3. Tingnan ang lahat ng papalabas na tugon bago ito ibalik sa mga kliyente  
4. Mag-log at mag-alerto sa mga paglabag sa kaligtasan  
5. Magpatupad ng angkop na error handling para sa mga nabigong content safety checks  

Nagbibigay ito ng matibay na depensa laban sa:  
- Mga pag-atake ng prompt injection  
- Mga pagtatangkang tool poisoning  
- Pagkuha ng data sa pamamagitan ng malisyosong inputs  
- Paglikha ng mapanganib na nilalaman  

## Mga Pinakamahusay na Gawain para sa Pagsasama ng Azure Content Safety

1. **Custom Blocklists**: Gumawa ng mga custom blocklists na partikular para sa mga pattern ng MCP injection  
2. **Severity Tuning**: I-adjust ang severity thresholds batay sa iyong partikular na gamit at antas ng panganib  
3. **Comprehensive Coverage**: Ipatupad ang content safety checks sa lahat ng inputs at outputs  
4. **Performance Optimization**: Isaalang-alang ang paggamit ng caching para sa mga paulit-ulit na content safety checks  
5. **Fallback Mechanisms**: Magtakda ng malinaw na fallback behaviors kapag hindi available ang content safety services  
6. **User Feedback**: Magbigay ng malinaw na feedback sa mga user kapag na-block ang nilalaman dahil sa mga isyu sa kaligtasan  
7. **Continuous Improvement**: Regular na i-update ang mga blocklists at pattern batay sa mga bagong banta

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.