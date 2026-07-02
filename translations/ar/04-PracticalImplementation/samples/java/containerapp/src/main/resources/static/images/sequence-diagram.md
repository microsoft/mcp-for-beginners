### كيفية تكبير صورة باستخدام PHP وكود GD

في هذا الدليل، سنتعلم كيفية زيادة أبعاد صورة باستخدام مكتبة GD في PHP.

#### الخطوة 1: تحميل الصورة الأصلية

أولاً، نحتاج إلى تحميل الصورة التي نريد تكبيرها. يمكننا استخدام دالة `imagecreatefromjpeg` إذا كانت الصورة بتنسيق JPEG.

#### الخطوة 2: إنشاء صورة جديدة بالأبعاد الجديدة

بعد تحديد الأبعاد الجديدة، يمكننا إنشاء صورة فارغة جديدة باستخدام `imagecreatetruecolor`.

#### الخطوة 3: إعادة تحجيم الصورة

نستخدم `imagecopyresampled` لنقل وضبط الصورة الأصلية إلى الصورة الجديدة ذات الأبعاد الأكبر.

#### الخطوة 4: حفظ الصورة الجديدة

أخيرًا، نحفظ الصورة الجديدة باستخدام `imagejpeg`.

### مثال عملي

```php
<?php
// تحميل الصورة الأصلية
$original_image = imagecreatefromjpeg('original.jpg');

// الحصول على أبعاد الصورة الأصلية
$width = imagesx($original_image);
$height = imagesy($original_image);

// أبعاد الصورة الجديدة (مثلاً تكبير 2x)
$new_width = $width * 2;
$new_height = $height * 2;

// إنشاء صورة جديدة بالأبعاد الجديدة
$resized_image = imagecreatetruecolor($new_width, $new_height);

// إعادة تحجيم الصورة
imagecopyresampled($resized_image, $original_image, 0, 0, 0, 0, $new_width, $new_height, $width, $height);

// حفظ الصورة الجديدة
imagejpeg($resized_image, 'resized.jpg');

// تحرير الذاكرة
imagedestroy($original_image);
imagedestroy($resized_image);
?>
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**تنويه**:
تمت ترجمة هذا المستند باستخدام خدمة الترجمة بالذكاء الاصطناعي [Co-op Translator](https://github.com/Azure/co-op-translator). بينما نسعى للدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الرسمي والمعتمد. للمعلومات الهامة، يُنصح بالاستعانة بترجمة بشرية محترفة. نحن غير مسؤولين عن أي سوء فهم أو تفسير ناتج عن استخدام هذه الترجمة.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->