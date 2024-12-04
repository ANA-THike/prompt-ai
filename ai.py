import google.generativeai as genai

# Configure the Generative AI client
genai.configure(api_key="AIzaSyCUU3rLgkLQ9iffWcZP5FdkLvHvD-qynkc")
model = genai.GenerativeModel("gemini-1.5-flash")

def chat_with_google_genai():
    print("Google Generative AI Chatbot: Hello! I am your chatbot. Type 'exit' to end the conversation.\n")
    conversation_history = ""  # To maintain context by combining all past inputs and responses

    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Google Generative AI Chatbot: Goodbye!")
            break
        
        # Append user input to conversation history
        conversation_history += f"You: {user_input}\n"
        
        try:
            # Generate response from the Generative AI model
            response = model.generate_content(conversation_history)
            
            # Extract the text response
            bot_reply = response.text.strip()
            
            # Display the bot's reply
            print(f"Google Generative AI Chatbot: {bot_reply}")
            
            # Append bot's reply to the conversation history
            conversation_history += f"Google Generative AI Chatbot: {bot_reply}\n"
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_google_genai()
