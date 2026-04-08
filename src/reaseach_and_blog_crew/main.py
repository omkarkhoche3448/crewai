from ants_platform import AntsPlatform
from ants_platform.crewai import EventListener

from reaseach_and_blog_crew.crew import ResearchAndBlogCrew


def run():
    """
    Run the crew.
    """
    # TEMP: hardcoded keys — rotate after confirming traces work
    _public_key = "pk-ap-c3a5359d-7025-4352-84ab-2ab5d8097001"
    _secret_key = "sk-ap-298f1932-c266-4eda-b77e-7e1916de40cb"
    _host = "https://app.agenticants.ai"

    ants_platform = AntsPlatform(
        public_key=_public_key,
        secret_key=_secret_key,
        host=_host,
        timeout=30,
    )
    listener = EventListener(
        public_key=_public_key,
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


