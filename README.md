# AWS Daily Helper Assistant

An intelligent AI assistant built with **Strands Agents** framework and deployed to **AWS Bedrock AgentCore**. This agent provides instant, expert guidance on AWS services, helping you optimize costs, improve security, and follow best practices.

## 🎯 Features

- **EC2 Management**: Instance optimization, security groups, Auto Scaling, and performance monitoring
- **S3 Best Practices**: Storage classes, versioning, lifecycle policies, bucket security, and ACLs
- **Lambda Optimization**: Memory sizing, environment variables, error handling, and cost monitoring
- **Cost Optimization**: Billing analysis, budget alerts, Reserved Instances, and resource cleanup
- **General AWS Guidance**: Architecture design, service recommendations, and security compliance

## 🚀 Quick Start

Get your AWS helper agent up and running in minutes!

## Prerequisites

- Python 3.8 or higher
- AWS Account with Bedrock access
- AWS CLI configured with appropriate credentials
- Strands Agents framework installed

## Installation

1. Clone this repository:
```bash
git clone https://github.com/aquavis12/AWS-Daily-Helper-Assistant
cd AWS-Daily-Helper-Assistant
```

2. Create and activate a virtual environment:

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure AWS credentials:
```bash
aws configure
```

## Setup with Starter Toolkit

### Step 1: Configure Your Agent

Configure the agent with the AgentCore toolkit:

```bash
agentcore configure --entrypoint my-agent.py
```
This command will:
- Set up the necessary configuration for deployment
- Create a Dockerfile for containerization
- Prepare your agent for AWS deployment

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

**Windows PowerShell:**
```powershell
agentcore invoke '{\"prompt\": \"How can I optimize my EC2 costs?\"}'
```

**Linux/Mac/Git Bash:**
```bash
agentcore invoke '{"prompt": "How can I optimize my EC2 costs?"}'
```

More test examples:

**Windows:**
```powershell
agentcore invoke '{\"prompt\": \"What are S3 best practices?\"}'
agentcore invoke '{\"prompt\": \"My Lambda function is timing out\"}'
agentcore invoke '{\"prompt\": \"How can I reduce my AWS bill?\"}'
```

**Linux/Mac:**
```bash
agentcore invoke '{"prompt": "What are S3 best practices?"}'
agentcore invoke '{"prompt": "My Lambda function is timing out"}'
agentcore invoke '{"prompt": "How can I reduce my AWS bill?"}'
```

## 💬 Interactive Chat

Run the interactive chat interface to have a conversation with your agent:

```bash
python chat.py
```

This provides a terminal-based chat where you can ask questions and get instant responses.

## 📝 Example Queries

Try asking questions like:

- "How can I optimize my EC2 costs?"
- "What's the best way to secure my S3 buckets?"
- "My Lambda function is timing out, what should I check?"
- "I'm getting a high AWS bill, how can I reduce costs?"
- "What's the best storage class for infrequently accessed data?"
- "How do I set up Auto Scaling for my application?"

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

For detailed architecture diagrams and flow charts, see [DIAGRAMS.txt](DIAGRAMS.txt).

## 📁 Project Structure

```
.
├── my_agent.py                 # Main agent implementation
├── chat.py                     # Interactive terminal chat interface
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── DIAGRAMS.txt                # ASCII architecture diagrams
```

## ⚙️ Configuration

The agent uses the following default configuration:
- **Region**: us-east-1
- **Runtime**: Python 3.11+ 
- **Agent Name**: my_agent (configurable during setup)
- **Deployment**: Serverless via AWS Bedrock AgentCore

Configuration is stored in `.bedrock_agentcore.yaml`. To modify settings, edit this file or reconfigure:

```bash
agentcore configure --entrypoint my_agent.py
```

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

## 🎓 Learn More

- **Blog Post**: Read [Dev.to](https://dev.to/aws-builders/building-an-aws-daily-helper-assistant-with-strands-agents-and-bedrock-agentcore-2290) for a detailed walkthrough of building this agent

## 📄 License

This project is licensed under the MIT License.

## 💡 Support

For issues and questions:
- Check the [Strands Agents documentation](https://strandsagents.com/latest/documentation/)
- Review [AWS Bedrock documentation](https://docs.aws.amazon.com/bedrock/)
- See [Bedrock AgentCore deployment guide](https://strandsagents.com/latest/documentation/docs/user-guide/deploy/deploy_to_bedrock_agentcore/)

## 🙏 Acknowledgments

Built with:
- [Strands Agents](https://strandsagents.com/) - AI agent framework
- [AWS Bedrock AgentCore](https://aws.amazon.com/bedrock/) - Serverless deployment platform
- Python 3.11+ - Programming language

---
