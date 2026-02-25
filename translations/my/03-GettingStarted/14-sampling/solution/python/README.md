# ဤနမူနာကို 실행ခြင်း

`uv` ကို 설치ရန်အကြံပြုသော်လည်း မဖြစ်မနေလိုအပ်သည်မှ မဟုတ်ပါ၊ [အညွှန်းများ](https://docs.astral.sh/uv/#highlights) ကိုကြည့်ပါ

## -0- 가상 환경 생성하기

```bash
python -m venv venv
```

## -1- 가상 환경 활성화하기

```bash
venv\Scripts\activate
```

## -2- 의존성 설치하기

```bash
pip install "mcp[cli]" openai
```

## -3- 샘플 실행하기


```bash
python client.py
```

အောက်ပါအတိုင်း ရလဒ်ကို တွေ့ရမည်-

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**စာချုပ်ချက်ချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်မှုဝန်ဆောင်မှုဖြစ်သည့် [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျနော်တို့သည် တိကျမှုအပေါ် သတိထားပါက ယဉ်ကျေးဘဲဖြစ်သော်လည်း အလိုအလျောက် ဘာသာပြန်မှုတွင် အမှားများ သို့မဟုတ် မမှန်ကန်မှုများ ရှိနိုင်မှုရှိသည်ကို သတိပြုပါ။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ အတည်ပြုရသော အချက်အလက်အဖြစ် သတ်မှတ်ရပါမည်။ အရေးကြီးသော သတင်းအချက်အလက်များအတွက် လူကြီးမင်းသည် ပရော်ဖက်ရှင်နယ် လူ့ဘာသာပြန်သူ၏ ဘာသာပြန်ချက်ကို တိုက်တွန်းအပ်ပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုမှုကြောင့် ဖြစ်ပေါ်နိုင်သည့် ရိုင်းစိုင်းခြင်းများ သို့မဟုတ် အဓိပ္ပာယ်မှားခြင်းများအတွက် ကျနော်တို့မှာ တာဝန်မရှိပါ။
<!-- CO-OP TRANSLATOR DISCLAIMER END -->