# Patakbuhin ang halimbawa

## Gumawa ng environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Mag-install ng mga dependency

```sh
pip install "mcp[cli]" dotenv PyJWT requeests
```

## Gumawa ng token

Kailangan mong gumawa ng token na gagamitin ng client para makipag-usap sa server.

Tumawag:

```sh
python util.py
```

## Patakbuhin ang code

Patakbuhin ang code gamit ang:

```sh
python server.py
```

Sa isang hiwalay na terminal, i-type:

```sh
python client.py
```

Sa terminal ng server, dapat mong makita ang ganito:

```text
Valid token, proceeding...
User exists, proceeding...
User has required scope, proceeding...
```

Sa window ng client, dapat kang makakita ng text na katulad ng:

```text
Tool result: meta=None content=[TextContent(type='text', text='{\n  "current_time": "2025-10-06T17:37:39.847457",\n  "timezone": "UTC",\n  "timestamp": 1759772259.847457,\n  "formatted": "2025-10-06 17:37:39"\n}', annotations=None, meta=None)] structuredContent={'current_time': '2025-10-06T17:37:39.847457', 'timezone': 'UTC', 'timestamp': 1759772259.847457, 'formatted': '2025-10-06 17:37:39'} isError=False
```

Ibig sabihin gumagana na ito.

### Baguhin ang impormasyon para makita ang error

Hanapin ang code na ito sa *server.py*:

```python
 if not has_scope(has_header, "Admin.Write"):
```

Baguhin ito upang sabihin na "User.Write". Ang kasalukuyang token mo ay wala pang ganitong antas ng pahintulot, kaya kung i-restart mo ang server at subukang patakbuhin muli ang client, dapat kang makakita ng error na katulad ng sumusunod sa terminal ng server:

```text
Valid token, proceeding...
User exists, proceeding...
-> Missing required scope!
```

Maaari mong ibalik ang iyong code sa server o gumawa ng bagong token na may karagdagang scope na ito, nasa sa iyo.

---

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't sinisikap naming maging tumpak, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na mapagkakatiwalaang pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.