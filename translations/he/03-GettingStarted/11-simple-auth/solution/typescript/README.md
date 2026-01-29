# הפעלת דוגמה

## התקנת תלותים

```sh
npm install
```

## בנייה

```sh
npm run build
```

## יצירת אסימונים

```sh
npm run generate
```

זה יוצר אסימון בקובץ *.env*. הלקוח יקרא מתוך הקובץ הזה.

## הפעלת הקוד

הפעל את השרת עם:

```sh
npm start
```

הפעל את הלקוח, בחלון טרמינל נפרד עם:

```sh
npm run client
```

בטרמינל של השרת, אתה אמור לראות פלט דומה ל:

```text
User exists
User has required scopes
Middleware executed
```

ובטרמינל של הלקוח, אתה אמור לראות פלט דומה ל:

```text
Connected to MCP server with session ID: c1e50d7b-acff-4f11-8f96-5ae490ca1eaa
Available tools: { tools: [ { name: 'process-files', inputSchema: [Object] } ] }
Client disconnected.
Exiting...
```

### שינוי דברים

בואו נוודא שאנחנו מבינים את ההרשאות. מצא את הקובץ *server.ts* ואת הקוד הזה:

```typescript
 if(!hasScopes(token, ["User.Read"])){
        res.status(403).send('Forbidden - insufficient scopes');
    }
```

זה אומר שהאסימון שהועבר צריך לכלול "User.Read", בואו נשנה את זה ל-"User.Write". עכשיו הרץ `npm run build` והפעל מחדש את השרת עם `npm start`. עכשיו אתה אמור לראות שהאימות נכשל כי אין לנו את ההרשאה הזו (יש לנו User.Read ו-Admin.Write):

הלקוח עכשיו אומר

```text
Error initializing client: Error: Error POSTing to endpoint (HTTP 403): Forbidden - insufficient scopes
```

ואתה יכול לראות בטרמינל של השרת שהוא אומר:

```text
User exists
```

ושהוא לא מתקדם מעבר לנקודה זו.

או שתוסיף את ההרשאה הזו "User.Write" ותפעיל `npm run generate` ותפעיל מחדש את הלקוח, או שתחזיר את הקוד של השרת למצב הקודם.

---

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירות תרגום מבוסס בינה מלאכותית [Co-op Translator](https://github.com/Azure/co-op-translator). למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. עבור מידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.