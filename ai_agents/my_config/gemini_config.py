from decouple import config
from agents import AsyncOpenAI, OpenAIChatCompletionsModel

api_key = config("GEMINI_API_KEY")
base_url = config("BASE_URL")

client = AsyncOpenAI(
    api_key=api_key,
    base_url=base_url
)

MODEL = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",  
    openai_client=client
)
