"""
Interactive Chat Interface for AWS Daily Helper Assistant
Run this to have a conversation with your agent
"""

from my_agent import agent


def chat():
    """Interactive chat with the AWS Daily Helper Assistant."""
    print("=" * 60)
    print("🚀 AWS Daily Helper Assistant - Interactive Chat")
    print("=" * 60)
    print("\nHello! I'm your AWS Daily Helper Assistant.")
    print("I can help you with EC2, S3, Lambda, cost optimization, and more!")
    print("\nType 'exit', 'quit', or 'bye' to end the conversation.\n")
    print("=" * 60)
    
    while True:
        # Get user input
        try:
            user_input = input("\n👤 You: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nGoodbye! Have a great day! 👋")
            break
        
        # Check for exit commands
        if user_input.lower() in ['exit', 'quit', 'bye', 'q']:
            print("\n🤖 Agent: Goodbye! Feel free to come back anytime you need AWS help! 👋")
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Process the request
        try:
            response = agent.process_request(user_input)
            print(f"\n🤖 Agent:\n{response}")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again with a different question.")


if __name__ == "__main__":
    try:
        chat()
    except KeyboardInterrupt:
        print("\n\nChat interrupted. Goodbye! 👋")
