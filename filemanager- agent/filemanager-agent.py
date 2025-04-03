from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.file import FileTools
from phi.tools.googlesearch import GoogleSearch
from phi.tools.crawl4ai_tools import Crawl4aiTools
import requests


# HTTP GET REQUEST
def send_request(addr: str) -> str:
    """Sends http get request to the given address and returns the response"""
    response = requests.get(addr)
    return response.text

groq_model = Groq(id="llama-3.3-70b-versatile", api_key="YOUR_API_KEY")


file_agent = Agent(
    model=groq_model,
    description="You are a computer file operator.",
    role="file writer",
    instructions=[
        "Read and write files.",
        "If you create file successfully, return the file name to the user.",
        "If you face with an error, return the error to the user.",
    ],
    tools=[FileTools()],
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
    debug_mode=True,
)

research_agent = Agent(
    model=groq_model,
    description="You are a researcher.",
    role="researcher",
    instructions=[
        "Search for the most relevant information on the web and return the results.",
        "If the information is not found, return that you could not find the information.",
    ],
    tools=[GoogleSearch(), DuckDuckGo()],
    add_history_to_messages=True,
    num_history_responses=2,
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
    debug_mode=True,
)

crawler_agent = Agent(
    model=groq_model,
    description="""
    You are a web site crawler.
    Your job is to get the content of the given website.
    """,
    instructions=[
        "Get the page content of the given web site",
        "If you can not get it, return that you could not get it."],
    tools=[Crawl4aiTools()],
    add_history_to_messages=True,
    num_history_responses=2,
    show_tool_calls=True,
    markdown=True,
    monitoring=True,
    debug_mode=True,
)

team = Agent(
    model=groq_model,

    description="""
        You are a team of experts about web research and file operations.
        Your job is to work together to solve the given problem.
    """,
    role="expert team",

    # Agent may use different tools to solve the problem.
    # Agent may use different agents to solve the problem.
    # Longer instructions are better. but too many lines of instructions may not be good.

    instructions=["If user asks something, search for the most relevant information on the web.",
                  "If user asks a file operation, use the file agent and write the information you gain to file",
                  "If user asks about the opinions of the people about the given topic, use the WebOpinion_Agent to get the opinions",
                  "If user asks about the content of the given website, use the crawler_agent to get the content",
                  "If user asks about the rating of the given content, use the Rate_Agent to get the content"
                  "If you face with any error return error message to the user"],
    team=[research_agent, file_agent, crawler_agent],
    add_history_to_messages=True,
    num_history_responses=2,
    show_tool_calls=True,
    monitoring=True,
    debug_mode=True,
)

user_input = input("How Can I Help You? ")

response = team.run(user_input)

print(response)
