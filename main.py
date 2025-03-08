import uvicorn
from urllib.parse import urlparse

from src.config import settings


parsed_url = urlparse(settings.ROUTE_API)
host = parsed_url.hostname
port = parsed_url.port or 8080

if __name__ == "__main__":
    uvicorn.run("src.manager:app", host=str(host), port=int(port), reload=True, workers=1, lifespan="on")
