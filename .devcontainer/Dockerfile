ARG VARIANT="9.0"
FROM mcr.microsoft.com/devcontainers/dotnet:${VARIANT}

ARG NODE_VERSION="none"
RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      python3.11 \
      python3-venv \
      python3-pip \
 && rm -rf /var/lib/apt/lists/*
