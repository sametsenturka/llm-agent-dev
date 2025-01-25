import requests
from bs4 import BeautifulSoup

from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.googlesearch import GoogleSearch
from phi.model.groq import Groq
from dotenv import load_dotenv

#set your api-key as env. variable.
load_dotenv()

def get_website_content(url):
    # Send a GET request to the website
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the text content of the website
        website_content = soup.get_text()
        return website_content
    else:
        return f"Failed to retrieve content. Status code: {response.status_code}"


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

# Example usage
while True:
    url = input(" \n URL > ");
    content = get_website_content(url)

    web_agent.print_response("Can You Briefly Explain This Content: \n " + content, stream=True)
