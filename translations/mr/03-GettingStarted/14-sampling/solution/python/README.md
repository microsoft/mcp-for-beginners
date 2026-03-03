# हा नमुना चालविणे

तुम्हाला `uv` इन्स्टॉल करण्याचा सल्ला दिला जातो, पण ते आवश्यक नाही, पाहा [सूचना](https://docs.astral.sh/uv/#highlights)

## -0- व्हर्च्युअल एन्व्हायर्नमेंट तयार करा

```bash
python -m venv venv
```

## -1- व्हर्च्युअल एन्व्हायर्नमेंट सक्रिय करा

```bash
venv\Scripts\activate
```

## -2- अवलंबित्वे इन्स्टॉल करा

```bash
pip install "mcp[cli]" openai
```

## -3- नमुना चालवा


```bash
python client.py
```

तुम्हाला आउटपुट हे प्रमाणे दिसेल:

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**सोडकर उल्लेख**:
हा दस्तऐवज AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) वापरून अनुवादित केला आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अपूर्णता असू शकतात. मूळ भाषेतील दस्तऐवज अधिकृत स्रोत मानावा. महत्त्वाच्या माहितीसाठी व्यावसायिक मानव अनुवाद शिफारस केला जातो. या अनुवादाच्या वापरामुळे उद्भवलेल्या कोणत्याही गैरसमजुतीसाठी किंवा चुकीच्या अर्थ लावण्यासाठी आम्ही जबाबदार नाही.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->