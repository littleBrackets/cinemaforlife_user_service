from fastapi import FastAPI
from src.routes import user_routes, auth_routes
from src.middlewares.request_id import RequestIDMiddleware

def create_app():
    app = FastAPI(title="Auth Service")
    app.add_middleware(RequestIDMiddleware)
    app.include_router(user_routes.router, prefix="/users", tags=["users"])
    app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
    return app
