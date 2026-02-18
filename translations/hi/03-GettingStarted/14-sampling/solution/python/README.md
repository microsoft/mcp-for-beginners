# इस नमूने को चलाना

आपको `uv` स्थापित करने की सलाह दी जाती है लेकिन यह अनिवार्य नहीं है, देखें [निर्देश](https://docs.astral.sh/uv/#highlights)

## -0- एक वर्चुअल वातावरण बनाएं

```bash
python -m venv venv
```

## -1- वर्चुअल वातावरण को सक्रिय करें

```bash
venv\Scripts\activate
```

## -2- निर्भरताएँ स्थापित करें

```bash
pip install "mcp[cli]" openai
```

## -3- नमूना चलाएं


```bash
python client.py
```

आपको इस जैसा आउटपुट दिखना चाहिए:

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकरण**:  
यह दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) का उपयोग करके अनूदित किया गया है। हालांकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या असंगतियाँ हो सकती हैं। मूल भाषा में मौलिक दस्तावेज़ को ही प्रामाणिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए पेशेवर मानव अनुवाद की सलाह दी जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम जिम्मेदार नहीं हैं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->