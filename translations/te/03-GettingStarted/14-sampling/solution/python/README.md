# ఈ నమూనాను నడుపుతున్నది

మీకు `uv` ని ఇన్‌స్టాల్ చేయాలని సిఫార్సు చేయబడింది, కానీ ఇది తప్పనిసరి కాదు, చూడండి [సూచనలు](https://docs.astral.sh/uv/#highlights)

## -0- ఒక వర్చువల్ ఇన్విరాన్‌మెంట్ సృష్టించండి

```bash
python -m venv venv
```

## -1- వర్చువల్ ఇన్విరాన్‌మెంట్‌ను యాక్టివేట్ చేయండి

```bash
venv\Scripts\activate
```

## -2- డిపెండెన్సీలను ఇన్‌స్టాల్ చేయండి

```bash
pip install "mcp[cli]" openai
```

## -3- నమూనాను నడపండి


```bash
python client.py
```

మీకు ఇంతలాగే ఉత్పత్తి కనిపించాలి:

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**సూచన**:  
ఈ దస్త్రాన్ని AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము శుద్ధతకు గణనీయంగా ప్రయత్నిస్తాం కాని, ఆటోమేటెడ్ అనువాదాలలో తప్పులు లేదా అసత్యతలు ఉండగలవని దయచేసి గమనించండి. స్థానిక భాషలో ఉన్న అసలు దస్త్రాన్ని అధికారిక మూలం గా పరిగణించాలి. కీలక సమాచారానికి, ప్రొఫెషనల్ మానవ అనువాదాన్ని సూచిస్తాము. ఈ అనువాదం ఉపయోగంతో కలిగే ఏవైనా అపార్థాలు లేదా తప్పు అర్థం చేసుకోబడిన పరిస్థితులకి మేము బాధ్యులు కాదు.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->