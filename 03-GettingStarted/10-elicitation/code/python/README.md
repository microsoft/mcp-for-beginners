# Run the code

This sample demonstrates the use of Elicitation

## Set up environment

```sh
python -m venv venv
source ./venv/bin/activate
```

## Run server

```sh
uvicorn server:app
```

You should see:

```text
INFO:     Started server process [5016]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

This should start a server on port 8000.

## Test out the server in VS Code

Add an entry like so to *mcp.json*:

```
"server": {
    "type": "sse",
    "url": "http://localhost:8000/sse"
    
}
```

and start the server. Now try typing the following prompt in the chat:

```text
Book trip on 2025-02-01
```

This prompt should trigger an Elicitation scenario where you're asked for more input. Typing "2025-01-01" should lead to a successful booking:

![Elicitation example VS Code](../../assets/elicitation.png)

## Run client

Run the following command:

```sh
python client.py
```

It should start the client and you should see the following output:

```text
Available tools: ['book_trip']
[CLIENT] Received elicitation data: No trips available on 2025-01-02. Would you like to try another date?
[CLIENT]: Selecting alternative date: 2025-01-01
Result:  [SUCCESS] Booked for 2025-01-01
```

Let's highlight a piece of code, the client handler for elicitation as we're hardcoding the responses back to the server:

```python
async def elicitation_callback_handler(context: RequestContext[ClientSession, None], params: ElicitRequestParams):
    print(f"[CLIENT] Received elicitation data: {params.message}")
 
    # 1. refuses no select other date
    # return ElicitResult(action="accept", content={
    #     "checkAlternative": False
    # }) # should say no booking made, WORKS

    # 2. cancels booking
    # return ElicitResult(action="decline"), WORKS

    print("[CLIENT]: Selecting alternative date: 2025-01-01")

    # 3. opts to select another date, 2025-01-01 which leads to a booking
    return ElicitResult(action="accept", content={
         "checkAlternative": True,
         "alternativeDate": "2025-01-01"
    }) # should book 1 jan instead of initial 2nd Jan
```

Here we are hardcoding back an "accept" response with a prefilled alternate date that the server will accept. We have also provided other response types like 1) User refuses to select a date which should lead to a response saying no booking has been made. 2) This response is more like the user dismisses the whole dialogue and also this leads to no booking taking place.

You're encouraged to improve this code by making this user-driven instead of hardcoded and also to try out the different responses to see the difference.
