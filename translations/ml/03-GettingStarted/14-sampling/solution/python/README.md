# ഈ സാംപിൾ ഓടിക്കുന്നത്

നിങ്ങൾക്ക് `uv` ഇൻസ്റ്റാൾ ചെയ്യണമെന്ന് ശിപാർശ ചെയ്യപ്പെടുന്നു, പക്ഷേ അതൊരു നിർബന്ധം അല്ല, കാണുക [instructions](https://docs.astral.sh/uv/#highlights)

## -0- ഒരു വെർച്ച്വൽ എൻവൈറൺമെന്റ് സൃഷ്ടിക്കുക

```bash
python -m venv venv
```

## -1- വെർച്ച്വൽ എൻവൈറൺമെന്റ് സജീവമാക്കുക

```bash
venv\Scripts\activate
```

## -2- ആശ്രിതത്വങ്ങൾ ഇൻസ്റ്റാൾ ചെയ്യുക

```bash
pip install "mcp[cli]" openai
```

## -3- സാംപിൾ പ്രവർത്തിപ്പിക്കുക


```bash
python client.py
```

താഴെ കാണുന്നതുപോലുള്ള ഔട്ട്പുട്ട് നിങ്ങൾക്ക് കാണാവുന്നതാണ്:

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**തള്ളിപ്പ്**:  
ഈ ഡോസ്യुमെന്റ് AI ഭാഷാന്തര സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ചു വിവർത്തനം ചെയ്തതാണ്. നമുക്ക് ശരിയായ പരിഭാഷ നൽകാൻ പ്രയത്‌നിച്ചിട്ടുണ്ടെങ്കിലും, യന്ത്ര വിവർത്തനത്തിൽ പിഴവുകൾ അല്ലെങ്കിൽ അമ്പരപ്പുകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. പ്രാഥമിക ഭാഷയിലെ യഥാർത്ഥ ഡോക്യുമെന്റ് അധികാരമുള്ള സ്രോതസ്സായി കണക്കാക്കണം. നിർണ്ണായക വിവരങ്ങൾക്കായി, പ്രൊഫഷണൽ മനുഷ്യ വിവർത്തനം അഭ്യർത്ഥിക്കുന്നു. ഈ വിവർത്തനത്തിന്റെ ഉപയോഗത്തിൽ ഉണ്ടാകുന്ന തെറ്റായ ധാരണകൾക്കും വ്യാഖ്യാനക്കുകള്ക്കും ഞങ്ങൾ ബാധ്യസ്ഥരല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->