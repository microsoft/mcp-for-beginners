# Running this sample

You need [Node.js](https://nodejs.org/) 18 or later.

## -1- Install the dependencies

```bash
npm install
```

## -2- Build the sample

```bash
npm run build
```

This compiles the server (`src/index.ts`) and the client (`src/client.ts`) into `build/`.

## -3- Run the client

```sh
npm run client
```

The client starts the server itself over stdio, so you don't need to run the server in another terminal. It gets a prompt, lists the resource templates, reads the `greeting://hello` resource, calls the `add` tool, and then exits.

You should see a result similar to:

```text
Prompt:  {
  type: 'text',
  text: 'Please review this code:\n\nconsole.log("hello");'
}
Resource template:  greeting
Resource:  Hello, hello!
Tool result:  { content: [ { type: 'text', text: '9' } ] }
```
