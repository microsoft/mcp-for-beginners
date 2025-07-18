<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "c3f4ea5732d64bf965e8aa2907759709",
  "translation_date": "2025-07-17T13:48:05+00:00",
  "source_file": "02-Security/mcp-security-best-practices-2025.md",
  "language_code": "my"
}
-->
# MCP လုံခြုံရေးအကောင်းဆုံး လေ့လာမှုများ - ၂၀၂၅ ခုနှစ် ဇူလိုင်လ အပ်ဒိတ်

## MCP အကောင်အထည်ဖော်မှုများအတွက် လုံခြုံရေးအကောင်းဆုံး လေ့လာမှုများ

MCP ဆာဗာများနှင့်အလုပ်လုပ်ရာတွင် သင့်ဒေတာ၊ အဆောက်အအုံနှင့် အသုံးပြုသူများကို ကာကွယ်ရန် အောက်ပါ လုံခြုံရေးအကောင်းဆုံး လေ့လာမှုများကို လိုက်နာပါ။

1. **အချက်အလက် စစ်ဆေးခြင်း** - ထည့်သွင်းသော အချက်အလက်များကို အမြဲစစ်ဆေးပြီး သန့်ရှင်းစေရန်၊ injection အတုများနှင့် confused deputy ပြဿနာများကို ကာကွယ်ရန်။
   - ကိရိယာ parameter အားလုံးအတွက် တင်းကြပ်သော စစ်ဆေးမှုများကို အကောင်အထည်ဖော်ပါ
   - မျှော်မှန်းထားသော ပုံစံများနှင့် ကိုက်ညီမှုရှိရန် schema စစ်ဆေးမှုကို အသုံးပြုပါ
   - လုပ်ဆောင်မှုမပြုမီ အန္တရာယ်ရှိနိုင်သော အကြောင်းအရာများကို စစ်ထုတ်ပါ

2. **ဝင်ရောက်ခွင့် ထိန်းချုပ်မှု** - MCP ဆာဗာအတွက် သင့်တော်သော အတည်ပြုခြင်းနှင့် ခွင့်ပြုချက်များကို အသေးစိတ် ထိန်းချုပ်ပါ။
   - Microsoft Entra ID ကဲ့သို့ အတည်ပြုသူများနှင့် OAuth 2.0 ကို အသုံးပြုပါ
   - MCP ကိရိယာများအတွက် role-based access control (RBAC) ကို အကောင်အထည်ဖော်ပါ
   - ရှိပြီးသား ဖြေရှင်းချက်များရှိသော်လည်း ကိုယ်ပိုင် အတည်ပြုမှု မဖန်တီးပါနှင့်

3. **လုံခြုံသော ဆက်သွယ်မှု** - MCP ဆာဗာနှင့် ဆက်သွယ်ရာတွင် HTTPS/TLS ကို အသုံးပြု၍ အထူးသတိထားရမည့် ဒေတာများအတွက် ထပ်မံ စာလုံးကူးခြင်း ထည့်သွင်းစဉ်းစားပါ။
   - အလားအလာရှိသည့်နေရာများတွင် TLS 1.3 ကို ဖွင့်ပါ
   - အရေးကြီးသော ချိတ်ဆက်မှုများအတွက် certificate pinning ကို အကောင်အထည်ဖော်ပါ
   - လက်မှတ်များကို ပုံမှန် ပြောင်းလဲပြီး တရားဝင်မှုကို စစ်ဆေးပါ

4. **နှုန်းထား ကန့်သတ်ခြင်း** - မတရားအသုံးပြုမှု၊ DoS တိုက်ခိုက်မှုများကို ကာကွယ်ရန်နှင့် အရင်းအမြစ် စားသုံးမှုကို စီမံရန် နှုန်းထား ကန့်သတ်မှုကို အကောင်အထည်ဖော်ပါ။
   - မျှော်မှန်းထားသော အသုံးပြုမှု ပုံစံများအပေါ် မူတည်၍ တောင်းဆိုမှု ကန့်သတ်ချက်များ သတ်မှတ်ပါ
   - များပြားသော တောင်းဆိုမှုများအတွက် အဆင့်လိုက် တုံ့ပြန်မှုများကို အကောင်အထည်ဖော်ပါ
   - အတည်ပြုမှု အခြေအနေအပေါ် မူတည်၍ အသုံးပြုသူအလိုက် နှုန်းထား ကန့်သတ်မှုများကို စဉ်းစားပါ

