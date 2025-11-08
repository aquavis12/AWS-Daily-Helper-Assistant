"""
AWS Daily Helper Assistant - Bedrock AgentCore Deployment

An AI assistant that helps users with daily AWS tasks and questions.
Deployed using Strands Agents framework to AWS Bedrock AgentCore.
Uses AWS Bedrock Claude 3 for intelligent responses.
"""

import json
import boto3
from typing import Dict
from bedrock_agentcore.runtime import BedrockAgentCoreApp
from strands import Agent

# Initialize the Bedrock AgentCore app
app = BedrockAgentCoreApp()

# Initialize Bedrock client for LLM
bedrock_runtime = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-east-1'
)


class AWSHelpingAssistant(Agent):
    """
    An AI assistant that helps with daily AWS tasks and questions.
    Uses AWS Bedrock Claude 3 for intelligent, context-aware responses.
    
    Capabilities:
    - EC2 instance management and optimization
    - S3 storage best practices and security
    - Lambda function troubleshooting and optimization
    - AWS cost optimization and billing guidance
    - General AWS architecture and service recommendations
    """
    
    # System prompt for the LLM
    SYSTEM_PROMPT = """You are an expert AWS Solutions Architect and DevOps consultant. Your role is to help users with AWS-related questions and provide practical, actionable advice.

Your expertise includes:
- EC2: Instance types, Auto Scaling, security groups, optimization
- S3: Storage classes, lifecycle policies, versioning, security, bucket policies
- Lambda: Function optimization, memory allocation, error handling, cost management
- Cost Optimization: Billing analysis, Reserved Instances, cost reduction strategies
- General AWS: Architecture design, best practices, security, compliance

Guidelines:
- Provide clear, concise, and actionable advice
- Use bullet points for easy reading
- Include specific examples when helpful
- Always consider cost optimization and security
- Be friendly and professional
- If you don't know something, be honest about it

Format your responses with clear sections and bullet points."""
    
    def __init__(self):
        super().__init__(
            name="AWS Daily Helper",
            description="An AI assistant powered by AWS Bedrock Claude 3 that helps with daily AWS tasks and questions. Provides expert guidance on EC2, S3, Lambda, cost optimization, and general AWS best practices."
        )
        self.model_id = "anthropic.claude-3-sonnet-20240229-v1:0"
        self.conversation_history = []
    
    def process_request(self, user_input: str) -> str:
        """
        Process user requests using AWS Bedrock LLM.
        
        Args:
            user_input: The user's question or request
            
        Returns:
            An intelligent response from Claude 3
        """
        if not user_input or not user_input.strip():
            return "Hello! I'm your AWS Daily Helper Assistant. How can I help you with AWS today?"
        
        try:
            # Get response from Bedrock LLM
            response = self._get_llm_response(user_input)
            return response
        except Exception as e:
            # Fallback to basic response if LLM fails
            return f"I apologize, but I encountered an error: {str(e)}\n\nPlease try rephrasing your question or check your AWS credentials."
    
    def _get_llm_response(self, user_input: str) -> str:
        """
        Get response from AWS Bedrock Claude 3.
        
        Args:
            user_input: The user's question
            
        Returns:
            The LLM's response
        """
        # Prepare the prompt
        prompt = f"\n\nHuman: {user_input}\n\nAssistant:"
        
        # Prepare the request body
        body = json.dumps({
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 1000,
            "system": self.SYSTEM_PROMPT,
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            "temperature": 0.7,
            "top_p": 0.9
        })
        
        # Call Bedrock
        response = bedrock_runtime.invoke_model(
            modelId=self.model_id,
            body=body
        )
        
        # Parse response
        response_body = json.loads(response['body'].read())
        
        # Extract the text from Claude's response
        if 'content' in response_body and len(response_body['content']) > 0:
            return response_body['content'][0]['text']
        else:
            return "I apologize, but I couldn't generate a response. Please try again."


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
