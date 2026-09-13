# నమూనాను నడపండి

> [!WARNING]
> ఈ నమూనా పాడెడ్ అయిన Sampling మరియు పాత HTTP+SSE ఎండ్‌పాయింట్‌ను ఉపయోగిస్తుంది. ఇది
> MCP `2025-11-25` అనుకూలత కోసం నిల్వ చేయబడింది. కొత్త అమలు చేసినవారు ప్రత్యక్షంగా LLM ప్రొవైడర్‌ను పిలవాలి మరియు దూర MCP ట్రాఫిక్ కోసం Streamable HTTP ఉపయోగించాలి.


## వర్చువల్ ఎన్విరాన్‌మెంట్ సృష్టించండి

```sh
python -m venv venv
source ./venv/bin/activate
```

## ఆధారాలను ఇన్స్టాల్ చేయండి

```sh
pip install "mcp[cli]"
```

## సర్వర్‌ను నడపండి

```sh
uvicorn server:app --port 8000
```

## GitHub Copilot మరియు VS Code తో సర్వర్‌ను పరీక్షించండి

mcp.json లో క్రింది విధంగా ఎంట్రీని జోడించండి:

```json
"servers": {
    "my-mcp-server-999e9ea3": {
        "url": "http://localhost:8001/sse",
        "type": "http"
    }
}
```

సర్వర్‌పై "start" క్లిక్ చేయడం ఖచ్చితంగా చేయండి.

GitHub Copilot లో కింది ప్రాంప్ట్‌ను పేస్ట్ చేయండి:

```text
create a blog post named "Where Python comes from", the content is "Python is actually named after Monty Python Flying Circus"
```

మొదటి సారి మీరు Sampling చర్యను అంగీకరించాలా అని అడుగుతారు, ఆ తర్వాత "create_blog" ను నడపడానికి టూల్‌ను అంగీకరించమా అని అడుగుతారు. మీరు క్రింది సమాధానం లాగా ఒక ప్రతిస్పందన చూడగలరు:

```json
{
  "result": "{\"id\": \"Where Python comes from\", \"abstract\": \"# Python's Origin\\n\\nPython, the popular programming language, derives its name from **Monty Python's Flying Circus**, the British comedy troupe, rather than the snake. This naming choice reflects the creator's desire to make programming more fun and accessible.\"}"
}
```

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**అస్వీకరణ**:
ఈ పత్రం AI అనువాద సేవ [Co-op Translator](https://github.com/Azure/co-op-translator) ఉపయోగించి అనువదించబడింది. మేము ఖచ్చితత్వానికి ప్రయత్నిస్తున్నప్పటికీ, ఆటోమేటెడ్ అనువాదాలు తప్పులు లేదా అసమగ్రతలను కలిగి ఉండవచ్చు. దాని స్వదేశ భాషలో ఉన్న అసలు పత్రాన్ని అధికారం కలిగిన మూలంగా పరిగణించాలి. కీలకమైన సమాచారం కోసం, ప్రొఫెషనల్ మానవ అనువాదాన్ని సిఫారసు చేస్తాము. ఈ అనువాదం ఉపయోగం వల్ల కలిగే ఏవైనా అపార్థాలు లేదా తప్పుదారులు కోసం మేము బాధ్యత వహించము.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->