5. **မှတ်တမ်းတင်ခြင်းနှင့် စောင့်ကြည့်ခြင်း** - MCP ဆာဗာတွင် မမှန်ကန်သော လှုပ်ရှားမှုများကို စောင့်ကြည့်ပြီး လုံးလုံးလေးလေး audit trail များကို အကောင်အထည်ဖော်ပါ။
   - အတည်ပြုမှု ကြိုးပမ်းမှုများနှင့် ကိရိယာ အသုံးပြုမှုများအားလုံးကို မှတ်တမ်းတင်ပါ
   - မမှန်ကန်သော ပုံစံများအတွက် အချိန်နှင့်တပြေးညီ သတိပေးမှုများကို အကောင်အထည်ဖော်ပါ
   - မှတ်တမ်းများကို လုံခြုံစွာ သိမ်းဆည်းထားပြီး ပြင်ဆင်ခြင်း မဖြစ်နိုင်စေရန် သေချာပါစေ

6. **လုံခြုံသော သိမ်းဆည်းမှု** - အထိခိုက်ရလွယ်သော ဒေတာများနှင့် လျှို့ဝှက်ချက်များကို အနားတွင် စာလုံးကူးခြင်းဖြင့် ကာကွယ်ပါ။
   - လျှို့ဝှက်ချက်များအတွက် key vault များ သို့မဟုတ် လုံခြုံသော credential store များကို အသုံးပြုပါ
   - အထိခိုက်ရလွယ်သော ဒေတာများအတွက် field-level encryption ကို အကောင်အထည်ဖော်ပါ
   - စာလုံးကူးသော key များနှင့် credential များကို ပုံမှန် ပြောင်းလဲပါ

7. **Token စီမံခန့်ခွဲမှု** - token passthrough အားလုံးကို ကာကွယ်ရန် မော်ဒယ် input နှင့် output များအားလုံးကို စစ်ဆေးပြီး သန့်ရှင်းပါ။
   - audience claim များအပေါ် မူတည်၍ token စစ်ဆေးမှုကို အကောင်အထည်ဖော်ပါ
   - သင့် MCP ဆာဗာအတွက် တိတိကျကျ ထုတ်ပေးထားသော token မဟုတ်ပါက လက်ခံမရပါ
   - token အသက်တာ စီမံခန့်ခွဲမှုနှင့် ပြောင်းလဲမှုကို သေချာစွာ အကောင်အထည်ဖော်ပါ

8. **Session စီမံခန့်ခွဲမှု** - session hijacking နှင့် fixation တိုက်ခိုက်မှုများကို ကာကွယ်ရန် လုံခြုံသော session ကိုင်တွယ်မှုကို အကောင်အထည်ဖော်ပါ။
   - လုံခြုံပြီး မကြိုတင်ခန့်မှန်းနိုင်သော session ID များကို အသုံးပြုပါ
   - session များကို အသုံးပြုသူအထူးသတ်မှတ်ချက်များနှင့် ချိတ်ဆက်ပါ
   - session သက်တမ်းကုန်ဆုံးမှုနှင့် ပြောင်းလဲမှုကို သေချာစွာ အကောင်အထည်ဖော်ပါ

9. **ကိရိယာ အကောင်အထည်ဖော်မှု Sandboxing** - ကိရိယာများကို သီးခြား ပတ်ဝန်းကျင်များတွင် လည်ပတ်စေ၍ ပျက်စီးမှုဖြစ်ပါက lateral movement ကို ကာကွယ်ပါ။
   - ကိရိယာ လည်ပတ်မှုအတွက် container isolation ကို အကောင်အထည်ဖော်ပါ
   - အရင်းအမြစ် ပျက်စီးမှုတိုက်ခိုက်မှုများကို ကာကွယ်ရန် resource ကန့်သတ်ချက်များကို သတ်မှတ်ပါ
   - လုံခြုံရေး domain များအလိုက် သီးခြား execution context များကို အသုံးပြုပါ

10. **ပုံမှန် လုံခြုံရေး စစ်ဆေးမှုများ** - MCP အကောင်အထည်ဖော်မှုများနှင့် မူလအခြေခံပစ္စည်းများကို ပုံမှန် လုံခြုံရေး ပြန်လည်သုံးသပ်ပါ။
    - ပုံမှန် penetration testing များကို အချိန်ဇယားချပြီး ပြုလုပ်ပါ
    - အလိုအလျောက် စကင်လုပ်နိုင်သော ကိရိယာများဖြင့် အန္တရာယ်များကို ရှာဖွေပါ
    - သိရှိပြီးသား လုံခြုံရေး ပြဿနာများကို ဖြေရှင်းရန် မူလအခြေခံပစ္စည်းများကို အဆက်မပြတ် update လုပ်ပါ

