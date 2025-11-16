import os
from pydantic import BaseModel

class DataPaths(BaseModel):
    legislators: str
    bills: str
    votes: str
    vote_results: str


class Settings(BaseModel):
    data: DataPaths


# Caminho base do projeto — detecta automaticamente
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

settings = Settings(
    data=DataPaths(
        legislators=os.path.join(BASE_DIR, "data/legislators.csv"),
        bills=os.path.join(BASE_DIR, "data/bills.csv"),
        votes=os.path.join(BASE_DIR, "data/votes.csv"),
        vote_results=os.path.join(BASE_DIR, "data/vote_results.csv"),
    )
)
