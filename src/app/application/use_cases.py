from app.application.ports import PersonRepositoryPort
from app.domain.entities import Person

class GetPersonUseCase:
    def __init__(self, repo: PersonRepositoryPort):
        self.repo = repo

    async def execute(self, person_id: int) -> Person:
        return await self.repo.get_person(person_id)