11. **အကြောင်းအရာ လုံခြုံရေး စစ်ထုတ်ခြင်း** - ထည့်သွင်းမှုနှင့် ထုတ်ပေးမှု အကြောင်းအရာများအတွက် လုံခြုံရေး စစ်ထုတ်မှုများကို အကောင်အထည်ဖော်ပါ။
    - Azure Content Safety သို့မဟုတ် ဆင်တူဝန်ဆောင်မှုများကို အသုံးပြု၍ အန္တရာယ်ရှိသော အကြောင်းအရာများကို ရှာဖွေပါ
    - prompt injection ကို ကာကွယ်ရန် prompt shield နည်းလမ်းများကို အကောင်အထည်ဖော်ပါ
    - ဖန်တီးထားသော အကြောင်းအရာများကို အထိခိုက်ရလွယ်သော ဒေတာ ထွက်ပေါက်မှုရှိမရှိ စစ်ဆေးပါ

12. **Supply Chain လုံခြုံရေး** - သင့် AI supply chain အတွင်း ပါဝင်သော အစိတ်အပိုင်းအားလုံး၏ တရားဝင်မှုနှင့် တည်ငြိမ်မှုကို စစ်ဆေးပါ။
    - လက်မှတ်ထိုးထားသော package များကို အသုံးပြု၍ လက်မှတ်များကို စစ်ဆေးပါ
    - software bill of materials (SBOM) စစ်ဆေးမှုကို အကောင်အထည်ဖော်ပါ
    - မူလအခြေခံပစ္စည်းများအတွက် မကောင်းသော update များကို စောင့်ကြည့်ပါ

13. **ကိရိယာ သတ်မှတ်ချက် ကာကွယ်မှု** - ကိရိယာ သတ်မှတ်ချက်များနှင့် metadata များကို လုံခြုံစွာ ထိန်းသိမ်း၍ tool poisoning ကို ကာကွယ်ပါ။
    - အသုံးမပြုမီ ကိရိယာ သတ်မှတ်ချက်များကို စစ်ဆေးပါ
    - ကိရိယာ metadata တွင် မမျှော်လင့်ထားသော ပြောင်းလဲမှုများကို စောင့်ကြည့်ပါ
    - ကိရိယာ သတ်မှတ်ချက်များအတွက် တည်ငြိမ်မှု စစ်ဆေးမှုများကို အကောင်အထည်ဖော်ပါ

14. **Dynamic Execution စောင့်ကြည့်မှု** - MCP ဆာဗာများနှင့် ကိရိယာများ၏ runtime အပြုအမူကို စောင့်ကြည့်ပါ။
    - မမှန်ကန်သော အပြုအမူများကို ရှာဖွေရန် behavioral analysis ကို အကောင်အထည်ဖော်ပါ
    - မမျှော်လင့်ထားသော လည်ပတ်မှု ပုံစံများအတွက် သတိပေးမှုများကို စီစဉ်ပါ
    - runtime application self-protection (RASP) နည်းလမ်းများကို အသုံးပြုပါ

15. **အနည်းဆုံး ခွင့်ပြုချက် 원칙** - MCP ဆာဗာများနှင့် ကိရိယာများကို လိုအပ်သည့် ခွင့်ပြုချက် အနည်းဆုံးဖြင့် လည်ပတ်စေပါ။
    - လုပ်ဆောင်ချက် တစ်ခုချင်းစီအတွက် လိုအပ်သော ခွင့်ပြုချက်များကိုသာ ပေးပါ
    - ခွင့်ပြုချက် အသုံးပြုမှုကို ပုံမှန် ပြန်လည်သုံးသပ်ပြီး စစ်ဆေးပါ
    - အုပ်ချုပ်မှု လုပ်ဆောင်ချက်များအတွက် just-in-time access ကို အကောင်အထည်ဖော်ပါ

**အကြောင်းကြားချက်**  
ဤစာတမ်းကို AI ဘာသာပြန်ဝန်ဆောင်မှု [Co-op Translator](https://github.com/Azure/co-op-translator) ဖြင့် ဘာသာပြန်ထားပါသည်။ ကျွန်ုပ်တို့သည် တိကျမှန်ကန်မှုအတွက် ကြိုးစားသော်လည်း အလိုအလျောက် ဘာသာပြန်ခြင်းတွင် အမှားများ သို့မဟုတ် မှားယွင်းချက်များ ပါဝင်နိုင်ကြောင်း သတိပြုပါရန် မေတ္တာရပ်ခံအပ်ပါသည်။ မူရင်းစာတမ်းကို မူလဘာသာဖြင့်သာ တရားဝင်အရင်းအမြစ်အဖြစ် ယူဆသင့်ပါသည်။ အရေးကြီးသော အချက်အလက်များအတွက် လူ့ဘာသာပြန်ပညာရှင်မှ ဘာသာပြန်ခြင်းကို အကြံပြုပါသည်။ ဤဘာသာပြန်ချက်ကို အသုံးပြုရာမှ ဖြစ်ပေါ်လာနိုင်သည့် နားလည်မှုမှားယွင်းမှုများအတွက် ကျွန်ုပ်တို့ တာဝန်မယူပါ။