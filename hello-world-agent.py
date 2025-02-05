from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from dotenv import load_dotenv

load_dotenv()

agent = Agent(
    model= Groq(id="llama-3.3-70b-versatile"),
    # model= Groq(id="deepseek-r1-distill-llama-70b"),
    # model = OpenAIChat(id="gpt-3.5-turbo"),
    show_tool_calls=True,
    markdown=True,
    debug_mode=True,
    structured_outputs=True
)

# print("Hello AI Agents!")
agent.print_response("Suggest 1 creative 2 words name for AI Agents")
