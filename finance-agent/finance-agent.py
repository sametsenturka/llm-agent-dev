from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

#set your api-key as env. variable.
load_dotenv()

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True, company_news=True), GoogleSearch(), DuckDuckGo()],
    instructions=["Use tables to display data",
                  "If any of the stock name isn't right, search that name in the web and find the right stock name of that company.",
                  "You can use the GoogleSearch & DuckDuckGo tools"
                  "You can use any tool given if needed"],

    show_tool_calls=True,
    markdown=True,
)

while True:
    prompt = input(" \n User > ")
    finance_agent.print_response(prompt, stream=True)

