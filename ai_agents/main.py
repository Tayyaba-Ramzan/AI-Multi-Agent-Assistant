from agents import Runner
from my_agent.weather_agent import weather_agent
from my_agent.news_agent import news_agent
from my_agent.math_agent import math_agent

while True:
    query = input("\n🔍 Ask me anything (or type 'exit' to quit): ")
    if query.lower() == "exit":
        break

    lower_query = query.strip().lower()

    if "mausam" in lower_query or "weather" in lower_query:
        response = Runner.run_sync(weather_agent, input=query)

    elif any(word in lower_query for word in ["solve", "add", "plus", "multiply", "minus", "+", "-", "*", "/"]):
        response = Runner.run_sync(math_agent, input=query)

    else:
        response = Runner.run_sync(news_agent, input=query)

    print(f"\nAgent: {response.agent_name}")
    print("🤖 Output:")
    print(response.final_output)
