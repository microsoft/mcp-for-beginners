FROM python:3.13-slim

# Oracle Instant Client version to download at build time.
# To use a different version, pass both ARGs together:
#   docker build \
#     --build-arg IC_URL=https://download.oracle.com/otn_software/linux/instantclient/2340000/instantclient-basic-linux.x64-23.4.0.24.05.zip \
#     --build-arg IC_DIR=instantclient_23_4 .
# Latest versions: https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html
ARG IC_URL=https://download.oracle.com/otn_software/linux/instantclient/2360000/instantclient-basic-linux.x64-23.6.0.24.10.zip
ARG IC_DIR=instantclient_23_6

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget unzip libaio1t64 && \
    rm -rf /var/lib/apt/lists/* && \
    # On Debian Bookworm, libaio1t64 ships libaio.so.1t64 but Oracle Instant
    # Client looks for libaio.so.1 — create the missing symlink.
    ln -sf /usr/lib/x86_64-linux-gnu/libaio.so.1t64 /usr/lib/x86_64-linux-gnu/libaio.so.1 && \
    wget -q "${IC_URL}" -O /tmp/ic.zip && \
    unzip -q /tmp/ic.zip -d /opt/oracle && \
    mv "/opt/oracle/${IC_DIR}" /opt/oracle/instantclient && \
    rm /tmp/ic.zip && \
    apt-get purge -y --auto-remove wget unzip

ENV ORACLE_CLIENT_LIB_DIR=/opt/oracle/instantclient
ENV LD_LIBRARY_PATH=/opt/oracle/instantclient

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY db.py kb.py server.py ./

ENV ORACLE_DRIVER_MODE=thick
ENV MCP_TRANSPORT=streamable-http
ENV MCP_HOST=0.0.0.0
ENV MCP_PORT=8000

EXPOSE 8000

CMD ["python", "server.py"]
