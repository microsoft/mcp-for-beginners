# ಈ ಮಾದರಿಯನ್ನು 실행 ಮಾಡುವುದು

ನೀವು `uv` ಅನ್ನು ಸ್ಥಾಪಿಸಲು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ ಆದರೆ ಇದು ಕಡ್ಡಾಯವಲ್ಲ, [ಸೂಚನೆಗಳು](https://docs.astral.sh/uv/#highlights) ನೋಡಿ

## -0- ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ರಚಿಸಿ

```bash
python -m venv venv
```

## -1- ವರ್ಚುವಲ್ ಪರಿಸರವನ್ನು ಸಕ್ರಿಯಗೊಳಿಸಿ

```bash
venv\Scripts\activate
```

## -2- ಅವಲಂಬನೆಗಳನ್ನು ಸ್ಥಾಪಿಸಿ

```bash
pip install "mcp[cli]" openai
```

## -3- ಮಾದರಿಯನ್ನು 실행 ಮಾಡಿ


```bash
python client.py
```

ನೀವು ಹೀಗೆಯಿರುವ ಔಟ್‌ಪುಟ್ ಅನ್ನು ನೋಡುವಿರಿ:

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ವಿಮರ್ಶೆ**:
ಈ ದಾಖಲೆವನ್ನು AI ಅನುವಾದ ಸೇವೆ [Co-op Translator](https://github.com/Azure/co-op-translator) ಉಪಯೋಗಿಸಿ ಕನ್ನಡಕ್ಕೆ ಅನುವದಿಸಲಾಗಿದೆ. ನಾವು ಸರಿಯಾದ ಅನುವಾದಕ್ಕಾಗಿ ಪ್ರಯತ್ನಿಸಲಿದ್ದಾರೆಂದೂ, ಸಹಜವಾಗಿ ಸ್ವಯಂಚಾಲಿತ ಅನುವಾದಗಳಲ್ಲಿ ದೋಷಗಳು ಅಥವಾ ತಪ್ಪುಗಳಿರಬಹುದು ಎಂಬುದನ್ನು ಗಮನದಲ್ಲಿಡಿ. ಮೂಲ ಭಾಷೆಯಲ್ಲಿರುವ ಮೂಲ ದಾಖಲೆಯನ್ನು ಅಧಿಕೃತ ಸ್ರೋತರಾಗಿ ಪರಿಗಣಿಸಬೇಕು. ಪ್ರಮುಖ ಮಾಹಿತಿಗಾಗಿ ವೃತ್ತಿಪರ ಮಾನವ ಅನುವಾದವನ್ನು ಶಿಫಾರಸು ಮಾಡಲಾಗಿದೆ. ಈ ಅನುವಾದದ ಬಳಕೆಯಿಂದ ಸಂಭವಿಸುವ ಯಾವುದೇ ತಪ್ಪು ಅರ್ಥಮಾಡಿಕೊಳ್ಳಿಕೆಗೆ ಅಥವಾ ಅಸ್ಪಷ್ಟತೆಗಳಿಗೆ ನಾವು ಹೊಣೆಗಾರರಾಗಿರುವುದಿಲ್ಲ.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->