from agents import Agent
from my_config.gemini_config import MODEL
from my_tools.weather_tool import get_weather

weather_agent = Agent(
    name="WeatherBot",
    instructions=(
        "You are a weather assistant capable of providing real-time weather updates. "
        "When a user inquires about the weather in a specific city, use the `get_weather` tool "
        "to retrieve and respond with accurate temperature and conditions. "
        "Ensure clarity and user-friendly formatting in the response."
    ),
    model=MODEL,
    tools=[get_weather]
)
