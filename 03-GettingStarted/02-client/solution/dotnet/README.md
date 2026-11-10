# Running this sample

You need the [.NET 10 SDK](https://dotnet.microsoft.com/download/dotnet/10.0).

## -1- Build the server

The client starts the compiled server from the sibling [server](../server/) project, so build it first:

```bash
cd ../server
dotnet build
cd ../dotnet
```

## -2- Install the dependencies

```bash
dotnet restore
```

## -3- Run the sample

```bash
dotnet run
```

You should see output similar to the following (the server's log messages on stderr are printed as well):

```text
Setting up stdio transport
Listing tools
Connected to server with tools: add
Result: Sum 4
```
