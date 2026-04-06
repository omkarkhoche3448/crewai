# Research & Blog Crew

A multi-agent AI system powered by [CrewAI](https://crewai.com) that researches a topic and generates a blog post.

## Agents

| Agent | Role |
|-------|------|
| Report Generator | Researches a topic and creates a detailed ~2000 word report |
| Blog Writer | Converts the report into a fun, easy-to-read blog post |

**Process:** Sequential (Report Generator → Blog Writer)

## Prerequisites

- Python >= 3.10, < 3.14
- [uv](https://docs.astral.sh/uv/) package manager
- OpenAI API key

## Setup

### 1. Install uv

```bash
pip install uv
```

### 2. Clone the repo

```bash
git clone https://github.com/omkarkhoche3448/crewai.git
cd crewai
```

### 3. Install dependencies

```bash
crewai install
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL_NAME=gpt-4o-mini
```

Get your OpenAI API key from [platform.openai.com/api-keys](https://platform.openai.com/api-keys).

## Running the Crew

```bash
crewai run
```

**Note (Windows):** If you see emoji encoding errors, run with:

```bash
PYTHONIOENCODING=utf-8 PYTHONUTF8=1 crewai run
```

The crew will generate a blog post at `blogs/blog.md`.

## Customizing the Topic

Edit `src/reaseach_and_blog_crew/main.py` and change the `topic` value:

```python
inputs = {
    'topic': 'Your topic here'
}
```

## Customizing Agents & Tasks

- `src/reaseach_and_blog_crew/config/agents.yaml` — Agent roles, goals, backstories
- `src/reaseach_and_blog_crew/config/tasks.yaml` — Task descriptions and expected outputs
- `src/reaseach_and_blog_crew/crew.py` — Agent/task logic and tools

## Deploy to CrewAI Platform

```bash
crewai login
crewai deploy create
crewai deploy push
crewai deploy status
```

## Project Structure

```
research_and_blog_crew/
├── .env                          # API keys (not committed)
├── pyproject.toml                # Project config
├── blogs/                        # Generated blog output
│   └── blog.md
└── src/reaseach_and_blog_crew/
    ├── config/
    │   ├── agents.yaml           # Agent definitions
    │   └── tasks.yaml            # Task definitions
    ├── crew.py                   # Crew orchestration
    ├── main.py                   # Entry point
    └── tools/
        └── custom_tool.py        # Custom tools
```
