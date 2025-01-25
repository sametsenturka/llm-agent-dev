from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from phi.model.groq import Groq
from dotenv import load_dotenv

#set your api-key as env. variable.
load_dotenv()

web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo(), GoogleSearch()],
    instructions=["Always include sources",
                  "give the shortest possible output",
                  "give the output in that given language",
                  "If any Error Occurs, tell me.",
                  "At the end of every output ask a question about the output to help the user more and more"],
    show_tool_calls=True,
    markdown=True,
)

while True:
    prompt = input(" \n User > ")
    web_agent.print_response(prompt, stream=True)


