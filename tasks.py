
from crewai import Task

class ResearchProject:
    def __init__(self, topic):
        self.topic = topic

    def research_task(self,agent):
        return Task(
            description=(
                f"Your task is to go to the internet and identify the related documents, research papers, or journals about {self.topic} and provide a review of the document content to the project writer. "
                f"Identify key challenges, advancements, best practices, and references related to {self.topic}. "
                f"Your final report should clearly articulate the key points and provide guidance and expertise in designing the overall architecture and approach for the project."
            ),
            expected_output='A comprehensive 5 paragraphs report on the topic with references paper',
            agent = agent
        )

    def write_task(self,agent):
        return Task(
            description=(
                f"Generate a well-written project content which includes the introduction, literature review, methodology, implementation details, results analysis, conclusion, and references on {self.topic}. "
                f"Ensure the content is well-structured, coherent, and follows academic standards and guidelines. "
                f"This article should be easy to understand, engaging, and positive. "
                f"Request for the illustrative references from the senior researcher."
            ),
            expected_output=f"Well-documented article on introduction, literature review, best implementation, conclusion, and references on {self.topic} based on senior researcher research.",
            agent = agent,
            async_execution=True,
            output_file='new_writeup.md' 
        )
