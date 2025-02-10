```markdown
```
LLM Agent Development (llm-agent-dev)
```

Welcome to the **LLM Agent Development** repository! This project is built using the **Phidata framework** and demonstrates how to create, customize, and deploy intelligent AI agents locally. Designed by a freshman, this project aims to explore the fundamentals of **Agentic AI Development** and provide a hands-on learning experience.

---
```
## Table of Contents
```
- [Introduction](#introduction)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
- [Common Issues & Tips](#common-issues--tips)

```
## Introduction
```
This repository showcases the development of an **AI agent team** using the **Phidata framework**. The goal is to understand how intelligent agents can be built, customized, and utilized for various tasks. Whether you're a beginner or an experienced developer, this project provides a practical example of working with AI agents and highlights the importance of proper setup and tool integration.

```
## Key Features
```

- **Phidata Framework:** Leverage the power of the Phidata framework to build and customize AI agents.
- **Local Development:** Run and test agents locally for easy experimentation.
- **Tool Integration:** Use tools like `DuckDuckGo()` and `GoogleSearch()` for task execution.
- **Modular Design:** Easily extend and customize agents for specific use cases.
- **Learning Resource:** A beginner-friendly project to understand the fundamentals of Agentic AI.

```
## Installation
```

To get started, follow these steps to set up the project locally:

1. **Clone the repository:**
```
   ```bash
   git clone https://github.com/sametsenturka/llm-agent-dev.git
   cd llm-agent-dev
   ```

2. **Set up a virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   - Rename `.env.example` to `.env` and update the necessary variables.

---

## Usage

Once the setup is complete, you can start using the AI agents. Here's how:

1. **Run the agent:**
   ```bash
   python main.py
   ```

2. **Interact with the agent:**
   - The agent will be ready to accept tasks and queries.
   - Example interaction:
     ```bash
     User: What's the weather today?
     Agent: Let me check that for you...
     ```

3. **Customize the agent:**
   - Modify the agent's behavior by editing the configuration files or adding new tools.

---

## Common Issues & Tips

Here are some common issues you might encounter and tips to resolve them:

- **Missing Imports/Installs:** Ensure all dependencies are installed correctly. Missing packages often lead to errors.
  ```bash
  pip install -r requirements.txt
  ```

- **Tool Behavior:** Agents may appear to work correctly even if the wrong tools are used. For example:
  - `DuckDuckGo()` might perform well even if the task was intended for `GoogleSearch()`, and vice versa.
  - This happens because the LLM relies on its trained data when it cannot access the specified tool.

- **Stuck? Check the Documentation:** If you encounter issues, refer to the [Official Phidata Framework Documentation](https://phidata.ai/docs) for guidance.
