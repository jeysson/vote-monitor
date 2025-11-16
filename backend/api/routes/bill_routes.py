from fastapi import APIRouter
from backend.config.container import container

router = APIRouter()


@router.get("/summary")
def bill_summary():
    service = container.bill_summary_service
    summaries = service.get_all_bill_summaries()
    return [summary.__dict__ for summary in summaries]
