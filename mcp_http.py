import os
import asyncio
from mcp_server import mcp

mcp.settings.host = "0.0.0.0"
mcp.settings.port = int(os.environ.get("PORT", 8080))

print("HOST:", mcp.settings.host)
print("PORT:", mcp.settings.port)

if __name__ == "__main__":
    asyncio.run(mcp.run_streamable_http_async())
