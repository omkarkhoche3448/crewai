import os
import logging
from ants_platform import AntsPlatform
from ants_platform.crewai import EventListener
from reaseach_and_blog_crew.crew import ResearchAndBlogCrew

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.WARNING)


def run():
    """
    Run the crew.
    """
    public_key = os.environ.get("ANTS_PLATFORM_PUBLIC_KEY")
    secret_key = os.environ.get("ANTS_PLATFORM_SECRET_KEY")
    host = os.environ.get("ANTS_PLATFORM_HOST", "https://app.agenticants.ai")

    # Debug: log using WARNING level so it definitely shows in platform logs
    logger.warning("[ANTS ENV] PUBLIC_KEY=%s", "SET("+public_key[:12]+"...)" if public_key else "NONE")
    logger.warning("[ANTS ENV] SECRET_KEY=%s", "SET" if secret_key else "NONE")
    logger.warning("[ANTS ENV] HOST=%s", host)

    ants_platform = AntsPlatform(
        public_key=public_key,
        secret_key=secret_key,
        host=host,
        timeout=30,
    )
    listener = EventListener(
        public_key=public_key,
        agent_name="research_and_blog_crew",
        agent_display_name="Research & Blog Crew v1.0",
    )

    inputs = {
        "topic": "The impact of artificial intelligence on the job market"
    }

    try:
        ResearchAndBlogCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
    finally:
        ants_platform.flush()