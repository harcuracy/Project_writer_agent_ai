import os
from tasks import ResearchProject
from agents import SchoolProjectAgents
from crewai import Crew
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from google.colab import userdata
from dotenv import load_dotenv
load_dotenv()

os.environ["GROQ_API_KEY"] = userdata.get("groq_api_key")
os.environ["EXA_API_KEY"] = userdata.get("EXA_API_KEY")

Groq = ChatGroq(model_name="mixtral-8x7b-32768")
Groq2 = ChatGroq(model_name = "llama3-70b-8192" )

topic = 'An unauthorized smart vehicle parking system detection using convolution neural network'
#topic = input("Enter your topic:")

Agents = SchoolProjectAgents(Groq,Groq2)
researcher_agent = Agents.researcher()
writer_agent = Agents.writer()


project = ResearchProject(topic)
researcher_task = project.research_task(researcher_agent)
writer_task = project.write_task(writer_agent)

crew = Crew(agents = [researcher_agent, writer_agent],
            tasks = [researcher_task,writer_task])
Bull = crew.kickoff()


# Print results
print("\n\n################################################")
print("## Here is the result")
print("################################################\n")


print(Bull)
