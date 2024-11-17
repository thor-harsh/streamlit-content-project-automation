import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("API_KEY"))

def chatbot_response(prompt, model_name="gemini-1.5-flash"):

    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        print(f"Error generating response: {e}")
        return "Sorry, I encountered an error. Please try again."

def run_chatbot():
    print("Welcome to the LLM Chatbot! Type 'exit' to quit.")
    while True:
        # Take user input
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break


        print("Generating response...")
        response = chatbot_response(user_input)


        print(f"Bot: {response}\n")

if __name__ == "__main__":
    run_chatbot()
