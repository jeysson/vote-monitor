class VoteService:

    def __init__(self, vote_legislator, vote_repository):
        self.leg_repo = vote_legislator
        self.vote_repo = vote_repository

    def get_legislator_vote_summary(self, legislator_id: int):
        legislator = self.leg_repo.get_by_id(legislator_id)
        if legislator is None:
            return None

        votes = self.vote_repo.get_by_legislatorall()

        supported = sum(1 for vote in votes if vote.legislator_id == legislator_id and vote.supported)
        opposed = sum(1 for vote in votes if vote.legislator_id == legislator_id and not vote.supported)

        return {
            'id': legislator.id,
            'name': legislator.name,
            'supported': supported,
            'opposed': opposed
        }

    def get_vote_by_id(self, vote_id):
        return self.vote_repository.get_by_id(vote_id)