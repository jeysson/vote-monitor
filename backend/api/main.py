from fastapi import FastAPI
from backend.api.routes.legislator_routes import router as legislator_router
from backend.api.routes.bill_routes import router as bill_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Vote Monitor API",
    version="1.0.0"
)

origins = [
    "http://localhost:3000",  # React dev server
    "http://127.0.0.1:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # quem pode acessar
    allow_credentials=True,
    allow_methods=["*"],    # quais métodos são permitidos
    allow_headers=["*"],    # quais headers são permitidos
)

app.include_router(legislator_router, prefix="/legislators", tags=["Legislators"])
app.include_router(bill_router, prefix="/bills", tags=["Bills"])
