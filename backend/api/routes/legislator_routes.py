from fastapi import APIRouter
from backend.config.container import container

router = APIRouter()

@router.get("/summary")
def legislator_summary():
    service = container.legislator_summary_service
    summaries = service.get_all_legislator_summaries()
    return summaries
