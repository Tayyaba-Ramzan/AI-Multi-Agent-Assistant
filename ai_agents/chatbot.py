import chainlit as cl
from agents import Runner
from my_agent.news_agent import news_agent
from my_agent.weather_agent import weather_agent
from my_agent.math_agent import math_agent

@cl.on_message
async def main(msg: cl.Message):
    prompt = msg.content.lower()

    # Select agent based on keywords
    if any(word in prompt for word in ["weather", "mausam", "temperature"]):
        agent = weather_agent
    elif any(word in prompt for word in ["news", "khabar", "headline"]):
        agent = news_agent
    elif any(word in prompt for word in ["solve", "plus", "add", "sum", "minus", "multiply", "+", "-", "*", "/"]):
        agent = math_agent
    else:
        agent = news_agent  # Default fallback

    # Run agent
    res = await Runner.run(agent, input=prompt)

    # Return response
    await cl.Message(content=res.final_output).send()
