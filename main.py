from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from app.routers import home, users, auth

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="some-random-string")

app.include_router(home.router)
app.include_router(users.router)
app.include_router(auth.router)
