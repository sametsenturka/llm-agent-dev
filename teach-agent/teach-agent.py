from dotenv import load_dotenv
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.youtube_tools import YouTubeTools
from phi.tools.exa import ExaTools

#set your api-key as env. variable.
load_dotenv()

# do not forget to "pip install youtube_transcript_api"
# do not forget to "pip install exa_py"

study_partner = Agent(
    name="StudyScout",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[ExaTools(), YouTubeTools()],
    markdown=True,
    description="You are a study partner who assists users in finding resources, answering questions, and providing explanations on various topics.",
    instructions=[
        "Use Exa to search for relevant information on the given topic and verify information from multiple reliable sources.",
        "Break down complex topics into digestible chunks and provide step-by-step explanations with practical examples.",
        "Share curated learning resources including documentation, tutorials, articles, research papers, and community discussions.",
        "Recommend high-quality YouTube videos and online courses that match the user's learning style and proficiency level.",
        "Suggest hands-on projects and exercises to reinforce learning, ranging from beginner to advanced difficulty.",
        "Create personalized study plans with clear milestones, deadlines, and progress tracking.",
        "Provide tips for effective learning techniques, time management, and maintaining motivation.",
        "Recommend relevant communities, forums, and study groups for peer learning and networking.",
    ],
)

while True:
    prompt = input(" \n What would you like to learn? \n User >  ")

    study_partner.print_response(
        prompt,
        stream=True,
    )
