# MCP Roots (Legacy Feature)

> [!WARNING]
> Ang Roots ay deprecated simula sa MCP `2026-07-28`. Nanatili ito sa rebisyong ito para sa
> compatibility at maaaring alisin sa unang rebisyon ng espesipikasyon na
> ilalabas sa o pagkatapos ng Hulyo 28, 2027. Ang mga bagong implementasyon ay dapat magpasa ng
> mga direktoryo o mga file sa pamamagitan ng mga parameter ng tool, mga resource URI, o server
> configuration.

## Overview

Pinapahintulutan ng Roots ang isang MCP client na sabihin sa isang server kung alin sa mga lokasyon ng filesystem ang may kaugnayan
sa kasalukuyang kahilingan. Ang isang root ay naglalaman ng kinakailangang `file://` URI at isang opsyonal
na human-readable na pangalan.

Ang Roots ay mga impormasyonal na palatandaan. Hindi sila mga conversation-history containers,
sessions ng protocol, o isang mekanismo ng access-control. Hindi pinipilit ng protocol na manatili ang server sa loob ng mga nakalistang roots.


## Learning Objectives

Sa pagtatapos ng leksyon na ito, magagawa mong:

- Ipaliwanag kung ano ang kinakatawan ng MCP Roots at kung ano ang hindi nito kinakatawan.
- Kilalanin ang kasalukuyang `roots/list` multi-round-trip na daloy.
- Ipatupad ang mga kontrol sa seguridad nang independyente mula sa Roots.
- Ilipat ang mga bagong implementasyon sa mga suportadong alternatibo.

## Root Data

Ibinabalik ng client ang bawat root bilang isang `file://` URI na may opsyonal na display name:

```json
{
  "roots": [
    {
      "uri": "file:///home/user/projects/weather-service",
      "name": "Weather Service"
    }
  ]
}
```

Dapat ilantad ng mga client ang mga lokasyon na naaprubahan lamang ng user. Dapat ituring ng mga server
ang resulta bilang gabay tungkol sa mga kaugnay na file, hindi bilang patunay ng awtorisasyon.

## MCP 2026-07-28 Flow

Ipinapahayag ng isang client na sumusuporta sa Roots ang kakayahan sa bawat kahilingan:

```json
{
  "_meta": {
    "io.modelcontextprotocol/clientCapabilities": {
      "roots": {}
    }
  }
}
```

Habang pinoproseso ang kahilingan ng client, maaaring magbalik ang server ng isang
`InputRequiredResult` na naglalaman ng isang `roots/list` input na kahilingan:

```json
{
  "resultType": "input_required",
  "inputRequests": {
    "workspaceRoots": {
      "method": "roots/list"
    }
  },
  "requestState": "opaque-state-from-server"
}
```

Kinokolekta ng client ang mga naaprubahang roots at inuulit ang orihinal na kahilingan gamit ang
tumutugmang `inputResponses` at hindi nabagong `requestState`. Pinapanatili ng multi-round-trip
na pattern na ito ang protocol na walang estado; walang `initialize` handshake o
session sa antas ng protocol.

## Legacy 2025-11-25 Behavior

Sa MCP `2025-11-25`, nag-anunsyo ang mga client ng Roots sa panahon ng initialization. Maaaring mag-isyu ang server ng direktang `roots/list` na kahilingan, at maaaring magpadala ang client ng
`notifications/roots/list_changed` kapag nagbago ang mga roots nito.


notification nito sa implementasyon ng `2026-07-28`.


## Recommended Replacements

### Tool Parameters

Gawing malinaw ang kinakailangang direktoryo o file sa tool schema:

```json
{
  "name": "analyze_project",
  "inputSchema": {
    "type": "object",
    "properties": {
      "projectDirectory": {
        "type": "string",
        "description": "Approved project directory to analyze"
      }
    },
    "required": ["projectDirectory"]
  }
}
```

### Resource URIs

Gamitin ang MCP Resources kapag maaaring ilantad ng server ang mga kaugnay na file sa pamamagitan ng matatag na
URI. Pinananatili nitong malinaw ang pagtuklas at pagkuha.

### Server Configuration

Para sa mga fixed deployment, i-configure ang pinapayagang mga direktoryo kapag nagsimula ang server.
Madalas mas malinaw ito kaysa sa pagtuklas sa panahon ng isang tawag sa tool.

## Security Requirements

Anumang kapalit ang piliin mo:

- Kumuha ng pahintulot ng user bago ilantad ang mga lokasyon ng filesystem.
- I-canonicalize at i-validate ang mga path upang maiwasan ang traversal.
- Ipatupad ang awtorisasyon at sandboxing nang independyente sa mga halaga ng root.
- Suriing muli ang mga permiso kapag ina-access ang file, hindi lamang kapag nakalista ito.
- Iwasang ibalik ang sensitibong mga path sa mga log o mensahe ng error.

## Key Takeaways

- Inilalarawan ng Roots ang mga kaugnay na lokasyon ng filesystem; hindi sila nag-iimbak ng estado ng usapan.

- Ang Roots ay gabay, hindi isang hangganan ng control ng access.
- Ang MCP `2026-07-28` ay nagdadala ng kakayahan bawat kahilingan at gumagamit ng
  `InputRequiredResult` para sa `roots/list`.
- Dapat gumamit ang mga bagong implementasyon ng mga parameter ng tool, resource URI, o server
  configuration bilang kapalit.

## Additional Resources

- [Roots in MCP 2026-07-28](https://modelcontextprotocol.io/specification/2026-07-28/client/roots)
- [Deprecated features registry](https://modelcontextprotocol.io/specification/2026-07-28/deprecated)
- [What's Changed in MCP: The 2026-07-28 Specification](../../01-CoreConcepts/mcp-2026-07-28.md)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Pagtatanggi**:
Ang dokumentong ito ay isinalin gamit ang serbisyo ng AI translation na [Co-op Translator](https://github.com/Azure/co-op-translator). Bagama't nagsusumikap kami para sa katumpakan, pakatandaan na ang awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na pangunahing sanggunian. Para sa mahahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang maling pagkakaintindi o maling interpretasyon na nagmula sa paggamit ng pagsasaling ito.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->