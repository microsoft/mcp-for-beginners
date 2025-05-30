<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "57f14126c1c6add76b3aef3844dfe4e3",
  "translation_date": "2025-05-17T05:39:35+00:00",
  "source_file": "SECURITY.md",
  "language_code": "ne"
}
-->
## सुरक्षा

माइक्रोसफ्टले हाम्रो सफ्टवेयर उत्पादन र सेवाहरूको सुरक्षालाई गम्भीर रूपमा लिन्छ, जसमा हाम्रा गिटहब संगठनहरू मार्फत व्यवस्थापन गरिएका सबै स्रोत कोड रिपोजिटरीहरू समावेश छन्, जसमा [Microsoft](https://github.com/Microsoft), [Azure](https://github.com/Azure), [DotNet](https://github.com/dotnet), [AspNet](https://github.com/aspnet) र [Xamarin](https://github.com/xamarin) समावेश छन्।

यदि तपाईंलाई कुनै माइक्रोसफ्टको स्वामित्वमा रहेको रिपोजिटरीमा [माइक्रोसफ्टको सुरक्षा कमजोरीको परिभाषा](https://aka.ms/security.md/definition) अनुसार सुरक्षा कमजोरी फेला परेको छ भन्ने लाग्छ भने, कृपया तल वर्णन गरिएको रूपमा हामीलाई रिपोर्ट गर्नुहोस्।

## सुरक्षा समस्या रिपोर्ट गर्ने

**कृपया सार्वजनिक गिटहब इश्यूहरू मार्फत सुरक्षा कमजोरीहरू रिपोर्ट नगर्नुहोस्।**

यसको सट्टा, कृपया तिनीहरूलाई माइक्रोसफ्ट सुरक्षा प्रतिक्रिया केन्द्र (MSRC) मा [https://msrc.microsoft.com/create-report](https://aka.ms/security.md/msrc/create-report) मा रिपोर्ट गर्नुहोस्।

यदि तपाईंले लगइन नगरी पेश गर्न रुचाउनुहुन्छ भने, [secure@microsoft.com](mailto:secure@microsoft.com) मा इमेल पठाउनुहोस्। सम्भव भएमा, हाम्रो PGP कुञ्जी प्रयोग गरेर आफ्नो सन्देश इन्क्रिप्ट गर्नुहोस्; कृपया यसलाई [Microsoft Security Response Center PGP Key page](https://aka.ms/security.md/msrc/pgp) बाट डाउनलोड गर्नुहोस्।

तपाईंले २४ घण्टा भित्र जवाफ प्राप्त गर्नु पर्छ। कुनै कारणले गर्दा तपाईंले जवाफ प्राप्त गर्नुभएन भने, कृपया इमेल मार्फत फोलो अप गर्नुहोस् ताकि हामीले तपाईंको मौलिक सन्देश प्राप्त गर्यौं भन्ने सुनिश्चित होस्। थप जानकारी [microsoft.com/msrc](https://www.microsoft.com/msrc) मा फेला पार्न सकिन्छ।

कृपया हामीलाई सम्भावित समस्याको प्रकृति र दायरा राम्रोसँग बुझ्न मद्दत गर्न तल सूचीबद्ध जानकारी समावेश गर्नुहोस् (जति धेरै तपाईंले प्रदान गर्न सक्नुहुन्छ):

  * समस्याको प्रकार (जस्तै बफर ओभरफ्लो, SQL इन्जेक्शन, क्रस-साइट स्क्रिप्टिङ, आदि)
  * समस्याको अभिव्यक्तिसँग सम्बन्धित स्रोत फाइल(हरू)को पूर्ण पथहरू
  * प्रभावित स्रोत कोडको स्थान (ट्याग/ब्रान्च/कमिट वा प्रत्यक्ष URL)
  * समस्यालाई पुन: उत्पादन गर्न आवश्यक विशेष कन्फिगरेसन
  * समस्यालाई पुन: उत्पादन गर्न चरण-दर-चरण निर्देशनहरू
  * प्रमाण-कन्सेप्ट वा एक्सप्लोइट कोड (यदि सम्भव छ भने)
  * समस्याको प्रभाव, जसमा आक्रमणकारीले कसरी समस्याको फाइदा उठाउन सक्छ भन्ने समावेश छ

यस जानकारीले हामीलाई तपाईंको रिपोर्ट छिटो प्रक्रिया गर्न मद्दत गर्नेछ।

यदि तपाईं बग बाउंटीको लागि रिपोर्ट गर्दै हुनुहुन्छ भने, थप पूर्ण रिपोर्टहरूले उच्च बाउंटी पुरस्कारमा योगदान पुर्याउन सक्छ। कृपया हाम्रा सक्रिय कार्यक्रमहरूको बारेमा थप विवरणहरूको लागि हाम्रो [Microsoft Bug Bounty Program](https://aka.ms/security.md/msrc/bounty) पृष्ठ भ्रमण गर्नुहोस्।

## प्राथमिक भाषाहरू

हामी सबै सञ्चार अंग्रेजीमा हुन प्राथमिकता दिन्छौं।

## नीति

माइक्रोसफ्टले [समन्वयित कमजोरी खुलासा](https://aka.ms/security.md/cvd) को सिद्धान्तलाई अनुसरण गर्दछ।

**अस्वीकरण**:  
यो दस्तावेज़ AI अनुवाद सेवा [Co-op Translator](https://github.com/Azure/co-op-translator) प्रयोग गरी अनुवाद गरिएको हो। हामी शुद्धताको लागि प्रयास गर्छौं, तर कृपया जानकार रहनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा असंगतिहरू हुन सक्छन्। यसको मौलिक भाषामा रहेको मूल दस्तावेजलाई प्राधिकृत स्रोत मानिनु पर्छ। महत्त्वपूर्ण जानकारीको लागि, पेशेवर मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न हुने कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी उत्तरदायी हुने छैनौं।