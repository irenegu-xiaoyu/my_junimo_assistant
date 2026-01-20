from typing import TypedDict, Annotated
from operator import add

class AgentState(TypedDict):
    """State that tracks the workflow"""
    messages: Annotated[list, add]  # Messages accumulate across invocations
    farm_status: dict
    specialist_responses: dict
    next_agents: list[str]
    final_response: dict | None
    user_preferences: dict  # Stores user preferences like playstyle, priorities, etc.
