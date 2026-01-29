# Run sample

## Set up environment

```sh
python -m venv
source ./venv/bin/activate
```

## Install dependencies

```sh
pip install PyJWT
```

## Run code

```sh
python lab.py
```

You go see output wey be like:

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

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Disclaimer**:  
Dis dokyument don use AI transle-shon service [Co-op Translator](https://github.com/Azure/co-op-translator) do di transle-shon. Even as we dey try make am correct, abeg make you sabi say transle-shon wey machine do fit get mistake or no dey accurate well. Di original dokyument for im native language na di one wey you go take as di correct source. For important mata, e good make you use professional human transle-shon. We no go fit take blame for any misunderstanding or wrong interpretation wey fit happen because you use dis transle-shon.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->