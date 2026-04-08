import os
from ants_platform import AntsPlatform
from ants_platform.crewai import EventListener

from reaseach_and_blog_crew.crew import ResearchAndBlogCrew


def run():
    """
    Run the crew.
    """
    # Initialize Ants Platform — reads ANTS_PLATFORM_* env vars injected by platform
    ants_platform = AntsPlatform(
        public_key=os.environ.get("ANTS_PLATFORM_PUBLIC_KEY"),
        secret_key=os.environ.get("ANTS_PLATFORM_SECRET_KEY"),
        host=os.environ.get("ANTS_PLATFORM_HOST", "https://app.agenticants.ai"),
        timeout=30,
    )
    listener = EventListener(
        public_key=os.environ.get("ANTS_PLATFORM_PUBLIC_KEY"),
        agent_name="research_and_blog_crew",
        agent_display_name="Research & Blog Crew v1.0",
    )

    inputs = {
        'topic': 'The impact of artificial intelligence on the job market'
    }

    try:
        ResearchAndBlogCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    finally:
        ants_platform.flush()


