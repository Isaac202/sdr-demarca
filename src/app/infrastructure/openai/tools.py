from openai_agents.tools import tool

from app.application.use_cases import GetPersonUseCase
from app.infrastructure.db.session import AsyncSessionLocal
from app.infrastructure.db.repository import PersonRepository

@tool
async def greet_person(person_id: int) -> str:
    """Tool to greet a person by ID using the domain use case"""
    async with AsyncSessionLocal() as session:
        repo = PersonRepository(session)
        use_case = GetPersonUseCase(repo)
        person = await use_case.execute(person_id)
        if person:
            return f"Hello, {person.name}!"
        return "Person not found."

