from agents import Runner
from my_agent.weather_agent import weather_agent
from my_agent.news_agent import news_agent
from my_agent.math_agent import math_agent

query = "solve 12 + 8 * 2"

# Lowercase for easier matching
lower_query = query.lower()

# Logic to select appropriate agent
if "mausam" in lower_query or "weather" in lower_query:
    response = Runner.run_sync(weather_agent, input=query)

elif any(word in lower_query for word in ["solve", "add", "plus", "multiply", "minus", "+", "-", "*", "/"]):
    response = Runner.run_sync(math_agent, input=query)

else:
    response = Runner.run_sync(news_agent, input=query)

print("🤖 Output:")
print(response.final_output)
