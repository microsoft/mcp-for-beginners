# Run sample

## Set up virtual environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Install dependencies

```sh
pip install "mcp[cli]>=2.3.0,<3"
```

## Run code

```sh
python client.py
```

You should see the text:

```text
Available tools: ['add']
Result of add tool: meta=None content=[TextContent(type='text', text='8.0', annotations=None, meta=None)] structured_content=None is_error=False result_type='complete'
```