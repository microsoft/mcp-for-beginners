# ដំណើរការឧទាហរណ៍នេះ

អ្នកត្រូវបានផ្តល់អនុសាសន៍ឱ្យដំឡើង `uv` ប៉ុន្តែមិនចាំបាច់ទេ សូមមើល [ការណែនាំ](https://docs.astral.sh/uv/#highlights)

## -0- បង្កើតបរិយាកាស virtual

```bash
python -m venv venv
```

## -1- បើកបរិយាកាស virtual

```bash
venv\Scripts\activate
```

## -2- ដំឡើងការពឹងផ្អែក

```bash
pip install "mcp[cli]" openai
```

## -3- អនុវត្តឧទាហរណ៍


```bash
python client.py
```

អ្នកគួរតែឃើញលទ្ធផលដូចខាងក្រោម៖

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**ការបដិសេធ**៖  
ឯកសារនេះត្រូវបានបម្រុងបំលែងជាភាសាដោយប្រើសេវាកម្មបម្រើការបកប្រែ AI [Co-op Translator](https://github.com/Azure/co-op-translator)។ នៅពេលដែលយើងខិតខំប្រឹងប្រែងសម្រាប់ភាពត្រឹមត្រូវ សូមយកចិត្តទុកដាក់ថាការបកប្រែដោយស្វ័យប្រវត្តិអាចមានកំហុស ឬភាពមិនត្រូវ។ ឯកសារដើមក្នុងភាសាមូលដ្ឋានគួរត្រូវបានគេគិតថាជា ការយោងដ៏ពិតប្រាកដ។ សម្រាប់ព័ត៌មានសំខាន់ៗ ការបកប្រែដោយមនុស្សអ្នកជំនាញត្រូវបានផ្តល់អនុសាសន៍។ យើងមិនទទួលខុសត្រូវចំពោះការយល់ច្រឡំ ឬការបកប្រែខុស ដែលកើតឡើងពីការប្រើប្រាស់ការបកប្រែនេះឡើយ។
<!-- CO-OP TRANSLATOR DISCLAIMER END -->