from pydantic import BaseModel

class RunAgentRequest(BaseModel):
    person_id: int

class RunAgentResponse(BaseModel):
    response: str

