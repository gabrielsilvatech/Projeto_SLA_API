from starlette.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, HTTPException

from src.routes.user.routes_user import RoutesUser
from src.routes.login.routes_login import RoutesLogin
from src.routes.ticket.routes_ticket import RoutesTicket


from .config import settings
from .middleware import CheckTokenMiddleware

app = FastAPI(
    title="API - TICKETFLOW",
    version="0.0.1",
    description="""
    Olá prezado, essa API visa trazer uma comunicação de usuário/aplicação de forma eficiente, 
    facilitando a rotina diária referente a controle de tickets.
    \n\n\n Desenvolvido para:  PROJETO IMPACTA.   \n DesenvolvedoR: Gabriel Silva - GitHub - [GabrielSilvaTech]
    """,
    contact={
        "name": "Suporte API",
        "email": "gabrielsilva.infotech@gmail.com.br",
    },
    servers=[
        {"url": f"{settings.ROUTE_API}", "description": "Servidor de Desenvolvimento"},
        {"url": f"{settings.ROUTE_API}", "description": "Servidor de Producão"},
    ],
    root_path="",
)



app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(settings.ROUTE_FRONT)],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "OPTIONS", "DELETE"],
    allow_headers=["*"]
)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        {"detail": exc.detail},
        status_code=exc.status_code
    )

route_login = RoutesLogin().route_login
route_user = RoutesUser().route_user
route_ticket = RoutesTicket().route_ticket

app.add_middleware(CheckTokenMiddleware)
app.include_router(route_login)
app.include_router(route_user)
app.include_router(route_ticket)

