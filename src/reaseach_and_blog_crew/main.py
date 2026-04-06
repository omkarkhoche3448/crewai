from ants_platform import AntsPlatform
from ants_platform.crewai import EventListener

from reaseach_and_blog_crew.crew import ResearchAndBlogCrew


def run():
    """
    Run the crew.
    """
    # Initialize Ants Platform observability
    ants_platform = AntsPlatform(timeout=30)
    listener = EventListener(
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


