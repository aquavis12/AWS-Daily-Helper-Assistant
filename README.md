# AWS Daily Helper Assistant

An intelligent AI assistant built with Strands Agents framework and deployed to AWS Bedrock AgentCore. This agent helps users with daily AWS tasks, providing expert guidance on EC2, S3, Lambda, cost optimization, and general AWS best practices.

## Features

- **EC2 Management**: Instance optimization, security group configuration, and Auto Scaling guidance
- **S3 Best Practices**: Storage class selection, versioning, lifecycle policies, and security
- **Lambda Optimization**: Memory allocation, error handling, and performance monitoring
- **Cost Optimization**: Billing analysis, budget alerts, and resource optimization strategies
- **General AWS Guidance**: Architecture recommendations and service selection advice

## Prerequisites

- Python 3.8 or higher
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials
- Strands Agents framework installed

## Installation

1. Clone this repository:
```bash
git clone https://github.com/aquavis12/AWS-Daily-Helper-Assistant
cd https://github.com/aquavis12/AWS-Daily-Helper-Assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure AWS credentials:
```bash
aws configure
```

## Setup with Starter Toolkit

### Step 1: Configure Your Agent

Configure the agent with the AgentCore toolkit:

```bash
agentcore configure --entrypoint my-agent.py
```

This will set up the necessary configuration for deployment.

### Step 2: Local Testing (Optional)

Test the agent locally before deploying. This requires Docker, Finch, or Podman:

```bash
agentcore launch --local
```

Or test directly with Python:

```bash
python my-agent.py
```

### Step 3: Deploy to AWS

Deploy the agent to AWS Bedrock AgentCore:

```bash
agentcore launch
```

The toolkit will:
- Package your agent code
- Create necessary AWS resources
- Deploy to Bedrock AgentCore
- Provide the agent endpoint

### Step 4: Test Your Agent

Test the deployed agent using the CLI:

```bash
agentcore invoke '{"prompt": "How can I optimize my EC2 costs?"}'
```

Or test with different queries:

```bash
agentcore invoke '{"prompt": "What are S3 best practices?"}'
agentcore invoke '{"prompt": "My Lambda function is timing out"}'
agentcore invoke '{"prompt": "How can I reduce my AWS bill?"}'
```

## Usage

### Via AgentCore CLI

The simplest way to interact with your agent:

```bash
agentcore invoke '{"prompt": "Your question here"}'
```

### Via AWS Console

1. Open Amazon Bedrock Console
2. Navigate to Agents
3. Select "AWS Daily Helper"
4. Use the test interface to interact with the agent

### Via Python API

```python
import boto3

client = boto3.client('bedrock-agent-runtime', region_name='us-east-1')

response = client.invoke_agent(
    agentId='<your-agent-id>',
    agentAliasId='<your-alias-id>',
    sessionId='<session-id>',
    inputText='How can I optimize my EC2 costs?'
)

print(response['completion'])
```

### Programmatic Usage

```python
import asyncio
from my-agent import agent

async def query_agent():
    response = await agent.process_request("How can I optimize my EC2 costs?")
    print(response)

asyncio.run(query_agent())
```

## Example Queries

- "How can I optimize my EC2 costs?"
- "What's the best way to secure my S3 buckets?"
- "My Lambda function is timing out, what should I check?"
- "I'm getting a high AWS bill, how can I reduce costs?"
- "What's the best storage class for infrequently accessed data?"

## Architecture

```
┌─────────────┐
│    User     │
└──────┬──────┘
       │
       ▼
┌─────────────────────────┐
│  Bedrock Agent Runtime  │
│  ┌───────────────────┐  │
│  │   @app.handler    │  │
│  └─────────┬─────────┘  │
└────────────┼────────────┘
             │
             ▼
┌────────────────────────────┐
│  AWSHelpingAssistant       │
│  ┌──────────────────────┐  │
│  │  process_request()   │  │
│  └──────────┬───────────┘  │
│             │              │
│    ┌────────┼────────┐     │
│    ▼        ▼        ▼     │
│  ┌───┐  ┌───┐  ┌──────┐   │
│  │EC2│  │S3 │  │Lambda│   │
│  └───┘  └───┘  └──────┘   │
│    ▼        ▼        ▼     │
│  ┌───┐  ┌──────────┐      │
│  │Cost│ │ General  │      │
│  └───┘  └──────────┘      │
└────────────────────────────┘
```

The agent is built using:
- **Strands Agents Framework**: For agent logic and orchestration
- **AWS Bedrock AgentCore**: For deployment and runtime
- **Service Handlers**: Specialized handlers for EC2, S3, Lambda, Cost, and General queries

For detailed architecture diagrams and flow charts, see [ARCHITECTURE.md](ARCHITECTURE.md).

## Project Structure

```
.
├── my-agent.py          # Main agent implementation
├── README.md            # This file
├── blog.md              # Blog post about the project
├── requirements.txt     # Python dependencies
└── .venv/               # Virtual environment
```

## Configuration

The agent uses the following default configuration:
- **Region**: us-east-1
- **Model**: Claude 3 Sonnet (via Bedrock)
- **Agent Name**: AWS Daily Helper

To modify these settings, update the deployment configuration in your deployment script.

## Troubleshooting

### Configuration Issues
```bash
# Reconfigure if needed
agentcore configure --entrypoint my-agent.py --force
```

### Local Testing Fails
- Ensure Docker, Finch, or Podman is installed and running
- Check that port 8080 is available
- Verify requirements.txt includes all dependencies

### Deployment Fails
- Ensure you have necessary IAM permissions for Bedrock
- Verify AWS credentials: `aws sts get-caller-identity`
- Check that Bedrock AgentCore is available in your region
- Review deployment logs: `agentcore logs`

### Agent Not Responding
- Check agent status: `agentcore status`
- View logs: `agentcore logs --tail 50`
- Verify the agent endpoint is accessible
- Test with a simple query first

### Common Commands

```bash
# Check agent status
agentcore status

# View logs
agentcore logs

# Update agent after code changes
agentcore launch

# Delete agent
agentcore delete
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Support

For issues and questions:
- Open an issue on GitHub
- Check the [Strands Agents documentation](https://strandsagents.com/latest/documentation/)
- Review AWS Bedrock documentation

## Acknowledgments

Built with [Strands Agents](https://strandsagents.com/) framework and deployed to AWS Bedrock AgentCore.
