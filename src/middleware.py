from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPBasicCredentials
from starlette.types import ASGIApp, Scope, Receive, Send

from .security import authenticate_user


from fastapi import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse
from fastapi.security import HTTPBasicCredentials
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.types import Scope, Receive, Send, ASGIApp

from .security import authenticate_user



class CheckTokenMiddleware(BaseHTTPMiddleware):
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        
        if scope["type"] == "lifespan":
            await self.app(scope, receive, send)
            return

        
        routes_with_token_check = ["/openapi.json", "/docs"]
        request = Request(scope, receive=receive)
       
       

        if request.url.path in routes_with_token_check:
            try:
                if request.url.path == "/openapi.json":
                    await self.app(scope, receive, send)
                    return                    
                
                credentials = HTTPBasicCredentials(
                    username=str(request.query_params.get("username")),
                    password=str(request.query_params.get("password"))
                )
                await authenticate_user(credentials)  # Autenticar o usuário
                await self.app(scope, receive, send)
                return
                
            except HTTPException:
                response = JSONResponse({"error": "Unauthorized"}, status_code=401)
                await response(scope, receive, send)
                return
                
    
        await self.app(scope, receive, send)
        return
