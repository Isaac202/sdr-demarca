
# Ensure that OpenAI Agents components import correctly and are available
import pytest

# Skip this module if openai_agents is not installed to avoid import errors in dev environments
pytest.importorskip("openai_agents", reason="openai_agents dependency not installed")

def test_agent_setup_imports():
    from app.infrastructure.openai.agent_setup import agent, runner

    assert agent is not None, "Agent instance should be initialized"
    assert runner is not None, "Runner instance should be initialized"

def test_default_model_import():
    from app.infrastructure.openai.model import default_model

    assert default_model is not None, "Default model should be defined"

def test_greet_person_tool_exists():
    from app.infrastructure.openai.tools import greet_person

    assert callable(greet_person), "greet_person should be a callable tool"
