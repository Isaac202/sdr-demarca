from app.domain.entities import Person
from app.infrastructure.db.models import PersonModel

class PersonRepository:
    def __init__(self, db_session):
        self.db_session = db_session

    async def get_person(self, person_id: int) -> Person:
        result = await self.db_session.get(PersonModel, person_id)
        if not result:
            return None
        return Person(id=result.id, name=result.name)

