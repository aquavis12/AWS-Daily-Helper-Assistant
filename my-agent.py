"""
AWS Daily Helper Assistant - Bedrock AgentCore Deployment

This agent helps users with daily AWS tasks and questions using chain of thought reasoning.
Deployed using Strands Agents framework to AWS Bedrock AgentCore.
"""

from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent

# Initialize the Bedrock AgentCore app
app = BedrockAgentCoreApp()


class AWSHelpingAssistant(Agent):
    """An AI assistant that helps with daily AWS tasks and questions."""
    
    def __init__(self):
        super().__init__(
            name="AWS Daily Helper",
            description="An AI assistant that helps with daily AWS tasks and questions using chain of thought reasoning",
            instructions="""You are an AWS expert assistant that helps users with their daily AWS tasks.
            
Your capabilities include:
- EC2 instance management and optimization
- S3 storage best practices and security
- Lambda function troubleshooting and optimization
- AWS cost optimization and billing guidance
- General AWS architecture and service recommendations

Always provide clear, actionable advice with best practices in mind.
Use chain of thought reasoning to break down complex questions."""
        )
    
    async def process_request(self, user_input: str) -> str:
        """Process user requests and provide AWS assistance."""
        # Analyze the request to determine the AWS service
        user_input_lower = user_input.lower()
        
        if "ec2" in user_input_lower:
            return await self._handle_ec2_query(user_input)
        elif "s3" in user_input_lower:
            return await self._handle_s3_query(user_input)
        elif "lambda" in user_input_lower:
            return await self._handle_lambda_query(user_input)
        elif "cost" in user_input_lower or "billing" in user_input_lower:
            return await self._handle_cost_query(user_input)
        else:
            return await self._handle_general_query(user_input)
    
    async def _handle_ec2_query(self, query: str) -> str:
        """Handle EC2-related queries."""
        return """**EC2 Assistance**

Here's help with your EC2 question:
- Check your instance types and sizes for cost optimization
- Ensure security groups are properly configured
- Consider using Auto Scaling for better resource management
- Monitor CloudWatch metrics for performance insights

Would you like specific guidance on any of these areas?"""
    
    async def _handle_s3_query(self, query: str) -> str:
        """Handle S3-related queries."""
        return """**S3 Assistance**

S3 best practices:
- Use appropriate storage classes (Standard, IA, Glacier)
- Enable versioning for important data
- Set up lifecycle policies to manage costs
- Configure proper bucket policies and ACLs

Need help with a specific S3 task?"""
    
    async def _handle_lambda_query(self, query: str) -> str:
        """Handle Lambda-related queries."""
        return """**Lambda Assistance**

Lambda optimization tips:
- Right-size your memory allocation
- Use environment variables for configuration
- Implement proper error handling and retries
- Monitor execution duration and costs

What specific Lambda challenge can I help with?"""
    
    async def _handle_cost_query(self, query: str) -> str:
        """Handle cost and billing queries."""
        return """**AWS Cost Optimization**

Cost management strategies:
- Use AWS Cost Explorer to analyze spending
- Set up billing alerts and budgets
- Consider Reserved Instances for predictable workloads
- Regularly review and terminate unused resources

Would you like help setting up cost monitoring?"""
    
    async def _handle_general_query(self, query: str) -> str:
        """Handle general AWS queries."""
        return """**AWS General Assistance**

I'm here to help with your AWS questions! I can assist with:
- Service recommendations and best practices
- Cost optimization strategies
- Security and compliance guidance
- Architecture design suggestions

Please provide more details about what you'd like help with."""


# Create the agent instance
agent = AWSHelpingAssistant()


@app.handler
async def handler(event, context):
    """
    Main handler for Bedrock AgentCore requests.
    
    This function is called by Bedrock AgentCore when the agent receives a request.
    It processes the user input and returns the agent's response.
    """
    # Extract user input from the event
    user_input = event.get("inputText", "")
    
    # Process the request using the agent
    response = await agent.process_request(user_input)
    
    # Return the response in the expected format
    return {
        "response": response,
        "sessionAttributes": event.get("sessionAttributes", {}),
    }


# For local testing
if __name__ == "__main__":
    import asyncio
    
    async def test_locally():
        """Test the agent locally before deploying."""
        print("🚀 AWS Daily Helper Assistant - Local Test")
        print("=" * 50)
        
        # Test queries
        test_queries = [
            "How can I optimize my EC2 costs?",
            "What's the best way to secure my S3 buckets?",
            "My Lambda function is timing out, what should I check?",
            "I'm getting a high AWS bill, how can I reduce costs?"
        ]
        
        for query in test_queries:
            print(f"\n🤔 User: {query}")
            print("-" * 30)
            response = await agent.process_request(query)
            print(f"🤖 Assistant: {response}")
            print("\n" + "=" * 50)
    
    asyncio.run(test_locally())
