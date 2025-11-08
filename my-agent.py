"""
AWS Daily Helper Assistant - Bedrock AgentCore Deployment

An AI assistant that helps users with daily AWS tasks and questions.
Deployed using Strands Agents framework to AWS Bedrock AgentCore.
"""

from typing import Dict, Callable
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent

# Initialize the Bedrock AgentCore app
app = BedrockAgentCoreApp()


class AWSHelpingAssistant(Agent):
    """
    An AI assistant that helps with daily AWS tasks and questions.
    
    Capabilities:
    - EC2 instance management and optimization
    - S3 storage best practices and security
    - Lambda function troubleshooting and optimization
    - AWS cost optimization and billing guidance
    - General AWS architecture and service recommendations
    """
    
    # Response templates for different AWS services
    RESPONSES = {
        "ec2": """**EC2 Assistance**

Here's help with your EC2 question:
• Check your instance types and sizes for cost optimization
• Ensure security groups are properly configured
• Consider using Auto Scaling for better resource management
• Monitor CloudWatch metrics for performance insights

Would you like specific guidance on any of these areas?""",
        
        "s3": """**S3 Assistance**

S3 best practices:
• Use appropriate storage classes (Standard, IA, Glacier)
• Enable versioning for important data
• Set up lifecycle policies to manage costs
• Configure proper bucket policies and ACLs

Need help with a specific S3 task?""",
        
        "lambda": """**Lambda Assistance**

Lambda optimization tips:
• Right-size your memory allocation
• Use environment variables for configuration
• Implement proper error handling and retries
• Monitor execution duration and costs

What specific Lambda challenge can I help with?""",
        
        "cost": """**AWS Cost Optimization**

Cost management strategies:
• Use AWS Cost Explorer to analyze spending
• Set up billing alerts and budgets
• Consider Reserved Instances for predictable workloads
• Regularly review and terminate unused resources

Would you like help setting up cost monitoring?""",
        
        "general": """**AWS General Assistance**

I'm here to help with your AWS questions! I can assist with:
• Service recommendations and best practices
• Cost optimization strategies
• Security and compliance guidance
• Architecture design suggestions

Please provide more details about what you'd like help with."""
    }
    
    def __init__(self):
        super().__init__(
            name="AWS Daily Helper",
            description="An AI assistant that helps with daily AWS tasks and questions. Provides expert guidance on EC2, S3, Lambda, cost optimization, and general AWS best practices."
        )
        
        # Map keywords to response types
        self.keyword_map = {
            "ec2": "ec2",
            "s3": "s3",
            "lambda": "lambda",
            "cost": "cost",
            "billing": "cost",
            "price": "cost",
            "budget": "cost"
        }
    
    def process_request(self, user_input: str) -> str:
        """
        Process user requests and provide AWS assistance.
        
        Args:
            user_input: The user's question or request
            
        Returns:
            A formatted response with AWS guidance
        """
        if not user_input or not user_input.strip():
            return self.RESPONSES["general"]
        
        # Detect the service type from user input
        service_type = self._detect_service(user_input)
        
        # Return the appropriate response
        return self.RESPONSES.get(service_type, self.RESPONSES["general"])
    
    def _detect_service(self, user_input: str) -> str:
        """
        Detect which AWS service the user is asking about.
        
        Args:
            user_input: The user's question
            
        Returns:
            The service type identifier
        """
        user_input_lower = user_input.lower()
        
        # Check for keyword matches
        for keyword, service_type in self.keyword_map.items():
            if keyword in user_input_lower:
                return service_type
        
        # Default to general assistance
        return "general"


# Create the agent instance
agent = AWSHelpingAssistant()


@app.entrypoint
def invoke(payload: Dict) -> Dict:
    """
    Main entry point for the agent when deployed to Bedrock AgentCore.
    
    Args:
        payload: Dictionary containing the user's prompt and other data
        
    Returns:
        Dictionary with the agent's response
    """
    # Extract user message from payload
    user_message = payload.get("prompt", "Hello! How can I help you today?")
    
    # Process the request using the agent
    result = agent.process_request(user_message)
    
    # Return the result in the expected format
    return {"result": result}


if __name__ == "__main__":
    # Run the app for local testing and deployment
    app.run()
