from fastapi import FastAPI
from backend.api.routes.legislator_routes import router as legislator_router
from backend.api.routes.bill_routes import router as bill_router

app = FastAPI(
    title="Vote Monitor API",
    version="1.0.0"
)

app.include_router(legislator_router, prefix="/legislators", tags=["Legislators"])
app.include_router(bill_router, prefix="/bills", tags=["Bills"])
