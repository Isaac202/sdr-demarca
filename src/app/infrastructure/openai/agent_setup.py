import os
from dotenv import load_dotenv
from openai_agents import Agent, Runner, set_default_openai_key

from app.infrastructure.openai.model import default_model
from app.infrastructure.openai.tools import greet_person

load_dotenv()
# Initialize OpenAI API key
set_default_openai_key(os.getenv("OPENAI_API_KEY"))

agent = Agent(
    instructions="Use the greet_person tool to greet a person by their ID.",
    tools=[greet_person],
    model=default_model,
)

# Runner for executing the agent
runner = Runner(agent=agent)

