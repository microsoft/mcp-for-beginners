# இந்த மாதிரியை இயக்குதல்

நீங்கள் `uv` ஐ நிறுவ பரிந்துரைக்கப்படுகிறது ஆனால் அது அவசியம் அல்ல, [வழிமுறைகள்](https://docs.astral.sh/uv/#highlights) பார்க்கவும்

## -0- ஒரு மெய்நிகர் சூழலை உருவாக்குக

```bash
python -m venv venv
```

## -1- மெய்நிகர் சூழலை செயல்படுத்துக

```bash
venv\Scripts\activate
```

## -2- சார்புகளை நிறுவுக

```bash
pip install "mcp[cli]" openai
```

## -3- மாதிரியை இயக்குக


```bash
python client.py
```

நீங்கள் அதே மாதிரி வெளியீட்டை காண வேண்டும்:

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**விதிமுறை அறிவிப்பு**:  
இந்த ஆவணம் [Co-op Translator](https://github.com/Azure/co-op-translator) என்ற செயற்கை நுண்ணறிவு மொழிபெயர்ப்பு சேவையை பயன்படுத்தி மொழிமாற்றம் செய்யப்பட்டுள்ளது. துல்லியத்துக்கு நாம் முயற்சி செய்தாலும், தானாக செய்யப்படும் மொழிபெயர்ப்புகளில் பிழைகள் அல்லது தவறுகள் இருக்க வாய்ப்பு உள்ளது என்பதை தயவுசெய்து கவனத்தில் கொள்ளவும். நாட்டுத் தனது மொழியில் உள்ள அசல் ஆவணம் அதிகாரப்பூர்வமான மூலமாக கருதப்பட வேண்டும். முக்கியமான தகவலுக்காக, தொழில்முறை மனித மொழிபெயர்ப்பை பரிந்துரைக்கப்படுகிறது. இந்த மொழிபெயர்ப்பின் பயன்பாட்டால் ஏற்படும் எந்த தவறுபாடுகளுக்கும் அல்லது தவறான புரிதல்களுக்கு நாம் பொறுப்பேற்கோம் என்று இல்லை.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->