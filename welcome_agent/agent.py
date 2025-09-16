from google.adk.agents import Agent
from google.genai import types # For further configuration controls

# In every file, you need to define root_agent - This is important!
root_agent = Agent(

    name = "welcome_agent", # Name of our AI Agent 
    model = "gemini-2.0-flash", # Underlying Model we will be using
    description = "Greeting Agent", # A brief description of the agent 
    instruction = "You are a helpful assistant that greets the user. Talk to me in a Jedi manner.", # Detailed things the Agent has to do

    generate_content_config=types.GenerateContentConfig(
        temperature=0.2, # More deterministic output, closer to 0 more deterministic it is
        max_output_tokens=250
    )
)

