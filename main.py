from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.tools.python.tool import PythonREPLTool

# Define LLM
llm = OpenAI(model="gpt-4", temperature=0)

# Define Tools
tools = [
    Tool(
        name="Python",
        func=PythonREPLTool().run,
        description="Executes Python code."
    ),
    Tool(
        name="Search",
        func=lambda query: "Dummy search result",  # Replace with a search API integration.
        description="Searches the web for resources."
    )
]

# Initialize Agent
agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

# Test Agent
response = agent.run("Generate a PyTorch code snippet for fire detection using object detection.")
print(response)
