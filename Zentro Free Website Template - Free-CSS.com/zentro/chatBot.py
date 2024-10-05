import ollama

print("Hi I'm Ollama a locally ran LLM")

while True:

    userText = input(">>")

    if userText == "/bye":
        print("Goodbye")
        break


    response = ollama.chat(model='llama3.2', messages=[
    {
        'role': 'user',
        'content': userText,
    },
    ])
    print(response['message']['content'])