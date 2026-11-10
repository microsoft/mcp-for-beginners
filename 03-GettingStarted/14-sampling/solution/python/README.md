# Running this sample

> [!WARNING]
> This sample uses deprecated Sampling. It is retained for MCP `2025-11-25`
> compatibility, and the server prints an `MCPDeprecationWarning`. New
> implementations should call an LLM provider directly.

The client starts `server.py` itself over stdio. When the server's `create_product` tool asks the client for an LLM completion (sampling), the client answers it with a model deployed in Microsoft Foundry (Azure OpenAI).

You need Python 3.10 or later. You're recommended to install `uv` but it's not a must, see [instructions](https://docs.astral.sh/uv/#highlights)

## -0- Create a virtual environment

```bash
python -m venv venv
```

## -1- Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

## -2- Install the dependencies

```bash
pip install "mcp[cli]>=2.3.0,<3" "openai>=3.44.0,<4"
```

## -3- Configure Microsoft Foundry

Deploy an active model such as `gpt-5.1` in Microsoft Foundry, then set:

```bash
export AZURE_OPENAI_ENDPOINT="https://<resource-name>.openai.azure.com"
export AZURE_OPENAI_API_KEY="<api-key>"
export AZURE_OPENAI_DEPLOYMENT="gpt-5.1"
```

On Windows PowerShell use `$env:AZURE_OPENAI_ENDPOINT="..."` instead of `export`.

## -4- Run the sample

```bash
python client.py
```

You should see output similar to:

```text
[02/18/26 13:16:34] INFO     Processing request of type ListToolsRequest               server.py:720
result: {"id": 1, "name": "paprika", "description": "**Product Description: Paprika - The Vibrant Red Wonder**\n\nElevate your culinary creations with our premium paprika, the jewel of spices that bursts with color, flavor, and nutrition. Harvested from the finest red, juicy peppers, our paprika is meticulously ground to preserve its rich, vibrant hue and aromatic essence, making it an essential ingredient in any kitchen.\n\nEach sprinkle of our paprika adds a delightful warmth and a subtle sweetness to a variety of dishes, from savory stews to vibrant salads and mouthwatering marinades. Its radiant red color not only enhances the visual appeal of your meals but also signifies the freshness and quality of the peppers used. \n\nRich in antioxidants and packed with vitamins, paprika not only tantalizes your taste buds but also contributes to a healthy lifestyle. Whether you're a professional chef or a home cook, this versatile spice will inspire your creativity and add a beautiful, flavorful touch to everything you whip up.\n\nDiscover the magic of our red, juicy paprika\u2014a spice that transforms ordinary dishes into"}
```

