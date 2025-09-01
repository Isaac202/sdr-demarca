from abc import ABC, abstractmethod

from app.domain.entities import Person

class PersonRepositoryPort(ABC):
    @abstractmethod
    async def get_person(self, person_id: int) -> Person:
        """Retrieve a Person by ID"""
        pass

