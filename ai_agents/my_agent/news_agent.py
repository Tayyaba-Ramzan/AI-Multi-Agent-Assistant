from agents import Agent
from my_config.gemini_config import MODEL
from my_tools.news_tool import get_latest_news

news_agent = Agent(
    name="News Headline",
    instructions=(
        "You are an intelligent AI assistant designed to provide up-to-date news headlines. "
        "When a user asks about recent events or news on a specific topic, use the `get_latest_news` tool "
        "to fetch and present the top 3 latest headlines. Ensure the information is timely, relevant, and clearly formatted."
    ),
    model=MODEL,
    tools=[get_latest_news]
)
