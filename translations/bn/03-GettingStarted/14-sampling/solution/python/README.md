# এই নমুনাটি চালানো

আপনাকে `uv` ইনস্টল করার পরামর্শ দেওয়া হয় তবে এটি আবশ্যক নয়, দেখুন [নির্দেশাবলী](https://docs.astral.sh/uv/#highlights)

## -0- একটি ভার্চুয়াল পরিবেশ তৈরি করুন

```bash
python -m venv venv
```

## -1- ভার্চুয়াল পরিবেশ সক্রিয় করুন

```bash
venv\Scripts\activate
```

## -2- নির্ভরশীলতাগুলি ইনস্টল করুন

```bash
pip install "mcp[cli]" openai
```

## -3- নমুনাটি চালান


```bash
python client.py
```

আপনি নিম্নলিখিত ধরণের আউটপুট দেখতে পাবেন:

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**অস্বীকৃতি**:  
এই ডকুমেন্টটি AI অনুবাদ সেবা [Co-op Translator](https://github.com/Azure/co-op-translator) ব্যবহার করে অনূদিত হয়েছে। আমরা যথাযথতার চেষ্টা করি, তবে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসঙ্গতি থাকতে পারে। মূল ডকুমেন্টটি তার নিজ নিজ ভাষায় প্রামাণিক উৎস হিসাবে বিবেচনা করা উচিত। গুরুতর তথ্যের জন্য পেশাদার মানব অনুবাদ সুপারিশ করা হয়। এই অনুবাদের ব্যবহারে উদ্ভূত কোনও বিভ্রান্তি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী নই।
<!-- CO-OP TRANSLATOR DISCLAIMER END -->