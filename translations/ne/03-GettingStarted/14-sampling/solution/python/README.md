# यो नमूना चलाउँदै

तपाईलाई `uv` स्थापना गर्न सिफारिस गरिन्छ तर यो अनिवार्य छैन, [निर्देशनहरू](https://docs.astral.sh/uv/#highlights) हेर्नुहोस्

## -0- भर्चुअल वातावरण सिर्जना गर्नुहोस्

```bash
python -m venv venv
```

## -1- भर्चुअल वातावरण सक्रिय गर्नुहोस्

```bash
venv\Scripts\activate
```

## -2- निर्भरता स्थापना गर्नुहोस्

```bash
pip install "mcp[cli]" openai
```

## -3- नमूना चलाउनुहोस्


```bash
python client.py
```

तपाईले यस्तै आउटपुट देख्नुपर्छ:

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**अस्वीकृति**:
यो दस्तावेज कृत्रिम बुद्धिमत्ता अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) को प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताको प्रयास गर्छौं भने पनि, कृपया ध्यान दिनुहोस् कि स्वचालित अनुवादमा त्रुटि वा अशुद्धता हुनसक्छ। मूल दस्तावेज यसको स्वदेशी भाषामा आधिकारिक स्रोत मानिनु पर्दछ। महत्वपूर्ण जानकारीका लागि व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै गलतफहमी वा गलत व्याख्याको जिम्मेवारी हामी लिदैनौं।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->