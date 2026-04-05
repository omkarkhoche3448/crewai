# CrewAI CLI Commands Reference

## Core Commands

| Command | Use Case |
|---------|----------|
| `crewai create crew <name>` | Scaffold a new crew project |
| `crewai create flow <name>` | Scaffold a new flow project |
| `crewai install` | Install crew dependencies |
| `crewai run` | Run the crew locally |
| `crewai chat` | Start interactive conversation with the crew |
| `crewai version` | Show installed CrewAI version |
| `crewai update` | Update pyproject.toml to latest CrewAI version |

## Testing & Training

| Command | Use Case |
|---------|----------|
| `crewai test -n 3` | Test crew for 3 iterations and evaluate results |
| `crewai test -n 2 -m gpt-4o` | Test crew with a specific model |
| `crewai train -n 5` | Train crew for 5 iterations to improve output |
| `crewai train -n 3 -f data.json` | Train with custom training data file |
| `crewai replay` | Replay crew execution from a specific task |

## Deployment

| Command | Use Case |
|---------|----------|
| `crewai login` | Authenticate with CrewAI platform |
| `crewai deploy create` | Register crew on the platform |
| `crewai deploy push` | Push/deploy crew to the platform |
| `crewai deploy status` | Check deployment status |
| `crewai deploy logs` | View deployment logs |
| `crewai deploy list` | List all your deployments |
| `crewai deploy remove` | Remove a deployment |

## Memory Management

| Command | Use Case |
|---------|----------|
| `crewai reset-memories -a` | Reset ALL memories |
| `crewai reset-memories -l` | Reset long-term memory only |
| `crewai reset-memories -s` | Reset short-term memory only |
| `crewai reset-memories -e` | Reset entity memory only |
| `crewai reset-memories -kn` | Reset knowledge storage |
| `crewai reset-memories -k` | Reset latest kickoff task outputs |
| `crewai log-tasks-outputs` | View latest kickoff task outputs |

## Tools

| Command | Use Case |
|---------|----------|
| `crewai tool create <name>` | Create a custom tool |
| `crewai tool install <name>` | Install a tool from the repository |
| `crewai tool publish` | Publish your tool to the repository |

## Flows

| Command | Use Case |
|---------|----------|
| `crewai flow kickoff` | Run a flow |
| `crewai flow plot` | Visualize flow as a diagram |
| `crewai flow add-crew <name>` | Add a crew to an existing flow |

## Triggers

| Command | Use Case |
|---------|----------|
| `crewai triggers list` | List available triggers from integrations |
| `crewai triggers run <slug>` | Execute crew with a trigger payload |

## Organization & Enterprise

| Command | Use Case |
|---------|----------|
| `crewai org` | Organization management |
| `crewai enterprise` | Enterprise configuration |
| `crewai config` | CLI configuration settings |
