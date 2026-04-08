from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import atexit
import os
from dotenv import load_dotenv
from ants_platform import AntsPlatform
from ants_platform.crewai import EventListener

# Load .env for local runs; on platform these are injected as system env vars
load_dotenv()

# Initialize Ants Platform observability at module load time
# so it works both locally and on CrewAI platform
_ants_platform = AntsPlatform(
    public_key=os.environ.get("ANTS_PLATFORM_PUBLIC_KEY"),
    secret_key=os.environ.get("ANTS_PLATFORM_SECRET_KEY"),
    host=os.environ.get("ANTS_PLATFORM_HOST", "https://app.agenticants.ai"),
    timeout=30,
)
_listener = EventListener(
    agent_name="research_and_blog_crew",
    agent_display_name="Research & Blog Crew v1.0",
)

# Ensure flush is always called on process exit
atexit.register(_ants_platform.flush)

# define the class for our crew
@CrewBase
class ResearchAndBlogCrew():
    
    agents: list[BaseAgent]
    tasks: list[Task]
    
    # define the paths of config files
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # ============= Agents ====================
    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["report_generator"]
        )
        
    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"]
        )
        
    # ============== Tasks ===========================
    # order of task definition matters
    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"]
        )
        
    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"],
            output_file="blogs/blog.md"
        )
        
    # ================ Crew ===============================
    
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )