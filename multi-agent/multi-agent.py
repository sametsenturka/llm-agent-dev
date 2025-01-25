import httpx
from pathlib import Path
from phi.agent import Agent
from phi.tools.csv_tools import CsvTools
from phi.tools.duckduckgo import DuckDuckGo
import os

from dotenv import load_dotenv

load_dotenv()

### SEARCH CUSTOMER DATABASE AGENT ####################################################

imdb_csv = Path(__file__).parent.joinpath("wip").joinpath("IMDB-Movie-Data.csv")

if not os.path.exists(imdb_csv):
    url = "https://phidata-public.s3.amazonaws.com/demo_data/IMDB-Movie-Data.csv"

    response = httpx.get(url)

    imdb_csv.parent.mkdir(parents=True, exist_ok=True)
    imdb_csv.write_bytes(response.content)



imdb_csv_agent = Agent(
    name="IMDB CSV Agent",
    tools=[CsvTools(csvs=[imdb_csv])],
    markdown=True,
    show_tool_calls=True,
    debug_mode=True,
    instructions=[
        "First always get the list of files",
        "Then check the columns in the file",
        "Then run the query to answer the question",
    ],
)

### SEARCH THE WEB ##################################################################

web_search_agent = Agent(
    name="Web Search Agent",
    tools=[DuckDuckGo()],
    markdown=True,
    show_tool_calls=True,
)

### MAIN AGENT #####################################################################

agent_team = Agent(
    name="Agent Team",
    team=[web_search_agent, imdb_csv_agent],
    instructions=[
        "You are an AI agent which knows everything about movies",
        "You can refer questions to two different agents: Web Search Agent and IMDB CSV Agent",
        "First you always use the IMDB agent, if it cannot answer your question you use the Web Search Agent",
    ],
    show_tool_calls=True,
    markdown=True,
)

agent_team.cli_app(stream=False)