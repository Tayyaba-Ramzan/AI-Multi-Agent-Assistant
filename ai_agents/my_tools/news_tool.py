import requests
from decouple import config
from agents import function_tool

NEWS_API_KEY = config("NEWS_API_KEY")

@function_tool
def get_latest_news(topic: str = "technology") -> str:
    """
    Fetch the top 3 latest news headlines related to a given topic.

    This tool uses the NewsAPI service to retrieve the most recent and relevant news articles.
    It queries the API using the specified topic and returns a formatted list of the top three
    article headlines sorted by their publish time.

    Example:
        >>> get_latest_news("artificial intelligence")
        '1. AI Revolutionizes Healthcare\n2. Google Introduces New AI Model\n3. Ethics of AI Under Scrutiny'

    Parameters:
        topic (str, optional): The topic to search for news articles. Defaults to "technology".

    Returns:
        str: A formatted string of the top 3 news headlines, or an error message if the request fails.
    """
    url = (
        f"https://newsapi.org/v2/everything?q={topic}&pageSize=3&sortBy=publishedAt"
        f"&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()

    if data.get("status") != "ok":
        return "An error occurred while fetching the news."

    articles = data.get("articles", [])
    headlines = [f"{i+1}. {article['title']}" for i, article in enumerate(articles)]

    return "\n".join(headlines)
