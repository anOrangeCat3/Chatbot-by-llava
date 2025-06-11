from llama_cpp import Llama

# Load the LLaMA model
llm = Llama(
    model_path="/home/idler/forclass/ee5112/models/Meta-Llama-3-8B-Instruct.Q4_0.gguf",
    chat_format="llama-3",
    verbose=False
)

print("Chatbot is ready! Type 'exit' to end the conversation.")
print("*"*50)

# Initialize conversation with system message
messages = [{"role": "system", "content": "You are an assistant who perfectly answer the problems."}]

while True:
    # Get user input
    user_input = input("You: ")
    
    if user_input.lower() == 'exit':
        break
    
    # Add user message to the conversation
    messages.append({"role": "user", "content": user_input})

    # Create chat completion
    response = llm.create_chat_completion(messages=messages)
    # print('*'*50)
    # Print the assistant's response
    print(f"LLaMA: {response['choices'][0]['message']['content']}")
    print()

    # Add assistant's response to the conversation for context
    messages.append({"role": "assistant", "content": response['choices'][0]['message']['content']})
