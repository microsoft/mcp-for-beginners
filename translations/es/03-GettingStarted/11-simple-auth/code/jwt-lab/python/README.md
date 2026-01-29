# Ejecutar ejemplo

## Configurar el entorno

```sh
python -m venv
source ./venv/bin/activate
```

## Instalar dependencias

```sh
pip install PyJWT
```

## Ejecutar código

```sh
python lab.py
```

Deberías ver una salida similar a:

```text
Encoded JWT: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlVzZXIgVXNlcnNvbiIsImFkbWluIjp0cnVlLCJpYXQiOjE3NTkxNjgzMDEsImV4cCI6MTc1OTE3MTkwMX0.tz0UYNNtGVC61DWjVDF8xlhpNkp5XBtxmQH3m_RNwe8
✅ Token is valid.
Decoded claims:
  sub: 1234567890
  name: User Userson
  admin: True
  iat: 1759168301
  exp: 1759171901
```

---

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando el servicio de traducción automática [Co-op Translator](https://github.com/Azure/co-op-translator). Aunque nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automáticas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que surjan del uso de esta traducción.