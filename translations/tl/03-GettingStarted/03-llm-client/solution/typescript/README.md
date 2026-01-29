# Pagpapatakbo ng sample na ito

Ang sample na ito ay nangangailangan ng LLM sa client. Kailangan mong patakbuhin ito sa Codespaces o mag-set up ng personal access token sa GitHub para gumana.

## -1- I-install ang mga dependencies

```bash
npm install
```

## -3- Patakbuhin ang server

```bash
npm run build
```

## -4- Patakbuhin ang client

```sh
npm run client
```

Makikita mo ang resulta na katulad ng:

```text
Asking server for available tools
MCPClient started on stdin/stdout
Querying LLM:  What is the sum of 2 and 3?
Making tool call
Calling tool add with args "{\"a\":2,\"b\":3}"
Tool result:  { content: [ { type: 'text', text: '5' } ] }
```

**Paalala**:  
Ang dokumentong ito ay isinalin gamit ang AI translation service na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagamat nagsusumikap kami para sa katumpakan, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o di-tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na maaaring magmula sa paggamit ng pagsasaling ito.