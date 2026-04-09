import os
import atexit
import logging

from ants_platform import AntsPlatform
from ants_platform.crewai import EventListener

logger = logging.getLogger("ants_debug")
logging.basicConfig(level=logging.DEBUG)

# ===== ANTS PLATFORM INIT START =====
_public_key = os.environ.get("ANTS_PLATFORM_PUBLIC_KEY")
_secret_key = os.environ.get("ANTS_PLATFORM_SECRET_KEY")
_host = os.environ.get("ANTS_PLATFORM_HOST", "https://app.agenticants.ai")

logger.warning("===== ANTS_PLATFORM_INIT =====")
logger.warning("ANTS_PK_EXISTS=%s ANTS_PK_PREFIX=%s", bool(_public_key), _public_key[:16] if _public_key else "EMPTY")
logger.warning("ANTS_SK_EXISTS=%s", bool(_secret_key))
logger.warning("ANTS_HOST=%s", _host)

try:
    _ants_platform = AntsPlatform(
        public_key=_public_key,
        secret_key=_secret_key,
        host=_host,
        timeout=30,
    )
    logger.warning("ANTS_CLIENT_CREATED tracing_enabled=%s", _ants_platform._tracing_enabled if hasattr(_ants_platform, '_tracing_enabled') else "UNKNOWN")
except Exception as e:
    logger.error("ANTS_CLIENT_FAILED error=%s", e)
    _ants_platform = None

try:
    _listener = EventListener(
        public_key=_public_key,
        agent_name="research_and_blog_crew",
        agent_display_name="Research & Blog Crew v1.0",
    )
    logger.warning("ANTS_LISTENER_CREATED")
except Exception as e:
    logger.error("ANTS_LISTENER_FAILED error=%s", e)
    _listener = None

if _ants_platform:
    atexit.register(_ants_platform.flush)

logger.warning("===== ANTS_PLATFORM_INIT_DONE =====")
# ===== ANTS PLATFORM INIT END =====

# Import crew AFTER SDK is initialized
from reaseach_and_blog_crew.crew import ResearchAndBlogCrew  # noqa: E402


def run():
    """
    Run the crew.
    """
    inputs = {
        "topic": "The impact of artificial intelligence on the job market"
    }

    try:
        logger.warning("ANTS_CREW_KICKOFF_START")
        ResearchAndBlogCrew().crew().kickoff(inputs=inputs)
        logger.warning("ANTS_CREW_KICKOFF_DONE")
    except Exception as e:
        logger.error("ANTS_CREW_KICKOFF_ERROR error=%s", e)
        raise Exception(f"An error occurred while running the crew: {e}")
    finally:
        if _ants_platform:
            logger.warning("ANTS_FLUSH_START")
            _ants_platform.flush()
            logger.warning("ANTS_FLUSH_DONE")
