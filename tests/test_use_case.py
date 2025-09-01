import pytest

from app.application.use_cases import GetPersonUseCase
from app.domain.entities import Person


class DummyRepo:
    async def get_person(self, person_id: int) -> Person:
        return Person(id=person_id, name="Test User")


@pytest.mark.asyncio
async def test_get_person_use_case():
    use_case = GetPersonUseCase(DummyRepo())
    person = await use_case.execute(1)
    assert person.id == 1
    assert person.name == "Test User"
