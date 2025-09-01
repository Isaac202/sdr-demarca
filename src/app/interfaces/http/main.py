from fastapi import FastAPI, HTTPException

from app.infrastructure.openai.agent_setup import runner
from app.interfaces.http.schemas import RunAgentRequest, RunAgentResponse

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/agents/run", response_model=RunAgentResponse)
async def run_agent(request: RunAgentRequest):
    try:
        result = runner.run({"person_id": request.person_id})
        # Extract content from result
        response = result.get("content") if isinstance(result, dict) else str(result)
        return RunAgentResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
