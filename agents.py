

from crewai import Agent
from Tools.Exa_Tool import ExaSearchTool


class SchoolProjectAgents:
    def __init__(self, model1, model2):
        self.Groq = model1
        self.Groq2 = model2
        self.tool = ExaSearchTool.tools()

    def researcher(self):
        return Agent(
            role='Senior Researcher',
            llm=self.Groq2,
            goal='You are a senior Researcher. Your goal is to conduct research on the task given.',
            verbose=True,
            memory=True,
            backstory=(
                "Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could impart the task given to you."
            ),
            tool=self.tool,
            max_iter=8,
            allow_delegation=True
        )

    def writer(self):
        return Agent(
            role='Project Writer',
            llm=self.Groq,
            goal='Your goal is to check through the document and paper given to you by the senior researcher and extract good insight from the document.',
            verbose=True,
            memory=True,
            backstory=(
                "With an in-depth documentation of complex topics, you craft engaging documentation that captivates and educates, bringing a well-documented project into light in an accessible manner."
            ),
            tool=self.tool,
            allow_delegation=False
        )
