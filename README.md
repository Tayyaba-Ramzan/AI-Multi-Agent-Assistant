# 🤖 AI Multi-Agent Assistant with Tool Calling (Gemini + Chainlit)

> 💡 A powerful multi-functional AI assistant built using **modular agents** and **tool calling**, capable of handling weather queries, fetching news headlines, and solving math expressions — all from a single smart interface.

---

## 🚀 Introduction

This intelligent assistant is designed to handle multiple tasks through specialized agents:

- 🌦 Answer real-time **weather** queries  
- 📰 Provide the latest **news headlines**  
- 🔢 Solve **math expressions** instantly  

The project is built using:

- 🧠 Google Gemini API  
- ⚙️ Tool Calling with decorators  
- 🖼️ Chainlit for an interactive UI  

---

## 🧠 Features

| Agent           | Functionality                              | Tool Used              |
|------------------|--------------------------------------------|------------------------|
| **Math Agent**   | Evaluates math expressions                 | `solve()`              |
| **News Agent**   | Fetches top 3 live news headlines          | `get_latest_news()`    |
| **Weather Agent**| Provides current weather for a city        | `get_weather()`        |

Each agent is modular, extendable, and utilizes **Python decorators** for tool calling integration. APIs are consumed securely and efficiently via proper configuration.

---

## 🛠️ Tech Stack

| Category        | Technology                     |
|-----------------|--------------------------------|
| Language        | Python 3.10+                   |
| LLM             | Google Gemini API              |
| UI              | Chainlit                       |
| Tool Calling    | `@function_tool` decorators    |
| Config Handling | `python-decouple` + `.env`     |
| APIs            | WeatherAPI, NewsAPI            |

---

## 📁 Project Structure

```
├── chatbot.py # Main Chainlit handler
├── my_agent/
│ ├── math_agent.py # Math Agent (tool: solve)
│ ├── weather_agent.py # Weather Agent (tool: get_weather)
│ └── news_agent.py # News Agent (tool: get_latest_news)
├── my_tools/
│ ├── math_tool.py
│ ├── weather_tool.py
│ └── news_tool.py
├── my_config/
│ └── gemini_config.py # Loads model + API configs
├── .env # Secret API keys
└── README.md
```


---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
https://github.com/Tayyaba-Ramzan/AI-Multi-Agent-Assistant.git
```

uv venv  # Optional: if you're using `uv` as a package manager
uv add chainlit python-decouple requests

GEMINI_API_KEY=your_gemini_api_key_here
BASE_URL=https://generativelanguage.googleapis.com/v1beta
WEATHER_API_KEY=your_weather_api_key_here
NEWS_API_KEY=your_news_api_key_here

4. Run the chatbot
chainlit run chatbot.py

💬 Sample Prompts
Try using these in your Chainlit interface:

"What is the result of (45 * 12) + (102 / 3) - 16 ** 2?"

"Lahore ka mausam kaisa hai?"

"Give me the latest 3 news about technology"

🧰 Tool Calling Explained
Each agent is powered by a specific tool decorated using @function_tool. Here's a sample:

✅ Tool Example
```
@function_tool
def solve(expression: str) -> str:
    """Evaluates basic math expressions like '5 + 2 * 3' and returns the result."""
    try:
        return f"Result: {eval(expression)}"
    except Exception as e:
        return f"Error: {str(e)}"
```

✅ Agent Setup
```
math_agent = Agent(
    name="MathBot",
    instructions="You are a math expert. Use the `solve` tool to evaluate any valid expression.",
    model=MODEL,
    tools=[solve]
)
```

## 🏆 Highlights

- ✅ **Multi-Agent Architecture**  
- ✅ **Real-Time Weather & News APIs**  
- ✅ **Robust Tool Calling System**  
- ✅ **Modular, Scalable, and Maintainable**  
- ✅ **Fully Documented**  
- ✅ **Easy to Extend** (Add more agents/tools anytime)


## 🙋 Why This Project?

This assistant was created to explore **real-world use cases** for tool-calling agents — including multi-task handling, agent selection, and contextual responses.  
It's built with best practices in mind and designed to scale.

---

## 👩‍💻 Author

**Tayyaba Ramzan**  
💼 Software Engineer | AI Explorer | Developer Advocate  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/tayyabaRamzan)

---

## 🤝 Want to Collaborate?

If you find this project helpful:

- ⭐ **Star the repository**  
- 🛠️ **Fork and build your own assistant**  
- 📢 **Share your feedback or open a pull request**

Let’s build something amazing — together! 🚀

