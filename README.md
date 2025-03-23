# 🤖🔧 LLM Agent Team 🚀 

- AI-powered agents that can do several tasks using natural language commands.
- Built with `phidata` and `groq`.

I used Groq (llama-3.3-70b-versatile) which provides a Free API Key & 1200Tokens/second.

## 🚀 Features

- File Manager Agent: Enables you to do File I/O using natural language commands.
- Finance Agent: Provides Financial Knowledge / Comparisons between stocks/companies.
- Search Agent: Search agents are mostly implemented in other agents to provide information based on the web.
- Teach Agent: Summarizes YouTube videos.


## 📋 Prerequisites

1. Libraries:
   ```bash
   pip install phidata
   ```

## 🔐 Configuration

#### Environment Variables (dotenv)

```bash
# Linux/Mac
export GROQ_API_KEY = "YOUR_API_KEY"

# Windows (PowerShell)
$env:GROQ_API_KEY= "YOUR_API_KEY"
```
### Imports

```python
from phi.agent import Agent
from phi.model.groq import Groq

from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.file import FileTools
from phi.tools.googlesearch import GoogleSearch
from phi.tools.crawl4ai_tools import Crawl4aiTools
from phi.tools.youtube_tools import YouTubeTools
from phi.tools.exa import ExaTools

from dotenv import load_dotenv

from bs4 import BeautifulSoup
import requests

load_dotenv()

```
## 💡 Examples

### File Manager Agent
```python

fileManager_agent.print_response("Find me 10 great Restaurants in Izmir and save them in a related named file", stream=True)

```

### Finance Agent
```python

finance_agent.print_response("NVDA or META? Buying which stock would be a better idea based on the news?", stream=True)

```

### Web-Content Agent
```python

web_agent.print_response("Can You Briefly Explain What LangChain is used for?", stream=True)

```

### Search Agent
```python

search_agent.print_response("What are some B2B Startups backed by YC?", stream=True)

```

### Teach Agent
```python

study_partner.print_response("Summarize the latest Andrej Karpathy video on YouTube", stream=True)

```

## Agents as a Tool

- You can implement these agents as a tool in your projects!
- Making an agent team with related agents as a tool can save you from deciding which agent to use.
- Check [https://github.com/openai/openai-agents-python] for more Agents as a tool implementation.
- You can avoid hallucinated generations by implementing the parallelization & tool routing examples.

- **Phidata Documentation**: [https://phidata.com](https://phidata.com)

**NOTE**: A freshman creates this repository. I believe some great opinions about this repo would lead me to learn & develop more.
```

