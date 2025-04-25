# Use the official .NET SDK image as the build image
FROM mcr.microsoft.com/dotnet/sdk:9.0 AS build
WORKDIR /src

# Copy the project file and restore dependencies
COPY ["calculator.csproj", "./"]
RUN dotnet restore

# Copy the remaining source code
COPY . .

# Build and publish the application
RUN dotnet publish -c Release -o /app/publish

# Create the runtime image
FROM mcr.microsoft.com/dotnet/runtime:9.0 AS runtime
WORKDIR /app
COPY --from=build /app/publish .

# Set the entry point for the container
ENTRYPOINT ["dotnet", "calculator.dll"]

# Configure container for MCP stdio communication
ENV DOTNET_RUNNING_IN_CONTAINER=true
ENV DOTNET_SYSTEM_GLOBALIZATION_INVARIANT=1

